from typing import List
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
import base64

def encode_categorical_features(dfs: List[pd.DataFrame]) -> List[pd.DataFrame]:
    encoder = OrdinalEncoder()
    dfs = [df.fillna("?") for df in dfs]

    encoder.fit(pd.concat(dfs, axis=0))
    res_dfs = []
    for df in dfs:
        encoded_df = encoder.transform(df)
        res_dfs.append(encoded_df)
    return res_dfs


def series_count_words(x):
    return len(str(x).split())


def text_to_continuous(df, text_columns: List[str]):
    for col in text_columns:
        df[col + "_char_len"] = df[col].fillna("").apply(len)
        df[col + "_word_count"] = df[col].fillna("").apply(series_count_words)
    return df


def transform_to_base64(path):
    with open(path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return "data:image/gif;base64," + encoded_string.decode('utf-8')
