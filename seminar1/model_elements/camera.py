from seminar1.staff.angle_3D import Angle3D
from seminar1.staff.point_3D import Point3D


class Camera:
    def __init__(self) -> None:
        self.location: Point3D = Point3D()
        self.angle: Angle3D = Angle3D()

    def rotate(self, angle: Angle3D) -> None:
        pass

    def move(self, point: Point3D) -> None:
        pass