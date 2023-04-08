import tkinter as tk
from tkinter import filedialog as fd
from tkinter import simpledialog as sd
from tkinter import messagebox as mb

import consts
from graph import Graph
from choices import choices



root = tk.Tk()
root.title('Представление знаний семантическими сетями')
root.minsize(consts.MAIN_WINDOW_WIDTH, consts.MAIN_WINDOW_HEIGHT)

def destroy_root():
  root.destroy()



graph = Graph()



#
# SELECT FILE FRAME
#
def select_file():
  filename = fd.askopenfilename()
  if filename:
    graph.set_file(filename)

def create_file():
  filename = fd.asksaveasfilename()
  if filename:
    graph.set_file(filename)

open_graph_frame = tk.Frame(root)

tk.Button(open_graph_frame, text='Открыть граф', command=select_file).pack(consts.PADDINGS, side=tk.TOP)
tk.Button(open_graph_frame, text='Создать граф', command=create_file).pack(consts.PADDINGS, side=tk.TOP)



#
# EDIT GRAPH FRAME
#
def add_node():
  node_name = sd.askstring('Добавление узла', 'Введите название узла')
  if node_name:
    graph.add_node(node_name)


def edit_node():
  def action(node_name):
    new_node_name = sd.askstring('Изменение узла', 'Введите новое название узла')

    if not new_node_name:
      mb.showerror('Ошибка', 'Название узла не указано')
      return

    graph.edit_node(node_name, new_node_name)

  choices('Изменение узла', graph.get_nodes(), action, 'Выберите узел', 'Готово')


def remove_node():
  def action(node_name):
    graph.remove_node(node_name)

  choices('Удаление узла', graph.get_nodes(), action, 'Выберите узел', 'Готово')


def add_connection():
  def action(node1):
    def action2(node2):
      connection_name = sd.askstring('Добавление связи', 'Введите название связи')

      if connection_name:
        graph.add_connection(connection_name, node1, node2)

    choices('Добавление связи', graph.get_nodes(), action2, 'Выберите узел', 'Готово')
  choices('Добавление связи', graph.get_nodes(), action, 'Выберите узел', 'Готово')


def remove_connection():
  def action(node1):
    def action2(node2):
      graph.remove_connection(node1, node2)

    choices('Удаление связи', graph.get_nodes(), action2, 'Выберите узел', 'Готово')
  choices('Удаление связи', graph.get_nodes(), action, 'Выберите узел', 'Готово')


def edit_connection():
  def action(node1):
    def action2(node2):
      connection_name = sd.askstring('Изменение связи', 'Введите название связи')

      if connection_name:
        graph.edit_connection(connection_name, node1, node2)

    choices('Изменение связи', graph.get_nodes(), action2, 'Выберите узел', 'Готово')
  choices('Изменение связи', graph.get_nodes(), action, 'Выберите узел', 'Готово')


def find():
  node1 = sd.askstring('Поиск связности понятий', 'Введите название первого узла')

  if not node1:
    mb.showerror('Ошибка', 'Название узла не указано')
    return

  node2 = sd.askstring('Поиск связности понятий', 'Введите название второго узла')

  if not node2:
    mb.showerror('Ошибка', 'Название узла не указано')
    return

  graph.find(node1, node2)


def show_graph():
  graph.show()


def close_graph():
  graph.set_file(None)


edit_graph_frame = tk.Frame(root)

controls_frame = tk.Frame(edit_graph_frame)
tk.Button(controls_frame, text='Добавить узел', command=add_node).pack(consts.PADDINGS, side=tk.TOP, anchor=tk.W)
tk.Button(controls_frame, text='Удалить узел', command=remove_node).pack(consts.PADDINGS, side=tk.TOP, anchor=tk.W)
tk.Button(controls_frame, text='Изменить узел', command=edit_node).pack(consts.PADDINGS, side=tk.TOP, anchor=tk.W)
tk.Button(controls_frame, text='Добавить связь', command=add_connection).pack(consts.PADDINGS, side=tk.TOP, anchor=tk.W)
tk.Button(controls_frame, text='Удалить связь', command=remove_connection).pack(consts.PADDINGS, side=tk.TOP, anchor=tk.W)
tk.Button(controls_frame, text='Изменить связь', command=edit_connection).pack(consts.PADDINGS, side=tk.TOP, anchor=tk.W)
tk.Button(controls_frame, text='Построить граф', command=show_graph).pack(consts.PADDINGS, side=tk.TOP, anchor=tk.W)
tk.Button(controls_frame, text='Поиск связности понятий', command=find).pack(consts.PADDINGS, side=tk.TOP, anchor=tk.W)
tk.Button(controls_frame, text='Закрыть граф', command=close_graph).pack(consts.PADDINGS, side=tk.BOTTOM, anchor=tk.W)
controls_frame.pack(side=tk.LEFT, anchor=tk.W, fill=tk.BOTH, expand=True)

filename_var = tk.StringVar()
tk.Label(edit_graph_frame, textvariable=filename_var).pack(side=tk.RIGHT, anchor=tk.N)
tk.Label(edit_graph_frame, text='Файл:').pack(side=tk.RIGHT, anchor=tk.N)




def toggle_file_select():
  if graph.has_file():
    open_graph_frame.place_forget()
    filename_var.set(graph.get_filename())
    edit_graph_frame.pack(consts.PADDINGS, side=tk.TOP, anchor=tk.W, fill=tk.BOTH, expand=True)
  else:
    edit_graph_frame.pack_forget()
    open_graph_frame.place(relx=.5, rely=.5, anchor="c")

toggle_file_select()
graph.subscribe(toggle_file_select)


# MAIN LOOP
root.mainloop()

graph.save()