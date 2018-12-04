from collections import defaultdict
from datetime import datetime
import re

f = open('4.txt')
lines = f.read().splitlines()

date_action = []
for line in lines:
    z = line.split('] ')
    date = z[0][1:]
    action = z[1]
    date = datetime.strptime(date, '%Y-%m-%d %H:%M')
    date_action.append((date, action))

guards_times = defaultdict(list)

for date, action in date_action:
    match = re.match(r'Guard #(\d+)', action)
    if match:
        guard = int(match.groups()[0])
    else:
        guards_times[guard].append((date, action))

guards = guards_times.keys()

guards_sleep = {}
for guard in guards:
    guards_sleep[guard] = {}
    for i in range(0, 60):
        guards_sleep[guard][i] = 0


for guard, dates_actions in guards_times.items():
    start_sleep = False
    for date, action in dates_actions:
        if not start_sleep:
            start_sleep = date
        else:
            start_sleep_minute = start_sleep.minute
            end_sleep_minute = date.minute
            for x in range(start_sleep_minute, end_sleep_minute):
                guards_sleep[guard][x] += 1
            start_sleep = False

result = []
for guard, minutes_sleep in guards_sleep.items():
    k = []
    for minute, sleep_time in minutes_sleep.items():
        k.append((minute, sleep_time))
    k.sort(key=lambda x: x[1])
    minute = k[-1][0]
    time = k[-1][1]
    result.append((guard, minute, time))

result.sort(key=lambda x: x[2])
target_guard = result[-1][0]
target_minute = result[-1][1]
print(target_guard * target_minute)