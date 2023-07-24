#DemoIndexing.py

strA = "python is very powerful"
print(strA[0])
print(strA[1])
print(strA[0:3])
#축약된표현식
print(strA[:3])
#디버깅하지 않고 CTRL+F5
print(strA[-3:])
print(strA[-8:])

#LIST
colors = ["red",'green','blue']
print(colors)
print(len(colors))
print(colors[0])

colors.append("black")
print(colors)

#디버깅할 때 중단점(breadk point)
for item in colors:
    print(item)

colors.append("white")
print(colors)
colors.insert(1,'pink')
print(colors)
print(colors.index('red'))
colors += "red"
print(colors.pop())
print(colors.pop())
print(colors.pop(1))
print(colors)

colors.extend(["red",'green','blue','pink'])
print(colors)
colors.remove('blue')
colors.remove('r')
print(colors)
colors.sort()
print(colors)
colors.reverse()
print(colors)

def calc(a,b):
        return a+b, a*b
result = calc(5,6)
print(result)
