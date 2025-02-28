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

> if you want to use the script to cluster IV-scan data;
>
> just choice the button: IV mode
> 
> if you want use same label of clustering result to class other Homologous data,such as the IV-scan and the GV-scan;
> 
> just choice the button: 'finished once and want to use the class on other'

# Subcection module

![Subcection](https://github.com/wanHAnuy/wanHAnuy/blob/main/badb18e2fd0e63c676ec1d04a03975a.png)

1. Redraw length figure
>
> both of the package of conductance and IV-scan, they all have 4 Parts:
>
> X_label(distance,voltage), Y_label(conductance,current),
>
> main feature(length , the conductance when junction fromed) and the point number of sample
>
> the length figure in conductance data package is correspond to the conductance when junction fromed in IV-scan data package
>
> now we just talk about the length figure
>
> such as the conductance peak value is 1e-5 GO,we setting the value of 'lenth value when conductance is /' to '-5' ,
>
> run and we get the length figure.
>
![length figure](https://github.com/wanHAnuy/wanHAnuy/blob/main/b33078cb140ccc8ac69a264289e7c4f.png)

2. Correlation analysis
   
> if you want to know the correlation about two different peaks or more peaks, you can try to use Correlation analysis
>
> just drag data package and run, and parameter of drawing is set in first page, and clink 'correlation run'

![Correlation analysis figure](https://github.com/wanHAnuy/wanHAnuy/blob/main/4fd96138c9c4d8407aca120cebad6e3.png)

3. Split by time

> it is very importante to analyse the fluctuation of conductance in molecular junction about time
> 
> in a data package with 1000+ single curve, we can devide 5 little package with 200,so we set the 'the number of curves in each packet ' to 200;
>
> run and we get the figure.
>
> by the way, all the operation in our script, we can get the intact data and drawing by clink 'save'.
>
> the second figure meaning the mean square error, we can clink the 'merge save' to abandon the bad data.
> 
![separated_data](https://github.com/wanHAnuy/wanHAnuy/blob/main/separated_data.png)


> and in this fingure we can observe the fluctuation of conductance in molecular junction about time
![separated_data2](https://github.com/wanHAnuy/wanHAnuy/blob/main/c6ea08317ca86c695730258aba60c89.png)
>
> and we can analyse the fluctuation of length in molecular junction about time, just clink ''

![separated_data3](https://github.com/wanHAnuy/wanHAnuy/blob/main/vfg.png)
4. Split by time and clustering
>
> we can divide by time and cluster at sametime,just clink''
![separated_data4](https://github.com/wanHAnuy/wanHAnuy/blob/main/separated_data_clustering.png)

> # don't forget to change the max value of 2D histogram!(in page 1)
> # new applcation!!! updating time 2025 -2 -28
> 1. CH SCAN! find the best number to cluster('cluster cacu'page)
> 2. IV Clustering('cluster cacu'page)
> 3. Merge saving('cluster cacu'page)
> 4. 'length' subsection
> 5. FN transform
> 6. IV data processing:'tdms'-->'npz'
> 7. IV data processing -- decapicity
> 8. psd data processing
