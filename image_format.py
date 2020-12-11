import copy


class ImageFormat:

    format_1 = {
        "top": [0, 1], "left": [1, 0], "front": [1, 1], "right": [1, 2], "back": [1, 3], "bottom": [2, 1]
    }
    format_1_dim = [3, 4]

    format_2 = {
        "top": [0, 2], "left": [1, 3], "front": [1, 2], "right": [1, 1], "back": [1, 0], "bottom": [2, 2]
    }
    format_2_dim = [3, 4]

    format_3 = {
        "top": [0, 1], "left": [3, 1], "front": [1, 0], "right": [1, 1], "back": [1, 2], "bottom": [2, 1]
    }
    format_3_dim = [4, 3]

    format_4 = {
        "top": [0, 2], "left": [0, 1], "front": [0, 4], "right": [0, 0], "back": [0, 5], "bottom": [0, 3]
    }
    format_4_dim = [1, 6]

    format_5 = {
        "top": [2, 0], "left": [1, 0], "front": [4, 0], "right": [0, 0], "back": [5, 0], "bottom": [3, 0]
    }
    format_5_dim = [6, 1]

    all_format_dicts = [format_1, format_2, format_3, format_4, format_5]
    all_format_dims = [format_1_dim, format_2_dim, format_3_dim, format_4_dim, format_5_dim]

    @staticmethod
    def get_format_dict(format_type):
        format_dict = ImageFormat.all_format_dicts[format_type - 1]
        return copy.deepcopy(format_dict)

    @staticmethod
    def get_format_dim(format_type):
        format_dims = ImageFormat.all_format_dims[format_type - 1]
        return copy.deepcopy(format_dims)


class ImageMapper:

    @staticmethod
    def map_split(image_split_calculation, format_type):
        format_dict = ImageFormat.get_format_dict(format_type)
        image_index = image_split_calculation.image_index
        for key, value in format_dict.items():
            if value == image_index:
                return key
        return None
