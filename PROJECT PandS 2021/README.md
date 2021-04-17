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

# Variable analysed

In this text file, the variables used for this demonstration are listed.
The file also provides with an overview of some basic statistical data such as count, mean, min, max...
Observing the table, one can note that there seems to be an important variation in size of petal length and width amonst the 3 studied species. For instance, the minimun measeared petal width is 0.1cm while its maximum value is 2.5cm. The widest petal is 25 times larger than the smallest. 

Similarly, the shortest measured petal is 1cm long while the longest is 6.9cm, almost 7 times longer.
Comparatively, it appears that the sepal measurements between the 3 flower species are more coherent, with a maximum length and width about 2 times larger than the minimum value collected. 

It seems like the disparities between the flower species are more important amongst the sepal measurements than petal's. This can be also seen by compring the mean value for the sepal and petal measurements to the maximum value collected for these variables. 

# Petal Length Histograms 

Here, two histograms are observed: hist_petal_length.png and histogram hist_petal_length.png.

First, let's observe the hist_petal_length.png histogram. This histogram display the repartition frequency of the variable 'petal length'. Looking at the histogram, we can see 2 blocks. One smaller one recording a quite high frequency of short petal length (from 1 to 2cm long). The 2nd block displays a repartiion more common of the data collected (3 to 7cm long, with the highest frequency between 4 and 6cm). 

Now, observing the 2nd histogram hist_petal_length.png, we get an insight of the repartion of the petal length measurement by flower type. The one smaller observed in the previous histogram is exclusively consisting of dqtq collected from Iris Setosa. The second block, more blended is composed of data from Iris Versicolor and Iris Virginica flowers. 
Taking only the petal length variable into consideration, there seems to be a sharp differentiation between the Iris setosa and the two other flower types. 






__________________________________


These histogram are the occasion to observe how the data points are distributed with respect to frequency.
See histograms: PetalLength.png, PetalWidth.png, SepalLength.png, SepalWidth.png
>> Observing these histograms, we notice that while sepal width and lenght appear to be normally distributed, petal length and width are unevenly distributed.


Diving down further into the details, the same analysis is carried out on the flower type/spiecies level. 
For each species, similar histograms are generated through Python. 
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ANALYSE AND OBSER+VE HERE





When superposed, XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX ANALYSE AND OBSER+VE HERE
