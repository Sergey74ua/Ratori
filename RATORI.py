#!/usr/bin/env python
# -*- coding: utf-8 -*-

# RATORI-game
__author__ = "Sergey Pokid'ko"
__contact__ = "Sergey74ua@gmail.com"
__copyright__ = "Copyright 2020, Hikki Coders"
__credits__ = ["Maxim", "Matvey"]
__date__ = "2020/12/01"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Sergey74ua"
__email__ = "Sergey74ua.github.io"
__status__ = "Production"

from pyautogui import *
from modules.Main import Main

current_version = 1  # запрос текущей версии игры

if __name__ == '__main__':
    main = Main()
    if main.game_version < current_version:
        _title = 'Обновление версии игры'
        _text = ('Ваша версия игры ' + str(main.game_version) + ' устарела.\nМожете скачать новую версию ' + str(current_version))
        alert(text=_text, title=_title, button='OK')
        #confirm(text=_text, title=_title, buttons=['Да', 'Отложить', 'Нет'])
    else:
        main.game_start()
