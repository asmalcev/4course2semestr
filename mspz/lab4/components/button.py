import tkinter as tk

import consts

def create_button(root, title, btn_options):
  local_frame = tk.Frame(root)

  tk.Label(local_frame, text=title).pack(consts.PADDINGS, side=tk.LEFT)
  btn = tk.Button(local_frame, btn_options).pack(consts.PADDINGS, side=tk.RIGHT)

  local_frame.pack(fill=tk.X)

  return btn