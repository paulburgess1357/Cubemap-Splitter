from image_format import ImageFormat
from image_format import ImageMapper
import numpy as np
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

    def set_image_mapped_name(self, mapped_name):
        self.image_mapped_name = mapped_name

    def print(self):
        print("X Min: %d" % self.x_min)
        print("X Max: %d" % self.x_max)
        print("Y Min: %d" % self.y_min)
        print("Y Max: %d" % self.y_max)
        print("Index: (%d, %d)" % (self.image_index[0], self.image_index[1]))
        print("Mapped Name: %s" % self.image_mapped_name)


class ImageSplitCalculator:
    def __init__(self, image, format_type):
        self.__image = image
        self.__format_type = format_type
        self.__image_splits = []
        self.__set_format_type()
        self.__calculate_splits()

    def __set_format_type(self):
        if isinstance(self.__format_type, str):
            auto_format = AutoImageFormat(self.__image)
            self.__format_type = auto_format.get_image_format()

    def __calculate_splits(self):
        vertical_increment = self.__calculate_vertical_increment()
        horizontal_increment = self.__calculate_horizontal_increment()

        image_shape = self.__image.get_data().shape
        for x_index, y in enumerate(range(0, image_shape[0], vertical_increment)):
            for y_index, x in enumerate(range(0, image_shape[1], horizontal_increment)):
                split_indices = SplitIndices(x, x + horizontal_increment, y, y + vertical_increment, x_index, y_index)
                mapped_name = ImageMapper.map_split(split_indices, self.__format_type)
                split_indices.set_image_mapped_name(mapped_name)
                self.__image_splits.append(split_indices)

    def __calculate_vertical_increment(self):
        row_num = ImageFormat.get_format_dim(self.__format_type)[0]
        vertical_increment = math.floor(self.__image.get_height() / row_num)
        return vertical_increment

    def __calculate_horizontal_increment(self):
        col_num = ImageFormat.get_format_dim(self.__format_type)[1]
        horizontal_increment = math.floor(self.__image.get_width() / col_num)
        return horizontal_increment

    def get_splits(self):
        return copy.deepcopy(self.__image_splits)


class AutoImageFormat:

    def __init__(self, image):
        self.image = image
        self.ratio = None
        self.__set_ratio()

    def __set_ratio(self):
        self.ratio = self.image.get_width()/self.image.get_height()

    def get_image_format(self):
        if self.ratio < 0.5:
            return 5
        elif self.ratio < 1.0:
            return 3
        elif self.ratio < 2.0:
            return self.__calculate_format_from_pixels()
        else:
            return 4

    def __calculate_format_from_pixels(self):
        image_split_calculator = ImageSplitCalculator(self.image, 1)
        image_splits = image_split_calculator.get_splits()

        square_compare_1 = self.__subset_image_data(image_splits, 2)
        square_compare_2 = self.__subset_image_data(image_splits, 3)

        overlap_pct = self.__calculate_element_overlap_pct(square_compare_1, square_compare_2)
        return self.__calculate_format_from_element_overlap(overlap_pct)

    def __subset_image_data(self, image_splits, square_index):
        image_data = self.image.get_data()
        square_split = image_splits[square_index]
        square_data = image_data[square_split.y_min:square_split.y_max, square_split.x_min:square_split.x_max:]
        return square_data

    @staticmethod
    def __calculate_element_overlap_pct(square_compare_1, square_compare_2):
        same_element_pct = np.sum(square_compare_1 == square_compare_2) / square_compare_1.size
        return same_element_pct

    @staticmethod
    def __calculate_format_from_element_overlap(overlap_pct):
        if overlap_pct >= 0.90:
            return 1
        else:
            return 2
