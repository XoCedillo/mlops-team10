from pathlib import Path

# Standard libraries
import pandas as pd
import typer
from loguru import logger
from tqdm import tqdm

from mlops_bootcamp_team10.config import PROCESSED_DATA_DIR, RAW_DATA_DIR

app = typer.Typer()


# Create downsampling
def downsample(df: pd.DataFrame):
    """
    Downsampling function
    df: Dataframe to perfom downsampling in minority class.
    """
    logger.info("Downsampling data...")
    tbl_reservations_not_cancelled = df.query("is_canceled == 0").sample(
        n=df.groupby(["is_canceled"]).size()[1], random_state=42
    )
    # Filter by minority class.
    tbl_reservations_cancelled = df.query("is_canceled == 1")

    logger.info(f"Cancelled data size: {tbl_reservations_not_cancelled.size}")
    logger.info(f"Not Canccelled data size: {tbl_reservations_not_cancelled.size}")

    return pd.concat([tbl_reservations_not_cancelled, tbl_reservations_cancelled])


@app.command()
def main(
    input_path: Path = RAW_DATA_DIR / "hotel_bookings.csv",
    output_path: Path = PROCESSED_DATA_DIR / "hotel_bookings.csv",
    # funcs: List[Callable[pd.DataFrame] pd.DataFrame] = None,
):
    """
    Main Function
    input_path: Raw data path defined on RAW_DATA_DIR config.py
    output_path: Output data path based PROCESSED_DATA_DIR config.py
    funcs: Scripts to download or generate data
    """
    funcs = [downsample]

    logger.info("Processing dataset...")
    logger.info(f"Input path {input_path}")

    # Perform cleaning of dataset based on transformations param
    processed_df = pd.read_csv(input_path)
    for func in tqdm(funcs):
        processed_df = func(processed_df)
    logger.success("Processing dataset complete.")

    # Saving processed dataset
    logger.info("Exporting dataset.")
    processed_df.to_csv(output_path, index=False)
    logger.success(f"Success! Dataset exported to {output_path}")


if __name__ == "__main__":
    app()
