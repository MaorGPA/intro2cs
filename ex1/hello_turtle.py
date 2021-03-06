import turtle


def draw_petal():
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)


def draw_tepal():
    turtle.left(45)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()


def draw_stem():
    turtle.right(45)
    turtle.forward(150)


def draw_flower():
    draw_tepal()
    draw_stem()


def draw_flower_advanced():
    draw_flower()
    # Move turtle to next flower starting position
    turtle.up()
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.down()


def draw_flower_bed():
    # Move turtle to starting position
    turtle.up()
    turtle.forward(200)
    turtle.down()

    # Draw three flowers
    draw_flower_advanced()
    draw_flower_advanced()
    draw_flower_advanced()


draw_flower_bed()
turtle.done()
