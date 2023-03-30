#
# Прототипы
#
nextid = 0

class File:
  def __init__(self, file_type, name, creation_date, last_change_date, size, location):
    global nextid
    self.id = nextid
    nextid += 1

    self.file_type = file_type
    self.name = name
    self.creation_date = creation_date
    self.last_change_date = last_change_date
    self.size = size
    self.location = location

  def __str__(self) -> str:
    return '\
File: {}\n\
file_type: {}\n\
name: {}\n\
creation_date: {}\n\
last_change_date: {}\n\
size: {}\n\
location: {}\n'\
.format(self.id, self.file_type, self.name, self.creation_date, self.last_change_date, self.size, self.location.toLine())

  def toLine(self) -> str:
    return 'File - {}.{} - {}'.format(self.name, self.file_type, self.id)

  def set_id(self, id):
    global nextid
    self.id = id
    nextid = id + 1


class Directory:
  def __init__(self, name, creation_date, location):
    global nextid
    self.id = nextid
    nextid += 1

    self.name = name
    self.creation_date = creation_date
    self.location = location

  def __str__(self) -> str:
    return '\
Directory: {}\n\
name: {}\n\
creation_date: {}\n\
location: {}\n'\
.format(self.id, self.name, self.creation_date, self.location.toLine())

  def toLine(self) -> str:
    return 'Directory - {} - {}'.format(self.name, self.id)

  def set_id(self, id):
    global nextid
    self.id = id
    nextid = id + 1


class Disk:
  def __init__(self, name, max_size):
    global nextid
    self.id = nextid
    nextid += 1

    self.name = name
    self.max_size = max_size

  def __str__(self) -> str:
    return '\
Disk: {}\n\
name: {}\n\
max_size: {}\n'\
.format(self.id, self.name, self.max_size)

  def toLine(self) -> str:
    return 'Disk - {} - {}'.format(self.name, self.id)

  def set_id(self, id):
    global nextid
    self.id = id
    nextid = id + 1


class Contains:
  def __init__(self, children, parent):
    global nextid
    self.id = nextid
    nextid += 1

    self.children = children
    self.parent = parent

  def __str__(self) -> str:
    return '\
Contains: {}\n\
children: {}\n\
parent: {}\n'\
.format(self.id, self.children.toLine(), self.parent.toLine())

  def toLine(self) -> str:
    return 'Contains - c:{} p:{} - {}'.format(id(self.children), id(self.children), self.id)

  def set_id(self, id):
    global nextid
    self.id = id
    nextid = id + 1