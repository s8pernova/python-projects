filename = "input_students.csv"

# Check if the field in a line is empty. If yes, replace it with "???"
def get_field_value(fields, index):
    if len(fields) > index and fields[index] != "":
        return fields[index]
    else:
        return "???"

# Make python read the file, then print it out in a readable format
def process_file():
    print()
    file_ptr = open(filename, "r")

    # Avoid typing in the headers
    headers = file_ptr.readline()

    # For each line in the csv file, it will print it out
    for line in file_ptr:
        line = line.strip()
        fields = line.split(",")
        id = get_field_value(fields, 0)
        fname = get_field_value(fields, 1)
        lname = get_field_value(fields, 2)
        gpa = get_field_value(fields, 3)
        iq = get_field_value(fields, 4)
        print(f"Id: {id}")
        print(f"Name: {fname} {lname}")
        print(f"GPA: {gpa}")
        print(f"IQ: {iq}")
        print()

    # Close the file at the end
    file_ptr.close()

def main():
    process_file()

main()
