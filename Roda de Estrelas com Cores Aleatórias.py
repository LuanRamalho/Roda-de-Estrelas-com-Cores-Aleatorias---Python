import turtle
import random

# Função para desenhar uma estrela
def desenha_estrela(turtle, tamanho):
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(tamanho)
        turtle.right(144)
    turtle.end_fill()

# Configuração inicial do Turtle
tela = turtle.Screen()
tela.bgcolor("black")
tela.title("Roda de Estrelas com Cores Aleatórias")

# Criação da tartaruga
estrela_turtle = turtle.Turtle()
estrela_turtle.speed(0)

# Parâmetros para a roda de estrelas
numero_de_estrelas = 12
tamanho_estrela = 50
raio_roda = 150

# Cores para selecionar aleatoriamente
cores = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan"]

# Desenho da roda de estrelas
for i in range(numero_de_estrelas):
    # Escolher uma cor aleatória para cada estrela
    estrela_turtle.color(random.choice(cores))
    
    # Posicionar a tartaruga para desenhar a estrela
    estrela_turtle.penup()
    estrela_turtle.goto(0, 0)
    estrela_turtle.forward(raio_roda)
    estrela_turtle.pendown()
    
    # Desenhar a estrela
    desenha_estrela(estrela_turtle, tamanho_estrela)
    
    # Rotacionar para a posição da próxima estrela
    estrela_turtle.right(360 / numero_de_estrelas)

# Finalização
estrela_turtle.hideturtle()
tela.mainloop()
