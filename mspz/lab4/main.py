import tkinter as tk
import re

from components.menu import init_menu
from components.option_list import create_option_list
from components.button import create_button
from components.list import create_scrollable_list
from components.add_data_window import open_add_data_window
from components.remove_data_window import open_remove_data_window

import consts
import prototypes
from frame_types import frame_types, frame_types_classes
from datalist import Data
from utils import *

data = Data('dump.json')

root = tk.Tk()
root.title('Представление знаний с помощью фреймов')
root.minsize(consts.MAIN_WINDOW_WIDTH, consts.MAIN_WINDOW_HEIGHT)


def destroy_root():
  root.destroy()

#
# INIT MAIN WINDOW COMPONENTS
#

# Универсальный поиск
u_search_frame = tk.LabelFrame(root, text='Универсальный поиск')
u_search_field = tk.Entry(u_search_frame)
u_search_field.pack(consts.PADDINGS, side=tk.LEFT, fill=tk.X, expand=True)


def u_search_set_filter():
  request = u_search_field.get()
  data.set_filter(lambda frame: str(frame).find(request) > -1)


u_search_btn = tk.Button(u_search_frame, text='Искать', command=u_search_set_filter).pack(consts.PADDINGS, side=tk.LEFT)

u_search_frame.pack(consts.PADDINGS, fill=tk.X)

# Поиск по атрибутам
attr_search_frame = tk.LabelFrame(root, text='')
attrs_search_frame = tk.Frame(attr_search_frame)

(frame_type, _) = create_option_list(attr_search_frame, 'Тип фрейма', 'Выбрать тип фрейма', list(frame_types.keys()))


inputs_storage = []
def frame_type_change(*props):
  global inputs_storage
  inputs_storage = []

  remove_children(attrs_search_frame)
  fill_with_inputs(attrs_search_frame, frame_types[frame_type.get()], data, inputs_storage)


frame_type.trace('w', frame_type_change)

attrs_search_frame.pack(consts.PADDINGS, fill=tk.X)

def attr_search_set_filter():
  ftype = frame_type.get()

  if not ftype in frame_types:
    return

  values = []
  current_frame_type = frame_types[ftype]

  for i in range(len(inputs_storage)):
    value = inputs_storage[i].get()

    if value:
      values.append((current_frame_type[i], value))

  instance_props = {}
  for v in values:
    current = v[0]

    if current['type'] == 'frame':
      m = re.search(r'\d*$', v[1])
      value = m.group(0)

      if value:
        value = int(value)
        instance_props[current['property_name']] = data.find(lambda v: v.id == value)
    elif current['type'] == 'text':
      instance_props[current['property_name']] = v[1]

  def filter_func(frame):
    is_right_frame_type = frame.__class__ == frame_types_classes[ftype]

    if not is_right_frame_type:
      return False

    for prop in instance_props:
      if repr(getattr(frame, prop)) != repr(instance_props[prop]):
        return False

    return True

  data.set_filter(filter_func)


attr_search_btn = tk.Button(attr_search_frame, text='Искать', command=attr_search_set_filter).pack(consts.PADDINGS, side=tk.LEFT)


toggle_btn_text = tk.StringVar(root)
toggle_btn_text.set('Развернуть')

is_attr_search_open = False
def toggle_attr_search():
  global is_attr_search_open

  if is_attr_search_open:
    attr_search_frame.pack_forget()
    toggle_btn_text.set('Развернуть')
  else:
    attr_search_frame.pack(consts.PADDINGS, fill=tk.X)
    toggle_btn_text.set('Свернуть')

  is_attr_search_open = not is_attr_search_open

create_button(root, 'Поиск по атрибутам', {
  'textvariable': toggle_btn_text,
  'command': toggle_attr_search,
})


def clear_filter():
  data.set_filter(None)

L, L_container = create_scrollable_list(root)
L_container.pack(consts.PADDINGS, side=tk.BOTTOM, fill=tk.BOTH, expand=True)

tk.Button(text='Очистить фильтры', command=clear_filter).pack(side=tk.BOTTOM)

def update_list(data):
  L.clear()
  for frag in data.get_filtered():
    L.insert('0.0', str(frag) + '\n')

data.set_update_callback(update_list)
data.call_update_callback()


def add_instance():
  open_add_data_window(root, 'Добавить экземпляр', data)

def remove_instance():
  open_remove_data_window(root, 'Удалить экземпляры', data)


#
# INIT MENU
#
edit_frames = init_menu(root, [
  {
    'label': 'Добавление',
    'command': add_instance,
  },
  {
    'label': 'Удаление',
    'command': remove_instance,
  },
])
edit_instances = init_menu(root, [
  {
    'label': 'Добавление',
    'command': add_instance,
  },
  {
    'label': 'Удаление',
    'command': remove_instance,
  },
])
menu = init_menu(root, [
  {
    'type': 'nested',
    'menu': {
      'label': 'Фреймы',
      'menu': edit_frames,
    },
  },
    {
    'type': 'nested',
    'menu': {
      'label': 'Экзмепляры',
      'menu': edit_instances,
    },
  },
  {
    'label': 'Выйти',
    'command': destroy_root,
  },
])

root.config(menu=menu)


# MAIN LOOP
root.mainloop()

data.dump()