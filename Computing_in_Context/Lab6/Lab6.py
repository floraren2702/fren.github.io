a = [1,4,3]
a.sort()
print(a)
a.sort(reverse=True)
print(a)

t = ["Hello", "apple", "Jelly"]
t.sort()
print(t)

a = "HeLlo"
a = a.lower()
print(a)
a = a.upper()
print(a)
b = a[2].lower()
print(b)
a = "Hello"
a = a[:2] + a[2] + a[4:]
print(a)

a = "hello"
print(a.islower())
a = "Hello"
print(a.islower())
a = "HELLO"
print(a.isupper())
print(a.isalpha())
a = "Hello!"
print(a.isalpha())
print("Hello World" .isalpha())

a = [1,2,3]
print(1 in a)
print(6 not in a)
