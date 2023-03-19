import datetime

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


#
# экземпляры
#
diskC = Disk(
  name='Диск C',
  max_size=78680887515136
)

mspz = Directory(
  name='МСПЗ',
  creation_date=datetime.datetime(
    year=2023,
    month=3,
    day=19,
    hour=11,
    minute=47,
  ),
  location=diskC
)

report1 = File(
  file_type='pdf',
  name='Отчет',
  creation_date=datetime.datetime(
    year=2023,
    month=3,
    day=19,
    hour=12,
    minute=0,
  ),
  last_change_date=datetime.datetime(
    year=2023,
    month=3,
    day=19,
    hour=12,
    minute=20,
  ),
  size=352512,
  location=mspz
)

report2 = File(
  file_type='pdf',
  name='Отчет2',
  creation_date=datetime.datetime(
    year=2023,
    month=3,
    day=19,
    hour=12,
    minute=24,
  ),
  last_change_date=datetime.datetime(
    year=2023,
    month=3,
    day=19,
    hour=12,
    minute=36,
  ),
  size=144326,
  location=mspz
)

c1 = Contains(children=diskC, parent=mspz)
c2 = Contains(children=mspz, parent=report1)
c3 = Contains(children=mspz, parent=report2)