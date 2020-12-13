# Makefile
# Jiacheng Wang, Dec 2020

# This driver script extract data from online
# source and creates figures and report
# for this project. This script takes no arguments.

# example usage:
# make all

all: doc/breast_cancer_predict_report.md


## Load data
data/winequality-red.csv: src/Download_file.py
	python src/Download_file.py --source=https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv --destination=data/winequality-red.csv

data/winequality-white.csv: src/Download_file.py
	python src/Download_file.py --source=https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv --destination=data/winequality-white.csv

## Data preprocessing
data/winequality-train.csv data/winequality-test.csv: src/Preprocessing.py data/winequality-white.csv data/winequality-red.csv
	python src/Preprocessing.py --raw_white=data/winequality-white.csv --raw_red=data/winequality-red.csv --preprocessed_train=data/winequality-train.csv --preprocessed_test=data/winequality-test.csv

## EDA
results/quality_all_variables.png results/quality_count.png: src/EDA.py data/winequality-train.csv
	python src/EDA.py --preprocessed_train=data/winequality-train.csv --quality_count_path=results/quality_count.png --quality_all_variables_path=results/quality_all_variables.png

## Machine learning analysis
results/dummy_results.csv results/knn_prediction.png results/knn_results.csv results/ridge_prediction.png results/ridge_results.csv results/model_comparison.csv results/test_set_result.csv: src/ML_analyses.py data/winequality-train.csv data/winequality-test.csv
	python src/ML_analyses.py --preprocessed_train=data/winequality-train.csv --preprocessed_test=data/winequality-test.csv --results_path=results

## Report
doc/breast_cancer_predict_report.md doc/wine_quality_predict_report.html: doc/wine_quality_predict_report.Rmd doc/refs.bib results/quality_count.png results/dummy_results.csv results/knn_prediction.png results/quality_all_variables.png results/knn_results.csv results/ridge_prediction.png results/ridge_results.csv results/model_comparison.csv results/test_set_result.csv
	Rscript -e "rmarkdown::render('doc/wine_quality_predict_report.Rmd')"

## Clean
clean :
	# Data removing
	rm -rf data/winequality-red.csv data/winequality-white.csv data/winequality-train.csv data/winequality-test.csv

	# EDA, analysis removing
	rm -rf results/quality_all_variables.png results/quality_count.png results/dummy_results.csv results/knn_prediction.png results/knn_results.csv results/ridge_prediction.png results/ridge_results.csv results/model_comparison.csv results/test_set_result.csv

	# Report removing
	rm -rf doc/wine_quality_predict_report.html
	rm -rf doc/wine_quality_predict_report.md
