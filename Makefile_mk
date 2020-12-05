# Makefile
# Mark Wang, Dec 2020

# This driver script runs the entire analytical process of the project. It downloads and transforms the necessary raw data, creates exploratory data analysis plots, and generates the final report. 

# Example usage:
# make all

all : results/quality_count.png results/quality_all_variables.png results/knn_results.csv results/ridge_results.csv doc/wine_quality_predict_report.Rmd 

# Data downloading and pre-processing
data/winequality-red.csv : src/Download_file.py
	python src/Download_file.py --source=https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv --destination=data/winequality-red.csv
data/winequality-white.csv : src/Download_file.py
	python src/Download_file.py --source=https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv --destination=data/winequality-white.csv

data/winequality-train.csv data/winequality-test.csv : src/Preprocessing.py data/winequality-white.csv data/winequality-red.csv
	python src/Preprocessing.py --raw_white=data/winequality-white.csv --raw_red=data/winequality-red.csv --preprocessed_train=data/winequality-train.csv --preprocessed_test=data/winequality-test.csv


# Exploratory data analyses
results/quality_count.png results/quality_all_variables.png : src/EDA.py data/winequality-train.csv
	python src/EDA.py --preprocessed_train=data/winequality-train.csv --quality_count_path=results/quality_count.png --quality_all_variables_path=results/quality_all_variables.png

# Model Tuning and Testing
results/knn_results.csv results/ridge_results.csv : src/ML_analyses.py data/winequality-train.csv data/winequality-test.cs
	python src/ML_analyses.py --preprocessed_train=data/winequality-train.csv --preprocessed_test=data/winequality-test.csv --knn_results_path=results/knn_results.csv --ridge_results_path=results/ridge_results.csv

# Render final report 
doc/wine_quality_predict_report.html : doc/wine_quality_predict_report.Rmd
	Rscript -e "rmarkdown::render('doc/wine_quality_predict_report.Rmd')"
