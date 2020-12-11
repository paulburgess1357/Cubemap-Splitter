import os


class OutputImagesFilePaths:
    def __init__(self, full_path):
        self.full_path = full_path
        self.base_dir = self.__get_base_directory()
        self.new_folder_name = self.__get_new_folder_name()
        self.new_folder_path = self.__get_new_folder_path()
        self.file_extension = self.__get_file_extension

    def create_new_folder(self):
        os.mkdir(self.new_folder_path)
        return self.new_folder_path

    def __get_new_folder_path(self):
        full_path = os.path.join(self.base_dir, self.new_folder_name)
        folder_append = 1
        while os.path.exists(full_path):
            full_path = os.path.join(self.base_dir, self.new_folder_name + "_" + str(folder_append))
            folder_append += 1
        return full_path

    def __get_new_folder_name(self):
        return os.path.basename(os.path.splitext(self.full_path)[0])

    def __get_base_directory(self):
        return os.path.dirname(self.full_path)

    def __get_file_extension(self):
        return os.path.splitext(self.full_path)[1]