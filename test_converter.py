import unittest as ut
import pandas as pd
from converter import enumerator, columnsMapper, convertX

class TestConverters(ut.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.df = pd.DataFrame({
            "Company": ["Toyota", "Hyundai", "Hyundai", "Hyundai", "Toyota"],
            "Model": ["Corolla", "I10", "Tucson", "I10", "Camry"]
        })
        self.mapper = {"Company": {"Toyota": 0, "Hyundai": 1}, "Model": {"Corolla": 0, "I10": 1, "Tucson": 2, "Camry": 3}}
    
    def test_enumerator(self):
        dct: dict[str, int] = enumerator(self.df["Model"].unique())
        valid_dct = self.mapper["Model"]
        self.assertEqual(sorted(valid_dct.keys()), sorted(dct.keys()))
        self.assertEqual(sorted(valid_dct.values()), sorted(dct.values()))

    def test_columns_mapper(self):
        mapper = columnsMapper(["Model"], self.df)
        self.assertEqual(["Model"], list(mapper.keys()))
        self.assertEqual(sorted(mapper["Model"].keys()), sorted(self.mapper["Model"].keys()))
        self.assertEqual(sorted(mapper["Model"].values()), sorted(self.mapper["Model"].values()))

    def test_convert_x(self):
        df_conv: DataFrame = convertX(self.df, self.mapper)
        self.assertEqual(sorted(df_conv.columns.to_list()), ["Company", "Model"])
        self.assertEqual([0, 1, 1, 1, 0], df_conv["Company"].to_list())
        self.assertEqual([0, 1, 2, 1, 3], df_conv["Model"].to_list())

if __name__ == '__main__':
    ut.main()