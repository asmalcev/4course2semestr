from components.entry import create_entry
from components.option_list import create_option_list

def fill_with_inputs(root, config, data, storage):
  for field in config:
    if field['type'] == 'text':
      storage.append(create_entry(root, field['name']))
    elif field['type'] == 'frame':
      options = list(map(
        lambda frame: frame.toLine(),
        filter(field['filter'], data.data)
      ))
      storage.append(create_option_list(root, field['name'], 'Выбрать фрейм', options)[0])

def remove_children(element):
  for child in element.winfo_children():
    child.destroy()