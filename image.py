import cv2
import copy


class Image:
    def __init__(self, image_path, format_type):
        self.path = image_path
        self.format_type = format_type
        self.data = None
        self.width = None
        self.height = None
        self.channels = None
        self.__load()
        self.__load_metadata()

    def __load(self):
        print("Reading Image: " + self.path)
        self.data = cv2.imread(self.path)
        if self.data is None:
            raise ImageNotFound("No image found at: " + self.path)

    def __load_metadata(self):
        self.height, self.width, self.channels = self.data.shape
        print("Image Metadata: Width: %d | Height: %d | Channels: %d" % (self.width, self.height,
                                                                         self.channels))

    def get_format_type(self):
        return self.format_type

    def get_data(self):
        return copy.deepcopy(self.data)

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_channels(self):
        return self.channels

    def get_path(self):
        return self.path


class ImageNotFound(Exception):
    """Raised when the image cannot be found"""
    pass
