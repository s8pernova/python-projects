first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

full_name = f"{first_name} {last_name}"

nova_id = str(input(f"\nHello, {full_name}. What is your myNova ID?: "))
gpa = float(input("What is your current GPA?: "))
semesters = int(input("How many semesters have you completed?: "))

gpa_thresholds = {
    2: "You should study more."
}

semesters_thresholds = {
    1: "You should try taking more classes."
}

print(f"\nHello, {full_name}.")
print(f"Your myNova ID is {nova_id}, but you already knew that.")
for threshold, message in gpa_thresholds.items():
    if gpa < threshold:
        print(f"Your GPA is only {gpa}? {message}")
    else:
        print(f"Woah, your GPA is {gpa}. Good job.")
for threshold, message in semesters_thresholds.items():
    if semesters < threshold:
        print(f"Also, {message}")
    else:
        print(f"Taking classes is a good way to get smart, and so far you took {semesters}.")