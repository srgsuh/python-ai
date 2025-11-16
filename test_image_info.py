import unittest as ut
from image_info import ImageInfo

class TestImageInfo(ut.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.no_person_img: ImageInfo = ImageInfo("./lonely_bag.jpg")
        cls.bag_and_person: ImageInfo = ImageInfo("./bag.jpg")

    def test_no_person(self) -> None:
        ii: ImageInfo = self.no_person_img
        dct = ii.suitcaseHandbagPerson(1)
        self.assertEqual(2, len(dct))
        for key in dct:
            self.assertIsNone(dct[key])
    
    def test_person_exists_large_dst(self) -> None:
        ii: ImageInfo = self.bag_and_person
        dct1 = ii.suitcaseHandbagPerson(1)
        self.assertEqual(1, len(dct1))
        for key in dct1:
            self.assertIsNotNone(dct1[key])
    
    def test_person_exists_small_dst(self) -> None:
        ii: ImageInfo = self.bag_and_person
        dct0 = ii.suitcaseHandbagPerson(1e-4)
        for key in dct0:
            self.assertIsNone(dct0[key])

if __name__ == "__main__":
    ut.main()