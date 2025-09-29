import turtle

# Рекурсивная функция для построения кривой Коха.
def koch_curve(t, length, level):
    if level == 0:
        t.forward(length)  # базовый случай: рисуем прямую
    else:
        # рекурсивно строим четыре части кривой с поворотами
        koch_curve(t, length / 3, level - 1)
        t.left(60)
        koch_curve(t, length / 3, level - 1)
        t.right(120)
        koch_curve(t, length / 3, level - 1)
        t.left(60)
        koch_curve(t, length / 3, level - 1)

# Функция для построения "снежинки Коха" — замкнутого фрактала из трёх кривых Коха.
def koch_snowflake(t, length, level):
    for _ in range(3):
        koch_curve(t, length, level)
        t.right(120)

if __name__ == "__main__":
    # Настройка черепахи и экрана для рисования фрактала
    t = turtle.Turtle()
    t.speed('fastest')
    t.hideturtle()
    window = turtle.Screen()
    window.bgcolor("white")

    t.penup()
    t.goto(-150, 90)  # начальное положение
    t.pendown()

    length = 300   # длина стороны
    level = 5      # уровень рекурсии (детализация фрактала)
    koch_snowflake(t, length, level)

    window.exitonclick()