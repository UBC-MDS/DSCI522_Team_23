# Makefile
# Jiacheng Wang, Dec 2020

# This driver script extract data from online 
# source and creates figures and report 
# for this project. This script takes no arguments.

# example usage:
# make all

all : doc/wine_quality_predict_report.html 

## Load data
data/winequality-red.csv data/winequality-white.csv : src/Download_file.py
	python src/Download_file.py

## Data preprocessing
data/winequality-train.csv data/winequality-test.csv  : src/Preprocessing.py data/winequality-red.csv d
ata/winequality-white.csv 
	python src/Preprocessing.py data/winequality-red.csv data/winequality-white.csv 

## EDA
results/quality_all_variables.png results/quality_count.png: src/EDA.py data/winequality-train.csv
	python src/EDA.py data/winequality-train.csv

## Machine learning analysis
results/knn_prediction.png results/knn_results.csv results/model_comparison.csv results/ridge_predicti
on.png results/ridge_results.csv results/test_set_result.csv : src/ML_analyses.py data/winequality-tra
in.csv data/winequality-test.csv
	python src/ML_analyses.py data/winequality-train.csv data/winequality-test.csv

## Report

doc/wine_quality_predict_report.html : doc/wine_quality_predict_report.Rmd results/knn_prediction.png r
esults/knn_results.csv results/model_comparison.csv results/ridge_prediction.png results/ridge_results.c
sv results/test_set_result.csv
    Rscript -e "rmarkdown::render('doc/wine_quality_predict_report.html')"


## Clean 
clean :
	# Data removing
    rm -rf data/winequality-red.csv data/winequality-white.csv data/winequality-train.csv data/winequality-test.csv
	
	# EDA, analysis removing
    rm -rf results/quality_all_variables.png results/quality_count.png results/knn_prediction.png results/knn_result
	s.csv results/model_comparison.csv results/ridge_prediction.png results/ridge_results.csv results/test_set_resul
	t.csv 
	
	# Report removing
    rm -rf doc/wine_quality_predict_report.html doc/wine_quality_predict_report.Rmd