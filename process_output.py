import time

filename = "output_students.csv"

def wait1():
    time.sleep(0.2)

def wait2():
    time.sleep(0.05)

def get_field_value(fields, index):
    if len(fields) > index and fields[index] != "":
        return fields[index]
    else:
        return "???"

def create_list():
    my_list = [
        ['John', 'Doe', 3.5, 110],
        ['Jane', 'Doe', 3.8, 115],
        ['Jim', 'Beam', 3.3, 105],
        ['Alice', 'Smith', 3.9, 120],
        ['Bob', 'Brown', 3.6, 112],
        ['Charlie', 'Davis', 1.7, 118]
    ]
    return my_list

# Append data to filename
""" def write_to_file(the_list):
    file_ptr = open(filename, "a")
    # file_ptr.write(f"First Name,Last Name,GPA,IQ\n")  # Header row
    for row in the_list:
        string = row[0] + "," \
                 + row[1] + "," \
                 + str(row[2]) + "," \
                 + str(row[3]) + "\n"
        # For each row, construct a string written to the file
        file_ptr.write(string)
    file_ptr.close() """

# Append data to filename, but better
def write_to_file(the_list):
    with open(filename, "a") as file_ptr:
        # For each row, construct a string written directly into the file
        for row in the_list:
            string = ",".join(map(str, row)) + "\n"
            file_ptr.write(string) 

# Print the data out
""" def print_list():
    file_ptr = open(filename, "r")
    headers = file_ptr.readline()
    counter = 1
    for line in file_ptr:
        line = line.strip()
        fields = line.split(",")
        fname = get_field_value(fields, 0).title()
        lname = get_field_value(fields, 1).title()
        gpa = get_field_value(fields, 2)
        iq = get_field_value(fields, 3)
        print(f"Student #{counter}")
        wait2()
        print(f"Name: {fname} {lname}")
        wait2()
        print(f"GPA: {gpa}")
        wait2()
        print(f"IQ: {iq}")
        wait2()
        print()
        wait1()
        counter += 1
    file_ptr.close() """        

# Print the data out, but better
def print_list():
    with open(filename, "r") as file_ptr:
        file_ptr.readline()  # Skip the first line (headers)
        for counter, line in enumerate(file_ptr, 1):
            fields = line.strip().split(",")
            fname, lname, gpa, iq = [get_field_value(fields, i).title() for i in range(len(fields))]
            print(f"Student #{counter}")
            # wait2()
            print(f"Name: {fname} {lname}\nGPA: {gpa}\nIQ: {iq}")
            # wait2()
            print()

def main():
    # student_list = create_list()
    # write_to_file(student_list)
    print_list()


if __name__ == "__main__":
    main()