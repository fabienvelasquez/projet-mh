import psutil

print(f"CPU Usage : {psutil.cpu_percent()}%")

memory = psutil.virtual_memory()
print(f"RAM Usage : {memory.percent}%")

disk = psutil.disk_usage("/")
print(f"DISK Usage : {disk.percent}%")