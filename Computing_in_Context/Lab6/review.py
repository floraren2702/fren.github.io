x = 7
y = 2
print(x % y) # Remainder:1
print(x // y) # Quotient: 3
print(x/y) # 3.5


y = 2
print(x/y) #3.0
print(x ** y) #36
print(x*y) #12

x = 6
if x > 5:
    print("Big")
elif x > 7:
    print("Medium")
else:
    print("Small")
# It will print only "Big"

if x > 5:
    print("Big")
if x > 7:
    print("Medium")
else:
    print("Small")
# It will print both "Big" and "Medium"


text = "Happy"
print(text.lower())
print(text[-1])
print(text[0:3])
print (text[:4])
text = text.lower()
print(text[0:3])
print(text[0:len(text):2])
print(text[::-1]) # or do a loop and start at the end

for i in range(len(text)-1,-1,-1):
    print(text[i], end="")

# For loop
for in in range(3):
    print(i)

x = 0
while x < 3
    print(x)
    x += 1

t = "Hello"
for ch in t:
    print(ch)
# for loop is always finite, while loop can be infinite

for i, val in enumerate(x):
    print(i, val)
    #0, H
    #1, e
    #2, l
    #3, l
    #4, o
