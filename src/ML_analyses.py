# author: Kangyu (Mark) Wang
# date: 2020-11-26

"""This script reads the train split csv file and produces exploratory data visualizations.
Usage: ML_analyses.py --preprocessed_train=<preprocessed_train> --preprocessed_test=<preprocessed_test> --knn_results_path=<knn_results_path> --ridge_results_path=<ridge_results_path>

Options:
--preprocessed_train=<preprocessed_train>                               Takes the unquoted relative path of the proprecessed train split as a csv file (this is a required option)
--preprocessed_test=<preprocessed_test>                                 Takes the unquoted relative path of the proprecessed test split as a csv file (this is a required option)
--knn_results_path=<knn_results_path>                                   Takes the unquoted relative path to store the knn results (this is a required option)
--ridge_results_path=<ridge_results_path>                               Takes the unquoted relative path to store the ridge results (this is a required option)
"""

from docopt import docopt
import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyRegressor
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor

import sys


opt = docopt(__doc__)


def main(opt):

    # Read-in train and test sets
    preprocessed_train = opt["--preprocessed_train"]
    preprocessed_test = opt["--preprocessed_test"]
    knn_results_path = opt["--knn_results_path"]
    ridge_results_path = opt["--ridge_results_path"]

    preprocessed_train = pd.read_csv(preprocessed_train)
    preprocessed_test = pd.read_csv(preprocessed_test)
    # preprocessed_train = pd.read_csv("../data/winequality-train.csv")
    # preprocessed_test = pd.read_csv("../data/winequality-test.csv")

    X_train = preprocessed_train.drop("quality", axis=1)
    y_train = preprocessed_train["quality"]

    X_test = preprocessed_test.drop("quality", axis=1)
    y_test = preprocessed_test["quality"]

    # Create preprocessor
    ## Feature types
    numeric_features = list(X_train.columns)
    numeric_features.remove("type")

    categorical_feature = ["type"]

    ## Feature preprocessors
    numeric_preprocessor = Pipeline(
        [("inputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())]
    )

    categorical_preprocessor = Pipeline(
        [
            ("inputer", SimpleImputer(strategy="constant", fill_value="missing")),
            ("ohe", OneHotEncoder(drop="if_binary")),
        ]
    )

    ## Preprocessor
    preprocessor = ColumnTransformer(
        [
            ("num", numeric_preprocessor, numeric_features),
            ("cat", categorical_preprocessor, categorical_feature),
        ]
    )

    # Create models
    ## Dummy basedline model
    dummy_pipe = Pipeline(
        [("preprocessor", preprocessor), ("dummy", DummyRegressor(strategy="mean"))]
    )
    dummy_pipe.fit(X_train, y_train)
    dummy_pipe.score(X_train, y_train)

    ## Ridge regression
    ridge_pipe = Pipeline([("preprocessor", preprocessor), ("ridge", Ridge())])
    ridge_param_grid = {"ridge__alpha": [0.001, 0.01, 0.1, 1, 10, 100, 1000]}

    ridge_reg = GridSearchCV(ridge_pipe, ridge_param_grid)
    ridge_reg.fit(X_train, y_train)
    pd.DataFrame(ridge_reg.cv_results_).sort_values("rank_test_score")

    ridge_results = pd.DataFrame(ridge_reg.cv_results_).sort_values("rank_test_score")[
        ["params", "mean_test_score", "rank_test_score"]
    ]

    y_pred_ridge = ridge_reg.predict(X_test)

    print(f"Ridge R^2 on the train split is {ridge_reg.score(X_train, y_train):.3f}")
    print(f"Ridge R^2 on the test split is {ridge_reg.score(X_test, y_test):.3f}")
    print(
        f"Ridge RMSE on the test split is {mean_squared_error(y_test, y_pred_ridge, squared=False):.3f}"
    )

    ## knn model
    knn_pipe = Pipeline(
        [("preprocessor", preprocessor), ("knn", KNeighborsRegressor())]
    )
    knn_param_grid = {"knn__n_neighbors": [5 * x + 1 for x in range(10)]}

    knn_reg = GridSearchCV(knn_pipe, knn_param_grid)
    knn_reg.fit(X_train, y_train)
    pd.DataFrame(knn_reg.cv_results_).sort_values("rank_test_score")

    knn_results = pd.DataFrame(knn_reg.cv_results_).sort_values("rank_test_score")[
        ["params", "mean_test_score", "rank_test_score"]
    ]

    y_pred_knn = knn_reg.predict(X_test)

    print(f"KNN R^2 on the train split is {knn_reg.score(X_train, y_train):.3f}")
    print(f"KNN R^2 on the test split is {knn_reg.score(X_test, y_test):.3f}")
    print(
        f"KNN RMSE on the test split is {mean_squared_error(y_test, y_pred_knn, squared=False):.3f}"
    )

    # Save results
    ridge_results["alpha"] = [
        dict["ridge__alpha"] for dict in list(ridge_results["params"])
    ]
    ridge_results = ridge_results.drop("params", axis=1)
    ridge_results.to_csv(ridge_results_path, index=False)

    knn_results["n_neighbors"] = [
        dict["knn__n_neighbors"] for dict in list(knn_results["params"])
    ]
    knn_results = knn_results.drop("params", axis=1)
    knn_results.to_csv(knn_results_path, index=False)


if __name__ == "__main__":
    main(opt)