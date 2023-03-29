import tkinter as tk

def init_menu(root, props):
  mainmenu = tk.Menu(root)

  for prop in props:
    mainmenu.add_command(prop)

  return mainmenu