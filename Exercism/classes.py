class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    total_aliens_created = 0

    def __init__(self, x_coordinate, y_coordinate, health=3):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = health
        Alien.total_aliens_created += 1

    def hit(self):
        self.health -= 1

    def is_alive(self):
        return self.health > 0

    def teleport(self, new_x_coordinate, new_y_coordinate):
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection(self, other):
        pass

    def __repr__(self):
        return f"Alien(x={self.x_coordinate}, y={self.y_coordinate}, health={self.health})"

def new_aliens_collection(start_positions):
    return [Alien(x, y) for x, y in start_positions]


alien_start_positions = [(4, 7), (-1, 0)]
aliens = new_aliens_collection(alien_start_positions)
print(aliens)
for idx, alien in enumerate(aliens):
    assert (alien.x_coordinate, alien.y_coordinate) == alien_start_positions[idx]
