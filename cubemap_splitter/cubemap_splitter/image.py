"""
The purpose of the image module is to provide a class that can read and store image information.

Classes
----------
Image

Exceptions
----------
ImageNotFound
"""

import cv2
import copy


class Image:
    """
    The Image class loads and retains image data.

    ...

    Attributes
    ----------
    __path : str
        Full path to image
    __image_data : numpy array
        Numpy array containing all the image data
    __width : int
        Image width
    __height : int
        Image height
    __channels : int
        Image channels

    Methods
    -------
    get_data()
        Returns a deep copy of the __image_data
    get_width()
        Returns image width
    get_height()
        Returns image height
    get_channels()
        Returns image channel number
    get_path()
        Returns the original image path
    """
    def __init__(self, image_path):
        """
        Parameters
        ----------
        image_path : str
            Full path to image
        """
        self.__path = image_path
        self.__image_data = None
        self.__width = None
        self.__height = None
        self.__channels = None
        self.__load_image_data()
        self.__load_image_metadata()

    def __load_image_data(self):
        """
        Loads image data as a numpy array into __image_data.

        Raises
        ------
        ImageNotFound
            No image found at self.__path
        """
        print("Reading Image: %s" % self.__path)
        self.__image_data = cv2.imread(self.__path, cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH)
        if self.__image_data is None:
            raise ImageNotFound("No image found at: " + self.__path)

    def __load_image_metadata(self):
        """
        Loads image metadata (__height, __width, __channels).
        """
        self.__height, self.__width, self.__channels = self.__image_data.shape
        print("Width: %d | Height: %d | Channels: %d" % (self.__width, self.__height, self.__channels))

    def get_data(self):
        """
        Returns a deep copy of the image data.

        Returns
        -------
        numpy array
            Numpy multidimensional array with image data.
        """
        return copy.deepcopy(self.__image_data)

    def get_width(self):
        """
        Returns image width.

        Returns
        -------
        int
            Image width.
        """
        return self.__width

    def get_height(self):
        """
        Returns image height.

        Returns
        -------
        int
            Image height.
        """
        return self.__height

    def get_channels(self):
        """
        Returns image channel number.

        Returns
        -------
        int
            Image channel number.
        """
        return self.__channels

    def get_path(self):
        """
        Returns original image path.

        Returns
        -------
        str
            Image path.
        """
        return self.__path


class ImageNotFound(Exception):
    """Raised when the image cannot be found"""
    pass
