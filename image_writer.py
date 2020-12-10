import cv2


class ImageWriter:
    def __init__(self, image, image_splits):
        self.image = image,
        self.image_splits = image_splits

    @staticmethod
    def write_image(image, image_split):
        cv2.imwrite("c:/users/pburgess/desktop/testpaul.png", image[image_split.x_min:image_split.x_max, image_split.y_min:image_split.y_max])

