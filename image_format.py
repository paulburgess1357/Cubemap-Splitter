"""
The purpose of the image_format module is to provide a class that contains the various format types that a cubemap
can be created as.  Additionally, a mapping class is provided that simply maps the index values to real world names.

Classes
----------
ImageFormat
ImageMapper
"""

import copy


class ImageFormat:
    """
    The ImageFormat class contains dictionary and dimension information for the various possible accepted cubemap
    formats.

    ...

    Methods
    -------
    get_format_dict(format_type)
        Returns a format dictionary with mapped values to image blocks.
    get_format_dim(format_type)
        Returns a list with image block dimension information.
    """
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
        """
        Returns a format dictionary with mapped values to image blocks.

        Parameters
        ----------
        format_type : int
            Specific image format type (1 - 5)

        Returns
        -------
        dict
            Dictionary with format information.
        """
        format_dict = ImageFormat.all_format_dicts[format_type - 1]
        return copy.deepcopy(format_dict)

    @staticmethod
    def get_format_dim(format_type):
        """
        Returns a list with image block dimension information.

        Parameters
        ----------
        format_type : int
            Specific image format type (1 - 5)

        Returns
        -------
        list
            List with format information [row_num, col_num].
        """
        format_dims = ImageFormat.all_format_dims[format_type - 1]
        return copy.deepcopy(format_dims)


class ImageMapper:
    """
    The Image mapper class provides the index mapping to name mapping.

    ...

    Methods
    -------
    map_split(image_split_calculation, format_type)
        Returns the mapped value to the split.  For example, when using format_type = 1, the position [0, 1] (row x col)
        is the top of the cubemap.  This would return 'top' in this example.
    """

    @staticmethod
    def map_split(split_index, format_type):
        """
        Returns the mapped value to the split.  For example, when using format_type = 1, the position [0, 1] (row x col)
        is the top of the cubemap.  This would return 'top' in this example.

        Parameters
        ----------
        split_index : SplitIndices
            The index split that is being mapped.
        format_type : int
            Image format type

        Returns
        -------
        str
            Mapped name.  If no match is found, None is returned.
        """
        format_dict = ImageFormat.get_format_dict(format_type)
        image_index = split_index.image_index
        for key, value in format_dict.items():
            if value == image_index:
                return key
        return None
