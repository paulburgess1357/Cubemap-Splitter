import cv2
from file_path import OutputImagesFilePaths


class ImageWriter:
    def __init__(self, image, image_splitter, output_directory=None):
        self.image = image
        self.image_data = image.get_data()
        self.image_splits = image_splitter.get_splits()
        self.output_images_path = OutputImagesFilePaths(image.get_path())
        self.output_directory = output_directory
        self.extension = self.output_images_path.get_extension()
        self.__get_output_directory()
        self.__get_extension()

    def __get_extension(self):
        self.extension = FilePath.get_file_extension(self.image.get_path())

    def __get_output_directory(self):
        if not self.output_directory:
            self.output_directory = FilePath.create_new_folder(self.image.get_path())

    def get_full_filepath(self, file_name):
        return self.output_directory + "/" + file_name + self.extension

    def write_images(self):
        print("Output Directory: %s" % self.output_directory)

        for image_split in self.image_splits:
            file_name = image_split.get_image_mapped_name()
            if file_name:
                full_file_path = self.get_full_filepath(file_name)
                result = cv2.imwrite(full_file_path, self.image_data[image_split.y_min:image_split.y_max, image_split.x_min:image_split.x_max:])

                if result:
                    print("File Successfully Written: %s" % file_name)
                else:
                    raise ImageFailedToWrite("Image: %s filed to write" % full_file_path)


class ImageFailedToWrite(Exception):
    """Raised when the image fails to write to the specified path"""
    pass