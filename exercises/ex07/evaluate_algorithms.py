"""Will evaluate and visualize the runtimes of sorting functions of increasing size."""
__author__ = "730469865"
from exercises.ex07.runtime_analysis_functions import *
from matplotlib import pyplot as plt

START_SIZE: int = 0
END_SIZE: int = 1000


times = evaluate_runtime("selection_sort", START_SIZE, END_SIZE)
plt.plot(times)
plt.title("Runtime Analysis of Selection Sort - erarnold")
plt.show()


times = evaluate_runtime("insertion_sort", START_SIZE, END_SIZE)
plt.plot(times)
plt.title("Runtime Analysis of Insertion Sort - erarnold")
plt.show()

usage = evaluate_memory_usage("selection_sort", START_SIZE, END_SIZE)
plt.plot(usage)
plt.title("Memory Usage Analysis of Selection Sort - erarnold")
plt.show()
 
usage = evaluate_memory_usage("insertion_sort", START_SIZE, END_SIZE)
plt.plot(usage)
plt.title("Memory Usage Analysis of Insertion Sort - erarnold")
plt.show()