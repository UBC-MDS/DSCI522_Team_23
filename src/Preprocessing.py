# author: Kangyu (Mark) Wang
# date: 2020-11-26

"""This script reads the downloaded csv files and conducts preprocessing for further analyses.
Usage: Preprocessing.py --raw_white=<raw_white> --raw_red=<raw_red> --preprocessed_train=<preprocessed_train> --preprocessed_test=<preprocessed_test>

Options:
--raw_white=<raw_white>                     Takes the unquoted relative path of csv file downloaded, with information of white wine (this is a required option)
--raw_red=<raw_red>                         Takes the unquoted relative path of csv file downloaded, with information of red wine (this is a required option)
--preprocessed_train=<preprocessed_train>   Takes the unquoted relative path to place the proprecessed train split output as a csv file (this is a required option)
--preprocessed_test=<preprocessed_test>     Takes the unquoted relative path to place the proprecessed test split output as a csv file (this is a required option)
"""

from docopt import docopt
import numpy as np
from os import path
import re
import pandas as pd
from sklearn.model_selection import train_test_split
import sys

opt = docopt(__doc__)


def main(opt):
    raw_white = opt["--raw_white"]
    raw_red = opt["--raw_red"]
    preprocessed_train = opt["--preprocessed_train"]
    preprocessed_test = opt["--preprocessed_test"]
    # raw_white = "../data/winequality-white.csv"
    # raw_red = "../data/winequality-red.csv"
    # preprocessed_train = "../data/winequality-train.csv"
    # Read in data
    try:
        white_wine = pd.read_csv(raw_white, sep=";")
    except FileNotFoundError:
        print("Input csv file of white wine does not exist.")
        sys.exit(1)

    try:
        red_wine = pd.read_csv(raw_red, sep=";")
    except FileNotFoundError:
        print("Input csv file of red wine does not exist.")
        sys.exit(1)

    # Combine two datasets
    white_wine["type"] = "white"
    red_wine["type"] = "red"
    wine = pd.concat([red_wine, white_wine], ignore_index=True)
    wine.columns = (
        wine.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("(", "")
        .str.replace(")", "")
    )

    # Create train and test splits
    wine_train, wine_test = train_test_split(wine, test_size=0.2)
    # Export file
    wine_train.to_csv(preprocessed_train, index=False)
    wine_test.to_csv(preprocessed_test, index=False)


if __name__ == "__main__":
    main(opt)