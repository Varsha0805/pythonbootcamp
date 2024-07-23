def check(s):
    s=s.split
    s=reversed(s)
    print(s)
    for i in s:
        rev=i[::-1]  
        print(rev,end=' ')
s='sri devi is engineering college'
check(s)