# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=['.'],
    binaries=[],
    datas=[('.\\*.dat', '.'), ('C:\\Users\\dmxth\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\sitepackages\\mediapipe\\modules', 'mediapipe\\modules'),('C:\\PycharmProjects\\please\\gaze\\gaze_tracking', 'please\\gaze\\.'),('C:\\PycharmProjects\\please\\gaze\\gaze_tracking\\*.py', 'gaze\\gaze_tracking\\.'),],
    hiddenimports=['pyautogui', 'dlib', 'win32', 'win32gui', 'win32con'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)
