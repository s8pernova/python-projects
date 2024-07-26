import json

filename = "input.json"

# Check if the field in a line is empty. If yes, replace it with "???"
def get_field_value(fields, index):
    value = fields.get(index)
    return "???" if value is None or value == "" else value
    # return fields.get(index, "???") if fields.get(index, "") != "" else "???"

def process_file():
    file_ptr = open(filename, "r")

    outmost_dict = json.load(file_ptr)
    student_list = outmost_dict.get("studentList")

    # Read each element in the list; each element is one student
    for student_dict in student_list:
        id = get_field_value(student_dict, "id")
        fname = get_field_value(student_dict, "firstName")
        lname = get_field_value(student_dict, "lastName")
        gpa = get_field_value(student_dict, "gpa")
        iq = get_field_value(student_dict, "iq")
        print(f"Id: {id}")
        print(f"Name: {fname} {lname}")
        print(f"GPA: {gpa}")
        print(f"IQ: {iq}")
        print()
    file_ptr.close()

def print_gpas():
    file_ptr = open(filename, "r")
    outmost_dict = json.load(file_ptr)

    gpa_list = []

    for student_dict in outmost_dict.get("studentList"):
        gpa_list.append(get_field_value(student_dict, "gpa"))

    print(f"Before sort: {gpa_list}")
    gpa_list.sort()
    print(f"After sort: {gpa_list}")

    file_ptr.close()

def main():
    process_file()
    print_gpas()


main()

