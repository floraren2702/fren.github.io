n = input("Enter a 9-digit number where no digit appears twice: ")

acceptable_answer = False
test = int(n)
while test <= 999999999 and acceptable_answer == False:
    test+=1
    original_numbers = list(n)
    for i in list(str(test)):
        if i in original_numbers:
            original_numbers.remove(i)
    if len(original_numbers) == 0:
        acceptable_answer = True
        print(test)

if acceptable_answer == False:
    print("Unacceptable answer!")
    