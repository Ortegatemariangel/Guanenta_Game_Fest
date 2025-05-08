import pygame
import sys
import math

pygame.init()

ANCHO, ALTO = 600, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Golf fest camp1")

# Colores
VERDE_CESPED = (142, 199, 57)
AZUL_AGUA = (47, 166, 255)
NARANJA_BORDE = (200, 100, 40)
VERDE_OSCURO = (50, 130, 30)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Pelota
radio_pelota = 8
pelota_x = 540
pelota_y = 555

# Hoyo
hoyo_x = 100
hoyo_y = 160
hoyo_radio = 10
victoria = False

# Fondo y escena
def fondo():
    ventana.fill(VERDE_OSCURO)
    pygame.draw.rect(ventana, VERDE_CESPED, (30, 70, 540, 500))
    pygame.draw.rect(ventana, NARANJA_BORDE, (30, 70, 540, 500), 8)

    # Zona de inicio
    pygame.draw.rect(ventana, (80, 40, 20), (470, 520, 100, 40))

    # Lagos (uno por uno con círculos)
    pygame.draw.circle(ventana, AZUL_AGUA, (140, 460), 40)
    pygame.draw.circle(ventana, AZUL_AGUA, (180, 450), 30)
    pygame.draw.circle(ventana, AZUL_AGUA, (160, 480), 35)
    pygame.draw.circle(ventana, AZUL_AGUA, (120, 440), 25)
    pygame.draw.circle(ventana, AZUL_AGUA, (180, 490), 25)
    pygame.draw.circle(ventana, AZUL_AGUA, (260, 310), 20)
    pygame.draw.circle(ventana, AZUL_AGUA, (270, 320), 15)
    pygame.draw.circle(ventana, AZUL_AGUA, (280, 300), 18)
    pygame.draw.circle(ventana, AZUL_AGUA, (360, 190), 20)
    pygame.draw.circle(ventana, AZUL_AGUA, (370, 180), 15)
    pygame.draw.circle(ventana, AZUL_AGUA, (350, 200), 12)

    # Árboles individuales
    pygame.draw.rect(ventana, (34, 139, 34), (80, 150, 20, 40))
    pygame.draw.rect(ventana, (255, 165, 0), (130, 190, 20, 40))
    pygame.draw.rect(ventana, (255, 215, 0), (400, 140, 20, 40))
    pygame.draw.rect(ventana, (139, 69, 19), (110, 330, 20, 40))
    pygame.draw.rect(ventana, (50, 205, 50), (470, 350, 20, 40))
    pygame.draw.rect(ventana, (34, 139, 34), (200, 160, 20, 40))
    pygame.draw.rect(ventana, (255, 165, 0), (300, 220, 20, 40))
    pygame.draw.rect(ventana, (255, 215, 0), (500, 100, 20, 40))
    pygame.draw.rect(ventana, (50, 205, 50), (50, 250, 20, 40))
    pygame.draw.rect(ventana, (34, 139, 34), (520, 270, 20, 40))
    pygame.draw.rect(ventana, (50, 205, 50), (150, 100, 20, 40))
    pygame.draw.rect(ventana, (34, 139, 34), (430, 300, 20, 40))

    # Hoyo
    pygame.draw.circle(ventana, NEGRO, (hoyo_x, hoyo_y), hoyo_radio)

    # Pelota
    pygame.draw.circle(ventana, BLANCO, (pelota_x, pelota_y), radio_pelota)

    # Texto
    fuente = pygame.font.SysFont(None, 28)
    texto = fuente.render("MAX GOLPES: 5", True, BLANCO)
    ventana.blit(texto, (ANCHO // 2 - texto.get_width() // 2, 10))

    if victoria:
        mensaje = fuente.render("¡HOYO EN UNO!", True, BLANCO)
        ventana.blit(mensaje, (ANCHO // 2 - mensaje.get_width() // 2, 40))

# Bucle
reloj = pygame.time.Clock()
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    fondo()
    pygame.display.flip()
    reloj.tick(60)
