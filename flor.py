import turtle
import os  # Para manejar rutas correctamente

# Configurar pantalla con resolución 2048x1176
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Flor Amarilla para Conisita")

# Ruta del archivo GIF (Asegúrate de usar "/" o una raw string con r""")
ruta_gif = r"C:/Users/Alleks/Desktop/purin7.gif"  # Cambia esto a la ruta real de tu imagen

# Verificar si el archivo existe
if os.path.exists(ruta_gif):
    screen.addshape(ruta_gif)  # Cargar la imagen en Turtle
    img = turtle.Turtle()
    img.shape(ruta_gif)

    # Posicionar la imagen en el centro
    img.penup()
    img.goto(0, 0)
else:
    print(f"Error: No se encontró la imagen en {ruta_gif}")

# Función para dibujar un corazón
def dibujar_corazon(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("red")
    t.begin_fill()
    t.left(140)
    t.forward(10)
    t.circle(-5, 200)
    t.left(120)
    
    t.circle(-5, 200)
    t.forward(10)
    t.end_fill()
    t.setheading(0)  # Resetear dirección

# Escribir el mensaje con sombra y borde
turtle.penup()
turtle.goto(0, 200)  # Mover el texto más al sur
turtle.pendown()

# Sombra en negro
turtle.color("black")
turtle.write("Feliz 21 de Marzo\nConisita linda", align="center", font=("Comic Sans MS", 36, "bold"))

# Mover un poco para el borde dorado
turtle.penup()
turtle.goto(0, 205)
turtle.pendown()
turtle.color("gold")
turtle.write("Feliz 21 de Marzo\nConisita linda", align="center", font=("Comic Sans MS", 36, "bold"))

# Dibujar corazones decorativos
t = turtle.Turtle()
t.speed(10)
dibujar_corazon(-70, 180)  # Corazón izquierdo
dibujar_corazon(70, 180)   # Corazón derecho

# Dibujar el tallo PRIMERO para que quede atrás y toque la flor
t.penup()
t.goto(0, -90)  # Subir un poco más para que toque la flor
t.pendown()
t.color("green")
t.pensize(10)
t.setheading(-90)  # Apuntar hacia abajo
t.forward(200)  # Hacerlo más largo si es necesario

# Dibujar los pétalos MÁS GRANDES
t.penup()
t.goto(0, 0)  # Posición centrada
t.pendown()
t.color("yellow")
t.begin_fill()
for _ in range(12):
    t.circle(90, 60)  # Pétalos grandes
    t.left(120)
    t.circle(90, 60)
    t.left(120)
    t.left(30)
t.end_fill()

# Dibujar el centro de la flor (ajustado más al oeste)
t.penup()
t.goto(-40, 0)  # Movido más a la izquierda (-15 en X) para centrarlo mejor
t.pendown()
t.color("orange")
t.begin_fill()
t.circle(38)  # Tamaño grande para que se vea bien
t.end_fill()

# Finalizar
t.hideturtle()
turtle.done()
