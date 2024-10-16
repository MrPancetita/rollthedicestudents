import random

def load_students(file_path):
    with open(file_path, 'r') as file:
        students = file.readlines()
    return [student.strip() for student in students]

def pick_random_student(students):
    return random.choice(students)

def main():
    file_path = input("Enter the path to the student list file: ")
    students = load_students(file_path)
    
    while True:
        selected_student = pick_random_student(students)
        print(f"Selected student: {selected_student}")
        
        reroll = input("Do you want to reroll and pick another? (yes/no): ").strip().lower()
        if reroll != 'yes':
            break

if __name__ == "__main__":
    main()