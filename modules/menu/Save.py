import datetime
import shelve


class Save(object):
    """ Сохранение / звгрузка """

    def __init__(self):
        name = self.file_name()
        path = "save/" + name
        self.file = shelve.open(path)
        self.data = None

    def __del__(self):
        self.file.close()

    def save_game(self, data):
        self.data = data
        self.file.data = self.data

    def load_game(self):
        self.file.data = self.data
        return self.data

    def file_name(self):
        dt = datetime.datetime.today()
        date = str(dt.year) + '_' + str(dt.month) + '_' + str(dt.day)
        time = str(dt.hour) + '_' + str(dt.minute) + '_' + str(dt.second)
        name = 'save-' + date + '-' + time
        return name

    def clear_folder(self):
        # список файлов в папке
        # os.listdir(path=".")
        # удаляем файл
        # os.remove("Test.txt")
        pass
