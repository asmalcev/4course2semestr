import tkinter as tk

import consts

def create_divider(root, width):
  c = tk.Canvas(root, width=width, height=consts.PADDING)
  c.create_line(consts.PADDING, consts.PADDING // 2, width - consts.PADDING, consts.PADDING // 2)

  return c
