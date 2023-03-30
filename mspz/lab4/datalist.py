import json

from frame_types import frame_types_classes_en

class Data():
  def __init__(self, dump_filename):
    self.data = []
    self.dump_filename = dump_filename

    self.read_dump()

  def set_update_callback(self, callback):
    self.update_callback = callback

  def append(self, item):
    self.data.append(item)

    if self.update_callback:
      self.update_callback(self)

  def remove(self, item):
    self.delete_deps(item)
    self.data.remove(item)

    if self.update_callback:
      self.update_callback(self)

  def delete(self, index):
    self.delete_deps(self.data[index])
    del self.data[index]

    if self.update_callback:
      self.update_callback(self)

  def find(self, condition):
    for i in self.data:
      if condition(i):
        return i
    return None

  def read_dump(self):
    with open(self.dump_filename, 'r') as f:
      data = json.load(f)

      for d in data:
        data_class = frame_types_classes_en[d['class']]

        id, args = (lambda id, **args: (id, args))(**d['args'])

        is_ok = True
        for key in ['location', 'children', 'parent']:
          if key in args:
            args[key] = self.find(lambda v: v.id == args[key])
            if not args[key]:
              is_ok = False
              break

        if is_ok:
          self.data.append(data_class(**args))
          self.data[-1].set_id(id)

  def dump(self):
    dump = []

    for d in self.data:
      data = {}

      data['class'] = d.__class__.__name__
      data['args'] = d.__dict__

      for key in ['location', 'children', 'parent']:
        if key in data['args']:
          data['args'][key] = data['args'][key].id

      dump.append(data)

    with open(self.dump_filename, 'w') as f:
      json.dump(dump, f)

  def call_update_callback(self):
    if self.update_callback:
      self.update_callback(self)

  def delete_deps(self, item):
    for d in self.data:
      for key in ['location', 'children', 'parent']:
        if hasattr(d, key) and getattr(d, key) == item:
          self.delete_deps(d)
          self.remove(d)
