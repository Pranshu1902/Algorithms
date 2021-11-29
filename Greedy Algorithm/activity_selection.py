# Activity Selection

activities = [[1020, 1100], [1030, 1130], [1100, 1200], [1000, 1130], [900, 1100]]

activities.sort(key = lambda x: x[1])

print(activities)

done = [activities[0]]

max = 1

for i in range(1,len(activities)-1):
    if done[-1][1] <= activities[i+1][0]:
        max += 1
        done.append(activities[i+1])

print(done)
print(max)
