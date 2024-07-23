#INDEX ERROR:
try:
    arr=[1,7,8,12,36]
    print(arr[41])
except IndexError:
    print('cannot access index value')
else:
    print('no exception occured')
finally:
    print('Finally Wednesday is a last day of training')