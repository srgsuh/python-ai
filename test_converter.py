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
        self.valid_dct: dict[str, int] = {"Corolla": 0, "I10": 1, "Tucson": 2, "Camry": 3}
    
    def test_enumerator(self):
        dct: dict[str, int] = enumerator(self.df["Model"].unique())
        self.assertEqual(sorted(self.valid_dct.keys()), sorted(dct.keys()))
        self.assertEqual(sorted(self.valid_dct.values()), sorted(dct.values()))

    def test_columns_mapper(self):
        mapper = columnsMapper(["Model"], self.df)
        self.assertEqual(["Model"], list(mapper.keys()))
        self.assertEqual(sorted(self.valid_dct.keys()), sorted(mapper["Model"].keys()))
        self.assertEqual(sorted(self.valid_dct.values()), sorted(mapper["Model"].values()))


if __name__ == '__main__':
    ut.main()