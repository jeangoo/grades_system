from logic import save_grades, view_grades
import time

def main():
    """main function"""
    print("Hi, follow the instructions and your grades are going to be saved in th efile data.txt\n")
    while True:
        print("what do you want to do? \n")
        print("1. Save grades 2. View grades 3. Exit")
        choice = input(" ")
        if choice == "1":
            save_grades()
        elif choice == "2":
            view_grades()
        elif choice == "3":
            print("Closing..")
            time.sleep(1)
            break
        else:
            print("Please enter a valid option.")


if __name__ == "__main__":
    main()