import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"],"excludes": ["tkinter"],
                     "include_files":["conf/"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
baseplt = None
if sys.platform == "win32":
    baseplt = "Win32GUI"

target = Executable(
    script="qmdz_main.py",
    base= baseplt,
    compress=False,
    copyDependentFiles=True,
    appendScriptToExe=True,
    appendScriptToLibrary=False,
    icon="icons/GRMS.ico",
    shortcutName="gas-sensing_resistors measurement system",
    shortcutDir="DesktopFolder"
    )

setup( 
	name = "GRMS2",
    version = "0.1",
    author="cygnushan",
    description = "gas-sensing_resistors measurement software",
    options = {"build_exe": build_exe_options},
    executables = [target]
    )



# python setup.py build
# python setup.py bdist_msi