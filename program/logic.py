def save_grades():
    grades = []
    name, lastname = input("Enter your name and lastname: \n").capitalize().split()
    while True:
        try:
            grade = float(input("Enter your grade: "))
        except ValueError:
            print("Please enter a valid float.")
        grades.append(grade)
        if len(grades) == 3:
            print("Data saved correctly")
            break

    average = sum(grades) / len(grades)
    
    with open("program/data.txt", "a+") as file:
        file.write(f"Name: {name} | Grades: {grades} | Average: {average:2f}\n")