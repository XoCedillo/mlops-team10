from pathlib import Path

import typer
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from mlops_bootcamp_team10.config import PROCESSED_DATA_DIR

app = typer.Typer()


@app.command()
def main(
    # ---- REPLACE DEFAULT PATHS AS APPROPRIATE ----
    input_path: Path = PROCESSED_DATA_DIR / "dataset.csv",
    output_path: Path = PROCESSED_DATA_DIR / "features.csv",
    # -----------------------------------------
):
    """Pre-processes csv before passing it to the training process"""
    # Read the dataset
    hotel_df = pd.read_csv(input_path)
    # Drop variables that add too much dimensionality or don't have enough data
    cols_to_drop = ["reservation_status_date", "country", "company", "reservation_status"]
    hotel_df.drop(columns=cols_to_drop, inplace=True)
    # Handle missing data
    hotel_df["agent"] = hotel_df["agent"].fillna(hotel_df["agent"].median())
    hotel_df["children"] = hotel_df["children"].fillna(hotel_df["babies"].median())
    # Split data into X and y
    x = hotel_df.drop(columns=["is_canceled"])

    # Define categorical and numerical features
    categorical_features = x.select_dtypes(include=["object"]).columns
    numerical_features = x.select_dtypes(include=["number"]).columns

    # Define transformers for each feature type
    categorical_transformer = OneHotEncoder()
    numerical_transformer = StandardScaler()

    # Create column transformer to apply transformers to specific columns
    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", categorical_transformer, categorical_features),
            ("num", numerical_transformer, numerical_features),
        ]
    )

    pipeline = Pipeline([("preprocessor", preprocessor)])

    x_transformed = pipeline.fit_transform(x)

    # Get the column names to apply to new df
    column_names = []
    for transformer in preprocessor.transformers_:
        if isinstance(transformer[1], OneHotEncoder):
            column_names.extend(transformer[1].get_feature_names_out())
        else:
            column_names.extend(transformer[2])

    x_transformed = pd.DataFrame(x_transformed, columns=column_names)
    # Write transformed data ready for model
    x_transformed.to_csv(output_path)

    return x_transformed


if __name__ == "__main__":
    app()
