import random

def get_student_ids(students):
    all_student_ids = []

    for name in students:
        count = 0
        student_id = ""
        current = name.split()[-1].lower()
        for letter in current:
            if count == 5:
                break
            else:
                student_id += letter
                count += 1
        student_id += str(random.randint(10000, 99999))
        all_student_ids.append(student_id)
    return all_student_ids

students = ["Yoongi Min", "San Choi", "Beomgyu Choi", "Kristel Jabbusch", "Brooke Vlahos"]
print(get_student_ids(students))