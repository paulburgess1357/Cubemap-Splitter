import cv2
import copy


class ImageLoader:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image_data = None
        self.image_width = None
        self.image_height = None
        self.image_channels = None
        self.__load_image()
        self.__load_image_metadata()

    def __load_image(self):
        print("Reading Image: " + self.image_path)
        self.image_data = cv2.imread(self.image_path)

    def __load_image_metadata(self):
        self.image_height, self.image_width, self.image_channels = self.image_data.shape
        print("Image Metadata: Width: %d | Height: %d | Channels: %d" % (self.image_width, self.image_height,
                                                                         self.image_channels))

    def get_image_data(self):
        return copy.deepcopy(self.image_data)

    def get_image_width(self):
        return self.image_width

    def get_image_height(self):
        return self.image_height

    def get_image_channels(self):
        return self.image_channels
