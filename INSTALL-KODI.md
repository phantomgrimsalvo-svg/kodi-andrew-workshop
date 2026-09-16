# Install Andrew's Kodi addons (newbie steps)

You need **Kodi 21 Omega** (Arctic Fuse 3 needs `xbmc.gui` 5.17). Fire Stick / Shield / PC all work the same. These zips are **public GitHub files** — no Cursor login, no GitHub login.

Cumination is an **adult** add-on. Install **TMDb Helper (Andrew)** before you switch to **Arctic Fuse 3 (Andrew)** — the skin talks to the Andrew helper id, not the stock one.

## Direct zip links (use these now)

Open any of these in a browser, save the file, then in Kodi: **Add-ons → Install from zip file** and pick the downloaded zip. Install **in this order**:

1. TMDb Helper (Andrew) 6.18.0  
   https://github.com/phantomgrimsalvo-svg/kodi-andrew-workshop/releases/download/v1.0.0/plugin.video.themoviedb.helper.andrew-6.18.0.zip
2. Arctic Fuse 3 (Andrew) 3.3.1  
   https://github.com/phantomgrimsalvo-svg/kodi-andrew-workshop/releases/download/v1.0.0/skin.arctic.fuse.3.andrew-3.3.1.zip
3. Cumination (Andrew) 1.2.1 (optional; adult)  
   https://github.com/phantomgrimsalvo-svg/kodi-andrew-workshop/releases/download/v1.0.0/plugin.video.cumination.andrew-1.2.1.zip
4. Workshop repository (optional, for later updates)  
   https://github.com/phantomgrimsalvo-svg/kodi-andrew-workshop/releases/download/v1.0.0/repository.andrew-1.0.0.zip

Same files as raw GitHub (no redirect; good if a TV browser chokes on the Release links):

- https://raw.githubusercontent.com/phantomgrimsalvo-svg/kodi-andrew-workshop/main/zips/plugin.video.themoviedb.helper.andrew-6.18.0.zip
- https://raw.githubusercontent.com/phantomgrimsalvo-svg/kodi-andrew-workshop/main/zips/skin.arctic.fuse.3.andrew-3.3.1.zip
- https://raw.githubusercontent.com/phantomgrimsalvo-svg/kodi-andrew-workshop/main/zips/plugin.video.cumination.andrew-1.2.1.zip
- https://raw.githubusercontent.com/phantomgrimsalvo-svg/kodi-andrew-workshop/main/zips/repository.andrew-1.0.0.zip

Release page with all four buttons: https://github.com/phantomgrimsalvo-svg/kodi-andrew-workshop/releases/tag/v1.0.0

---

## 0. One-time Kodi settings

1. Open **Settings** (gear).
2. Set the settings level to **Standard** or **Advanced** (bottom-left).
3. **System → Add-ons → Unknown sources → ON**. Confirm the warning.

Also install the **jurialmunkey** repository (needed for TMDb Helper / Arctic Fuse dependencies such as `script.module.jurialmunkey` and `script.skinvariables`):

- File Manager source: `https://kodi.jurialmunkey.net/repository.jurialmunkey/`
- Then **Add-ons → Install from zip file → jurialmunkey → repository.jurialmunkey-*.zip**

Cumination also needs **ResolveURL** (`script.module.resolveurl` and `script.module.resolveurl.xxx`). Install those from the ResolveURL / dobbelina repository you already use.

---

## 1. File Manager source (optional)

Type this exact URL as a Kodi file source (GitHub Pages; may take a few minutes the first time):

```
https://phantomgrimsalvo-svg.github.io/kodi-andrew-workshop/zips/
```

Steps:

1. **Settings → File manager → Add source**.
2. Click **\<None\>**.
3. Paste the URL above.
4. Name it `andrew-workshop`.
5. Click **OK**.
6. **Add-ons → Install from zip file → andrew-workshop** and pick each zip in the order in the Direct zip links section.

If that URL 404s (Pages still warming up), skip File Manager and use the Direct zip links.

---

## 2. Switch to the skin

**Settings → Interface → Skin → Skin → Arctic Fuse 3 (Andrew)**. First launch can sit on “building textures” for a minute.

---

## 3. Optional: Install from repository next time

After `repository.andrew-1.0.0.zip` is installed:

1. **Add-ons → Install from repository → Andrew's Kodi Workshop**.
2. Open **Video add-ons** or **Look and feel → Skins** and install the Andrew forks.

The repository reads:

```
https://raw.githubusercontent.com/phantomgrimsalvo-svg/kodi-andrew-workshop/main/addons.xml
```

---

## What you should see after install

| Add-on | Where it appears | Id |
|---|---|---|
| TMDb Helper (Andrew) | Add-ons → Video add-ons | `plugin.video.themoviedb.helper.andrew` 6.18.0 |
| Cumination (Andrew) | Add-ons → Video add-ons | `plugin.video.cumination.andrew` 1.2.1 |
| Arctic Fuse 3 (Andrew) | Settings → Interface → Skin | `skin.arctic.fuse.3.andrew` 3.3.1 |

If Arctic widgets are empty, confirm **TMDb Helper (Andrew)** is enabled — not the original `plugin.video.themoviedb.helper`.
