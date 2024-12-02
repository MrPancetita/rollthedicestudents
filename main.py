import random

def load_students(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        students = file.readlines()
    return [student.strip() for student in students]

def pick_random_student(students):
    return random.choice(students)

def assign_pc_to_student(students):
    student = random.choice(students)
    pc_number = random.randint(1, 100)  # Assuming there are 100 PCs
    return student, pc_number

def main():
    
    file_path = input("Enter the path to the student list file: ")
    students = load_students(file_path)
    
    while True:
        print("Menu:")
        print("1. Pick a random student to answer a question")
        print("2. Randomly assign seats to students")
        choice = input("Enter your choice (1/2): ").strip()
     
        if choice == '1':
            selected_student = pick_random_student(students)
            print(f"Selected student: {selected_student}")
        elif choice == '2':
            student, pc_number = assign_pc_to_student(students)
            print(f"Assigned PC {pc_number} to student: {student}")
        else:
            print("Invalid choice. Please enter 1 or 2.")
            continue
        
        reroll = input("Do you want to reroll and pick another? (yes/no): ").strip().lower()
        if reroll != 'yes':
            break

if __name__ == "__main__":
    main()