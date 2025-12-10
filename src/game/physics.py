from .shape import Vec2, Rect2

class Physics():
    # Distance between two point vectors.
    @staticmethod
    def distance(v1: Vec2, v2: Vec2) -> Vec2:
        return (v1 - v2).length()
    
    # Collision function which rounds rectangle to circle.
    @staticmethod
    def simple_collide(r1: Rect2, r2: Rect2) -> Rect2:
        c1: float = (r1.size.x + r1.size.y) / 4
        c2: float = (r2.size.x + r2.size.y) / 4
        d: float = Physics.distance(r1.pos, r2.pos)
        return d < c1 + c2

    # Checking the point is inside the rect.
    @staticmethod
    def point_inside_rect(point: Vec2, rect: Rect2) -> bool:
        return point.x > rect.pos.x - rect.size.x / 2 and point.x < rect.pos.x + rect.size.x / 2 and point.y > rect.pos.y - rect.size.y / 2 and point.y < rect.pos.y + rect.size.y / 2