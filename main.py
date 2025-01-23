import random

def load_students(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        students = file.readlines()
    return [student.strip() for student in students]

def pick_random_student(students):
    return random.choice(students)

def pick_random_student_v2(students):
    # WIP
    # This will work as a raffle, each student is assigned a ticket, and a ticket among those distributed is picked
    # The students that have not won are assigned an extra ticket each round
    # The student that wons delivers all their tickets and starts from scratch gaining one ticket each round
    # The process is repeated until it is stopped by the user
    # This is a more fair way to pick a student as the chances of being picked increase the more rounds they have not been picked
    tickets = {student: 1 for student in students}
    while True:
        winning_student = random.choice(list(tickets.keys()))
        tickets[winning_student] = 0
        if all(ticket == 0 for ticket in tickets.values()):
            tickets = {student: 1 for student in students}
        else:
            break

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