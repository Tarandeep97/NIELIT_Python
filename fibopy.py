f0=0
f1=1
fnxt=0
print(f0)
print(f1)
while f1<50:
    fnxt=f0+f1
    f0=f1
    f1=fnxt
    if fnxt>34:
        break
    print(fnxt)
