import random
x=int(input('jaka długość ma mieć haslo'))
z=''
y=("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
for i in range(x):
    z+=random.choice(y)
print(z)
