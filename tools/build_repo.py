#!/usr/bin/env python3
"""Fetch fork zips, build repository.andrew zip, regenerate addons.xml/.md5 and index pages."""
import hashlib, html, json, os, re, shutil, sys, urllib.request, zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ZIPS = os.path.join(ROOT, "zips")
PAGES = "https://phantomgrimsalvo-svg.github.io/kodi-andrew-workshop/zips/"


def vkey(v):
    return [int(p) if p.isdigit() else -1 for p in re.split(r"[.+~-]", v)]


def addon_xml_from_zip(path):
    with zipfile.ZipFile(path) as z:
        bad = z.testzip()
        if bad:
            sys.exit(f"corrupt member {bad} in {path}")
        names = [n for n in z.namelist() if n.count("/") == 1 and n.endswith("/addon.xml")]
        if len(names) != 1:
            sys.exit(f"{path}: expected one <id>/addon.xml, got {names}")
        text = z.read(names[0]).decode("utf-8")
    m = re.search(r"<addon\b[^>]*>", text, re.S)
    tag = m.group(0)
    aid = re.search(r'\bid="([^"]+)"', tag).group(1)
    ver = re.search(r'\bversion="([^"]+)"', tag).group(1)
    if names[0].split("/")[0] != aid:
        sys.exit(f"{path}: folder {names[0]} != id {aid}")
    return aid, ver, text


def place(src, aid, ver):
    fname = f"{aid}-{ver}.zip"
    os.makedirs(os.path.join(ZIPS, aid), exist_ok=True)
    for dst in (os.path.join(ZIPS, aid, fname), os.path.join(ZIPS, fname)):
        if os.path.abspath(src) != os.path.abspath(dst):
            shutil.copyfile(src, dst)


def fetch(entry):
    tmp = os.path.join(ROOT, ".dl.zip")
    print("fetch", entry["url"])
    urllib.request.urlretrieve(entry["url"], tmp)
    h = hashlib.sha256(open(tmp, "rb").read()).hexdigest()
    if h != entry["sha256"]:
        sys.exit(f"sha256 mismatch for {entry['url']}: {h}")
    aid, ver, _ = addon_xml_from_zip(tmp)
    if os.path.basename(entry["url"]) != f"{aid}-{ver}.zip":
        sys.exit(f"name/version mismatch: {entry['url']} has {aid} {ver}")
    place(tmp, aid, ver)
    os.remove(tmp)


def build_repo_zip():
    src = os.path.join(ROOT, "repository.andrew")
    text = open(os.path.join(src, "addon.xml"), encoding="utf-8").read()
    ver = re.search(r'<addon\b[^>]*\bversion="([^"]+)"', text, re.S).group(1)
    out = os.path.join(ROOT, ".repo.zip")
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr(zipfile.ZipInfo("repository.andrew/", (2026, 1, 1, 0, 0, 0)), "")
        for f in sorted(os.listdir(src)):
            zi = zipfile.ZipInfo(f"repository.andrew/{f}", (2026, 1, 1, 0, 0, 0))
            zi.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(zi, open(os.path.join(src, f), "rb").read())
    place(out, "repository.andrew", ver)
    os.remove(out)


def main():
    cfg = json.load(open(os.path.join(ROOT, "tools", "sources.json")))
    for e in cfg["zips"]:
        fetch(e)
    build_repo_zip()
    latest = {}
    for aid in sorted(os.listdir(ZIPS)):
        d = os.path.join(ZIPS, aid)
        if not os.path.isdir(d):
            continue
        for f in os.listdir(d):
            if not f.endswith(".zip"):
                continue
            zid, ver, text = addon_xml_from_zip(os.path.join(d, f))
            if zid != aid or f != f"{aid}-{ver}.zip":
                sys.exit(f"bad zip {aid}/{f}: contains {zid} {ver}")
            if aid not in latest or vkey(ver) > vkey(latest[aid][0]):
                latest[aid] = (ver, text)
    parts = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>', "<addons>"]
    order = ["repository.andrew"] + sorted(a for a in latest if a != "repository.andrew")
    for aid in order:
        body = re.sub(r"^\s*<\?xml[^>]*\?>\s*", "", latest[aid][1]).strip()
        parts.append(body)
    parts.append("</addons>")
    xml = "\n".join(parts) + "\n"
    open(os.path.join(ROOT, "addons.xml"), "w", encoding="utf-8", newline="\n").write(xml)
    md5 = hashlib.md5(xml.encode("utf-8")).hexdigest()
    open(os.path.join(ROOT, "addons.xml.md5"), "w").write(md5)
    for aid in order:
        print(f"latest {aid} {latest[aid][0]}")

    names = {
        "repository.andrew": "Andrew's Kodi Workshop repo (install this once; Kodi then auto-updates the rest)",
        "plugin.video.cumination.andrew": "Cumination (Andrew)",
        "skin.arctic.fuse.3.andrew": "Arctic Fuse 3 (Andrew)",
        "plugin.video.themoviedb.helper.andrew": "TMDb Helper (Andrew)",
    }
    li = "\n".join(
        f'    <li>{html.escape(names.get(a, a))} {latest[a][0]}: '
        f'<a href="zips/{a}-{latest[a][0]}.zip">{a}-{latest[a][0]}.zip</a></li>' for a in order)
    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Andrew's Kodi Workshop</title>
  <style>
    body {{ font-family: sans-serif; max-width: 42rem; margin: 2rem auto; padding: 0 1rem; line-height: 1.45; }}
    code, a {{ word-break: break-all; }}
    li {{ margin: 0.35rem 0; }}
  </style>
</head>
<body>
  <h1>Andrew's Kodi Workshop</h1>
  <p>Public zips for Andrew Webber's personal Kodi forks. See <a href="INSTALL-KODI.md">INSTALL-KODI.md</a> for the File Manager steps.</p>
  <p>Kodi File Manager source (GitHub Pages):</p>
  <p><code>{PAGES}</code></p>
  <p>Install <b>repository.andrew</b> from that source once (Add-ons, Install from zip file), then install the add-ons from Install from repository, Andrew's Kodi Workshop. Kodi keeps them updated automatically.</p>
  <h2>Latest zips</h2>
  <ul>
{li}
  </ul>
</body>
</html>
"""
    open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(page)

    flat = sorted(f for f in os.listdir(ZIPS) if f.endswith(".zip"))
    nested = sorted(f"{a}/{f}" for a in os.listdir(ZIPS) if os.path.isdir(os.path.join(ZIPS, a))
                    for f in os.listdir(os.path.join(ZIPS, a)) if f.endswith(".zip"))
    items = "\n".join(f'<li><a href="{html.escape(f)}">{html.escape(f)}</a></li>' for f in flat + nested)
    open(os.path.join(ZIPS, "index.html"), "w", encoding="utf-8").write(
        "<!DOCTYPE html>\n<html><head><meta charset=\"utf-8\"><title>Andrew Kodi zips</title></head>\n<body>\n"
        "<h1>Andrew's Kodi Workshop zips</h1>\n<ul>\n" + items + "\n</ul>\n</body></html>\n")


if __name__ == "__main__":
    main()
