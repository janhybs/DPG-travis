import sys
import multiprocessing as mp

print("Python version %s " % str(sys.version))
print("Cores          %s " % str(mp.cpu_count()))


if 1:
  print("tady")
else:
  print("tady nikdy")
