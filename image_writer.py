import cv2
import os
from file_path import ImageFilePaths


class BlockImageWriter:
    def __init__(self, image, split_calculator, output_directory=None):
        self.__image = image
        self.__split_calculator = split_calculator
        self.__output_directory = output_directory
        self.__path_handler = None
        self.__set_path_handler()
        self.__set_output_directory()

    def __set_path_handler(self):
        image_path = self.__image.get_path()
        self.__path_handler = ImageFilePaths(image_path)

    def __set_output_directory(self):
        if not self.__output_directory:
            self.__path_handler.create_new_folder()
            self.__output_directory = self.__path_handler.get_new_folder_path()

    def get_full_file_path(self, file_name):
        file_name += self.__path_handler.get_file_extension()
        file_path = os.path.join(self.__output_directory, file_name)
        return file_path

    def write_image_blocks(self):
        print("Output Directory: %s" % self.__output_directory)
        image_data = self.__image.get_data()
        image_splits = self.__split_calculator.get_splits()
        for image_split in image_splits:
            file_name = image_split.image_mapped_name
            if file_name:
                full_file_path = self.get_full_file_path(file_name)
                write_result = cv2.imwrite(full_file_path, image_data[image_split.y_min:image_split.y_max,
                                                                      image_split.x_min:image_split.x_max:])
                self.__check_write_result(write_result, full_file_path)

    @staticmethod
    def __check_write_result(write_result, full_file_path):
        if write_result:
            print("File Successfully Written: %s" % full_file_path)
        else:
            raise ImageFailedToWrite("Image: %s filed to write" % full_file_path)


class ImageFailedToWrite(Exception):
    """Raised when the image fails to write to the specified path"""
    pass
