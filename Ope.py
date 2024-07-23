names=['varsha','srija','jaanu','harshini','pragathi']
names.insert(2,'oppo')
print(names)
names.pop()
print(names)
names.remove('srija')
print(names)
names.append('deekshitha')
print(names)
count=1
for ele in names:
    print(count,ele)
    count+=1
for i in range(0,len(names)):
    if i%2==0:
        print(names[i])
for i in range(0,len(names)):
    if i%2==0:
        rev=names[i]
        print(rev[::-1])
    else:
        print(names[i])

