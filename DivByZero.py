#DIVIDE BY ZERO ERROR:
try:
    a=10
    b=0
    c=a/b
    print(c)
except Exception:
    print('Divide by zero is not possible')