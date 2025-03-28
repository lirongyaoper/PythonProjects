class Person:
    color = 1

    def __init__(self):
        self.name = "Jack"

    def say(self):
        print("Hello from person")

    def print_color(self):
        print(self.color)


class Student(Person):
    color = 2

    def __init__(self):
        super().__init__()
        self.school = "Abc"

    def say(self):
        super().say()
        print("Hello from student")


class Worker(Person):
    pass


def render(person: Person):
    person.say()


def main():
    student = Student()
    student.say()
    print("***************************************************")
    person = Person()
    person.say()
    print("***************************************************")
    person = Student()
    person.say()
    print("***************************************************")
    render(student)
    render(Worker())
    print("***************************************************")
    print(Student.color)
    student.print_color()


if __name__ == '__main__':
    main()
