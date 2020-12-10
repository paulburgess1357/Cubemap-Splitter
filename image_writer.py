import cv2
from image_format import ImageMapper


class ImageWriter:
    def __init__(self, image_data, image_splits, extension):
        self.image_data = image_data
        self.image_splits = image_splits
        self.extension = extension

    def write_images(self, output_folder):
        for image_split in self.image_splits:
            file_name = image_split.get_image_mapped_name()
            if file_name:
                cv2.imwrite(output_folder + "/" + file_name + self.extension,
                            self.image_data[image_split.y_min:image_split.y_max, image_split.x_min:image_split.x_max:])