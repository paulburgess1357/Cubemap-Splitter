import os


class ImageFilePaths:
    """
    The ImageFilePaths class handles folder creation and image path values.

    ...

    Attributes
    ----------
    __full_path : str
        Full path to image
    __base_dir : str
        Base folder containing the image
    __new_folder_name : str
        Output folder name
    __new_folder_path : str
        Output folder path
    __file_extension : str
        Output file extension (e.g. .jpg, .png. etc.)

    Methods
    -------
    create_new_folder()
        Creates a brand new folder.  This will be located in the same location as the image.  The name of the folder is
        based on the image name.  If a folder with the image name exists, the folder will be named <image_name>_v1,
        <image_name>_v2, etc.
    get_base_dir()
        Returns the path to the directory containing the image.
    get_new_folder_name()
        Returns the new folder (being created) name.
    get_new_folder_path()
        Returns the full path that includes the new_folder_name.
    get_file_extension()
        Returns the file extension for the image.
    """

    def __init__(self, image_path):
        """
        Parameters
        ----------
        image_path : str
            Full path to image
        """
        self.__full_path = image_path
        self.__base_dir = None
        self.__new_folder_name = None
        self.__new_folder_path = None
        self.__file_extension = None
        self.__set_folder_values()

    def __set_folder_values(self):
        """
        Loads the following attributes:
        __base_dir
        __new_folder_name
        __new_folder_path
        __file_extension
        """
        self.__set_base_directory()
        self.__set_new_folder_name()
        self.__set_new_folder_path()
        self.__set_file_extension()

    def __set_base_directory(self):
        """
        Sets the base directory: __base_dir.
        """
        self.__base_dir = os.path.dirname(self.__full_path)

    def __set_new_folder_name(self):
        """
        Sets the new_folder_name: __new_folder_name.
        """
        self.__new_folder_name = os.path.basename(os.path.splitext(self.__full_path)[0])

    def __set_new_folder_path(self):
        """
        Sets the new_folder_path: __new_folder_path.  If the directory exists, the __new_folder_name will be updated
        to: <image_name>_v1. <image_name>_v2, etc.
        """
        full_path = os.path.join(self.__base_dir, self.__new_folder_name)
        folder_append = 1
        while os.path.exists(full_path):
            full_path = os.path.join(self.__base_dir, self.__new_folder_name + "_v" + str(folder_append))
            folder_append += 1
        self.__new_folder_path = full_path

    def __set_file_extension(self):
        """
        Sets the file extension: __file_extension
        """
        self.__file_extension = os.path.splitext(self.__full_path)[1]

    def create_new_folder(self):
        """
        Creates a new directory.  The directory name is the image name without the extension.  The location is where
        the image is located.
        """
        os.mkdir(self.__new_folder_path)

    def get_base_dir(self):
        """
        Returns the path to the directory containing the image.

        Returns
        -------
        str
            Image base directory.
        """
        return self.__base_dir

    def get_new_folder_name(self):
        """
        Returns the new folder (being created) name.

        Returns
        -------
        str
            Image new folder name
        """
        return self.__new_folder_name

    def get_new_folder_path(self):
        """
        Returns the full path that includes the new_folder_name.

        Returns
        -------
        str
            Image new folder path.
        """
        return self.__new_folder_path

    def get_file_extension(self):
        """
        Returns the file extension for the image.

        Returns
        -------
        str
            Image file extension.
        """
        return self.__file_extension
