from cubemap_splitter.cubemap_splitter.image import Image
from cubemap_splitter.cubemap_splitter.image_splitter import ImageSplitCalculator, AutoImageFormat, SplitIndices
import unittest
import pathlib


class TestImageSplitter(unittest.TestCase):

    def setUp(self):
        self.image = Image(pathlib.Path(__file__).parent.joinpath("test_image.png").as_posix())
        self.image_split_calculator = ImageSplitCalculator(self.image, 1)

    def tearDown(self):
        del self.image

    def test_set_format_type(self):
        image_split_calculator = self.image_split_calculator
        format_type = image_split_calculator._ImageSplitCalculator__format_type
        self.assertEqual(format_type, 1)

    def test_set_format_type_auto(self):
        image = self.image
        image_split_calculator = ImageSplitCalculator(image, "auto")
        format_type = image_split_calculator._ImageSplitCalculator__format_type
        self.assertEqual(format_type, 1, "Auto format type should be 1 for test_image.png")

    def test_calculate_vertical_increment(self):
        image_split_calculator = self.image_split_calculator
        vertical_increment = image_split_calculator._ImageSplitCalculator__calculate_vertical_increment()
        self.assertEqual(vertical_increment, 102)

    def test_calculate_horizontal_increment(self):
        image_split_calculator = self.image_split_calculator
        horizontal_increment = image_split_calculator._ImageSplitCalculator__calculate_horizontal_increment()
        self.assertEqual(horizontal_increment, 102)

    def test_get_splits(self):
        image_splits = self.image_split_calculator.get_splits()
        total_splits = len(image_splits)
        self.assertEqual(total_splits, 20)


class TestAutoImageFormat(unittest.TestCase):
    def setUp(self):
        self.image = Image(pathlib.Path(__file__).parent.joinpath("test_image.png").as_posix())
        self.auto_format_class = AutoImageFormat(self.image)

    def tearDown(self):
        del self.image

    def test_set_ratio(self):
        auto_format_class = self.auto_format_class
        ratio = auto_format_class._AutoImageFormat__ratio
        self.assertEqual(round(ratio, 2), 1.34)

    def test_calculate_image_format(self):
        auto_format_class = self.auto_format_class
        image_format = auto_format_class.calculate_image_format()
        self.assertEqual(image_format, 1)

    def test_calculate_image_format_from_element_pct(self):
        auto_format_class = self.auto_format_class
        image_format = auto_format_class._AutoImageFormat__calculate_format_from_element_overlap(0.91)
        self.assertEqual(image_format, 1)

    def test_calculate_image_format_from_element_pct_type2(self):
        auto_format_class = self.auto_format_class
        image_format = auto_format_class._AutoImageFormat__calculate_format_from_element_overlap(0.85)
        self.assertEqual(image_format, 2)


class TestSplitIndices(unittest.TestCase):
    def setUp(self):
        self.split_indices = SplitIndices(0, 100, 10, 1000, 1, 1)

    def tearDown(self):
        del self.split_indices

    def test_x_min(self):
        self.assertEqual(self.split_indices.x_min, 0)

    def test_x_max(self):
        self.assertEqual(self.split_indices.x_max, 100)

    def test_y_min(self):
        self.assertEqual(self.split_indices.y_min, 10)

    def test_y_max(self):
        self.assertEqual(self.split_indices.y_max, 1000)

    def test_mapped_name_is_none(self):
        self.assertIsNone(self.split_indices.image_mapped_name)

    def test_set_image_mapped_name(self):
        self.split_indices.set_image_mapped_name("mapped name")
        self.assertEqual(self.split_indices.image_mapped_name, "mapped name")


if __name__ == '__main__':
    unittest.main()
