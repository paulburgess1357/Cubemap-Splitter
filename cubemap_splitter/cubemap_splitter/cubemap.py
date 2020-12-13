"""
The purpose of the cubemap module is to provide a simple one line function call to take a cubemap image file and split
it into the corresponding blocks (top, bottom, front, back, left, right).

Functions
----------
split_cubemap(image_path, format_type="auto", output_directory=None)
"""


from .image import Image
from .image_splitter import ImageSplitCalculator
from .image_writer import BlockImageWriter


def split_cubemap(image_path, format_type="auto", output_directory=None):
    """
    Splits the cubemap into 6 images (top, bottom, left, right, front back).  The new images will be written to the
    output directory.  If the output directory is not defined, the new images will be written to a new folder that will
    be created at the image location.

    Parameters
    ----------
    image_path : str
        Full path to the image.
    format_type : int, optional
        When format type is set to "auto", the image format will automatically be determined.  If the output images look
        incorrect, you can define the format type (int): 1 - 5.  By default, the format_type is set to auto.

        format_type: 1
            [
                [None, Top, None, None]
                [Left, Front, Right, Back]
                [None, Bottom, None, None]
            ]

        format_type: 2
            [
                [None, None, Top, None]
                [Back, Right, Front, Left]
                [None, None, Bottom, None]
            ]

        format_type: 3
            [
                [None, Top, None]
                [Front, Right, Back]
                [None, Bottom, None]
                [None, Left, None]
            ]

        format_type: 4
            [
                [Right, Left, Top, Bottom, Front, Back]
            ]

        format_type: 5
            [
                [Right]
                [Left]
                [Top]
                [Bottom]
                [Front]
                [Back]
            ]
    output_directory : str, optional
        Output directory to store the new image blocks.  If the output directory is not defined, the new images will be
        written to a new folder that will be created at the image location.
    """
    image = Image(image_path)
    image_split_calculator = ImageSplitCalculator(image, format_type)
    image_writer = BlockImageWriter(image, image_split_calculator, output_directory)
    image_writer.write_image_blocks()
