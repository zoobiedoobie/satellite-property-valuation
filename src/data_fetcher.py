import pandas as pd

def load_raw_data(data_path="../data"):
    train = pd.read_csv(f"{data_path}/train.csv")
    test  = pd.read_csv(f"{data_path}/test.csv")
    return train, test

def load_processed_data(data_path="../data"):
    train = pd.read_csv(f"{data_path}/train_processed.csv")
    test  = pd.read_csv(f"{data_path}/test_processed.csv")
    return train, test
