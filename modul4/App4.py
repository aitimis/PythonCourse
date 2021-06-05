def conversation():
    name=None
    city=None
    def hello():
        print('Hello John ')
    def respone_hello():
        nonlocal name
        name= input('My name is ')
    def question():
        print(name ,', how is the weather ?')
        print("And where do you live, ", name, "?")
        nonlocal city
        city = input("I live in: ")
    def answer():
        print("It was sunny")
        print("And I live in, ",city)
    return hello , respone_hello , question, answer
c = conversation()
c[0]()
c[1]()
c[2]()
c[3]()

