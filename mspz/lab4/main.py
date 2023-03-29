import math
import tkinter as tk

from components.menu import init_menu
from components.divider import create_divider

import consts
import prototypes

root = tk.Tk()
root.title("Представление знаний с помощью фреймов")
root.minsize(consts.MAIN_WINDOW_WIDTH, consts.MAIN_WINDOW_HEIGHT)
root.maxsize(consts.MAIN_WINDOW_WIDTH, consts.MAIN_WINDOW_HEIGHT)


def destroy_root():
  root.destroy()

#
# INIT MENU
#
mainmenu = init_menu(root, [
  {
    'label': 'Добавление',
  },
  {
    'label': 'Выйти',
    'command': destroy_root,
  },
])
root.config(menu=mainmenu)

#
# INIT MAIN WINDOW COMPONENTS
#

# Универсальный поиск
tk.Label(text="Универсальный поиск").grid(row=0, column=0, pady=consts.PADDING, padx=consts.PADDING)
search_field = tk.Entry().grid(row=0, column=1, pady=consts.PADDING, padx=consts.PADDING)
search_btn = tk.Button(text="Искать").grid(row=0, column=2, pady=consts.PADDING, padx=consts.PADDING)

divider1 = create_divider(root, consts.MAIN_WINDOW_WIDTH)
divider1.grid(row=1, column=0, columnspan=consts.MAIN_WINDOW_COLUMNS)

# MAIN LOOP
root.mainloop()
