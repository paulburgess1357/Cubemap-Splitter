import math
import copy


class SplitIndices:
    def __init__(self, x_min, x_max, y_min, y_max, x_index, y_index):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.image_index = [x_index, y_index]

    def print(self):
        print("X Min: " + str(self.x_min))
        print("X Max: " + str(self.x_max))
        print("Y Min: " + str(self.y_min))
        print("Y Max: " + str(self.y_max))
        print("Index: (%d, %d)" % (self.image_index[0], self.image_index[1]))


class SkyboxSplitter:
    def __init__(self, image_loader):
        self.image_loader = image_loader
        self.image_splits = None

    def calculate_horizontal_increment(self):
        horizontal_increment = math.floor(self.image_loader.get_image_width() / 4)
        return horizontal_increment

    def calculate_vertical_increment(self):
        vertical_increment = math.floor(self.image_loader.get_image_height() / 3)
        return vertical_increment

    def calculate_image_splits(self):
        print("Calculating Splits")
        self.image_splits = []

        image_data = self.image_loader.get_image_data()
        vertical_increment = self.calculate_vertical_increment()
        horizontal_increment = self.calculate_horizontal_increment()

        for x_index, y in enumerate(range(0, image_data.shape[0], vertical_increment)):
            for y_index, x in enumerate(range(0, image_data.shape[1], horizontal_increment)):
                self.image_splits.append(SplitIndices(x, x + horizontal_increment, y, y + vertical_increment, x_index, y_index))

    def get_image_splits(self):
        return copy.deepcopy(self.image_splits)


class SkyboxMapper:
    pass
