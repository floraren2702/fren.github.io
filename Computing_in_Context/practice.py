# x = 0
# while (x < 5):
# 	print(x)
# 	if (x % 2 == 0):
# 		for i, y in enumerate(["hello", "world"]):
# 			print(i)
# 		x = x + i
# 	else:
# 		print("x")
# 		break

# for i in range(5):
#    for j in range(5):
#        if i * j % 2 == 0:
#            print(i, j)

# nested_list = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for row in nested_list:
#     for element in row:
#         print(element, end=" ")
#     print()

# my_number = int(input("Give me a number: "))
# for i in range(my_number):
#     for j in range(5):
#         print(i, j)

# a = ["a", "b", "c", "d", "e", "f"]
# funsies = 0
# for i in range(len(a) - 1):
#     print(a[i - funsies])
#     if funsies < 2:
#         funsies += 1
#     else:
#         funsies = 3

# for i in range(1,16):
#     if i % 3 == 0 and i % 5 == 0:
#         print("fizzbuzz")
#     elif i % 3 == 0:
#         print("fizz")
#     elif i % 5 == 0:
#         print("buzz")


# for i in range(10,0,2):
#     print(i)

# a="1"
# a=a*5
# print(a)

# for i in range(10):
#     if i **2 < 50:
#         print(i, end=" ")
#     if i == 1: 
#         print("One", end=" ")
#     elif i > 5:
#         print(i/2, end=" ")

# number = "34986"
# for i in range(4):
#    if int(number[i]) % 3 == 0:
#        print(i + 1)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for num in numbers:

#     if (num % 2 == 0):

#         print(num)

#     elif (num % 4 == 0):
       
#         print(num)

#     if (num % 3 == 0):
       
#         print(num + 1)

# x = 10
# while x > 0:
#     if x % 2:
#         print("ooga")
#     else:
#         print("booga")
#     x = -1

# for i in range(10):
#     x = i**2
#     if (x % 2 == 0):
#         print(len(str(x)))

# def foo(x,y):	
#     y = x	
#     x = y	
#     return x+y 
# x = 3
# y = 4
# print(foo(y,x))

# def foo(x,y):	
#     return x+y

# x = 4
# y = 1
# print(foo(y,x) + foo(x,x) + foo(x,y))

# x=10
# y=0
# z=x+y

# def fun(x,y,z):
#     x=10
#     y=x
#     z=z
#     return [z,y,x]

# def funfun(a,b,c):
#     return [a+x,b+y,c+z]

# print(fun(3,4,1))
# intermediate=funfun(x,y,z)
# print(intermediate[0],intermediate[1], intermediate[2])
      
# def mystery(a, b):
#     if a[::-1] == b:
#         return a + "??"
#     return b + "!"

# secret = "open"
# key = "nepo"
# print(mystery(secret, key))

# def f(x, items=[]):
#     items.append(x)
#     return sum(items)

# def g(n):
#     total = 0
#     for i in range(0, n, 3):
#         if i % 2 == 0:
#             total += f(i)
#         else:
#             total += f(i, [])
#     return total

# print(g(13))
# print(g(12))

# def foo(x, y, z):
#     x = y*5
#     y = z**2
#     z = x + y
#     list = [z, y, x, y, z]

#     total_1 = 0
#     total_2 = 0

#     for i in range(len(list)-1):
#         if list[i] % 2 == 0:
#             total_1 += list[i]
#         else: 
#             total_2 += list[i]

#     return total_2, total_1

# print(foo(5, 8, 2))
# print(foo(100, 3, 6))

# x = 2
# y = 3
# z = 4

# def compute(x, y, z):
#     x = y + z
#     y = z
#     z = x
#     return [x, y, z]

# result = compute(y, z, x)
# print(result[0], result[1], result[2])

# def funWord(word):
#     out = ""
#     for i in range(len(word)):
#         if i % 2 == 0:
#             out += word[-(i+1)]
#         else:
#             out += word[i]
#     return out

# msg = "python"
# print(funWord(msg))

# for i in range(3):
#     for j in range(i):
#         print(i, j)

# x = 1
# for i in range(1, 4):
#     x = x + i
#     print("After i =", i, "x =", x)

# def foo(x, y):
#    result = []
#    for i in range(1, 4):
#        if (x + y) % i == 0:
#            x += i
#            y -= i
#        else:
#            y += i
#        result.append(x*y)
#    return result

# print(foo(3,2))
# print(foo(2,1))

# worked_hard = False
# worked_hard = True
# if worked_hard:
#     print("I will do well on this exam")


# def count_a(x):
#     count = 0 
#     for ch in x:
#         if ch == "a":
#             count = count + 1
#     return count

# print(count_a("abba"))

