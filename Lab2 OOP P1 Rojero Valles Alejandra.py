class usser:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def create_post(self, text):
        return post(text, self)

    def create_comment(self, text, post_obj):
        return comment(text, self, post_obj)

    def send_message(self, text, receiver):
        return message(text, self, receiver)


class post:
    def __init__(self, content, usser):
        self.content = content
        self.usser = usser

    def show_post(self):
        print(f"{self.usser.name} posted: {self.content}")


class comment:
    def __init__(self, content, usser, post_obj):
        self.content = content
        self.usser = usser
        self.post = post_obj

    def show_comment(self):
        print(f"{self.usser.name} commented: '{self.content}' on post: '{self.post.content}'")


class message:
    def __init__(self, content, send, recive):
        self.content = content
        self.send = send
        self.recive = recive

    def show_message(self):
        print(f"Message from {self.send.name} to {self.recive.name}: {self.content}")


# Instancias
Al = usser("Al", "Al@gmail.com")
Susu = usser("Susu", "Susu@gmail.com")

posT = post("Buenas buenas", Al)
commenT = comment("Hoy amanecimos ricas, sabrosas, deliciosas", Susu, posT) # Se corrigió 'post' por la instancia 'posT'
messagE = message("JAJAJA!", Susu, Al)

# Llamada a los métodos usando las instancias
posT.show_post()
commenT.show_comment()
messagE.show_message()






class Student:
    def __init__(self, name):
        self.name = name

    def enroll(self, course):
        self.course = course
    def show_course(self):
        print(f"{self.name} is enrolled in {self.course.name}")

class Course:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Course: {self.name}")

# Instances
student = Student("Carlos")
course = Course("Python Programming")

# Creating a relationship
student.enroll(course)

# Use the Relationship
student.show_course()