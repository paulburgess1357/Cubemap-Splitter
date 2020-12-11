from image_format import ImageFormat
from image_format import ImageMapper
import numpy as np
import math
import copy


class SplitIndices:
    """
    The SplitIndices class contains the necessary data for splitting the larger image into the smaller block.

    ...

    Attributes
    ----------
    x_min : int
        Min x value
    x_max : int
        Max x value
    y_min : int
        Min y value
    y_max : int
        Max y value
    image_index : list
        [row, col] block index location
    image_mapped_name : str
        Mapped image name

    Methods
    -------
    print()
        Displays the split index class values.
    set_image_mapped_name()
        Sets the image_mapped_name attribute.
    """
    def __init__(self, x_min, x_max, y_min, y_max, x_index, y_index):
        """
        Parameters
        ----------
        x_min : int
            Min x value
        x_max : int
            Max x value
        y_min : int
            Min y value
        y_max : int
            Max y value
        x_index : int
            Row location of the subset block.
        y_index : int
            Column location of the subset block
        """
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.image_index = [x_index, y_index]
        self.image_mapped_name = None

    def set_image_mapped_name(self, mapped_name):
        """
        Sets the image_mapped_name attribute.

        Parameters
        ----------
        mapped_name : str
            Name of the cubemap block (e.g. top, bottom, etc.)
        """
        self.image_mapped_name = mapped_name

    def print(self):
        """
        Displays the split index class values.
        """
        print("X Min: %d" % self.x_min)
        print("X Max: %d" % self.x_max)
        print("Y Min: %d" % self.y_min)
        print("Y Max: %d" % self.y_max)
        print("Index: (%d, %d)" % (self.image_index[0], self.image_index[1]))
        print("Mapped Name: %s" % self.image_mapped_name)


class ImageSplitCalculator:
    """
    The ImageSplitCalculator class calculates the proper locations to split the data into the 6 desired blocks for the
    cubemap (top, bottom, front, back. left, right).

    ...

    Attributes
    ----------
    __image : Image
        Image class
    __format_type : int
        Image format type
    __image_splits : list
        Image splits (list of SplitIndices)

    Methods
    -------
    get_splits()
        Returns a deep copy of the __image_splits
    """
    def __init__(self, image, format_type):
        """
        Parameters
        ----------
        image : Image
            Loaded image data
        format_type : int
            Image format type
        """
        self.__image = image
        self.__format_type = format_type
        self.__image_splits = []
        self.__set_format_type()
        self.__calculate_splits()

    def __set_format_type(self):
        """
        Sets the __format_type attribute.  If the format type is set to "auto", the AutoImageFormat class will
        calculate the image format type.
        """
        if isinstance(self.__format_type, str):
            auto_format = AutoImageFormat(self.__image)
            self.__format_type = auto_format.calculate_image_format()

    def __calculate_splits(self):
        """
        Sets the __image_splits attribute.  The image data (numpy array) is iterated over block by block.  The image
        data is stored in the SplitIndices class.
        """
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
        """
        Calculates the vertical increment pixel value.
        """
        row_num = ImageFormat.get_format_dim(self.__format_type)[0]
        vertical_increment = math.floor(self.__image.get_height() / row_num)
        return vertical_increment

    def __calculate_horizontal_increment(self):
        """
        Calculates the horizontal increment pixel value.
        """
        col_num = ImageFormat.get_format_dim(self.__format_type)[1]
        horizontal_increment = math.floor(self.__image.get_width() / col_num)
        return horizontal_increment

    def get_splits(self):
        """
        Returns a deep copy of the __image_splits

        Returns
        -------
        list
            List full with SplitIndices classes.
        """
        return copy.deepcopy(self.__image_splits)


class AutoImageFormat:
    """
    The AutoImageFormat class calculates the cubemap image format (types 1 - 5).
    ...

    Attributes
    ----------
    __image : Image
        Image class

    Methods
    -------
    calculate_image_format()
        Calculates and returns the image format type.
    """
    def __init__(self, image):
        """
        Parameters
        ----------
        image : Image
            Loaded image data
        """
        self.__image = image
        self.__ratio = None
        self.__set_ratio()

    def __set_ratio(self):
        """
        Calculates and returns the image format type.
        """
        self.__ratio = self.__image.get_width() / self.__image.get_height()

    def calculate_image_format(self):
        """
        Calculates the image format.

        Returns
        -------
        int
            Image format type.
        """
        if self.__ratio < 0.5:
            return 5
        elif self.__ratio < 1.0:
            return 3
        elif self.__ratio < 2.0:
            return self.__calculate_format_from_pixels()
        else:
            return 4

    def __calculate_format_from_pixels(self):
        """
        Calculates the image format from pixel values.

        Returns
        -------
        int
            Image format type.
        """
        image_split_calculator = ImageSplitCalculator(self.__image, 1)
        image_splits = image_split_calculator.get_splits()

        square_compare_1 = self.__subset_image_data(image_splits, 2)
        square_compare_2 = self.__subset_image_data(image_splits, 3)

        overlap_pct = self.__calculate_element_overlap_pct(square_compare_1, square_compare_2)
        return self.__calculate_format_from_element_overlap(overlap_pct)

    def __subset_image_data(self, image_splits, square_index):
        """
        Subsets the image data by the specified block index.

        Returns
        -------
        numpy array
            Image block array values.
        """
        image_data = self.__image.get_data()
        square_split = image_splits[square_index]
        square_data = image_data[square_split.y_min:square_split.y_max, square_split.x_min:square_split.x_max:]
        return square_data

    @staticmethod
    def __calculate_element_overlap_pct(square_compare_1, square_compare_2):
        """
        Calculates the overlap between two numpy arrays.

        Returns
        -------
        float
            Overlap percent.
        """
        same_element_pct = np.sum(square_compare_1 == square_compare_2) / square_compare_1.size
        return same_element_pct

    @staticmethod
    def __calculate_format_from_element_overlap(overlap_pct):
        """
        Calculates the format type based on the overlap percent.

        Returns
        -------
        int
            Format type.
        """
        if overlap_pct >= 0.90:
            return 1
        else:
            return 2
