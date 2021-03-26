txt = "00003,00004"

arr = txt.split(",")
for i in arr:
    a = i[0:4]
    b = i[4:]
    print(a,b)