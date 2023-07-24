#DemoDict.py

device = {"아이폰":5, "갤럭시":10 , "윈도우":30}
#search
print(device["아이폰"])
#insert
device["맥북"] = 15
print(device)
#modify
device["아이폰"] = 6
print(device)
device["갤럭시"] = 20
print(device)
#delete
del device["아이폰"]
print(device)

for item in device.items():
    print(item)

for key in device.keys():
    print(key)

for values in device.values():
    print(values)
#print(device.values)

phone = {"kim":"1111", "lee":"2222", "park":"3333"}
print(phone.values())
print(phone.keys())
print("kim" in phone)
print("kang" not in phone)
p = phone
print(p)
print(id(phone),id(p))
p["kang"] = "1234"
print(p)
print(phone)
print(id(phone),id(p))

print("-----논리식------")
isRight = True
print(type(isRight))
print(1<2)
print(1!=2)
print(1==2)
print(True and True and False)
print(True and True and False)
print(True or False or False)