# def more_as_than_bs(s):
#     count_a = 0
#     count_b = 0
#     for char in s:
#         if char == "a":
#             count_a += 1
#         elif char == "b":
#             count_b += 1
#     return count_a > count_b   

# print(more_as_than_bs("broom"))




# # This question tests basic print
# print("I have learned a lot")

# # This question tests basic if statements
# worked_hard = False
# worked_hard = True
# if worked_hard:
#     print("I will do well on this exam")

# # This question tests if elif statements
# x = 5
# y = 10
# if x > y:
#     print(x)
# elif x < y:
#     print(y)

# # This question tests if elif statements with follow-up
# balloons = 10
# print("I have", balloons, "balloons")
# turtles = 10
# if balloons > turtles:
#     print(balloons)
# elif balloons < turtles:
#     print(turtles)
# print(balloons + turtles)

# This question tests if elif statements with follow-up
# popsicle = 4
# children = 3
# if popsicle > children:
#     print(popsicle)
# elif popsicle < children:
#     print(children)
# print(popsicle + children)

# This question tests else statements
# x = 7
# y = 3
# if x < y:
#     print(x)
# else:
#     print(y)

# This question tests nested conditionals
# x = 3
# y = 7
# z = 4
# if x < y:
#     print(x)
#     x = x + 1
#     if x > z:
#         print(x)
#     else:
#         print(y+2)
# else:
#     print(y)
#     if y > z:
#         print(y)
#     else:
#         print(z)

# This question tests basic variable assignment and arithmetic
# x = 2
# y = 3
# x = y + x
# y = y + x
# print(y)

# # This question tests variable names vs string literals
# x = "o"
# o = "x"
# o = x
# print(x + o + "o")

# # This question tests string concatenation
# string_1 = "A"
# string_2 = "B"
# y = string_1 + string_2 + "B" + "A"
# print(y)

# # This question tests string indexing
# y = "ABCDE"
# print(y[3] + y[1])

# This question tests list indexing
# my_list = [6, 7, 8, 9, 10]
# if (my_list[0] + my_list[1] > 12):
#     print(my_list[4])
# else:
#     print(my_list[3])

# # This question tests loops
# for i in range(3):
#     print(i)
# print("Done")

# This question tests modulo operator
# x = 10
# y = 3
# if x % 2 == 0:
#     print(x)
# if y % 2 == 0:
#     print(y)
# if (x + y) % 2 == 0:
#     print(x + y)
# else:
#     print(x - y)

# # This question tests loops with if statements
# for i in range(5):
#     if i % 2 == 0:
#         print(i)
#     else:
#         print(i + 1)
# print("Yay!")

#This question tests loops with if statements and variable updates
# x = 0
# for i in [1,2,3]:
#     if i % 2 == 0:
#         x = x + i
#     else:
#         x = x - 1
# print(x)
# print("Phew!")

# This question tests functions
# def foo(x):
#     x = x + 1
#     return x + 1
# print(foo
#       (3))

#this question tests functions with multiple parameters
# def bar(x, y):
#     return x + y
# print(bar(2, 5))

# this question tests nested function calls
# def bar(x, y):
#     return x + y
# print(bar(2, bar(3, 4)))

# this question tests variable scope
# def bar(x, y):
#     x = x + 1
#     return x + y
# def foo(x):
#     if x > 3:
#         return x + 1
#     else:
#         return x - 1
# x = 3
# y = bar(x, 2)
# x = foo(y)
# print(x)

# this question functions calling other functions
# def bar(x, y):
#     return x + y    
# def foo(x):
#     if x > 3:
#         return bar(x, 2)
#     else:
#         return bar(x, 3)
# x = 3
# y = foo(x)
# print(y)

# this question tests functions with loops
# def foo(x):
#     y = 0
#     for i in range(x):
#         y = y + i
#     return y
# print(foo(4))

# this question tests functions with loops and scope
# def bar(x):
#     x = x + 1
#     return x
# x = 0
# for i in range(4):
#     x = x + bar(i)
# print(x)

# this question tests dicts
# my_dict = {"a": 1, "b": 2, "c": 3}
# print(my_dict["b"])

# this question tests nested dicts
# my_dict = {"a": {"x": 1, "y": 2}, "b": {"x": 3, "y": 4}}
# print(my_dict["b"]["y"])

# this question tests nested dicts with loops
# my_dict = {"a": {"x": 1, "y": 2}, "b": {"x": 3, "y": 4}}
# total = 0   
# for key in my_dict:
#     total = total + my_dict[key]["x"]
# print(total)

# def count_as(word):
#     count = 0
#     for i in word:
#         if i == "a":
#             count += 1
#     return count
# print(count_as("abracadabra"))

# count = 0
# while count < 3:
#     for i in range(4):
#         if i % 2 == 0:
#             print("Type 1:", i)
#         if i == count:
#             print("Type 2:", i)
#     count += 1
# # What are Type 1 and Type 2 numbers?

