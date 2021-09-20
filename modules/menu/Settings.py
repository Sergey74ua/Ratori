import json

class Settings(object):  # ПОКА ТОЛЬКО НАБРОСОК

    _path_ = 'save/options.json'

    def __init__(self):
        self.options = {
            'game_version': 1,
            'window_width': 800,
            'window_height': 600,
            'window_frequency': 60
        }

        if not self._path_:
            file_json = open(self._path_, mode='w')
            options = {
                'game_version': 1,
                'window_width': 800,
                'window_height': 600,
                'window_frequency': 60
            }
            json.dump(options, file_json)
            file_json.close()
        else:
            path = 'save/options.json'
            file_json = open(path, mode='r')
            json_data = json.load(file_json)

            self.game_version = json_data['game_version']
            self.width = json_data['window_width']
            self.height = json_data['window_height']
            self.fps = json_data['window_frequency']

            file_json.close()

        print("настройки игры")
