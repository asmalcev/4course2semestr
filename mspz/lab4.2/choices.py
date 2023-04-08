import tkinter as tk

import consts

def choices(title, choicelist, callback, text, btntext):
  window = tk.Toplevel()
  window.title(title)
  window.minsize(consts.MAIN_WINDOW_WIDTH, 200)

  tk.Label(window, text=text).pack(consts.PADDINGS, side=tk.TOP)

  var = tk.StringVar()
  var.set('')
  popupMenu = tk.OptionMenu(window, var, *choicelist)
  popupMenu.pack(consts.PADDINGS, side=tk.TOP)

  def done():
    callback(var.get())
    window.destroy()

  tk.Button(window, text=btntext, command=done).pack(consts.PADDINGS, side=tk.TOP)