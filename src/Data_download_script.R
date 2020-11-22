# Author: Ling Lin
# Date: 2020-11-21

# This script allows users to download and read in data in csv files for the wine quality statistical analysis. 

# Install necessary packages
# install.packages("tidyverse")
library(tidyverse)

# Data url links 
red_wine_url <- "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
white_wine_url <- "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv"

# Download and save files 
download.file(red_wine_url, "red_wine.csv")
download.file(white_wine_url, "white_wine.csv")

# Read in data
red_wine <- read_delim("red_wine.csv", ";", escape_double = FALSE, trim_ws = TRUE)
white_wine <- read_delim("white_wine.csv", ";", escape_double = FALSE, trim_ws = TRUE)
