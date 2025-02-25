import math

class Vector:
    def __init__(self, *args):
        """Initialize a vector with n-dimensional components."""
        self.args=tuple(args)
    def __repr__(self):
        """Return a string representation of the vector."""
        return f"Vector{self.args}"
    def __add__(self, other):
        if len(self.args)!=len(other.args):
            raise  ValueError("Vectors must be of the same dimension.")
        return Vector(*(a + b for a, b in zip(self.args, other.args)))
    def __sub__(self, other):
        if len(self.args)!=len(other.args):
            raise  ValueError("Vectors must be of the same dimension.")
        return Vector(*(a - b for a, b in zip(self.args, other.args)))
    def dot(self, other):
        if len(self.args)!=len(other.args):
            raise  ValueError("Vectors must be of the same dimension.")
        return Vector(*(a * b for a, b in zip(self.args, other.args)))
    def magnitude(self):
        """Compute the magnitude (length) of the vector."""
        return math.sqrt(sum(a ** 2 for a in self.args))
    def scalar(self, a: int):
        return Vector(*(b*a for b in self.args))
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print(v1 + v2)   # Vector(5, 7, 9)
print(v1 - v2)   # Vector(-3, -3, -3)
print(v1.dot(v2)) # 32
print(v1.magnitude()) # 3.7416573867739413
print(Vector.scalar(v1, 3))