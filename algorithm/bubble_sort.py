"""
冒泡排序练习
"""
data = [10, 4, 33, 21, 54, 3, 8, 11, 5, 22, 2, 1, 17, 13, 16]
count = 0
for i in range(len(data)):
    for j in range(i+1, len(data)):
        if data[i] > data[j]:
            data[i], data[j] = data[j], data[i]
        count+=1

print(data, count)
