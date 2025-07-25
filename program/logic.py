import time

def save_grades():
    grades = []
    name, lastname = input("Enter your name and lastname: \n").capitalize().split()
    while True:
        try:
            grade = float(input("Enter your grade: "))
            grades.append(grade)
        except ValueError:
            print("Please enter a valid float.")

        if len(grades) == 3:
            print("Data saved correctly")
            break

    average = sum(grades) / len(grades)
    
    with open("program/data.txt", "a+") as file:
        file.write(f"Name: {name} | Grades: {grades} | Average: {average:2f}\n")
    
    is_approved(average)

def is_approved(average):
    if average > 70:
        print("Congrats!, you are approve.")
    else:
        print("Im sorry, you are not approve.")


def view_grades():
    name = input("What grades do you want to see? \n").capitalize()
    try:
        with open("program/data.txt", "r", encoding="utf-8") as     file:
            found = False
            for line in file:
                if f"Name: {name}" in line:
                    print("Fetching...")
                    time.sleep(1.5)
                    print("Grades found.")
                    print(line.strip())
                    found = True
                    break
                if not found:
                    print("Student not found.")
    except FileNotFoundError:
        print("The file does not exist.")

