from cubemap_splitter.cubemap_splitter.image import Image, ImageNotFound
import unittest
import pathlib


class TestImage(unittest.TestCase):

    def setUp(self):
        self.image = Image(pathlib.Path(__file__).parent.joinpath("test_image.png").as_posix())

    def tearDown(self):
        del self.image

    def test_get_image_data(self):
        image = self.image
        image_data = image.get_data()
        self.assertIsNotNone(image_data, "Image data should not be none!  The data has not been read in properly.")

    def test_get_image_width(self):
        image = self.image
        image_width = image.get_width()
        self.assertEqual(image_width, 410)

    def test_get_image_height(self):
        image = self.image
        image_height = image.get_height()
        self.assertEqual(image_height, 307)

    def test_get_image_path(self):
        image_path = pathlib.Path(__file__).parent.joinpath("test_image.png").as_posix()
        image = self.image
        image_path_result = image.get_path()
        self.assertEqual(image_path_result, image_path)

    def test_image_not_found(self):
        self.assertRaises(ImageNotFound, Image, "waffle.png")


if __name__ == '__main__':
    unittest.main()
