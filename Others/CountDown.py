from time import strftime, localtime

d = strftime("%M:%S", localtime())
f = strftime("%M:%S", localtime())
start_time = int(d[3:5])
finish_time = int(f[3:5])

print(start_time, finish_time)
