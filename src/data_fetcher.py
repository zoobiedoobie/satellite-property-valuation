import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

# Project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Data directory
DATA_DIR = os.path.join(BASE_DIR, "data")


def load_coordinates(split="train"):
    """
    Load latitude and longitude columns
    split: 'train' or 'test'
    """
    file_path = os.path.join(DATA_DIR, f"{split}.csv")
    df = pd.read_csv(file_path)

    return df[["lat", "long"]]


def load_raw_data():
    """
    Load raw train and test CSV files
    """
    train_path = os.path.join(DATA_DIR, "train.csv")
    test_path  = os.path.join(DATA_DIR, "test.csv")

    train = pd.read_csv(train_path)
    test  = pd.read_csv(test_path)

    return train, test


def load_processed_data():
    """
    Load processed train and test CSV files
    """
    train_path = os.path.join(DATA_DIR, "train_processed.csv")
    test_path  = os.path.join(DATA_DIR, "test_processed.csv")

    train = pd.read_csv(train_path)
    test  = pd.read_csv(test_path)

    return train, test
