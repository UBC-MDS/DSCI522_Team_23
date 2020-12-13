# author: Kangyu (Mark) Wang, Jiacheng Wang
# date: 2020-11-26

"""This script reads the train split csv file and produces exploratory data visualizations.
Usage: EDA.py --preprocessed_train=<preprocessed_train> --quality_count_path=<quality_count_path> --quality_all_variables_path=<quality_all_variables_path> 

Options:
--preprocessed_train=<preprocessed_train>                               Takes the unquoted relative path of the proprecessed train split as a csv file (this is a required option)
--quality_count_path=<quality_count_path>                               Takes the unquoted relative path to place the output png file depicting the distribution of wine quality
--quality_all_variables_path=<quality_all_variables_path>               Takes the unquoted relative path to place the output png file depicting the relationship between wine quality and 11 physicochemical variables
"""

from altair_saver import save
import altair as alt
from docopt import docopt
import numpy as np
import pandas as pd
import sys

opt = docopt(__doc__)


def main(opt):
    preprocessed_train = opt["--preprocessed_train"]

    # Read in data
    try:
        wine_train = pd.read_csv(preprocessed_train)
    except FileNotFoundError:
        print("Input csv file of train set does not exist.")
        sys.exit(1)
    # wine_train = pd.read_csv("../data/winequality-train.csv")
    # Create visualizations
    wine_train["quality"] = wine_train["quality"].astype("category")
    alt.data_transformers.disable_max_rows()

    ## Distribution of outcome variable
    quality_count_path = opt["--quality_count_path"]

    count_chart = (
        alt.Chart(wine_train)
        .mark_bar(size=40)
        .encode(
            x=alt.X(
                "quality:O",
                type="quantitative",
                title="Quality",
                axis=alt.Axis(
                    format=".0f",
                ),
            ),
            y=alt.Y("count()"),
            color=alt.Color(
                "quality", title="Wine Grade", scale=alt.Scale(scheme="viridis")
            ),
        )
        .properties(width=400, title="Histogram: Number of Wines by Quality Class")
    )

    count_chart.save(quality_count_path)

    ## Create repeated charts for all 11 explanatory variables

    quality_all_variables_path = opt["--quality_all_variables_path"]
    # quality_all_variables_path = "../results/quality_all_variables.png"

    wine_train_for_plotting = wine_train.copy()
    new_colnames = map(
        lambda t: " ".join([word.capitalize() for word in t.split("_")]),
        list(wine_train.columns),
    )
    wine_train_for_plotting.columns = list(new_colnames)

    pych_variables = [
        "Fixed Acidity",
        "Volatile Acidity",
        "Citric Acid",
        "Residual Sugar",
        "Chlorides",
        "Free Sulfur Dioxide",
        "Total Sulfur Dioxide",
        "Density",
        "Ph",
        "Sulphates",
        "Alcohol",
    ]

    bar = (
        alt.Chart(wine_train_for_plotting)
        .mark_bar()
        .encode(
            x=alt.X("Quality", title="Quality"),
            y=alt.Y(
                alt.repeat("row"),
                type="quantitative",
                aggregate="mean",
                scale=alt.Scale(zero=False),
            ),
            color=alt.Color(
                "Quality", title="Wine Grade", scale=alt.Scale(scheme="viridis")
            ),
        )
        .properties(width=400, height=300)
    )

    error = (
        alt.Chart(wine_train_for_plotting)
        .mark_errorbar()
        .encode(
            x=alt.X("Quality"),
            y=alt.Y(
                alt.repeat("row"),
                type="quantitative",
                scale=alt.Scale(zero=False),
            ),
        )
    )

    quality_all_variables_left = (bar + error).repeat(
        row=pych_variables[:4],
    )

    quality_all_variables_middle = (bar + error).repeat(
        row=pych_variables[4:8],
    )

    quality_all_variables_right = (bar + error).repeat(
        row=pych_variables[8:],
    )

    quality_all_variables = (
        quality_all_variables_left
        | quality_all_variables_middle
        | quality_all_variables_right
    )

    quality_all_variables.save(quality_all_variables_path)


if __name__ == "__main__":
    main(opt)