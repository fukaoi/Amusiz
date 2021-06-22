<div align="center">
  <img src="https://raw.githubusercontent.com/mirkobrombin/Amusiz/master/data/pm.mirko.Amusiz.svg" width="64">
  <h1 align="center">Amusiz</h1>
  <p align="center">An Amazon Music client for Linux (unpretentious)</p>
</div>

<br/>

<div align="center">
  <a href="https://www.codefactor.io/repository/github/mirkobrombin/amusiz">
    <img src="https://www.codefactor.io/repository/github/mirkobrombin/amusiz/badge" alt="CodeFactor" />
  </a>
  <a href="https://github.com/mirkobrombin/Amusiz/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/License-GPL--3.0-blue.svg">
  </a>
  <a href="https://github.com/mirkobrombin/Amusiz/actions">
    <img src="https://github.com/mirkobrombin/Amusiz/workflows/Build%20release%20packages/badge.svg">
  </a>
  <a href="https://aur.archlinux.org/packages/amusiz/">
    <img alt="AUR version" src="https://img.shields.io/aur/version/amusiz">
  </a>
</div>

<br />

<div align="center">
    <img  src="https://raw.githubusercontent.com/mirkobrombin/Amusiz/main/data/screenshot.png">
</div>

## ↗️ Install
You can install Amusiz in multiple ways, choose your favorite.

### 🚀 AppImage
[Here](https://github.com/mirkobrombin/Amusiz/releases) you can find the latest AppImage build.

### AUR
There is the official package of Amusiz on AUR for ArchLinux and derivatives.

<a href='https://aur.archlinux.org/packages/amusiz/'>
  <img alt="AUR version" src="https://img.shields.io/aur/version/amusiz?style=for-the-badge">
</a>

### Snap
[![Get it from the Snap Store](https://snapcraft.io/static/images/badges/en/snap-store-black.svg)](https://snapcraft.io/amusiz)

### Build dependencies
- meson
- ninja
- libhandy
- WebKit2

### Know issues
**Amusiz ask me to re-login each time**  
Choose the correct language from the preferences.

### 🛠️ Build
```bash
meson build
cd build
ninja install
```
