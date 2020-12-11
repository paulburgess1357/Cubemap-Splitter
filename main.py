from image import Image
from image_splitter import ImageSplitCalculator
from image_writer import ImageWriter
from file_path import FilePath

image_path = "C:/Users/paulb/Desktop/night_blue.png"
image = Image(image_path, format_type=1)

image_split_calculator = ImageSplitCalculator(image)


image_writer = ImageWriter(image, image_split_calculator, None)
image_writer.write_images()


#TODO AUto format type
#Directory handler - user says directory or it writes to the image directory in its own folder
# Crop image?