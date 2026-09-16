# Install Andrew's Kodi addons (newbie steps)

You need **Kodi 21 Omega** (Arctic Fuse 3 requires Kodi's `xbmc.gui` 5.17). Fire Stick / Shield / PC all work the same. These zips are **public** — no GitHub or Cursor login.

Cumination is an **adult** add-on. Arctic Fuse 3 (Andrew) expects TMDb Helper (Andrew), so install Helper **before** you switch skins.

## 0. One-time Kodi settings

1. Open **Settings** (gear).
2. Set the settings level to **Standard** or **Advanced** (bottom-left).
3. **System → Add-ons → Unknown sources → ON**. Confirm the warning.
4. Still on that screen, turn **Update official add-ons from** to **Any repositories** if you see that option.

Also install the **jurialmunkey** repository (needed for TMDb Helper / Arctic Fuse dependencies such as `script.module.jurialmunkey` and `script.skinvariables`):

- File Manager source: `https://kodi.jurialmunkey.net/repository.jurialmunkey/`
- Then **Add-ons → Install from zip file → jurialmunkey → repository.jurialmunkey-*.zip**

Cumination also needs **ResolveURL** (`script.module.resolveurl` and `script.module.resolveurl.xxx`). Install those from the usual ResolveURL / dobbelina repository you already use, or from the official / community zip you used before.

---

## 1. Add Andrew's zip folder as a Kodi source

This is the URL to type. Copy it exactly:

```
https://phantomgrimsalvo-svg.github.io/kodi-andrew-workshop/zips/
```

If GitHub Pages is still spinning up (first 1–2 minutes after publish), use this instead (also public, no login):

```
https://cdn.jsdelivr.net/gh/phantomgrimsalvo-svg/kodi-andrew-workshop@main/zips/
```

### File Manager steps

1. **Settings → File manager → Add source**.
2. Click **\<None\>**.
3. Paste one of the URLs above.
4. Name it `andrew-workshop`.
5. Click **OK**.

---

## 2. Install from zip (do these in order)

1. **Add-ons** (the box icon) → open the **Add-on browser** (the box with an open-lid icon, top-left).
2. **Install from zip file**.
3. Allow unknown sources if asked.
4. Open **andrew-workshop**.
5. Install **in this order**:

   1. `plugin.video.themoviedb.helper.andrew-6.18.0.zip`
   2. `skin.arctic.fuse.3.andrew-3.3.1.zip`
   3. `plugin.video.cumination.andrew-1.2.1.zip` (optional; adult)
   4. `repository.andrew-1.0.0.zip` (optional; lets you use **Install from repository** next time)

6. Wait for **Add-on enabled** / **Skin installed**.

### Switch to the skin

**Settings → Interface → Skin → Skin → Arctic Fuse 3 (Andrew)**. Let it rebuild textures; first launch can take a minute.

### If File Manager cannot list the folder

Download the zips in a normal web browser (phone, PC, or the Kodi device), copy them into Kodi's `Downloads` folder or a USB stick, then **Install from zip file** from that local folder.

Direct zip links (open in a browser, no login):

- https://raw.githubusercontent.com/phantomgrimsalvo-svg/kodi-andrew-workshop/main/zips/plugin.video.themoviedb.helper.andrew-6.18.0.zip
- https://raw.githubusercontent.com/phantomgrimsalvo-svg/kodi-andrew-workshop/main/zips/skin.arctic.fuse.3.andrew-3.3.1.zip
- https://raw.githubusercontent.com/phantomgrimsalvo-svg/kodi-andrew-workshop/main/zips/plugin.video.cumination.andrew-1.2.1.zip
- https://raw.githubusercontent.com/phantomgrimsalvo-svg/kodi-andrew-workshop/main/zips/repository.andrew-1.0.0.zip

jsDelivr mirrors (often nicer on TV browsers):

- https://cdn.jsdelivr.net/gh/phantomgrimsalvo-svg/kodi-andrew-workshop@main/zips/plugin.video.themoviedb.helper.andrew-6.18.0.zip
- https://cdn.jsdelivr.net/gh/phantomgrimsalvo-svg/kodi-andrew-workshop@main/zips/skin.arctic.fuse.3.andrew-3.3.1.zip
- https://cdn.jsdelivr.net/gh/phantomgrimsalvo-svg/kodi-andrew-workshop@main/zips/plugin.video.cumination.andrew-1.2.1.zip
- https://cdn.jsdelivr.net/gh/phantomgrimsalvo-svg/kodi-andrew-workshop@main/zips/repository.andrew-1.0.0.zip

---

## 3. Optional: Install from repository next time

After `repository.andrew-1.0.0.zip` is installed:

1. **Add-ons → Install from repository → Andrew's Kodi Workshop**.
2. Open **Video add-ons** / **Look and feel → Skins** and install the Andrew forks from the list.

The repository reads:

- `https://phantomgrimsalvo-svg.github.io/kodi-andrew-workshop/addons.xml`

---

## What you should see after install

| Add-on | Where it appears |
|---|---|
| TMDb Helper (Andrew) | Add-ons → Video add-ons |
| Cumination (Andrew) | Add-ons → Video add-ons |
| Arctic Fuse 3 (Andrew) | Settings → Interface → Skin |

Addon ids (for logs / troubleshooting):

- `plugin.video.themoviedb.helper.andrew` 6.18.0
- `skin.arctic.fuse.3.andrew` 3.3.1
- `plugin.video.cumination.andrew` 1.2.1

The skin talks to **TMDb Helper (Andrew)**, not the stock `plugin.video.themoviedb.helper`. If widgets are empty, confirm Helper (Andrew) is enabled.
