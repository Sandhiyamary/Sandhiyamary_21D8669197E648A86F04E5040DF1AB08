class student:

  def __init__(self, name, roll_num, cgpa):
    self.name = name
    self.roll_number = roll_num 
    self.cgpa = cgpa


  def sort_students(student_list):
    # short the list of students in descending order of CGPA
    sort_students = sorted(student_list,
                    key=lambda student: student.cgpa, 
                            reverse=True)
    return  sorted_students


# Example usage:
students = [
    student("Hari", "A123", 7.8), 
    student("Srikanth", "A124", 8.9),
    student("Saumya", "A125", 9.1),
    student("Mahidhar", "A126", 9.9),
]

sorted_students = sort_students(students)