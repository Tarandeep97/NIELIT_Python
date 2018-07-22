f0=0
f1=1
fnxt=0
print(f0)
print(f1)
n = int(input())
while f1<50:
    fnxt=f0+f1
    f0=f1
    f1=fnxt
    if fnxt<=50:
        print(fnxt)
    else:
        break
    print(fnxt)
