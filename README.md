# Prediction of Wine Quality based on Physicochemical Tests 

### Data

The data sets used in this project are of the prediction of wine quality based on physicochemical tests, related to red and white vinho verde wine samples, from the north of Portugal. The data were created by Paulo Cortez at the University of Minho, Guimarães, Portugal (Cortez, Cerdeira, Almeida, Matos, &amp; Reis, 2009). It was sourced from the UCI Machine Learning Repository (Dua and Graff 2017) and can be found [here](https://archive.ics.uci.edu/ml/datasets/Wine+Quality), specifically this [file](https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/). The data provided only have physicochemical (inputs) and sensory (the output) variables available (e.g. there is no data about grape types, wine brand, wine selling price, etc.). There are a total of 4898 instances in our combined dataset of red wine and white wine.

### Research Question

From the data set provided, we are interested in predicting the wine quality (white wine and red wine) based on the physicochemical tests. We are engaged in predicting the quality score (score between 0 and 10) of a wine based on variables including:

- fixed acidity
- volatile acidity
- citric acid
- residual sugar
- chlorides
- free sulfur dioxide
- total sulfur dioxide
- density
- pH
- sulphates
- alcohol

Moreover, we will also attempt to look for the correlation between the explanatory variables, to see if there are any multicollinearity occurs. Assuming all variables are independent, if the variables are correlated and the degree of correlation between variables is high enough, it can be a problem when fitting the model and the result may not be accurate. 

### Analysis

The k-nearest neighbors (k-nn) algorithm will be used to build a regression model to predict the quality score of the wine, including white and red wine. All variables included in the original dataset will be used in fitting our model. Since there are no missing values in our dataset, there is no need for any imputation. 
Also, the support vector machines (SVMs) with RBF kernel will be our second model in predicting the quality score of wine. We are hoping to see improvement in our model, given the support vectors. Lastly, we will also include the most commonly used regression model - Multiple Linear Regression (MLR). It is an extension of the Simple Linear Regression (SLR) that involves more than one explanatory variable. From the regression model, we can identify trends and relationships between variables. Most of our analysis will be done using Python and R programming languages (R Core Team 2019; Van Rossum and Drake 2009). 






### References

Cortez, P., Cerdeira, A., Almeida, F., Matos, T., &amp; Reis, J. (2009, June 09). Modeling wine preferences by data mining from physicochemical properties. Retrieved November 21, 2020, from https://www.sciencedirect.com/science/article/abs/pii/S0167923609001377?via=ihub

Dua, Dheeru, and Casey Graff. 2017. “UCI Machine Learning Repository.” University of California, Irvine, School of Information; Computer Sciences. http://archive.ics.uci.edu/ml.

R Core Team. 2019. R: A Language and Environment for Statistical Computing. Vienna, Austria: R Foundation for Statistical Computing. https://www.R-project.org/.

Van Rossum, Guido, and Fred L. Drake. 2009. Python 3 Reference Manual. Scotts Valley, CA: CreateSpace.

