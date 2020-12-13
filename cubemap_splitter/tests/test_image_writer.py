from cubemap_splitter.cubemap_splitter.image import Image
from cubemap_splitter.cubemap_splitter.image_writer import BlockImageWriter
from cubemap_splitter.cubemap_splitter.image_splitter import ImageSplitCalculator
import unittest
import pathlib


class TestImageWriter(unittest.TestCase):

    def setUp(self):
        self.image = Image(pathlib.Path(__file__).parent.joinpath("test_image.png").as_posix())
        self.image_split_calculator = ImageSplitCalculator(self.image, 1)
        self.image_writer = BlockImageWriter(self.image, self.image_split_calculator, "C:/users/paulb/test")

    def tearDown(self):
        del self.image
        del self.image_split_calculator

    def test_set_output_directory(self):
        image_writer = self.image_writer
        output_directory = image_writer._BlockImageWriter__output_directory
        self.assertEqual(output_directory, "C:/users/paulb/test")

    def test_get_full_filepath(self):
        image_writer = self.image_writer
        file_path = image_writer._BlockImageWriter__get_full_file_path("fake_name")
        self.assertEqual(file_path, "C:/users/paulb/test\\fake_name.png")

    def test_path_handler_is_not_none(self):
        image_writer = self.image_writer
        path_handler = image_writer._BlockImageWriter__path_handler
        self.assertIsNotNone(path_handler)


if __name__ == '__main__':
    unittest.main()
