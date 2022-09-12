
from print import oo
from utils import coerce


def parser(csv_string, fun, sep):
  csv_lines = csv_string.split('\n')
  for line in csv_lines:
    t = []
    for element in line.split(sep):
      t.append(coerce(element))
    fun(t)
      

    

    