import tkinter as tk

from components.menu import init_menu
from components.option_list import create_option_list
from components.entry import create_entry
from components.button import create_button

import consts
import prototypes
from frame_types import frame_types

root = tk.Tk()
root.title("Представление знаний с помощью фреймов")
root.minsize(consts.MAIN_WINDOW_WIDTH, consts.MAIN_WINDOW_HEIGHT)


def destroy_root():
  root.destroy()

def remove_children(element):
  for child in element.winfo_children():
    child.destroy()

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
u_search_frame = tk.LabelFrame(root, text="Универсальный поиск")
u_search_field = tk.Entry(u_search_frame).pack(consts.PADDINGS, side=tk.LEFT, fill=tk.X, expand=True)
u_search_btn = tk.Button(u_search_frame, text="Искать").pack(consts.PADDINGS, side=tk.LEFT)

u_search_frame.pack(consts.PADDINGS, fill=tk.X)

# Поиск по атрибутам
attr_search_frame = tk.LabelFrame(root, text="")
attrs_search_frame = tk.Frame(attr_search_frame)

(frame_type, _) = create_option_list(attr_search_frame, "Тип фрейма", "Выбрать тип фрейма", list(frame_types.keys()))


def frame_type_change(*props):
  remove_children(attrs_search_frame)

  for field in frame_types[frame_type.get()]:
    if field['type'] == 'entry':
      create_entry(attrs_search_frame, field['name'])


frame_type.trace("w", frame_type_change)

attrs_search_frame.pack(consts.PADDINGS, fill=tk.X)

attr_search_btn = tk.Button(attr_search_frame, text="Искать").pack(consts.PADDINGS, side=tk.LEFT)


toggle_btn_text = tk.StringVar(root)
toggle_btn_text.set("Открыть")

is_attr_search_open = False
def toggle_attr_search():
  global is_attr_search_open

  if is_attr_search_open:
    attr_search_frame.pack_forget()
    toggle_btn_text.set("Открыть")
  else:
    attr_search_frame.pack(consts.PADDINGS, fill=tk.X)
    toggle_btn_text.set("Закрыть")

  is_attr_search_open = not is_attr_search_open

create_button(root, "Поиск по атрибутам", {
  "textvariable": toggle_btn_text,
  "command": toggle_attr_search,
})


# MAIN LOOP
root.mainloop()
