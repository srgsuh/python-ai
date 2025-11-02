from typing import Iterable
import pandas as pd


def enumerator(values: Iterable[str]) -> dict[str, int]:
    return {x:idx for idx, x in enumerate(values)}

def columnsMapper(columnsStr: list[str], df: pd.DataFrame)->dict[str, dict[str, int]]:
    return {col_name: enumerator(df[col_name].unique()) for col_name in columnsStr}

def convertX(df: pd.DataFrame, mapper: dict[str, dict[str, int]])-> pd.DataFrame:
    dct = {}
    for col_name in df.columns:
        if col_name in mapper:
            dct[col_name] = [mapper[col_name][value] for value in df[col_name]]
        else:
            dct[col_name] = df[col_name]
    return pd.DataFrame(dct)