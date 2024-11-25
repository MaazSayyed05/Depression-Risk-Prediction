import os, sys
from pathlib import Path
from datetime import datetime
from dp_risk_pred import logger
import joblib
from box.exceptions import BoxValueError
import yaml
import json
import pandas as pd
import numpy as np
from ensure import ensure_annotations
from box import ConfigBox
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read a YAML file and return a ConfigBox object.
    """
    try:
        with open(path_to_yaml, "r") as file:
            content = yaml.safe_load(file)
            logger.info(f"YAML file read successfully: {path_to_yaml}")
            return ConfigBox(content)

    except BoxValueError:
        raise ValueError("yaml file is empty.")

    except Exception as e:
        logger.error(f"Error reading YAML file: {e}")
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates list of directories

    Arguments: path_to_directories

    """

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)

        if verbose:
            logger.info(f"Created Directory at {path}.")


@ensure_annotations
def save_csv(path: Path, data: pd.DataFrame):
    """
    save csv data

    Args:
    path(Path): path to save csv
    data(pd.DataFrame): data to be save to csv file

    """
    data.to_csv(path, index=False)
    logger.info(f"csv file saved at: {path}.")
    # return path


@ensure_annotations
def save_json(path: Path, data: dict):
    """
    save json data

    Args:
    path(Path): path to save json
    data(dict): data to be save to json file

    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}.")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)

    