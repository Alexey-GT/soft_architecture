from Homework_1.Stuff.point3d import Point3D
from Homework_1.Stuff.angle3d import Angle3D


class Camera:
    def __init__(self):
        self.location: Point3D
        self.angle: Angle3D

    def Rotate(self, angle: Angle3D):
        pass

    def Move(self, location: Point3D):
        pass