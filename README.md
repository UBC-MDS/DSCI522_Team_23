Prediction of Wine Quality based on Physicochemical Tests
=========================================================

-   author: Jiajie (Joshua) Lim, Ling (Elina) Lin, Jiacheng Wang, Kangyu
    (Mark) Wang

This project aims to build machine learning models that predict a given
wine’s quality based on its physicochemical characters. It uses
classification and regression techniques k-nearest neighbors (k-NN) and
support vector machines (SVMs) with RBF kernel.

Data
----

The data sets used in this project are of the prediction of wine quality
based on physicochemical tests, related to red and white vinho verde
wine samples, from the north of Portugal. The data were created by Paulo
Cortez et al at the University of Minho, Guimarães, Portugal (2009). It
was sourced from the UCI Machine Learning Repository (Dua and Graff
2017) and can be found
[here](https://archive.ics.uci.edu/ml/datasets/Wine+Quality),
specifically this
[file](https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/).
The data provided only have physicochemical (inputs) and sensory (the
output) variables available (e.g. there is no data about grape types,
wine brand, wine selling price, etc.). There are a total of 4898
instances in our combined dataset of red wine and white wine.

Research Question
-----------------

From the data set provided, we are interested in predicting the wine
quality (white wine and red wine) based on the physicochemical tests. We
are engaged in predicting the quality score (score between 0 and 10) of
a wine based on variables including:

-   fixed acidity
-   volatile acidity
-   citric acid
-   residual sugar
-   chlorides
-   free sulfur dioxide
-   total sulfur dioxide
-   density
-   pH
-   sulphates
-   alcohol

Moreover, we will also attempt to look for the correlation between the
explanatory variables, to see if there are any multicollinearity occurs.
Assuming all variables are independent, if the variables are correlated
and the degree of correlation between variables is high enough, it can
be a problem when fitting the model and the result may not be accurate.

Analysis
--------

The k-nearest neighbors (k-nn) algorithm will be used to build a
regression model to predict the quality score of the wine, including
white and red wine. All variables included in the original dataset will
be used in fitting our model. Since there are no missing values in our
dataset, there is no need for any imputation. Also, the ridge regression model
will be our second model in predicting the quality score of wine. We are hoping to see improvement in our
model. Most of our analysis will be done
using Python and R programming languages (R Core Team 2020; Van Rossum
and Drake 2009).

Exploratory Data Analysis (EDA)
-------------------------------

EDA table:

-   We will be using python `data.info()` to check for information on
    our data. From this table, we can check for the data type of each
    column and look for missing values contained in every column. If
    there are any missing values, we would want to clean the data first
    before proceeding with any analysis. Also, `data.describe` is also
    useful in identifying the minimum, maximum, and mean of each
    numerical columns. We would want to double-check if the values
    returned from the table are ‘acceptable’.

EDA figure:

-   We will be plotting a histogram on all the variables to gain insight
    into the probability distribution that the dataset follows. With a
    histogram, it is easy for us to see how the data is distributed.
    Also, scatterplot will be used to show the relationship between two
    variables. If the points between two variables resemble a straight
    line, this indicates that the relationship between the two variables
    we have is approximately linear.

Sharing Results of Analysis
---------------------------

We would compare the results of our cross-validation analysis to test
analysis and see whether there exists any overfitting or underfitting in
our model. Also, we would return the confusion matrix of model
performance on the test data to check for misclassification errors.

Report
-----
The final report can be found [here](https://htmlpreview.github.io/?https://raw.githubusercontent.com/UBC-MDS/DSCI522_Team_23/main/doc/wine_quality_predict_report.html).

Usage
-----

#### 1. Using Docker

note - the instructions in this section also depends on running this in a unix shell (e.g., terminal or Git Bash)

To replicate the analysis, install Docker. Then clone this GitHub repository and run the following command at the command line/terminal from the root directory of this project:

    docker run --rm -v /$(pwd):/home/rstudio/project dsci522_t23 make -C /home/rstudio/project all

To reset the repo to a clean state, with no intermediate or results files, run the following command at the command line/terminal from the root directory of this project:

    docker run --rm -v /$(pwd):/home/rstudio/project dsci522_t23 make -C /home/rstudio/project clean

#### 2. Without Using Docker

To replicate the analysis, clone this GitHub repository, install the
[dependencies](#dependencies) listed below, and run the following
command at the command line/terminal from the root directory of this
project:

    make all

To reset the repo to a clean state, with no intermediate or results
files, run the following command at the command line/terminal from the
root directory of this project:

    make clean

Dependencies
------------

-   Python 3.8.3 and Python packages:
    -   ipykernel==5.1.2
    -   docopt==0.6.2
    -   pandas==0.25.1
    -   altair==4.1.0
    -   scikit-learn>=0.21.3

-   R version 4.0.3 and R packages:
    -   knitr==1.30
    -   tidyverse==1.3.0
    -   dplyr==2.0.0
    -   readr==1.4.0
  
-   GNU make 4.2.1
  
References
==========

Cortez, Paulo, António Cerdeira, Fernando Almeida, Telmo Matos, and José
Reis. 2009. “Modeling Wine Preferences by Data Mining from
Physicochemical Properties.” *Decision Support Systems* 47 (4): 547–53.

Dua, Dheeru, and Casey Graff. 2017. “UCI Machine Learning Repository.”
University of California, Irvine, School of Information; Computer
Sciences. <http://archive.ics.uci.edu/ml>.

R Core Team. 2020. *R: A Language and Environment for Statistical
Computing*. Vienna, Austria: R Foundation for Statistical Computing.
<https://www.R-project.org/>.

Van Rossum, Guido, and Fred L. Drake. 2009. *Python 3 Reference Manual*.
Scotts Valley, CA: CreateSpace.
