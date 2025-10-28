serial_num = input("Enter the serial number on your bill: ")
if (serial_num[0] == serial_num[7] and serial_num[1] == serial_num[6]) and (
    serial_num[2] == serial_num[5] and serial_num[3] == serial_num[4]):
    print("Palindrome!")
elif (serial_num[0] == serial_num[3] and serial_num[1] == serial_num[2]) or (
    serial_num[4] == serial_num[7] and serial_num[5] == serial_num[6]):
    print("Partial Palindrome!")
if (serial_num[0] == "0" and serial_num[1] == "0") and (
    serial_num[2] == "0" and serial_num[3] == "0" and serial_num[4] == "0"):
    print("Low Number!")
elif serial_num[0] == "9":
    print("High Number!")
four_in_a_row = False
for i in range(5):
    if (serial_num[i] == serial_num[i+1]) and (
        serial_num[i+1] == serial_num[i+2] and serial_num[i+2] == serial_num[i+3]):
        four_in_a_row = True
if four_in_a_row == True:
    print("Four in a row!")

