import tkinter as tk

import consts

def create_divider(root, width):
  c = tk.Canvas(root, width=width, height=consts.PADDING * 2)
  c.create_line(consts.PADDING, consts.PADDING, width - consts.PADDING, consts.PADDING)

  return c
