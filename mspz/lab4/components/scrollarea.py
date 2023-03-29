import tkinter as tk

def create_scroll_area(root):
  scroll_frame = tk.Frame(root)

  scrollbar = tk.Scrollbar(scroll_frame, orient=tk.VERTICAL)
  scrollbar.config(command=tk.YView)

  scroll_frame.pack()

  return scroll_frame