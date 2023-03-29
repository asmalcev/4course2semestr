import json

class Data():
  def __init__(self, dump_filename):
    self.data = []
    self.dump_filename = dump_filename

  def set_update_callback(self, callback):
    self.update_callback = callback

  def append(self, item):
    self.data.append(item)

    if self.update_callback:
      self.update_callback(self)

  def remove(self, item):
    self.data.remove(item)

    if self.update_callback:
      self.update_callback(self)

  def find(self, condition):
    for i in self.data:
      if condition(i):
        return i
    return None

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
      f.write(json.dumps(dump))