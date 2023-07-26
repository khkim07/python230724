#DemoFile.py

print("---오른쪽 정렬---")
for x in range(1,6):
    print(x , "*" , x , "=" , x*x)

print("---오른쪽 정렬---")
for x in range(1,6):
    print(x , "*" , x , "=" , str(x*x).rjust(3))

print("---@로 채우기---")
for x in range(1,6):
    print(x , "*" , x , "=" , str(x*x).zfill(5))


#파일쓰기
f = open("c:\\work\\demo.txt","wt",encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close()

#파일읽기
f = open("c:\\work\\demo.txt","rt",encoding="utf-8")
result = f.read()
f.close()
print(result)