from typing import Iterable
import pandas as pd


def enumerator(values: Iterable[str]) -> dict[str, int]:
    return {x:idx for idx, x in enumerate(values)}

def columnsMapper(columnsStr: list[str], df: pd.DataFrame) -> dict[str, dict[str, int]]:
    return {col_name: enumerator(df[col_name].unique()) for col_name in columnsStr}

def convertX(df: pd.DataFrame, mapper: dict[str, dict[str, int]]) -> pd.DataFrame:
    dct = {col: df[col] if col not in mapper else [mapper[col][val] for val in df[col]] for col in df.columns}
    return pd.DataFrame(dct)