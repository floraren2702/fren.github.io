import json

def read_json_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

json_data = read_json_file("students.json")
# print("Name:", json_data[0]["name"])

def compute_summary():
    # you need to write this, compute something like average age, or 
    # average number of letters in the name. Put it in a dictionary, 
    # like {“avg”: 99}.

    num_students = len(json_data)
    total_age = 0
    for student in json_data:
        total_age += student["age"]
    average_age = total_age / num_students

    return({"avg": average_age})

summary_stats = compute_summary()

def write_json_file(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

write_json_file('summary_data.json', summary_stats)

print("Data written to summary_data.json")
