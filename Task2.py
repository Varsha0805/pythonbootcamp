arr=[1,2,3,4,5]
k=4
first=arr[k-1:]
second=arr[:k-1]
print(first+second)


arr=[1,2,3,4,5]
k=4
first=arr[k-1:]
second=arr[:k-1]
first.extend(second)
print(first)