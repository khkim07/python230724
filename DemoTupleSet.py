#DemoTupleSet.py

a = {1,2,3,3}
b = {3,4,4,5}
print(a)
print(type(a))
print(a.union(b))
print(a.intersection(b)) # 교
print(a.difference(b)) # 차

print('-----tuple-------')
tp = (10,20,30)
print(len(tp))
print(tp[0])
print("id:%s, name:%s" %("kim","김유신"))

# 함수정의
def calc(a,b):
    return a+b, a*b
result = calc(3,4)
print(result)


##형식변환
a = set((1,2,3))
print(a)
b = list(a)
b.append(4)
print(b)
c = tuple(b)
print(c)

color = {"apple":"red" ,"banana":"yellow"}
print(len(color))
print(color["apple"])
color["cherry"] = "red"
print(color)


isRight = False
print(type(isRight))
