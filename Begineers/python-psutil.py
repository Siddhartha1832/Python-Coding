'''
Install below Python Module before You run this code.
>>> pip install psutil --upgrade

# psutil (python system and process utilities) is a cross-platform library 
# for retrieving information on running processes and system utilization 
# (CPU, memory, disks, network, sensors) in Python. It is useful mainly for 
# system monitoring, profiling, limiting process resources and the management 
# of running processes. It implements many functionalities offered by UNIX 
# command line tools such as: ps, top, lsof, netstat, ifconfig, who, df, kill, 
# free, nice, ionice, iostat, iotop, uptime, pidof, tty, taskset, pmap. 
# psutil currently supports the following platforms such as Linux, Windows, 
# macOS, FreeBSD, OpenBSD, NetBSD, Sun Solaris, AIX.

'''

import psutil
print("\n *** Getting Running Processes and System Utilization *** \n")
print(f' CPU details : {psutil.cpu_times()}')

for x in range(5):
	print(psutil.cpu_percent(interval=1, percpu=True))

print(f'\n CPU Count: {psutil.cpu_count()}')
print(f' CPU Count: {psutil.cpu_count(logical=False)}')
print(f' CPU Stats: {psutil.cpu_stats()}')
print(f' CPU Frequency: {psutil.cpu_freq()}')

# Memory
print(f'\n Virtual Memory: {psutil.virtual_memory()}')
print(f' Swap Memory: {psutil.swap_memory()}')

# Disks
print(f'\n Disk partitions: {psutil.disk_partitions()}')
print(f" Disk Usage: {psutil.disk_usage('/')}")
print(f' Disk IO Counters: {psutil.disk_io_counters(perdisk=False)}')

# Network
print(f'\n Network IO Counter : {psutil.net_io_counters(pernic=True)}')

# Process Management
print(f'\n Process IDs: {psutil.pids()}')
# Replace process ID
proc_id = 4
p = psutil.Process(proc_id)
print(f'\n Process Name : {p.name()} || Process Status : {p.status()} || Process UserName : {p.username()} ')
