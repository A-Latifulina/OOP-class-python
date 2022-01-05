list = (47)
count = len(list)
for i in range(count - 1):
        minSubscript = i
        for j in range (i+1, count ):
            if list[j] < list[minSubscript]:
                minSubscript = j
print(minSubscript)
         #   else:
          #      swap(list,i, minSubscript)
