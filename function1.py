#function1.py

def setValue(newValue):
    x = newValue
    print("지역변수",  x)

result = setValue(5)
print(result)

def swap(x,y):
    return y,x

print(swap(3,4))

def interset(prelist, postlist):
    result = []
    #H(0) | A(1) | M(2)
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result

print(interset("HAM","SPAM"))