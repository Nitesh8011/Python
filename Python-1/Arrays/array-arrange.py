import array as ar
import numpy as np

arr = ar.array('i', [1, 2, 8, 4, 5, 0, 6, 1])

final_set = list(arr)
print(final_set)

arrange = np.sort(final_set)
print(arrange)