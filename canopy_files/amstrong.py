a = int(input("enter the no."))
x = a
s = 0
while a != 0:
    no = a % 10
    s = s + no**3
    a = a / 10


print('sum is', s)

if (x == s):
    print(x, "it is amstrong no.")

else:
    print(x, "it is not amstrong no")
