from pathlib import Path

import typer
from loguru import logger
from tqdm import tqdm
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
    # ---- REPLACE THIS WITH YOUR OWN CODE ----
    logger.info("Generating features from dataset...")    
    # Read the dataset
    hotel_df = pd.read_csv(input_path)
    # Drop variables that add too much dimensionality or don't have enough data
    hotel_df.drop(columns=['reservation_status_date', 'country', 'company', 'reservation_status'], inplace=True)
    # Handle missing data
    hotel_df['agent'] = hotel_df['agent'].fillna(hotel_df['agent'].median())
    hotel_df['children'] = hotel_df['children'].fillna(hotel_df['babies'].median())
    # Split data into X and y
    y = hotel_df['is_canceled']
    X = hotel_df.drop(columns=['is_canceled'])

    # Define categorical and numerical features
    categorical_features = X.select_dtypes(include=['object']).columns
    numerical_features = X.select_dtypes(include=['number']).columns

    # Define transformers for each feature type
    categorical_transformer = OneHotEncoder()
    numerical_transformer = StandardScaler()

    # Create column transformer to apply transformers to specific columns
    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', categorical_transformer, categorical_features),
            ('num', numerical_transformer, numerical_features)
        ])

    pipeline = Pipeline([
        ('preprocessor', preprocessor)
    ])

    X_transformed = pipeline.fit_transform(X)

    # Get the column names to apply to new df
    column_names = []
    for transformer in preprocessor.transformers_:
        if isinstance(transformer[1], OneHotEncoder):
            column_names.extend(transformer[1].get_feature_names_out())
        else:
            column_names.extend(transformer[2])
    
    X_transformed = pd.DataFrame(X_transformed, columns=column_names)
    # Write transformed data ready for model
    X_transformed.to_csv(output_path)
    
    return X_transformed

if __name__ == "__main__":
    app()
