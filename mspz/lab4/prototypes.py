#
# Прототипы
#
nextid = 0

class Frame:
  def __init__(self):
    global nextid
    self.set_id(nextid)

  def __str__(self) -> str:
    outstr = []

    for key in self.__dict__:
      outstr.append('{}: {}'.format(key, repr(self.__dict__[key])))

    outstr.append('')

    return '\n'.join(outstr)

  def __repr__(self) -> str:
    return '{} - {}'.format(type(self).__name__, self.id)

  def set_id(self, id):
    global nextid
    self.id = id
    nextid = id + 1

  def toLine(self):
    return repr(self)


class File(Frame):
  def __init__(self, file_type, name, creation_date, last_change_date, size, location):
    super()

    self.file_type = file_type
    self.name = name
    self.creation_date = creation_date
    self.last_change_date = last_change_date
    self.size = size
    self.location = location


class Directory(Frame):
  def __init__(self, name, creation_date, location):
    super()

    self.name = name
    self.creation_date = creation_date
    self.location = location


class Disk(Frame):
  def __init__(self, name, max_size):
    super()

    self.name = name
    self.max_size = max_size


class Contains(Frame):
  def __init__(self, children, parent):
    super()

    self.children = children
    self.parent = parent