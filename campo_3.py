import pygame
import sys

pygame.init()

ancho = 600
alto = 600
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Golf camp granjita")

jugador_x = 290
jugador_y = 550
jugador_ancho = 20
jugador_alto = 20
velocidad = 3

negro = (0, 0, 0)
verde = (50, 200, 50)
rojo = (200, 50, 50)
amarillo = (255, 255, 0)
naranja = (255, 140, 0)
marron = (150, 75, 0)
blanco = (255, 255, 255)
gris = (100, 100, 100)
azul = (50, 100, 255)

reloj = pygame.time.Clock()

def dibujar_animales():
    # Vacas
    pygame.draw.rect(pantalla, blanco, (60, 80, 20, 20))
    pygame.draw.rect(pantalla, negro, (65, 85, 5, 5)) 
    pygame.draw.rect(pantalla, blanco, (90, 80, 20, 20))
    pygame.draw.rect(pantalla, negro, (95, 85, 5, 5)) 

    # Ovejas
    pygame.draw.ellipse(pantalla, blanco, (50, 40, 20, 15))
    pygame.draw.circle(pantalla, negro, (52, 47), 4)
    pygame.draw.ellipse(pantalla, blanco, (80, 40, 20, 15))
    pygame.draw.circle(pantalla, negro, (82, 47), 4)

    # Pollos
    pygame.draw.circle(pantalla, blanco, (500, 120), 10)
    pygame.draw.polygon(pantalla, rojo, [(510, 120), (515, 115), (515, 125)]) 
    pygame.draw.circle(pantalla, blanco, (520, 120), 10)
    pygame.draw.polygon(pantalla, rojo, [(530, 120), (535, 115), (535, 125)])  

    # Gallinas negras
    pygame.draw.circle(pantalla, negro, (60, 160), 10)
    pygame.draw.circle(pantalla, negro, (90, 160), 10)

    # Vaca grande abajo
    pygame.draw.rect(pantalla, blanco, (50, 470, 30, 20))
    pygame.draw.rect(pantalla, negro, (55, 475, 6, 6))

    # Tractor azul
    pygame.draw.rect(pantalla, azul, (290, 450, 30, 20))
    pygame.draw.circle(pantalla, negro, (295, 470), 6)
    pygame.draw.circle(pantalla, negro, (315, 470), 6)

def dibujar_muros_y_ambiente():
    # Fondo
    pantalla.fill(verde)

    # Muros
    pygame.draw.rect(pantalla, marron, (0, 0, ancho, 20))
    pygame.draw.rect(pantalla, marron, (0, 0, 20, alto))
    pygame.draw.rect(pantalla, marron, (ancho - 20, 0, 20, alto))
    pygame.draw.rect(pantalla, marron, (0, alto - 20, ancho, 20))
    pygame.draw.rect(pantalla, marron, (0, 200, 220, 20))
    pygame.draw.rect(pantalla, marron, (380, 200, 220, 20))
    pygame.draw.rect(pantalla, marron, (0, 400, 220, 20))
    pygame.draw.rect(pantalla, marron, (380, 400, 220, 20))

    # Hoyo y bandera
    pygame.draw.circle(pantalla, negro, (300, 80), 25)
    pygame.draw.polygon(pantalla, rojo, [(300, 30), (300, 70), (340, 50)])
    pygame.draw.line(pantalla, negro, (300, 30), (300, 80), 3)

    # Flotadores
    pygame.draw.circle(pantalla, amarillo, (200, 260), 25)
    pygame.draw.circle(pantalla, rojo, (200, 260), 10)
    pygame.draw.circle(pantalla, amarillo, (400, 260), 25)
    pygame.draw.circle(pantalla, rojo, (400, 260), 10)

    # Árboles
    posiciones_arboles = [(100, 480), (200, 520), (300, 480), (400, 520)]
    for x, y in posiciones_arboles:
        pygame.draw.rect(pantalla, gris, (x, y, 10, 25))
        pygame.draw.circle(pantalla, naranja, (x + 5, y), 15)

# Bucle principal
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jugador_x -= velocidad
    if teclas[pygame.K_RIGHT]:
        jugador_x += velocidad
    if teclas[pygame.K_UP]:
        jugador_y -= velocidad
    if teclas[pygame.K_DOWN]:
        jugador_y += velocidad

    dibujar_muros_y_ambiente()
    dibujar_animales()
    pygame.draw.rect(pantalla, blanco, (jugador_x, jugador_y, jugador_ancho, jugador_alto))

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
sys.exit()
