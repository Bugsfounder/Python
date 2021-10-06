# oopsInherit1

# CREATE A CLASS 2-D VECTOR AND USE IT TO CREATE ANOTHER CLASS REPRESENTING A 3-D VECTOR

class Vector2D:
    def __init__(self, distance):
        self.distance = distance
        print(f"This is the distance of vector {self.distance}")


class Vector3D(Vector2D):
    def __init__(self, distance, direction):
        super().__init__(distance)
        self.direction = direction
        print(
            f"This is the distance of the vector {self.distance} and the direction of vector is: {self.direction} ")


v2 = Vector2D(10)

v3 = Vector3D(10, "East 4 km")
