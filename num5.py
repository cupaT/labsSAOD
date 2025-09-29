import turtle
import random


def tree(branchLen, t):
    if branchLen > 5:
        # 1. Толщина
        thickness = max(branchLen // 10, 1)
        t.width(thickness)

        t.forward(branchLen)

        # 3. Случайный угол
        angle = random.randint(15, 45)
        t.right(angle)

        # 4. Случайное уменьшение длины
        decrement = random.randint(10, 20)
        tree(branchLen - decrement, t)

        t.left(angle * 2)
        decrement2 = random.randint(10, 20)
        tree(branchLen - decrement2, t)

        # 2. Цвет
        if branchLen < 20:
            t.color("green")
        else:
            t.color("brown")

        t.right(angle)
        t.backward(branchLen)


if __name__ == "__main__":
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.speed(0)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("brown")
    tree(75, t)
    t.hideturtle()
    myWin.exitonclick()
