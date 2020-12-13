Prediction of Wine Quality based on Physicochemical Tests
================
JiaJie (JOSHUA) Lim, Ling (ELINA) Lin
2020/11/26 (updated: 2020-12-12)

-   [Summary](#summary)
-   [Introduction](#introduction)
-   [Methods](#methods)
    -   [Data](#data)
    -   [Analysis](#analysis)
-   [Results & Discussion](#results-discussion)
-   [References](#references)

# Summary

With the wine quality data, we are attempting to build a regression
model to help us identify the best red and white variants of the
Portuguese “Vinho Verde” wine. We plan to build a predictive regression
model that can effectively predict the wine quality score given the
physicochemical tests variable.

Our final regression model- the k-nearest neighbors (k-NN) regressor
performs fairly well on an unseen test data set, with an RMSE score of
0.7171.

A lower value of RMSE indicates a better fit and it is a good measure of
how accurate our model predicts the response. From our result, our RMSE
score for the test set is pretty similar to the RMSE score for the
validation set. There is no overfitting nor underfitting problems in our
model.

We selected the k-NN regressor as our final model after making a
comparison with the baseline model, dummy regressor and the ridge
regressor based on the mean cross-validation RMSE score with
hyperparameter tuning. We then used the best-tuned hyperparameter, k= 16
for k-NN regressor and alpha=10 for ridge regressor to obtain an overall
RME score for our training set. We can see that it is obvious the k-NN
regressor has a lower RMSE score compared to other models.

| Model            | RMSE.on.train.set |
|:-----------------|------------------:|
| dummy\_regressor |             0.873 |
| Ridge\_regressor |             0.734 |
| K-nn\_Regressor  |             0.637 |

Table 1: RMSE Score for All Models Training Set

The model we obtained may not be the best model to be used in the
industry to predict the wine quality score since there are still spaces
for improvement to reduce the RMSE score. Thus we recommend continuing
study to improve this prediction model before we use this in production.

# Introduction

As wine tasting is gaining increasing popularity, more efficient and
lower-cost wine quality assessments are of urgent interest for the wine
industry to support the growing consumption. Wine certification is an
essential issue within such context and quality assessment is the key
component of certification. Wine quality is generally determined by two
types of tests: physiochemical (e.g. pH) tests and sensory (e.g. wine
expert assessments) tests (Ebeler 1999). The relationship between
chemical composition and human taste preferences is complex and not
explicitly known (Legin et al. 2003). Wine quality assurance still
relies heavily on human expertise, thus time-consuming and expensive.

Researchers have explored the usage of machine learning techniques to
assess wine quality, but still a great scope for improvement. Here we
ask if we can use a machine learning algorithm to predict the quality of
wine based on the physiochemical features. If a machine learning
algorithm can successfully predict and quantify complex human sensory
evaluation scores, such assessment could lead to more cost-efficient and
accurate certification for wine quality assurance.

# Methods

## Data

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

## Analysis

The k-nearest neighbors (k-NN) algorithm and linear regression (Ridge)
were used to build regression models to predict wine quality (found in
the quality column of the data set). Not only that, but we also include
a dummy regressor model for baseline comparison. The mean strategy was
chosen to generate predictions. We used all variables in the original
data set to fit the model and carried out cross-validation. After
carrying out parameter tuning together with cross-validation, we chose
16 for hyperparameter k of k-NN algorithm and 10 for the alpha of Ridge.
The R (R Core Team 2020) and Python (Van Rossum and Drake 2009)
programming languages and the following R and Python packages were used
to perform the analysis: tidyverse (Wickham et al. 2019), knitr (Xie
2020), docopt (de Jonge 2020), numpy (Harris et al. 2020), Pandas
(McKinney and others 2010), altair (Sievert 2018), scikit-learn
(Pedregosa et al. 2011), dplyr (Wickham et al. 2020), readr (Wickham and
Hester 2020). The code used to perform the analysis and create this
report can be found here: <https://github.com/UBC-MDS/DSCI522_Team_23>.

# Results & Discussion

To look at our distributions of the dataset, we started by plotting
histograms and error bars for all our variables. We hope to find if
there is any pattern or trends in our data. Most of our variables are
evenly distributed across all our response variables (quality). However,
there are some variables that actually show some distinction. From
Figure 1, we can actually see that as the alcohol value, pH, and citric
acid increases, we tend to have a better wine quality. On the other
hand, the quality score tends to increase gradually when fixed acidity,
chlorides and density decreases. We did not choose to omit any variables
in our preliminary analysis as we think that all features that consist
of our data play an important role in quality prediction.

<div class="figure" style="text-align: center">

<img src="../results/quality_all_variables.png" alt="Figure 1. All Variables vs Quality" width="100%" />
<p class="caption">
Figure 1. All Variables vs Quality
</p>

</div>

Also, we plotted the number of wines by quality class to observe the
range of quality score in our data. From Figure 2, we can see that most
of our wine grade centers around 5 to 7.

<div class="figure" style="text-align: center">

<img src="../results/quality_count.png" alt="Figure 2. Number of Wines by Quality Class" width="50%" />
<p class="caption">
Figure 2. Number of Wines by Quality Class
</p>

</div>

We chose to use a simple regression model using the k-nearest neighbors’
algorithm, ridge regressor and dummy regressor for predictions. To find
the model that best predicted the wine quality score, we performed the
default 5-fold cross-validation to find the best k and best alpha for
our prediction model. From table 3 and 4, we observed the best optimal k
was 16, with a validation RMSE of 0.698 and the best alpha value is 10,
with a validation RMSE of 0.731.

| mean\_train\_negative\_RMSE | mean\_validation\_negative\_RMSE | rank\_cv\_score | n\_neighbors |
|----------------------------:|---------------------------------:|----------------:|-------------:|
|                   0.6443910 |                        0.7032121 |               1 |           11 |
|                   0.5963137 |                        0.7046002 |               2 |            6 |
|                   0.6656110 |                        0.7064989 |               3 |           16 |
|                   0.6771219 |                        0.7072481 |               4 |           21 |
|                   0.6843655 |                        0.7087261 |               5 |           26 |
|                   0.6914291 |                        0.7090271 |               6 |           36 |
|                   0.6937821 |                        0.7098824 |               7 |           41 |
|                   0.6959995 |                        0.7099454 |               8 |           46 |
|                   0.6878570 |                        0.7099662 |               9 |           31 |
|                   0.0000000 |                        0.8076507 |              10 |            1 |

Table 2: Cross-validation RMSE Score for kNN

| mean\_train\_negative\_RMSE | mean\_validation\_negative\_RMSE | rank\_cv\_score | alpha |
|----------------------------:|---------------------------------:|----------------:|------:|
|                   0.7336325 |                        0.7371091 |               1 | 1e+01 |
|                   0.7335934 |                        0.7371607 |               2 | 1e+00 |
|                   0.7335929 |                        0.7371713 |               3 | 1e-01 |
|                   0.7335929 |                        0.7371724 |               4 | 1e-02 |
|                   0.7335929 |                        0.7371725 |               5 | 1e-03 |
|                   0.7346083 |                        0.7377460 |               6 | 1e+02 |
|                   0.7434954 |                        0.7458514 |               7 | 1e+03 |

Table 3: Cross-validation RMSE Score for Ridge Regressor

By comparing the best validation RMSE scores among our models, we can
see that the baseline model, dummy regressor performs the worst,
followed by ridge regression and kNN regressor.

| Dummy Regressor                  | RMSE value |
|:---------------------------------|-----------:|
| mean\_validation\_negative\_RMSE |   0.873566 |

Table 4: Cross-validation RMSE Score for Dummy Regressor

We also compare the actual vs prediction score values for our validation
set on the kNN and Ridge models. From here, we can see that the
predicted quality falls within the range of 4 to 8, which are reasonable
values. One of our concerns when performing regression on our data was
the predictions fell out of our quality score range, which is between
0-10.

<div class="figure" style="text-align: center">

<img src="../results/ridge_prediction.png" alt="Figure 3. Ridge Predictions vs Actual" width="50%" />
<p class="caption">
Figure 3. Ridge Predictions vs Actual
</p>

</div>

<div class="figure" style="text-align: center">

<img src="../results/knn_prediction.png" alt="Figure 4. KNN Predictions vs Actual" width="50%" />
<p class="caption">
Figure 4. KNN Predictions vs Actual
</p>

</div>

We then used our selected model with k=16 to perform predictions on our
test set.

| Model | test\_split\_RMSE |
|:------|------------------:|
| k-NN  |          0.688928 |

Table 5: RMSE Score for Test Sset

Our prediction model performed quite well on test data, with an RMSE
score of 0.7171 , which is pretty similar to our validation score of the
KNN regressor.

There are a few suggestions to improve our model. First, we could try
more power regression models such as Random Forests Algorithm and model
incluing SVM. Also, given a relatively small number of features in the
dataset, we could use forward selection to reduce the number of
features. We could also engineer new features. One possible feature is
the percentage of molecular sulphur dioxide which is the active form
that acts as germicide and antioxidant in winemaking and is potentially
associated with wine quality. The percentage of molecular sulphur
dioxide can be calculated with the concentration of free SO2 and the pH
(Sudraud and Chauvet 1985).

# References

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-docopt" class="csl-entry">

de Jonge, Edwin. 2020. *Docopt: Command-Line Interface Specification
Language*. <https://CRAN.R-project.org/package=docopt>.

</div>

<div id="ref-ebeler1999linking" class="csl-entry">

Ebeler, Susan E. 1999. “Linking Flavor Chemistry to Sensory Analysis of
Wine.” In *Flavor Chemistry*, 409–21. Springer.

</div>

<div id="ref-harris2020array" class="csl-entry">

Harris, Charles R., K. Jarrod Millman, St’efan J. van der Walt, Ralf
Gommers, Pauli Virtanen, David Cournapeau, Eric Wieser, et al. 2020.
“Array Programming with NumPy.” *Nature* 585 (7825): 357–62.
<https://doi.org/10.1038/s41586-020-2649-2>.

</div>

<div id="ref-legin2003evaluation" class="csl-entry">

Legin, A, A Rudnitskaya, L Lvova, Yu Vlasov, C Di Natale, and A D’amico.
2003. “Evaluation of Italian Wine by the Electronic Tongue: Recognition,
Quantitative Analysis and Correlation with Human Sensory Perception.”
*Analytica Chimica Acta* 484 (1): 33–44.

</div>

<div id="ref-mckinney2010data" class="csl-entry">

McKinney, Wes, and others. 2010. “Data Structures for Statistical
Computing in Python.” In *Proceedings of the 9th Python in Science
Conference*, 445:51–56. Austin, TX.

</div>

<div id="ref-scikit-learn" class="csl-entry">

Pedregosa, F., G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O.
Grisel, M. Blondel, et al. 2011. “Scikit-Learn: Machine Learning in
Python.” *Journal of Machine Learning Research* 12: 2825–30.

</div>

<div id="ref-R" class="csl-entry">

R Core Team. 2020. *R: A Language and Environment for Statistical
Computing*. Vienna, Austria: R Foundation for Statistical Computing.
<https://www.R-project.org/>.

</div>

<div id="ref-2018-altair" class="csl-entry">

Sievert, Jacob VanderPlas AND Brian E. Granger AND Jeffrey Heer AND
Dominik Moritz AND Kanit Wongsuphasawat AND Arvind Satyanarayan AND
Eitan Lees AND Ilia Timofeev AND Ben Welsh AND Scott. 2018. “Altair:
Interactive Statistical Visualizations for Python.” *The Journal of Open
Source Software* 3 (32). <http://idl.cs.washington.edu/papers/altair>.

</div>

<div id="ref-sudraud1985anti" class="csl-entry">

Sudraud, P, and S Chauvet. 1985. “\[the Anti-Yeast Activity of Molecular
Sulfur Dioxide \[in Wines\]\].” *Connaissance de La Vigne Et Du Vin
(France)*.

</div>

<div id="ref-Python" class="csl-entry">

Van Rossum, Guido, and Fred L. Drake. 2009. *Python 3 Reference Manual*.
Scotts Valley, CA: CreateSpace.

</div>

<div id="ref-tidyverse" class="csl-entry">

Wickham, Hadley, Mara Averick, Jennifer Bryan, Winston Chang, Lucy
D’Agostino McGowan, Romain François, Garrett Grolemund, et al. 2019.
“Welcome to the <span class="nocase">tidyverse</span>.” *Journal of Open
Source Software* 4 (43): 1686. <https://doi.org/10.21105/joss.01686>.

</div>

<div id="ref-dplyr" class="csl-entry">

Wickham, Hadley, Romain François, Lionel Henry, and Kirill Müller. 2020.
*Dplyr: A Grammar of Data Manipulation*.
<https://CRAN.R-project.org/package=dplyr>.

</div>

<div id="ref-readr" class="csl-entry">

Wickham, Hadley, and Jim Hester. 2020. *Readr: Read Rectangular Text
Data*. <https://CRAN.R-project.org/package=readr>.

</div>

<div id="ref-knitr" class="csl-entry">

Xie, Yihui. 2020. *Knitr: A General-Purpose Package for Dynamic Report
Generation in r*. <https://yihui.org/knitr/>.

</div>

</div>
