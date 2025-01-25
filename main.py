import random

def load_students(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        students = file.readlines()
    return [student.strip() for student in students]

def pick_random_student(students):
    return random.choice(students)

def pick_pseudorandom_student(student_dict):

    # Debug flag
    debug = False

    # This will work as a raffle, each student is assigned a ticket, and a ticket among those distributed is picked
    # The students that have not won are assigned an extra ticket each round
    # The student that wons delivers all their tickets and starts from scratch gaining one ticket each round
    # The process is repeated until it is stopped by the user
    # This is a more fair way to pick a student as the chances of being picked increase the more rounds they have not been picked
    
    # Crear una lista de estudiantes y una lista de pesos correspondientes
    students = list(student_dict.keys())
    weights = [student_dict[student]["entries"] for student in students]
    
    # Elegir un estudiante basado en los pesos
    chosen_student = random.choices(students, weights=weights, k=1)[0]

    # Hacer 0 el número de entradas del estudiante elegido
    student_dict[chosen_student]["entries"] = 0

    # Aumentar en 1 el número de entradas de los estudiantes que no fueron elegidos
    for student in student_dict:
        if student != chosen_student:
            student_dict[student]["entries"] += 1
    
    if debug:
        print(f"Student dict: {student_dict}")
    
    return chosen_student


def main():

    file_path = input("Enter the path to the student list file: ")
    students = load_students(file_path)

    # Create the dict to store the student name and the number of entries for the raffle.
    # Initially, each student has one entry
    student_dict = {name: {"entries": 1} for name in students}

    while True:

        selected_student = pick_pseudorandom_student(student_dict)
        print(f"Selected student: {selected_student}")
        
        reroll = input("Do you want to reroll and pick another? (yes/no): ").strip().lower()
        if reroll != 'yes':
            break

if __name__ == "__main__":
    main()