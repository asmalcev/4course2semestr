import tkinter as tk

import consts

def create_entry(root, title):
  local_frame = tk.Frame(root)

  tk.Label(local_frame, text=title).pack(consts.PADDINGS, side=tk.LEFT)
  entry = tk.Entry(local_frame).pack(consts.PADDINGS, fill=tk.X, side=tk.LEFT, expand=True)

  local_frame.pack(fill=tk.X)

  return entry