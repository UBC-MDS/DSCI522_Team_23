# author: Kangyu (Mark) Wang
# date: 2020-11-26

"""This script reads the train split csv file and produces exploratory data visualizations.
Usage: ML_analyses.py --preprocessed_train=<preprocessed_train> --preprocessed_test=<preprocessed_test> --results_path=<results_path>  

Options:
--preprocessed_train=<preprocessed_train>                               Takes the unquoted relative path of the proprecessed train split as a csv file (this is a required option)
--preprocessed_test=<preprocessed_test>                                 Takes the unquoted relative path of the proprecessed test split as a csv file (this is a required option)
--results_path=<results_path>                                           Takes the unquoted relative path to the folder where analytical results should be stored (this is a required option)

"""

import altair as alt
from docopt import docopt
import numpy as np
import os
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyRegressor
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV, cross_validate
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor

import sys


opt = docopt(__doc__)


def main(opt):

    alt.data_transformers.disable_max_rows()
    # Read-in train and test sets
    preprocessed_train = opt["--preprocessed_train"]
    preprocessed_test = opt["--preprocessed_test"]
    results_path = opt["--results_path"]
    # results_path = "../results"

    dummy_results_path = os.path.join(results_path, "dummy_results.csv")
    knn_results_path = os.path.join(results_path, "knn_results.csv")
    ridge_results_path = os.path.join(results_path, "ridge_results.csv")
    test_set_result_path = os.path.join(results_path, "test_set_result.csv")
    model_comparison_path = os.path.join(results_path, "model_comparison.csv")
    knn_prediction_chart_path = os.path.join(results_path, "knn_prediction.png")
    ridge_prediction_chart_path = os.path.join(results_path, "ridge_prediction.png")

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
    dummy_cv_scores = cross_validate(
        dummy_pipe,
        X_train,
        y_train,
        scoring="neg_root_mean_squared_error",
        return_train_score=True,
    )
    dummy_results = pd.DataFrame(dummy_cv_scores).mean(axis=0)[
        ["train_score", "test_score"]
    ]

    dummy_pipe.fit(X_train, y_train)
    y_pred_dummy = dummy_pipe.predict(X_train)

    ### Check train set RMSE

    print(
        f"Dummy RMSE on the train split is {mean_squared_error(y_train, y_pred_dummy, squared=False):.3f}"
    )

    ## Ridge regression
    ridge_pipe = Pipeline([("preprocessor", preprocessor), ("ridge", Ridge())])
    ridge_param_grid = {"ridge__alpha": [0.001, 0.01, 0.1, 1, 10, 100, 1000]}

    ridge_reg = GridSearchCV(
        ridge_pipe,
        ridge_param_grid,
        scoring="neg_root_mean_squared_error",
        return_train_score=True,
    )
    ridge_reg.fit(X_train, y_train)
    pd.DataFrame(ridge_reg.cv_results_).sort_values("rank_test_score")

    ridge_results = pd.DataFrame(ridge_reg.cv_results_).sort_values("rank_test_score")[
        ["params", "mean_train_score", "mean_test_score", "rank_test_score"]
    ]

    ## Get training RMSE
    y_pred_ridge = ridge_reg.predict(X_train)

    print(
        f"Ridge RMSE on the train split is {mean_squared_error(y_train, y_pred_ridge, squared=False):.3f}"
    )

    ## knn model
    knn_pipe = Pipeline(
        [("preprocessor", preprocessor), ("knn", KNeighborsRegressor())]
    )
    knn_param_grid = {"knn__n_neighbors": [5 * x + 1 for x in range(10)]}

    knn_reg = GridSearchCV(
        knn_pipe,
        knn_param_grid,
        scoring="neg_root_mean_squared_error",
        return_train_score=True,
    )
    knn_reg.fit(X_train, y_train)
    pd.DataFrame(knn_reg.cv_results_).sort_values("rank_test_score")

    knn_results = pd.DataFrame(knn_reg.cv_results_).sort_values("rank_test_score")[
        ["params", "mean_train_score", "mean_test_score", "rank_test_score"]
    ]

    ## Get training RMSE
    y_pred_knn = knn_reg.predict(X_train)

    print(
        f"K-nn RMSE on the train split is {mean_squared_error(y_train, y_pred_knn, squared=False):.3f}"
    )

    # Visualizations
    knn_true_pred = pd.DataFrame({"true_quality": y_train, "knn_pred": y_pred_knn})
    knn_prediction_chart = (
        alt.Chart(knn_true_pred)
        .mark_circle(size=60)
        .encode(
            x=alt.X("true_quality", scale=alt.Scale(zero=False), title="True Quality"),
            y=alt.Y("knn_pred", scale=alt.Scale(zero=False), title="Predicted Quality"),
        )
        .properties(title="K-nn Predictions vs. True Qualities on Train Set")
    )

    knn_prediction_chart.save(knn_prediction_chart_path)

    ridge_true_pred = pd.DataFrame(
        {"true_quality": y_train, "ridge_pred": y_pred_ridge}
    )
    ridge_prediction_chart = (
        alt.Chart(ridge_true_pred)
        .mark_circle(size=60)
        .encode(
            x=alt.X("true_quality", scale=alt.Scale(zero=False), title="True Quality"),
            y=alt.Y(
                "ridge_pred", scale=alt.Scale(zero=False), title="Predicted Quality"
            ),
        )
        .properties(title="Ridge Predictions vs. True Qualities on Train Set")
    )

    ridge_prediction_chart.save(ridge_prediction_chart_path)

    # Model comparison
    model_comparison = pd.DataFrame(
        {
            "Model": ["dummy_regressor", "Ridge_regressor", "K-nn_Regressor"],
            "RMSE on train set": [
                mean_squared_error(y_train, y_pred_dummy, squared=False),
                mean_squared_error(y_train, y_pred_ridge, squared=False),
                mean_squared_error(y_train, y_pred_knn, squared=False),
            ],
        }
    )

    # We should choose K-nn model
    y_pred_knn_test = knn_reg.predict(X_test)
    print(
        f"K-nn RMSE on the test split is {mean_squared_error(y_test, y_pred_knn_test, squared=False):.3f}"
    )

    test_set_result = pd.DataFrame(
        {
            "Model": ["k-NN"],
            "test_split_RMSE": [
                mean_squared_error(y_test, y_pred_knn_test, squared=False)
            ],
        }
    )

    # Save results
    dummy_results.index = [
        "mean_train_negative_RMSE",
        "mean_validation_negative_RMSE",
    ]
    dummy_results.to_csv(dummy_results_path)

    ridge_results.columns = [
        "params",
        "mean_train_negative_RMSE",
        "mean_validation_negative_RMSE",
        "rank_cv_score",
    ]
    ridge_results["alpha"] = [
        dict["ridge__alpha"] for dict in list(ridge_results["params"])
    ]
    ridge_results = ridge_results.drop("params", axis=1)
    ridge_results.to_csv(ridge_results_path, index=False)

    knn_results.columns = [
        "params",
        "mean_train_negative_RMSE",
        "mean_validation_negative_RMSE",
        "rank_cv_score",
    ]
    knn_results["n_neighbors"] = [
        dict["knn__n_neighbors"] for dict in list(knn_results["params"])
    ]
    knn_results = knn_results.drop("params", axis=1)
    knn_results.to_csv(knn_results_path, index=False)

    model_comparison.to_csv(model_comparison_path, index=False)
    test_set_result.to_csv(test_set_result_path, index=False)


if __name__ == "__main__":
    main(opt)