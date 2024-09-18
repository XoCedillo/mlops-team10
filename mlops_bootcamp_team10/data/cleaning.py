# Standard libraries
import pandas as pd
from loguru import logger


# Create downsampling
def downsample(df: pd.DataFrame, logger: logger = None):
    """
    Downsampling function
    df: Dataframe to perfom downsampling in minority class.
    logger: logger to inform about progress
    """
    logger.info("Downsampling data...")
    tbl_reservations_not_cancelled = df.query("is_canceled == 0").sample(
        n=df.groupby(["is_canceled"]).size()[1], random_state=42
    )
    # Filter by minority class.
    tbl_reservations_cancelled = df.query("is_canceled == 1")

    logger.debug(f"Cancelled data size: {tbl_reservations_not_cancelled.size}")
    logger.debug(f"Not Canccelled data size: {tbl_reservations_not_cancelled.size}")

    return pd.concat([tbl_reservations_not_cancelled, tbl_reservations_cancelled])
