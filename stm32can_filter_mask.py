ID = 0x0600
Mask = 0x07F8
print(bin(ID))
print(bin(Mask))
for i in range(0x0800):
    if i & Mask == ID:
        print(hex(i))