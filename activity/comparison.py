# add your get_student_with_more_classes function here!
def get_student_with_more_classes(student_1, student_2):
    if student_1.get_num_classes() > student_2.get_num_classes():
        return student_1.name
    elif student_1.get_num_classes() < student_2.get_num_classes():
        return student_2.name
    else:
        return f"Tie: {student_1.name} and {student_2.name}"
