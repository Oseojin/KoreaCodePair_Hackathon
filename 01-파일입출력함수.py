f = open("./test.txt", "w")
for i in range(1, 6):
    f.write(f"{i}번째 줄 입니다.\n")
f.close()

f = open("./test.txt", "r")
result = f.readlines()
f.close()
for i in result:
    print(i.strip())