import tkinter as tk
from tkinter import messagebox as mb
import re

import consts
from frame_types import frame_types, frame_types_classes
from components.option_list import create_option_list
from utils import *

def open_add_data_window(root, title, data):
  window = tk.Toplevel(root)
  window.title(title)
  window.minsize(consts.MAIN_WINDOW_WIDTH, consts.MAIN_WINDOW_HEIGHT)

  tk.Label(window, text=title).pack(consts.PADDINGS)
  (frame_type, _) = create_option_list(window, 'Тип фрейма', 'Выбрать тип фрейма', list(frame_types.keys()))

  attrs_frame = tk.Frame(window)

  inputs_storage = []

  def frame_type_change(*props):
    inputs_storage.clear()
    remove_children(attrs_frame)
    fill_with_inputs(attrs_frame, frame_types[frame_type.get()], data, inputs_storage)

  frame_type.trace('w', frame_type_change)

  attrs_frame.pack(consts.PADDINGS, fill=tk.X)


  def add_instance(e):
    ftype = frame_type.get()

    if not ftype in frame_types:
      return

    values = []

    current_frame_type = frame_types[ftype]
    for i in range(len(inputs_storage)):
      value = inputs_storage[i].get()

      if not value:
        mb.showerror('Ошибка', 'Все поля должны быть заполнены')
        return

      values.append((current_frame_type[i], value))

    instance_props = {}
    for v in values:
      current = v[0]

      if current['type'] == 'frame':
        m = re.search(r'\d*$', v[1])
        value = m.group(0)

        if not value:
          mb.showerror('Ошибка', 'Все поля должны быть заполнены')
          return

        value = int(value)

        instance_props[current['property_name']] = data.find(lambda v: v.id == value)
      elif current['type'] == 'text':
        instance_props[current['property_name']] = v[1]

    data.append(frame_types_classes[ftype](**instance_props))
    window.destroy()


  add_btn = tk.Button(window, text='Добавить')
  add_btn.bind('<Button>', add_instance)
  add_btn.pack(consts.PADDINGS)

