# REPORT - THE FISHER IRIS DATASET

## SECTION 1 - Introduction to the Iris Flowers Dataset

This dataset was introduced in 1936 by  the British statistician and biologist Ronald Fisher in his research paper 'The use of multiple measurements in taxonomic problems'.
The majority of the data was collected at the Gaspe Peninsula, in Canada.

The dataset consists of 150 records. 50 records for each of the 3 iris spicies: 
* Iris setosa
* Iris virginica
* Iris versicolor

For each species 4 features/variables were collected: 
* Sepals lenght (cm)
* Sepals width (cm)
* Petals lenght (cm)
* Petals width (cm)

Over the years, the Iris flower data set has become a classic test case for numerous statistical and data analysis techniques.
In this demonstration, python language will be leverage to analyse the Irish Flower dataset. From this analysis should emerge trends that will help provide an interpretation to the data.  

## SECTION 2 - Observations

In order to generates the data plots and text file used for this investigation, please run the program analysis.py

Analysis.py will call and execute two separate programs (IrisFlowersPlot.py and variable.py). These program output and save on your local directories the plot files (png) and text file used during this analysis.

Three other programs were also added to this GITHUB directory.
These programs are not leveraged or analysed in this demonstration, they are there if user wishes to visualize the variable data at a flower type level.
These programs are:
* setosa.py
* versicolor.py
* virginica.py

The three above mentioned programs will output histogram plots for each variable (petal lengt/width, sepal length/width), at a species level.

After running analysis.py, several files will be saved on your local machine:
* variable.txt
* petal_scatter_plot.png
* sepal_scatter_plot.png
* hist_petal_length.png
* hist_petal_width.png
* hist_sepal_length.png
* hist_sepal_width.png
* hist_petal_length_overlap.png
* hist_petal_width_overlap.png
* hist_sepal_length_overlap.png
* hist_sepal_width_overlap.png

###  Variable analysed

In this text file, the variables used for this demonstration are listed.
The file also provides with an overview of some basic statistical data such as count, mean, min, max...
Observing the table, one can note that there seems to be an important variation in size of petal length and width amonst the 3 studied species. For instance, the minimun measeared petal width is 0.1cm while its maximum value is 2.5cm. The widest petal is 25 times larger than the smallest. 

Similarly, the shortest measured petal is 1cm long while the longest is 6.9cm, almost 7 times longer.
Comparatively, it appears that the sepal measurements between the 3 flower species are more coherent, with a maximum length and width about 2 times larger than the minimum value collected. 

It seems like the disparities between the flower species are more important amongst the sepal measurements than petal's. This can be also seen by comparing the mean value for the sepal and petal measurements to the maximum value collected for these variables. 

### Petal Length Histograms 

Here, two histograms are observed: hist_petal_length.png and histogram hist_petal_length_overlap.png.
 
First, let's observe the hist_petal_length.png histogram. This histogram displays the repartition frequency of the variable 'petal length'. Looking at the histogram, we can see 2 blocks, or cluster. The smaller one is recording quite a high frequency of short petal length (from 1 to 2cm long). The 2nd block displays a repartiion more normal of the data collected (3 to 7cm long, with the highest frequency between 4 and 6cm). 

Observing the 2nd histogram hist_petal_length.png, we get an insight of the repartion of the petal length measurement by flower type. The smaller one, observed in the previous histogram, consists exclusively of data collected from Iris Setosa. The second block, more blended is composed of data from Iris Versicolor and Iris Virginica flowers. 
Taking only the petal length variable into consideration, there seems to be a sharp differentiation between the Iris setosa and the two other flower types. In the second cluster, iris versicolor and iris virginica barely overlap, meaning this variable could be used to differentiate the 3 flower types.

### Petal Width Histograms

Here, two histograms are observed: hist_petal_width.png and histogram hist_petal_width_overlap.png.

First, let's observe the hist_petal_width.png histogram. Similarly to the petal lenght histogram, we can disctinctly observe a first block, with high frequency between 0 and 0.5cm. The second block appears more coherent, with most of the petal width measured between 1.25 and 2.5cm. The second block have more even distribution of the frequency of the petal width, while the first block appears to  

The second histogram is similar to the previous one, but it presents each flower species data in a different color. With this insight, we can notice that once again that the setosa petal width measurment follow a trend very different from versicolor and virginica flowers. 
Based on the petal length and width variables, it seems like the Iris setosa flowers have petal caracteristics deferienciating them from the 2 other flower species. It can be see by observing the blue block on this histogram vs the other red and green block. 

### Sepal Length Histogram

Here, two histograms are observed: hist_sepal_length.png and histogram hist_sepal_length_overlap.png.

Observing the first histogram, hist_sepal_length.png, the repartition of the data accross the 3 species seems to be homogeneous, with most of the data points between 4.75cm and 6.75cm. 
If switching to the detailed version of this histogram, hist_length_overlap.png, we can observe the Iris setosa (blue) overlapping on Iris versicolor (red), and the Iris versicolor overlapping the Iris virgnica (green). 
The sepal length data points appears as uniformly distributed. 

### Sepal Width Histogram

Here, two histograms are observed: hist_sepal_width.png and histogram hist_sepal_width_overlap.png.

Observing both histograms, it appears that the data of all flower species is uniformly distributed. 
The majority of the datapoints are distributed between 2.5cm and 4cm width. Looking at the overlaping histogram, the Iris virginica data points (green) are almost entirely covered, meaning it is matching the value of both Iris setosa and Iris virginica flowers. 

### Histogram summary

In a nutshell, based on the above analysis of the histograms, several observations can be made:
1. The distribution of the Iris setosa flower petals is totally different from the two other flower types.
2. Sepal length and sepal width can't be used to differentiate the flower species as the datapoints for these variables were overlapping for all 3 flower types.
3. The petal length variable can be used to differentiate the 3 different iris species.

### Petal Scatter plot

After observing and commenting on the histograms of each of the 4 collected variables, we'll know observe the scatter plots for petal and sepal variables.
Scatter plot are a good way to visualize 2 variables that pair well together and that way, have a visual representation of their relationship.
First comment when observing the scatter plots, is the linear repartition of the data points between petal length and petal width. Here the petal scatter plot display 2 distincs clusters, the first one, in blue in the file petal_scatter_plot.png, represents the setosa flowers. Once again, this flower type features are easily set apart from the two other iris species. The relationship between petal width and length is also strong. 
In the second cluster, virginica and versicolor flowers are distributed in a linear fashion as well. Within this cluster there is a clear disctinction between the 2 species. 
Based on this scatter plot, the petal feature can be used a differentiator to tell the 3 flower species apart.

### Sepal Scatter Plot

The second scatter plot, speal_scatter_plot.png, doesn't present a linear repartition of the data points the way the petal variable does.
Two clusters can be spotted. The first one, containing the greatest value for the sepal width variable, is representing the iris setosa flower. The second cluster contains the two other flower types. In this cluster the data points are overlapped and it is impossible to leverage this data to differentiate versicolor flowers from the virginica flowers. 

__________________________________


These histogram are the occasion to observe how the data points are distributed with respect to frequency.
See histograms: PetalLength.png, PetalWidth.png, SepalLength.png, SepalWidth.png
>> Observing these histograms, we notice that while sepal width and lenght appear to be normally distributed, petal length and width are unevenly distributed.


Diving down further into the details, the same analysis is carried out on the flower type/spiecies level. 
For each species, similar histograms are generated through Python. 
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ANALYSE AND OBSER+VE HERE





When superposed, XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ANALYSE AND OBSER+VE HERE
