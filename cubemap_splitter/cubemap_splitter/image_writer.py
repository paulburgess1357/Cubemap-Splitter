"""
The purpose of the image_writer module is to provide a way to take image data, subset it, and write it to a new folder.

Classes
----------
BlockImageWriter

Exceptions
----------
ImageFailedToWrite
"""

from .file_path import ImageFilePaths
import cv2
import os


class BlockImageWriter:
    """
    The BlockImageWriter class writes out image subset blocks using the SplitIndices class information.

    ...

    Attributes
    ----------
    __image : Image
        Image class
    __split_calculator : SplitCalculator
        SplitCalculator class
    __output_directory : str
        Output directory location
    __path_handler : ImageFilePaths
        File/Folder path handler

    Methods
    -------
    write_image_blocks()
        Writes image blocks into the output_directory.  If the output directory is not supplied, a folder will be
        created at the image location.
    """
    def __init__(self, image, split_calculator, output_directory=None):
        """
        Parameters
        ----------
        image : Image
            Instantiated Image class
        split_calculator : SplitCalculator
            Instantiated SplitCalculator class
        output_directory : str, optional
            Output directory to write all subset images to.
        """
        self.__image = image
        self.__split_calculator = split_calculator
        self.__output_directory = output_directory
        self.__path_handler = None
        self.__set_path_handler()
        self.__set_output_directory()

    def __set_path_handler(self):
        """
        Sets the __path_handler attribute.  The path handler will use the image path for its directory information.
        """
        image_path = self.__image.get_path()
        self.__path_handler = ImageFilePaths(image_path)

    def __set_output_directory(self):
        """
        If the output directory is not supplied, the __path_handler will set the output directory to be where the
        image is located.
        """
        if not self.__output_directory:
            self.__path_handler.create_new_folder()
            self.__output_directory = self.__path_handler.get_new_folder_path()

    def __get_full_file_path(self, file_name):
        """
        Returns the full file path of the subset block image being written.

        Parameters
        ----------
        file_name : str
            filename

        Returns
        -------
        str
            Returns the full file path
        """
        file_name += self.__path_handler.get_file_extension()
        file_path = os.path.join(self.__output_directory, file_name)
        return file_path

    def write_image_blocks(self):
        """
        Writes each image block to the output directory location.  If the output directory is not supplied, the image
        blocks will be written to a new folder located at the image location.
        """
        print("Output Directory: %s" % self.__output_directory)
        image_data = self.__image.get_data()
        image_splits = self.__split_calculator.get_splits()
        for image_split in image_splits:
            file_name = image_split.image_mapped_name
            if file_name:
                full_file_path = self.__get_full_file_path(file_name)
                write_result = cv2.imwrite(full_file_path, image_data[image_split.y_min:image_split.y_max,
                                                                      image_split.x_min:image_split.x_max:])
                self.__check_write_result(write_result, full_file_path)

    @staticmethod
    def __check_write_result(write_result, full_file_path):
        """
        Checks the the results successfully write.

        Raises
        ------
        ImageFailedToWrite
            Raised if the image fails to write.
        """
        if write_result:
            print("File Successfully Written: %s" % full_file_path)
        else:
            raise ImageFailedToWrite("Image: %s failed to write.  Does the folder exist?" % full_file_path)


class ImageFailedToWrite(Exception):
    """Raised when the image fails to write to the specified path"""
    pass
