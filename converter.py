from typing import Iterable
import pandas as pd


def enumerator(values: Iterable[str]) -> dict[str, int]:
    return {x:idx for idx, x in enumerate(values)}

def columnsMapper(columnsStr: list[str], df: pd.DataFrame)->dict[str, dict[str, int]]:
    raise NotImplementedError()

def convertX(df:pd.DataFrame, mapper: dict[str, dict[str, int]])-> pd.DataFrame:
    raise NotImplementedError()