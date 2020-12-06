import image_loader as iml
import skybox_splitter as spl

image_path = "C:\\Users\\paulb\\Desktop\\SkyboxFormat.png"
image_loader = iml.ImageLoader(image_path)

skybox_splitter = spl.SkyboxSplitter(image_loader)
skybox_splitter.calculate_image_splits()