# def add(x, y):
#     return x + y   
# def addTwice(x, y):
#     return add(add(x,y),y)
# print(add(3, addTwice(3,4)))

# def foo(x):
#     x = x + 2
#     return 2 + x
# def bar(x, y):
#     return foo(x) + foo(y)   
# print(foo(bar(3, foo(1))))

# def foo(x):
#     x = x + 2
#     return 2 + x
# def bar(x, y):
#     if (x > 0):
#         return foo(x)
#     else:
#         return foo(y)   
# print(foo(bar(3, foo(1))))

# a = 0.5
# b = 1
# print(f"type(a): {type(a)}, type(b): {type(b)}")

# if True:
#     print("True")
# if not False:
#     print("not False")

# print(True and True)
# print(True and False)
# print(False and False)
# print(True or False)

# x = 0
# while (x < 4):
# 	x = x + 1
# 	y = 3
# print (y)

# x = 5
# x = 6
# print(x)
# x = (x == 5)
# print(x)

# x = 10
# while x > 0:
#     if x % 2:
#         print("ooga")
#     else:
#         print("booga")
#     x = -1

# current_time_int = int(input("What is the current time (in hours)? "))
# waiting_time_int = int(input("How many hours do you have to wait? "))

# hours = current_time_int + waiting_time_int

# timeofday = hours % 24

# print(timeofday)


# x = 1
# while x <= 5:
#    print("hi")
#    x += 1

# for x in range (1, 100, 2):
#     print(x, end=' ')

# s = "Hello"

# for i in s:
#     print(i)

# print(s[0])
# print(s[2])
# print(s[-1])

# # slicing
# # s[start:end]
# print(s[0:4])
# print(s[:4])
# print(s[1:5])
# print(s[1])

# # s[start:end:skip]
# print(s[0:5:2])
# print(s[0:5:1], s[0:5], 5)
# print(s[::-1]) # olleH
# print(s[::-2]) # olH

# # print(len(s))

# # s1 = "Heyyyy"
# # print(s1 == s)
# # s3 = s + s1
# # print(s3)
# # a = "hi"
# # print(a*3)

# # string = "Hi"
# # list_of_chars = ["Hi", "i"]
# # # string[0] = "B"

# # list_of_chars[0] = "B"
# # print(list_of_chars)


# # # variable_name = value
# # x = 5
# # y = x + 3
# # # if x = y:
# # #     #Notice = assignment, == check
# # if x == y:
# #     print("In if")

# # x = 6
# # if x > 5:
# #     print("In if 1")
# #     if x > 7:
# #         print("In if 2")
# #     else:
# #         print("In else")
# # else:
# #     print("In Else 1")

# # text = "Happy"
# # print(text.lower()) #happy
# # print(text[-1]) #y
# # print(text[0:3]) #Hap
# # print(text[:4]) #Happ
# # text = text.lower()
# # print(text[0:3]) #hap
# # print(text[0:len(text):2]) #hpy

# # print(text[::-1]) #yppah
# # for i in range(len(text)-1,-1,-1):
# #     print(text[i], end="") #Reverses a string
# # print()


# for i in range(3):
#     print(i)

# x = 0
# while x < 3:
#     print(x)
#     x = x + 1


# t = "Hello"
# for ch in t:
#     print(ch) 

# for i in range(len(t)):
#     print(t[i])


# x = "Hello"
# for val in x:
#     print(val) #H, e, l, l, o

# for i in range(len(x)):
#     print(i, x[i])

# for i, val in enumerate(x):
#     print(i, val) 
#     #0, H
#     #1, e
#     #2, l
#     #3, l
#     #4, o

# def add(a, b):
#     return a + b

# print(add(2, 3)) 


# def foo(x):
#     return x + 1

# def bar(x, y):
#     return x + y

# print(bar(2, foo(3))) 
# # First foo(3) is evaluated. Then bar(2,4). Then prints 6

# x = 3
# y = 5
# def foo1(x):
#     y = 1
#     x = x + 1
#     return x

# print(foo1(x)) # 4 
# print(x) # 3 Notice scope
# print(y) # 5      

my_dict = {"a": 1, "b": 2}
print(my_dict["a"]) #1
my_dict["c"] = 3 
my_dict["d"] = 4
print(my_dict) #{"a": 1, "b": 2, "c":3}

for key in my_dict:
    print(key, my_dict[key])

data = {"a": {"x": 1}, "b": {"x": 2}}
print(data["b"]["x"])  # 2

n = 3
count = 0
while n > 0:
    count += n
    n -= 1
print(count, n)


def f(x):
    return x + 1

def g(x):
    x = f(x)
    return f(x)

x = 2
print(g(x), x)
