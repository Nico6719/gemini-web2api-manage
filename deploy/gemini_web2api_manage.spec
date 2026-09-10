# -*- mode: python ; coding: utf-8 -*-
"""PyInstaller spec for the Gemini Web2API Manage server."""

from pathlib import Path
import sys

# SPECPATH 指向项目根目录下的 deploy 目录，
# 因此向上一级才是项目根目录。
ROOT = Path(SPECPATH).resolve().parent

UPSTREAM = ROOT / "_upstream"

if str(UPSTREAM) not in sys.path:
    sys.path.insert(0, str(UPSTREAM))

from PyInstaller.utils.hooks import collect_submodules


# 前端源码构建产物的实际位置
ADMIN_STATIC = ROOT / "gemini_web2api_manage" / "admin_static"


hiddenimports = (
    collect_submodules("gemini_web2api")
    + collect_submodules("gemini_web2api_manage")
)


a = Analysis(
    [
        str(ROOT / "gemini_web2api_manage" / "__main__.py"),
    ],
    pathex=[
        str(ROOT),
        str(UPSTREAM),
    ],
    binaries=[],
    datas=[
        # 左侧：源码中的实际目录
        # 右侧：程序运行时实际读取的目录
        (
            str(ADMIN_STATIC),
            "gemini_web2api/admin_static",
        ),
    ],
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)


pyz = PYZ(a.pure)


exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="gemini-web2api-manage",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
