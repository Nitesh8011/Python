import psutil

print(psutil.cpu_count())
print(psutil.disk_usage('/'))
print(psutil.virtual_memory())
print(psutil.net_connections())