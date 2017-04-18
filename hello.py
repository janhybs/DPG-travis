import sys
import multiprocessing as mp

print("Python version %s " % str(sys.version))
print("Cores          %s " % str(mp.cpu_count()))


if True:
  print("tady")
else:
  print("tady nikdy")
  a = 0
  b = 1
  c = b / a
