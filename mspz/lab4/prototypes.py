#
# прототипы
#
class File:
  def __init__(self, file_type, name, creation_date, last_change_date, size, location):
    self.file_type = file_type
    self.name = name
    self.creation_date = creation_date
    self.last_change_date = last_change_date
    self.size = size
    self.location = location

class Directory:
  def __init__(self, name, creation_date, location):
    self.name = name
    self.creation_date = creation_date
    self.location = location

class Disk:
  def __init__(self, name, max_size):
    self.name = name
    self.max_size = max_size

class Contains:
  def __init__(self, children, parent):
    self.children = children
    self.parent = parent