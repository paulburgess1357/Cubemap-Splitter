import os


class ImageFilePaths:
    def __init__(self, full_path):
        self.__full_path = full_path
        self.__base_dir = None
        self.__new_folder_name = None
        self.__new_folder_path = None
        self.__file_extension = None
        self.__set_folder_values()

    def __set_folder_values(self):
        self.__set_base_directory()
        self.__set_new_folder_name()
        self.__set_new_folder_path()
        self.__set_file_extension()

    def __set_base_directory(self):
        self.__base_dir = os.path.dirname(self.__full_path)

    def __set_new_folder_name(self):
        self.__new_folder_name = os.path.basename(os.path.splitext(self.__full_path)[0])

    def __set_new_folder_path(self):
        full_path = os.path.join(self.__base_dir, self.__new_folder_name)
        folder_append = 1
        while os.path.exists(full_path):
            full_path = os.path.join(self.__base_dir, self.__new_folder_name + "_" + str(folder_append))
            folder_append += 1
        self.__new_folder_path = full_path

    def __set_file_extension(self):
        self.__file_extension = os.path.splitext(self.__full_path)[1]

    def create_new_folder(self):
        os.mkdir(self.__new_folder_path)

    def get_base_dir(self):
        return self.__base_dir

    def get_new_folder_name(self):
        return self.__new_folder_name

    def get_new_folder_path(self):
        return self.__new_folder_path

    def get_file_extension(self):
        return self.__file_extension
