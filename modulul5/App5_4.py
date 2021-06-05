class Car:
    color = 'green'
    number_of_doors = 5
    speed = 0

    def change_color(self, new_color):
        self.color = self.color.replace('green', new_color)

    def accelerate(self, val_acc, time):
        self.speed += val_acc * time


    def decelerate(self, val_acc, time):
        self.speed -= val_acc * time

bmw = Car()
bmw.change_color('red')

bmw.accelerate(4, 20)
print(bmw.speed)

