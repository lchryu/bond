import turtle

# Tạo màn hình
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Demo Vẽ Hình với Turtle")

# Tạo "bút vẽ"
pen = turtle.Turtle()
pen.speed(5)  # tốc độ vẽ (1 chậm, 10 nhanh)j

# Vẽ hình vuông
for _ in range(4):
    pen.forward(100)  # tiến 100 đơn vị
    pen.right(90)     # quay phải 90 độ

# Di chuyển sang chỗ khác
pen.penup()
pen.goto(-150, 0)
pen.pendown()

# Vẽ hình tròn
pen.color("red")
pen.circle(50)

# Di chuyển tiếp
pen.penup()
pen.goto(150, 0)
pen.pendown()

# Vẽ ngôi sao 5 cánh
pen.color("green")
for _ in range(5):
    pen.forward(120)
    pen.right(144)

# Giữ màn hình cho đến khi click
screen.mainloop
