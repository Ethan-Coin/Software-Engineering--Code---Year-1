from graphics import *
from utilities import *


class Car:
    "Methods for building a car and moving it"

    def __init__(self, topLeftX, topLeftY, widthCarTop, heightCarTop, diff, carColour, win):
        self.car_parts = []
        self.win = win
        self.top_left_x = topLeftX
        self.top_left_y = topLeftY
        self.width_car_top = widthCarTop
        self.height_car_top = heightCarTop
        self.diff = diff
        self.car_colour = carColour

    def buildCarTop(self):
        "Build the car top"
        top_left_point = Point(self.top_left_x, self.top_left_y)
        bottom_right_point = Point(
            self.top_left_x + self.width_car_top, self.top_left_y + self.height_car_top)
        car_top = Utilities.drawRectangle(
            self.win, top_left_point, bottom_right_point, self.car_colour)
        self.car_parts.append(car_top)

    def buildCarBody(self):
        "Build the car body"
        top_left_point = Point(self.top_left_x - self.diff,
                               self.top_left_y + self.height_car_top)
        bottom_right_point = Point(self.top_left_x + self.width_car_top + self.diff,
                                   self.top_left_y + self.height_car_top + self.height_car_top)
        car_body = Utilities.drawRectangle(
            self.win, top_left_point, bottom_right_point, self.car_colour)
        self.car_parts.append(car_body)

    def buildLeftWheel(self):
        "Build the left wheel"
        center = Point(self.top_left_x, self.top_left_y +
                       self.height_car_top + self.height_car_top)
        radius = self.height_car_top / 2
        black_circle = Utilities.drawCircle(self.win, center, radius, "black")
        white_radius = radius - 10
        white_circle = Utilities.drawCircle(
            self.win, center, white_radius, "white")
        self.car_parts.extend([black_circle, white_circle])

    def buildRightWheel(self):
        "Build the right wheel"
        center = Point(self.top_left_x + self.width_car_top,
                       self.top_left_y + self.height_car_top + self.height_car_top)
        radius = self.height_car_top / 2
        black_circle = Utilities.drawCircle(self.win, center, radius, "black")
        white_radius = radius - 10
        white_circle = Utilities.drawCircle(
            self.win, center, white_radius, "white")
        self.car_parts.extend([black_circle, white_circle])

    def buildCar(self):
        "Build the car"
        self.buildCarTop()
        self.buildCarBody()
        self.buildLeftWheel()
        self.buildRightWheel()

    def move(self, dx, dy):
        "Move the car by dx and dy"
        for car_part in self.car_parts:
            car_part.move(dx, dy)
