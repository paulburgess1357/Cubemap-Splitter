from image import Image
from image_splitter import ImageSplitCalculator
from image_writer import ImageWriter

image_path = "C:/Users/paulb/Desktop/cubemap_formats - Copy/format_1.png"
image = Image(image_path, format_type=1)

image_split_calculator = ImageSplitCalculator(image)
image_writer = ImageWriter(image_data=image.get_data(), image_splits=image_split_calculator.get_splits(), extension=".png")

output_folder = "c:/users/paulb/desktop/testing_output"
image_writer.write_images("c:/users/paulb/desktop/testing_output")

# TODO make write excepction error.  This returns true if it writes and false if it does not.