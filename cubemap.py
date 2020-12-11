from image import Image
from image_splitter import ImageSplitCalculator
from image_writer import BlockImageWriter


def split_cubemap(image_path, format_type="auto", output_directory=None):
    image = Image(image_path)
    image_split_calculator = ImageSplitCalculator(image, format_type)
    image_writer = BlockImageWriter(image, image_split_calculator, output_directory)
    image_writer.write_image_blocks()