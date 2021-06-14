""" Homework 5 - needs to be presented before exam day
We want to create class for an object that behaves like a triangle, that has flexible sides and angles.
Because of approximations in python the triangle will get distorted after some of the changes so this is not a
perfect model
30P
 - class constructor can receive 3 arguments for angles (with default value of 60) and 3 arguments for sides (with
default value of 1)
class variables for sides will be called A, B, C
class variables for angles will be called AB, BC, CA (indicating sides)
30P
- class implements method to modify_angle:
  - modify_angle method takes two argument:
      - "angle" and can be one of 3 string values 'AB', 'BC', 'CA'
      - "degrees" that can be a positive or negative and represents the amount by which the angle will be modified
If as a result of the change any of the angles will be outside interval (0, 180) then method should raise an exception
When an angel is modifies you will need to recalculate the opposing side which can be done using the following
example: angle AB is changed then C = (A**2 + B**2 - 2*A*B*cos(AB))**(1/2)
Because angles in a triangle must sum up to 180 degrees unmodified angles need to be recalculated after we have
recalculated the opposite side using the following example:
angle AB is changed then BC = arccos((B**2+ C**2 - A**2) / 2*B*C), CA = arccos((C**2+ A**2 - B**2) / 2*C*A),
30P
- class implements method to modify_side:
  - modify_side method takes two argument:
      - "side" and can be one of 3 string values 'A', 'B', 'C'
      - "meters" that can be a positive or negative and represents the amount by which the side will be modified
If as a result of the change sum of the unmodified sides is less than or equal to the changed side then method should
throw an exception
If as a result of the change side will be less than or equal to 0 then method should raise a different exception
When a side is modified by some value all other sides need to be modified by the fraction of the change to maintain
the same triangle angles. For example, if A increase by +1 then B = ((A+1)/A)*B and C = ((A+1)/A)*C
10P
Create an object from your class with default constructor values and modify angle AB by +30 degrees and side A by +1.5
!!! HINT: results from functions in math module are usually in radians and you will need to import degree function
using a different name since you are asked to use an argument called degrees
"""
import math
from math import cos, acos
from math import degrees as deg


class exception_one(Exception):
    pass

class exception_two(Exception):
    pass


class Triangle:

    def __init__(self, A = 1, B = 1, C = 1, AB = 60, BC = 60, CA = 60):
        self.A = A
        self.B = B
        self.C = C
        self.AB = AB
        self.BC = BC
        self.CA = CA


    def modify_angle(self, angle, degrees):
        if angle == 'AB':
            val_AB = self.AB
            self.AB += degrees
            if self.AB != val_AB:
                self.C = math.sqrt(self.A ** 2 + self.B ** 2 - 2 * self.A * self.B * cos(self.AB))
                self.BC = acos((self.B ** 2 + self.C ** 2 - self.A ** 2) / (2 * self.B * self.C))
                self.BC = deg(self.BC)
                self.CA = acos((self.C ** 2 + self.A ** 2 - self.B ** 2) / (2 * self.C * self.A))
                self.CA = deg(self.CA)
                print('Angle AB: ', tr_res.AB)
        elif angle == 'BC':
            val_BC = self.BC
            self.BC += degrees
            if self.BC != val_BC:
                self.A = math.sqrt(self.B ** 2 + self.C ** 2 - 2 * self.B * self.C * cos(self.BC))
                self.AB = acos((self.A ** 2 + self.B ** 2 - self.C ** 2) / (2 * self.A * self.B))
                self.AB = deg(self.AB)
                self.CA = acos((self.C ** 2 + self.A ** 2 - self.B ** 2) / (2 * self.C * self.A))
                self.CA = deg(self.CA)
                print('Angle BC: ', tr_res.BC)
        elif angle == 'CA':
            val_AB = self.CA
            self.CA += degrees
            if self.CA != val_AB:
                self.B = math.sqrt(self.C ** 2 + self.A ** 2 - 2 * self.C * self.A * cos(self.CA))
                self.AB = acos((self.A ** 2 + self.B ** 2 - self.C ** 2) / (2 * self.A * self.B))
                self.AB = deg(self.AB)
                self.BC = acos((self.B ** 2 + self.C ** 2 - self.A ** 2) / (2 * self.B * self.C))
                self.BC = deg(self.BC)
                print('Angle CA: ', tr_res.CA)



    def modify_side(self, side, meters):
        val_A = self.A
        val_B = self.B
        val_C = self.C

        if side == 'A':
            self.A += meters
            if val_A != self.A:
                self.B = (self.A / val_A) * self.B
                self.C = (self.A / val_A) * self.C
                print('Side A: ', tr_res.A)
        if side == 'B':
            self.B += meters
            if val_B != self.B:
                self.A = (self.B / val_B) * self.A
                self.C = (self.B / val_B) * self.C
                print('Side B: ', tr_res.B)
        if side == 'C':
            self.C += meters
            if val_C != self.C:
                self.A = (self.C / val_C) * self.A
                self.B = (self.C / val_C) * self.B
                print('Side C: ', tr_res.C)


tr_res = Triangle()
tr_res.modify_angle('AB', 30)
tr_res.modify_side('A', 1.5)
