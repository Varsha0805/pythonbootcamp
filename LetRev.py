def check(s):
    rev=' '
    for i in s:
        rev=i+rev
    print(type(rev))
    return rev 
s='sri devi is engineering college'
print(check(s))