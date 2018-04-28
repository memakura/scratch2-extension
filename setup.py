# -*- coding: utf-8 -*-

from cx_Freeze import setup, Executable

# --- for resolving KeyError: 'TCL_LIBRARY' ---
import os.path
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')
# ------

name = "s2extest"
version = "1.0.0"
description = "Scratch 2 extension test"
author = "memakura"
url = "https://github.com/memakura/scratch2-extension"

# バージョンアップ管理したい場合は変更しない
upgrade_code = "{7A37B0C0-64E1-479D-A64C-6CCFCB2E1149}"

# ----------------------------------------------------------------
# セットアップ
# ----------------------------------------------------------------
shortcut_table = [
    ('DesktopShortcut',        # Shortcut
     'DesktopFolder',          # Directory_
     "s2extest",               # Name
     'TARGETDIR',              # Component_
     '[TARGETDIR]s2extest.exe',   # Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     'TARGETDIR',              # WkDir
    )
    ]

# Table dictionary
msi_data = {'Shortcut': shortcut_table}

# 追加モジュールで必要なものを packages に入れる
build_exe_options = {'packages': ["asyncio"],
                     'excludes': [],
                     'includes': [],
                     'include_files': [
                         "icons/",
                         ("test.s2e", "00scratch/test.s2e"),
                         ("s2extest.sb2", "00scratch/s2extest.sb2")
                         ]
}

bdist_msi_options = {'upgrade_code': upgrade_code,
                     'add_to_path': False,
                     'data': msi_data
}

options = {
    'build_exe': build_exe_options,
    'bdist_msi': bdist_msi_options
}

# CUI : None
base = None 
# GUI :  'Win32GUI' if sys.platform == 'win32' else None

icon = "icons/icon_256x256.ico"

# exe にしたい python ファイルを指定
exe = Executable(script="s2extest.py",
                 targetName="s2extest.exe",
                 base=base,
                 icon=icon
                 )

# セットアップ
setup(name=name,
      version=version,
      author=author,
      url=url,
      description=description,
      options=options,
      executables=[exe]
      )
