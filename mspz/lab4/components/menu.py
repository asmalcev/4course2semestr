import tkinter as tk

def init_menu(root, props):
  menu = tk.Menu(root, tearoff=0)

  for prop in props:
    if 'type' in prop and prop['type'] == 'nested':
      menu.add_cascade(prop['menu'])
    else:
      menu.add_command(prop)

  return menu