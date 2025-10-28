current_time = int(input("What is the current time (in hours)? "))
waiting_time = int(input("How many hours do you have to wait? "))
hours = current_time + waiting_time
timeofday = hours % 24

print(timeofday)