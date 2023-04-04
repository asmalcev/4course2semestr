import tkinter as tk

import consts

class List(tk.Text):
  def __init__(self, *args):
    tk.Text.__init__(self, *args, state='disabled', height=4)

  def insert(self, *args):
    self.config(state='normal')
    super().insert(*args)
    self.config(state='disabled')

  def clear(self):
    self.config(state='normal')
    self.delete('1.0', tk.END)
    self.config(state='disabled')

def create_scrollable_list(root, *args):
  container = tk.Frame(root)
  L = List(container, *args)

  scroll = tk.Scrollbar(container, command=L.yview)
  scroll.pack(side=tk.RIGHT, fill=tk.Y)

  L.config(yscrollcommand=scroll.set)

  L.pack(consts.PADDINGS, side=tk.BOTTOM, fill=tk.BOTH, expand=True)

  return (L, container)