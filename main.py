try:
    import psutil
except:
    print("Please install psutil using pip install psutil")
import os
# Get memory usage information
memory = psutil.virtual_memory()

# Total physical memory in megabytes
total_memory = int(memory.total / 1_000_000_000)

# Available physical memory in megabytes
available_memory = round(memory.available / 1_000_000_000, 2)

# Used physical memory in megabytes
used_memory = round(memory.used / 1_000_000_000, 2)

# Memory usage percentage
memory_percentage = memory.percent

try:
    os.system('clear')
except:
    os.system('cls')
    
print('-------------- Memory Usage Monitor --------------\n')

# Print the memory information in MB
print(f"Total Memory     ==> {total_memory} GB\n")
print(f"Available Memory ==> {available_memory} GB\n")
print(f"Used Memory      ==> {used_memory} GB\n")
print(f"Memory Usage     ==> {memory_percentage} %")