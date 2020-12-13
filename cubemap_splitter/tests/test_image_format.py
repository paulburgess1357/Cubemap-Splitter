from cubemap_splitter.cubemap_splitter.image_format import ImageFormat
import unittest


class TestImageFormat(unittest.TestCase):

    def test_get_format_dict(self):
        image_format = ImageFormat()
        format_dict = image_format.get_format_dict(1)
        self.assertTrue(isinstance(format_dict, dict))

    def test_get_format_dim(self):
        image_format = ImageFormat()
        format_dim = image_format.get_format_dim(1)
        self.assertTrue(isinstance(format_dim, list))


if __name__ == '__main__':
    unittest.main()
