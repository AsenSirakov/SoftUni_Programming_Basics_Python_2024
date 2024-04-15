import turtle


def apply_rules(character):
    if character == 'F':
        return 'F+F-F-F+F'
    else:
        return character


def generate_l_system(axiom, iterations):
    l_system = axiom
    for _ in range(iterations):
        l_system = ''.join(apply_rules(char) for char in l_system)
    return l_system


def draw_l_system(l_system, angle, distance):
    turtle.speed(0)
    for char in l_system:
        if char == 'F':
            turtle.forward(distance)
        elif char == '+':
            turtle.left(angle)
        elif char == '-':
            turtle.right(angle)

if __name__ == "__main__":
    axiom = "F"
    iterations = 4
    angle = 90
    distance = 5

    l_system = generate_l_system(axiom, iterations)
    draw_l_system(l_system, angle, distance)

    turtle.done()
