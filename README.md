# InJunction: STM-BJ data processing
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
> Default algorithm is the most effictive way to cluster. clink 'cluster cacu', and you will look that parameter. 
![the cluster](https://github.com/wanHAnuy/wanHAnuy/blob/main/fig4.png)

> Just clink open or drag the file(single_trance.npz/IV_data.npz) on the interface.
> 
> Such as Default algorithm module like that picture.
>
> We use Tailor & 1 D HIS + No dimensionality reduction(in fact the single 1d his data has been reducted by PCA).
>
> 'UMAP + Tailor & 1 D HIS+ GMM' is also recommended!
>
> If you want look the pre-data for clustering --Tailor & 1 D HIS,just clink 'single preview'.


# Example

Single trance test

![single trance](https://github.com/wanHAnuy/wanHAnuy/blob/main/single_trance_1.png)
>
> So you can see 4 picture meaning different approch to pre-processing raw data.
>
> Tailor is meaning we cut the increased range of break junction test and the red box is the data range.
>
> The range you can choice molecular peak situation.
>
> You can also choice the different data-type and different mode to cluster.
>
> and if you clink 'single_save',you can get the PNG and data for draw.
>
> Now let us talk about the clustering, just clink 'clustering run'


Conductance data cluster test

![big_fig](https://github.com/wanHAnuy/wanHAnuy/blob/main/merged_image2.png)
>
> it contain all the result of clustering, and we can save all figure, data, and data for draw.
>
> just clink 'clustering save'
>
> that is very useful! and if we need to merge the same class.such as 'class 2' and 'class 3' is target signal.
>
> they are the single-stage. 
> 
> just clink 'Merge save'and  choice class 1 and class 3

Merge save test

![merge_fig](https://github.com/wanHAnuy/wanHAnuy/blob/main/class%5B1%2C%203%5D_73.2%25.png)

> the detail and data will save at same time!
