def selection(list):
    n = len(list)
    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            if list[min] > list[j]:
                min = j
        list[i], list[min] = list[min], list[i]
    return list


n = int(input("Enter the size : "))
list = []
for i in range(n):
    list.append(int(input("Enter number : ")))

print(list)
sortedList = selection(list)

print(sortedList)