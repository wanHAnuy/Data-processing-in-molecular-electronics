import sys
import os
from cx_Freeze import setup, Executable

files = ['icon.ico', 'themes/']

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="icon.ico"
)

setup(
    name="Data processing App",
    version="1.8.1",
    description=" Single-molecule research only.",
    author="Wang Haoyu",
    options={'build_exe': {'include_files': files}},
    executables=[target]

)
