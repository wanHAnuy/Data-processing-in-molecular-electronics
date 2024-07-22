# InJunction STM-BJ data processing
# 

> The UI interface is created by Mr.Wanderson-Magalhaes, more detail please refer:
>
>  https://github.com/Wanderson-Magalhaes/Modern_GUI_PyDracula_PySide6_or_PyQt6
>
> some sode from that project:XMe_DataAnalysis
>
> https://github.com/Pilab-XMU/XMe_DataAnalysis


# Multiple Themes
![PyDracula_Default_Dark](https://user-images.githubusercontent.com/60605512/112993874-0b647700-9140-11eb-8670-61322d70dbe3.png)


# High DPI
> Qt Widgets is an old technology and does not have a good support for high DPI settings, making these images look distorted when your system has DPI applied above 100%.
You can minimize this problem using a workaround by applying this code below in "main.py" just below the import of the Qt modules.
```python
# ADJUST QT FONT DPI FOR HIGHT SCALE
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96"
```


> **modules/resources_rc.py**: "resource.qrc" file compiled for python using the command: ```pyside6-rcc resources.qrc -o resources_rc.py```.

> **modules/ui_functions.py**: add here only functions related to the user interface / GUI.

**Malicious programs will not be added**!



