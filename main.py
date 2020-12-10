import image as img
import image_splitter as ims
import image_format as imf
import cv2

test = imf.ImageFormat.get_format_dictionary(1)
test['top'] = None

image_path = "C:\\Users\\paulb\\Desktop\\cubemap_formats\\format_1.png"
image = img.Image(image_path)

image_splitter = ims.ImageSplitter(image)
image_splitter.calculate_splits()

splits = image_splitter.get_splits()

image_mapper = imm.ImageMapper(splits[1], 1)

result = image_mapper.map_split()

image_mapper.map_split()


image = image.get_image_data()
split_image = splits[0]

# TODO make write excepction error.  This returns true if it writes and false if it does not.
cv2.imwrite("c:/users/paulb/desktop/testpaul.png", image[image_split.x_min:image_split.x_max, image_split.y_min:image_split.y_max])