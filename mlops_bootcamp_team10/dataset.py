from pathlib import Path

# Standard libraries
import pandas as pd
import typer
from loguru import logger
from tqdm import tqdm

from typing import List, Callable, Union

# Standard libraries
import pandas as pd
import numpy as np

from mlops_bootcamp_team10.config import PROCESSED_DATA_DIR, RAW_DATA_DIR
from mlops_bootcamp_team10.data import clean

app = typer.Typer()


@app.command()
def main(
    input_path: Path = RAW_DATA_DIR / "hotel_bookings.csv",
    output_path: Path = PROCESSED_DATA_DIR / "hotel_bookings.csv",
    funcs: List[str] = ["downsampling"],
):
    """
    Main Function
    input_path: Raw data path defined on RAW_DATA_DIR config.py
    output_path: Output data path based PROCESSED_DATA_DIR config.py
    funcs: Scripts to download or generate data
    """
    ops = {
        "downsampling": clean.downsample,
    }

    logger.info("Processing dataset...")
    logger.info(f"Input path {input_path}")

    # Perform cleaning of dataset based on transformations param
    processed_df = pd.read_csv(input_path)
    for func in tqdm(funcs):
        processed_df = ops[func](processed_df, logger=logger)
    logger.success("Processing dataset complete.")

    # Saving processed dataset
    logger.info("Exporting dataset.")
    processed_df.to_csv(output_path, index=False)
    logger.success(f"Success! Dataset exported to {output_path}")

    # Separate features and target
    logger.debug("Separate features and target")
    X = processed_df.drop(columns=["is_canceled"])
    y = processed_df["is_canceled"]
    return X, y


if __name__ == "__main__":
    app()
