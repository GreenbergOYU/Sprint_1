times = '1h 45m,360s,25m,30m 120s,2h 60s'
time_summ = 0
def time_period  (var1):
    if 'h' in var1:
        var1 = var1.replace('h','')
        return int(var1)*60
    if 'm' in var1:
        var1 = var1.replace('m', '')
        return int(var1)
    if 's' in var1:
        var1 = var1.replace('s', '')
        return int(var1) / 60
time_list = times.split(',')
for i in time_list:
    var2 = i.split(' ')
    for j in var2:
      time_summ += time_period(j)
print(time_summ)