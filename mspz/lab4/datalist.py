import json

from frame_types import frame_types_classes_en

class Data():
  def __init__(self, dump_filename):
    self.data = []
    self.dump_filename = dump_filename
    self.update_callback = []

    self.read_dump()

  def set_update_callback(self, callback):
    self.update_callback.append(callback)

  def append(self, item):
    self.data.append(item)

    for callback in self.update_callback:
      callback(self)

  def remove(self, item):
    self.data.remove(item)

    for callback in self.update_callback:
      callback(self)

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

        for key in ['location', 'children', 'parent']:
          if key in args:
            args[key] = self.find(lambda v: v.id == args[key])

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

    # with open(self.dump_filename, 'w') as f:
      # json.dump(dump, f)

  def call_update_callback(self):
    for callback in self.update_callback:
      callback(self)