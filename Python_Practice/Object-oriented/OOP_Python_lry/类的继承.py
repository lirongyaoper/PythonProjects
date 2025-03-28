class Person:
    def __init__(self):
        print("Person:init is called")
        self.name = "Jack"


class Student(Person):
    def __init__(self):
        super().__init__()
        print("Student:init is called")
        self.school = "Abc"


class Stone:
    pass


def main():
    student = Student()
    print(student.name)
    print(student.school)
    print("*************************************************")
    print(isinstance(student, Student))
    print(isinstance(student, Person))
    print("*************************************************")
    person = Person()
    print(isinstance(person, Student))
    print("*************************************************")
    print(issubclass(Student, Person))#True
    print(issubclass(Person, Student)) #false
    print("*************************************************")
    stone = Stone()
    print(issubclass(Stone, Student))  #false
    print(isinstance(stone, Person)) #false


if __name__ == '__main__':
    main()
