from image_format import ImageFormat
from image_format import ImageMapper
import math
import copy


class SplitIndices:
    def __init__(self, x_min, x_max, y_min, y_max, x_index, y_index):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.image_index = [x_index, y_index]
        self.image_mapped_name = None

    def print(self):
        print("X Min: %d" % self.x_min)
        print("X Max: %d" % self.x_max)
        print("Y Min: %d" % self.y_min)
        print("Y Max: %d" % self.y_max)
        print("Index: (%d, %d)" % (self.image_index[0], self.image_index[1]))
        print("Mapped Name: %s" % self.image_mapped_name)

    def get_image_index(self):
        return copy.deepcopy(self.image_index)

    def set_image_mapped_name(self, mapped_name):
        self.image_mapped_name = mapped_name

    def get_image_mapped_name(self):
        return self.image_mapped_name


class ImageSplitCalculator:
    def __init__(self, image):
        self.image_width = image.get_width()
        self.image_height = image.get_height()
        self.format_type = image.get_format_type()
        self.image_shape = image.get_data().shape
        self.image_splits = None
        self.__calculate_splits()

    def __calculate_horizontal_increment(self):
        col_num = ImageFormat.get_format_dimensions(self.format_type)[1]
        horizontal_increment = math.floor(self.image_width / col_num)
        return horizontal_increment

    def __calculate_vertical_increment(self):
        row_num = ImageFormat.get_format_dimensions(self.format_type)[0]
        vertical_increment = math.floor(self.image_height / row_num)
        return vertical_increment

    def __calculate_splits(self):
        print("Calculating Splits")
        self.image_splits = []
        vertical_increment = self.__calculate_vertical_increment()
        horizontal_increment = self.__calculate_horizontal_increment()

        for x_index, y in enumerate(range(0, self.image_shape[0], vertical_increment)):
            for y_index, x in enumerate(range(0, self.image_shape[1], horizontal_increment)):
                split_indices = SplitIndices(x, x + horizontal_increment, y, y + vertical_increment, x_index, y_index)
                split_indices.set_image_mapped_name(ImageMapper.map_split(split_indices, self.format_type))
                self.image_splits.append(split_indices)

    def get_splits(self):
        return copy.deepcopy(self.image_splits)