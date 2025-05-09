import pygame
import sys
import math

pygame.init()

ANCHO, ALTO = 600, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Golf ¡Encuentra el hoyo!")

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

# Velocidad de la pelota
velocidad = 4

# Función para detectar si la pelota entra al hoyo
def detectar_entrada_hoyo():
    distancia = math.sqrt((pelota_x - hoyo_x) ** 2 + (pelota_y - hoyo_y) ** 2)
    if distancia < radio_pelota + hoyo_radio:
        return True
    return False

# Fondo y escena del primer nivel
def fondo_nivel_1():
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

# Bucle del primer nivel
def nivel_1():
    global pelota_x, pelota_y, victoria

    reloj = pygame.time.Clock()
    jugador_x, jugador_y = pelota_x, pelota_y # Definir las coordenadas iniciales de la pelota
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            jugador_x -= velocidad
        if teclas[pygame.K_RIGHT]:
            jugador_x += velocidad
        if teclas[pygame.K_UP]:
            jugador_y -= velocidad
        if teclas[pygame.K_DOWN]:
            jugador_y += velocidad
        
        # Actualizamos la posición de la pelota
        pelota_x, pelota_y = jugador_x, jugador_y

        # Detectamos si la pelota entra en el hoyo
        if detectar_entrada_hoyo():
            victoria = True
            # Pasar al siguiente nivel después de 2 segundos
            pygame.time.delay(2000)
            return # Termina el nivel y pasa al siguiente

        fondo_nivel_1()
        pygame.display.flip()
        reloj.tick(60)

# Segundo nivel
def nivel_2():
    F = (0, 167, 231)
    P = (69, 194, 2)
    L = (219, 119, 0)
    N = (0, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        ventana.fill(F)

        pygame.draw.ellipse(ventana,P, (10,550,250,150))
        pygame.draw.rect(ventana,P, ((80,50), (100,550)))
        pygame.draw.rect(ventana,P, ((180,50), (370,100)))
        pygame.draw.rect(ventana,P, ((450,150), (100,300)))
        pygame.draw.rect(ventana,P, ((270,350), (180,100)))
        pygame.draw.ellipse(ventana,P, (200,280,150,250))
        pygame.draw.rect(ventana,L, ((50,580), (30,30)))
        pygame.draw.rect(ventana,L, ((200,580), (30,30)))
        pygame.draw.rect(ventana,L, ((95,600), (90,90)))
        pygame.draw.rect(ventana,L, ((115,250), (30,150)))
        pygame.draw.rect(ventana,L, ((450,50), (30,30)))
        pygame.draw.rect(ventana,L, ((510,50), (30,30)))
        pygame.draw.rect(ventana,L, ((520,110), (30,30)))
        pygame.draw.rect(ventana,L, ((520,170), (30,30)))
        pygame.draw.rect(ventana,L, ((220,330), (30,30)))
        pygame.draw.rect(ventana,L, ((250,290), (30,30)))
        pygame.draw.circle(ventana,N, (300,340), 20)
        pygame.draw.rect(ventana,L, ((230,430), (60,60)))

        pygame.display.flip()

# Iniciar el juego
nivel_1()
nivel_2()