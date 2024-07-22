# InJunction STM-BJ data processing
# 

> The UI interface is created by Mr.Wanderson-Magalhaes, more detail please refer:
>
> https://github.com/Wanderson-Magalhaes/Modern_GUI_PyDracula_PySide6_or_PyQt6
>
> some code from:XMe_DataAnalysis
>
> https://github.com/Pilab-XMU/XMe_DataAnalysis
>
> Python 3.10 ,The package refer to requirements.txt


# Multiple approach
> The script invove 3 main data for STM-BJ,and we have developed various tpye ways for classing, clustering,drawing fig,and data processing.
> 
![the icon](https://github.com/wanHAnuy/wanHAnuy/blob/main/fig1.png)
>
> **OPEN MAIN PAGE**
>
> so fist, when you has prepared all files and environment,you can type that code on terminal to oackage it (about 150MB) or just run main.py to open:
> 
```
pyinstaller -F --icon=icon.ico main.py --hidden-import matplotlib.backends.backend_ps
```
![the main page](https://github.com/wanHAnuy/wanHAnuy/blob/main/fig2.png)

# CLUSTER module
Now let us introduce the fist module - CLUSTER!!
> Default algorithm is the most effictive way to cluster. clink the butten cluster cacu, and you will look that parameter. 


> Just clink open or drag the file(single_trance.npz/IV_data.npz) on the interface.
> 
> Such as Default algorithm module like that picture.
>
> We use Tailor & 1 D HIS + No dimensionality reduction(in fact the single 1d his data has been reducted by PCA).
>
>  if you want look the pre-data for cluster --Tailor & 1 D HIS,just clink single preview.
