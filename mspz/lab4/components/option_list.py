import tkinter as tk

import consts

def create_option_list(root, title, std_value, options):
  local_frame = tk.Frame(root)

  value_inside = tk.StringVar(local_frame)
  value_inside.set(std_value)

  tk.Label(local_frame, text=title).pack(consts.PADDINGS, side=tk.LEFT)
  opt_list = tk.OptionMenu(local_frame, value_inside, *options).pack(consts.PADDINGS, fill=tk.X, side=tk.LEFT)

  local_frame.pack(fill=tk.X)

  return (value_inside, opt_list)