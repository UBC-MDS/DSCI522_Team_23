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
import pandas as pd
from sklearn.model_selection import train_test_split

opt = docopt(__doc__)


def main(opt):
    raw_white = opt["--raw_white"]
    raw_red = opt["--raw_red"]
    # raw_white = "./data/winequality-white.csv"
    # raw_red = "./data/winequality-white.csv"
    preprocessed_train = opt["--preprocessed_train"]
    # preprocessed = "./data/winequality-all.csv"
    preprocessed_test = opt["--preprocessed_test"]

    # Rread in data
    white_wine = pd.read_csv(raw_white, sep=";")
    red_wine = pd.read_csv(raw_red, sep=";")

    # Combine two datasets
    white_wine["type"] = "white"
    red_wine["type"] = "red"
    wine = pd.concat([red_wine, white_wine])

    # Create train and test splits
    wine_train, wine_test = train_test_split(wine, test_size=0.2)
    # Export file
    wine_train.to_csv(preprocessed_train)
    wine_test.to_csv(preprocessed_test)


if __name__ == "__main__":
    main(opt)