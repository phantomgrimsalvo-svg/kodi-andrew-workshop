# kodi-andrew-workshop update (prepared 2026-10-06)
Copy tools/, repository.andrew/addon.xml (v1.2.0) and optionally .github/workflows/publish-kodi-repo.yml
into a clone of phantomgrimsalvo-svg/kodi-andrew-workshop (main), then:
    python3 tools/build_repo.py   # downloads cumination 1.2.10 + skin 3.3.2 from their GitHub releases (sha256-pinned),
                                  # builds repository.andrew-1.2.0.zip, regenerates addons.xml/.md5, index.html, zips/index.html
    git add -A && git commit -m "Publish Cumination 1.2.10, Arctic Fuse 3 3.3.2, repository.andrew 1.2.0" && git push
If the push is refused for .github/workflows/*, drop that file and push the rest.
Expected addons.xml.md5 after build: ce1a730fe56eafe40540c1fbef194f1b
