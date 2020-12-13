from cubemap_splitter.cubemap_splitter.file_path import ImageFilePaths
import unittest


class TestImageFilePaths(unittest.TestCase):

    def setUp(self):
        self.image_paths = ImageFilePaths("C:/users/paulb/desktop/fake_folder/fake_image.png")

    def test_base_dir(self):
        image_paths = self.image_paths
        base_dir = image_paths.get_base_dir()
        self.assertEqual(base_dir, "C:/users/paulb/desktop/fake_folder",
                         "Expected base directory to be: C:/users/paulb/desktop/fake_folder")

    def test_new_folder(self):
        image_paths = self.image_paths
        new_folder_name = image_paths.get_new_folder_name()
        self.assertEqual(new_folder_name, "fake_image", "Expected folder name to be fake_folder")

    def test_new_folder_path(self):
        image_paths = self.image_paths
        new_folder_path = image_paths.get_new_folder_path()
        self.assertEqual(new_folder_path, "C:/users/paulb/desktop/fake_folder\\fake_image",
                         "Expected new folder path to be: C:/users/paulb/desktop/fake_folder\\fake_image")

    def test_get_file_extension(self):
        image_paths = self.image_paths
        file_extension = image_paths.get_file_extension()
        self.assertEqual(file_extension, ".png", "Expected file extension to be: .png")


if __name__ == '__main__':
    unittest.main()
