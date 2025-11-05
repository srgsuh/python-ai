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
        self.mapper = columnsMapper(["Company", "Model"], self.df)
    
    def test_enumerator(self):
        correct_dct: dict[str, int] = {"Corolla": 0, "I10": 1, "Tucson": 2, "Camry": 3}
        tested_dct: dict[str, int] = enumerator(self.df["Model"].unique())
        self.assertEqual(sorted(correct_dct.keys()), sorted(tested_dct.keys()))
        self.assertEqual(sorted(correct_dct.values()), sorted(tested_dct.values()))

if __name__ == '__main__':
    ut.main()