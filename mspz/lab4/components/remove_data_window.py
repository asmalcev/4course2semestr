import tkinter as tk

import consts
from utils import *

def open_remove_data_window(root, title, data):
  window = tk.Toplevel(root)
  window.title(title)
  window.minsize(consts.MAIN_WINDOW_WIDTH, consts.MAIN_WINDOW_HEIGHT)

  tk.Label(window, text=title).pack(consts.PADDINGS, side=tk.TOP)

  box = tk.Listbox(window, selectmode=tk.EXTENDED)
  scroll = tk.Scrollbar(command=box.yview)
  scroll.pack(side=tk.RIGHT, fill=tk.Y)
  box.config(yscrollcommand=scroll.set)

  def delete_item():
    select = list(map(lambda i: data.data[i], box.curselection()))
    for d in select:
      data.remove(d)

  delete_btn_frame = tk.Frame(window)
  tk.Label(delete_btn_frame, text='Выберите элементы для удаления').pack(consts.PADDINGS, side=tk.LEFT)
  tk.Button(delete_btn_frame, text='Удалить', command=delete_item).pack(consts.PADDINGS, side=tk.RIGHT)

  delete_btn_frame.pack(side=tk.TOP, fill=tk.X)
  box.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

