s = "Hello"

# for i in s:
# print(i)
#     print(i)

# print(s[0])
# print(s[2])
# print(s[-1])

# slicing
# s[start:end]
print(s[0:4])
print(s[:4])
print(s[1:5])
print(s[1])

# s[start:end:skip]
print(s[0:5:2])
print(s[0:5:1], s[0:5], 5)
print(s[::-1]) # olleH
print(s[::-2]) # olH

print(len(s))

s1 = "Heyyyy"
print(s1 == s)
s3 = s + s1
print(s3)
a = "hi"
print(a*3)

string = "Hi"
list_of_chars = ["Hi", "i"]
# string[0] = "B"

list_of_chars[0] = "B"
print(list_of_chars)