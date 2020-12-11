import cv2
import copy


class Image:
    def __init__(self, image_path):
        self.__path = image_path
        self.__image_data = None
        self.__width = None
        self.__height = None
        self.__channels = None
        self.__load_image_data()
        self.__load_image_metadata()

    def __load_image_data(self):
        print("Reading Image: %s" % self.__path)
        self.__image_data = cv2.imread(self.__path)
        if self.__image_data is None:
            raise ImageNotFound("No image found at: " + self.__path)

    def __load_image_metadata(self):
        self.__height, self.__width, self.__channels = self.__image_data.shape
        print("Width: %d | Height: %d | Channels: %d" % (self.__width, self.__height, self.__channels))

    def get_data(self):
        return copy.deepcopy(self.__image_data)

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_channels(self):
        return self.__channels

    def get_path(self):
        return self.__path


class ImageNotFound(Exception):
    """Raised when the image cannot be found"""
    pass
