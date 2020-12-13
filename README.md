README
================

# Prediction of Wine Quality based on Physicochemical Tests

-   author: Jiajie (Joshua) Lim, Ling (Elina) Lin, Jiacheng Wang, Kangyu
    (Mark) Wang

This project aims to build machine learning models that predict a given
wine’s quality based on its physicochemical characters. It uses
classification and regression techniques k-nearest neighbors (k-NN) and
support vector machines (SVMs) with RBF kernel.

## Data

The data sets used in this project are of the prediction of wine quality
based on physicochemical tests, related to red and white vinho verde
wine samples, from the north of Portugal. The data were created by Paulo
Cortez et al at the University of Minho, Guimarães, Portugal (Cortez et
al. 2009). It was sourced from the UCI Machine Learning Repository (Dua
and Graff 2017) and can be found
[here](https://archive.ics.uci.edu/ml/datasets/Wine+Quality),
specifically this
[file](https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/).
The data provided only have physicochemical (inputs) and sensory (the
output) variables available (e.g. there is no data about grape types,
wine brand, wine selling price, etc.). There are a total of 4898
instances in our combined dataset of red wine and white wine.

## Research Question

From the data set provided, we are interested in predicting the wine
quality (white wine and red wine) based on the physicochemical tests. We
are engaged in predicting the quality score (score between 0 and 10) of
a wine based on variables including:

-   fixed acidity: most acids involved with wine or fixed or nonvolatile
    (do not evaporate readily).
-   volatile acidity: the amount of acetic acid in wine, which at too
    high of levels can lead to an unpleasant, vinegar taste.
-   citric acid: found in small quantities, citric acid can add
    ‘freshness’ and flavor to wines.
-   residual sugar: the amount of sugar remaining after fermentation
    stops, it’s rare to find wines with less than 1 gram/liter and wines
    with greater than 45 grams/liter are considered sweet.
-   chlorides: the amount of salt in the wine.
-   free sulfur dioxide: the free form of SO2 exists in equilibrium
    between molecular SO2 (as a dissolved gas) and bisulfite ion; it
    prevents microbial growth and the oxidation of wine.
-   total sulfur dioxide: amount of free and bound forms of S02; in low
    concentrations, SO2 is mostly undetectable in wine, but at free SO2
    concentrations over 50 ppm, SO2 becomes evident in the nose and
    taste of wine.
-   density: the density of wine is close to that of water depending on
    the percent alcohol and sugar content.
-   pH: describes how acidic or basic a wine is on a scale from 0 (very
    acidic) to 14 (very basic); most wines are between 3-4 on the pH
    scale.
-   sulphates: a wine additive which can contribute to sulfur dioxide
    gas (S02) levels, wich acts as an antimicrobial and antioxidant.
-   alcohol: the percent alcohol content of the wine.

Moreover, we will also attempt to look for the correlation between the
explanatory variables, to see if there are any multicollinearity occurs.
Assuming all variables are independent, if the variables are correlated
and the degree of correlation between variables is high enough, it can
be a problem when fitting the model and the result may not be accurate.

## Analysis

The k-nearest neighbors (k-nn) algorithm will be used to build a
classification model to predict the quality score of the wine, including
white and red wine. All variables included in the original dataset will
be used in fitting our model. Since there are no missing values in our
dataset, there is no need for any imputation. Also, the support vector
machines (SVMs) with RBF kernel will be our second model in predicting
the quality score of wine. We are hoping to see improvement in our
model, given the support vectors. Most of our analysis will be done
using Python and R programming languages (R Core Team 2020; Van Rossum
and Drake 2009).

## Exploratory Data Analysis (EDA)

EDA table:

-   We will be using python `data.info()` to check for information on
    our data. From this table, we can check for the data type of each
    column and look for missing values contained in every column. If
    there are any missing values, we would want to clean the data first
    before proceeding with any analysis. Also, `data.describe` is also
    useful in identifying the minimum, maximum, and mean of each
    numerical columns. We would want to double-check if the values
    returned from the table are ‘acceptable.’

EDA figure:

-   We will be plotting a histogram on all the variables to gain insight
    into the probability distribution that the dataset follows. With a
    histogram, it is easy for us to see how the data is distributed.
    Also, scatterplot will be used to show the relationship between two
    variables. If the points between two variables resemble a straight
    line, this indicates that the relationship between the two variables
    we have is approximately linear.

## Sharing Results of Analysis

We would compare the results of our cross-validation analysis to test
analysis and see whether there exists any overfitting or underfitting in
our model. Also, we would return the confusion matrix of model
performance on the test data to check for misclassification errors.

## Usage

To replicate the analysis, clone this GitHub repository, install the
[dependencies](#dependencies) listed below, and run the following
commands at the command line/terminal from the root directory of this
project:

    # download data
    python src/Download_file.py --source=https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv --destination=data/winequality-red.csv
    python src/Download_file.py --source=https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv --destination=data/winequality-white.csv
    # pre-process data 
    python src/Preprocessing.py --raw_white=data/winequality-white.csv --raw_red=data/winequality-red.csv --preprocessed_train=data/winequality-train.csv --preprocessed_test=data/winequality-test.csv
    # create exploratory data visualizations
    python src/EDA.py --preprocessed_train=data/winequality-train.csv --quality_count_path=results/quality_count.png --quality_all_variables_path=results/quality_all_variables.png
    # tune and test model
    python src/ML_analyses.py --preprocessed_train=data/winequality-train.csv --preprocessed_test=data/winequality-test.csv --results_path=results
    # render final report
    Rscript -e "rmarkdown::render('doc/wine_quality_predict_report.Rmd')"

## Dependencies

-   Python 3.8.3 and Python packages:
    -   ipykernel
    -   docopt==0.6.2
    -   pandas==0.24.2
    -   altair&gt;=4.1.0
    -   scikit-learn&gt;=0.23.2
-   R version 4.0.3 and R packages:
    -   knitr==1.29
    -   tidyverse==1.2.1
    -   numpy==1.19.1
    -   dplyr==1.0.2
    -   readr==1.4.0
-   GNU make 4.2.1

# References

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-cortez2009modeling" class="csl-entry">

Cortez, Paulo, António Cerdeira, Fernando Almeida, Telmo Matos, and José
Reis. 2009. “Modeling Wine Preferences by Data Mining from
Physicochemical Properties.” *Decision Support Systems* 47 (4): 547–53.

</div>

<div id="ref-Dua2019" class="csl-entry">

Dua, Dheeru, and Casey Graff. 2017. “UCI Machine Learning Repository.”
University of California, Irvine, School of Information; Computer
Sciences. <http://archive.ics.uci.edu/ml>.

</div>

<div id="ref-R" class="csl-entry">

R Core Team. 2020. *R: A Language and Environment for Statistical
Computing*. Vienna, Austria: R Foundation for Statistical Computing.
<https://www.R-project.org/>.

</div>

<div id="ref-Python" class="csl-entry">

Van Rossum, Guido, and Fred L. Drake. 2009. *Python 3 Reference Manual*.
Scotts Valley, CA: CreateSpace.

</div>

</div>
