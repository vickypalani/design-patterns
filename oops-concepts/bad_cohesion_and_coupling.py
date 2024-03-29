import random

# cohension represents the Single responsibility of the SOLID principles


# example of low cohension


class StudentRegistry:
    """
    Generate student name and roll no.
    """

    def generate_student_roll_no(self):
        """Roll number is generated using the random.randint function"""
        return random.randint(0, 1000)

    def generate_student_name(self, roll_no):
        """Student name is generated by concatenating the roll no. to student"""
        return f"Student-{roll_no}"


class ClassRoom:
    """
    Represents a classromm in a school
    """

    def register_student(self):
        """Generate student name and roll no. and register the student"""
        student = StudentRegistry()
        roll_no = student.generate_student_roll_no()
        name = student.generate_student_name(roll_no)
        print(f"{name} has roll no. {roll_no}")

        if roll_no % 2 == 0:
            print(f"{name} is one of the toppers")
        else:
            print(f"{name} is not one of the toppers")


if __name__ == "__main__":
    classroom = ClassRoom()
    classroom.register_student()

# As we can see, the classroom class is responsible for generating the student roll no. and name.
# Also responsible for checking whether the student is topper or not
# Also printing out the response as desired
# This violates the Single Responsibility Principle, as it has multiple responsibilities.
# This also has a tight coupling as the ClassRoom is completely dependent on the StudentRegistry class.
