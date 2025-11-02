import unittest as ut
from converter import enumerator, columnsMapper, convertX

class TestConverters(ut.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.data: list[str] = ["dict", "heap", "list", "queue", "set"]
        self.empty: list[str] = []
    
    def test_enumerator(self):
        enumerated: dict[str, int] = enumerator(self.data)
        self.assertEqual(sorted(enumerated.keys()), self.data)
        self.assertEqual(sorted(enumerated.values()), [x for x in range(len(self.data))])

if __name__ == '__main__':
    ut.main()