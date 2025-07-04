import pygame
import sys
import math

pygame.init()

ancho, alto = 600, 600
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Golf camp granjita")

posicion_inicial = (290, 550)
pelota_x, pelota_y = posicion_inicial
radio = 10
vx, vy = 0, 0
friccion = 0.98
en_movimiento = False
golpes = 0
max_golpes = 6

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

obstaculos = []

def registrar_rect(x, y, w, h):
    rect = pygame.Rect(x, y, w, h)
    obstaculos.append(rect)

def dibujar_animales():
    # Vacas
    registrar_rect(60, 80, 20, 20)
    pygame.draw.rect(pantalla, blanco, (60, 80, 20, 20))
    pygame.draw.rect(pantalla, negro, (65, 85, 5, 5))
    registrar_rect(90, 80, 20, 20)
    pygame.draw.rect(pantalla, blanco, (90, 80, 20, 20))
    pygame.draw.rect(pantalla, negro, (95, 85, 5, 5))

    # Ovejas
    registrar_rect(50, 40, 20, 15)
    pygame.draw.ellipse(pantalla, blanco, (50, 40, 20, 15))
    pygame.draw.circle(pantalla, negro, (52, 47), 4)
    registrar_rect(80, 40, 20, 15)
    pygame.draw.ellipse(pantalla, blanco, (80, 40, 20, 15))
    pygame.draw.circle(pantalla, negro, (82, 47), 4)

    # Pollos
    registrar_rect(490, 110, 20, 20)
    pygame.draw.circle(pantalla, blanco, (500, 120), 10)
    pygame.draw.polygon(pantalla, rojo, [(510, 120), (515, 115), (515, 125)])
    registrar_rect(510, 110, 20, 20)
    pygame.draw.circle(pantalla, blanco, (520, 120), 10)
    pygame.draw.polygon(pantalla, rojo, [(530, 120), (535, 115), (535, 125)])

    # Gallinas negras
    registrar_rect(50, 150, 20, 20)
    pygame.draw.circle(pantalla, negro, (60, 160), 10)
    registrar_rect(80, 150, 20, 20)
    pygame.draw.circle(pantalla, negro, (90, 160), 10)

    # Vaca grande abajo
    registrar_rect(50, 470, 30, 20)
    pygame.draw.rect(pantalla, blanco, (50, 470, 30, 20))
    pygame.draw.rect(pantalla, negro, (55, 475, 6, 6))

    # Tractor azul
    registrar_rect(290, 450, 30, 20)
    pygame.draw.rect(pantalla, azul, (290, 450, 30, 20))
    pygame.draw.circle(pantalla, negro, (295, 470), 6)
    pygame.draw.circle(pantalla, negro, (315, 470), 6)

def dibujar_muros_y_ambiente():
    pantalla.fill(verde)

    muros = [
        (0, 0, ancho, 20), (0, 0, 20, alto),
        (ancho - 20, 0, 20, alto), (0, alto - 20, ancho, 20),
        (0, 200, 220, 20), (380, 200, 220, 20),
        (0, 400, 220, 20), (380, 400, 220, 20)
    ]
    for muro in muros:
        registrar_rect(*muro)
        pygame.draw.rect(pantalla, marron, muro)

    # Lago
    registrar_rect(250, 100, 100, 50)
    pygame.draw.ellipse(pantalla, azul, (250, 100, 100, 50))

    # Hoyo y bandera
    pygame.draw.circle(pantalla, negro, (300, 80), 25)
    pygame.draw.polygon(pantalla, rojo, [(300, 30), (300, 70), (340, 50)])
    pygame.draw.line(pantalla, negro, (300, 30), (300, 80), 3)
    registrar_rect(275, 55, 50, 50)

    # Flotadores
    flotadores = [(200, 260), (400, 260), (125, 525), (325, 575), (475, 525)]
    for x, y in flotadores:
        registrar_rect(x - 25, y - 25, 50, 50)
        pygame.draw.circle(pantalla, amarillo, (x, y), 25)
        pygame.draw.circle(pantalla, rojo, (x, y), 10)

    # Árboles
    arboles = [(100, 480), (200, 520), (300, 480), (400, 520)]
    for x, y in arboles:
        registrar_rect(x, y, 20, 40)
        pygame.draw.rect(pantalla, gris, (x, y, 10, 25))
        pygame.draw.circle(pantalla, naranja, (x + 5, y), 15)

def colision_circulo_rect(cx, cy, r, rect):
    # Encuentra el punto más cercano en el rectángulo al centro del círculo
    closest_x = max(rect.left, min(cx, rect.right))
    closest_y = max(rect.top, min(cy, rect.bottom))
    # Calcula la distancia entre ese punto y el centro
    distancia_x = cx - closest_x
    distancia_y = cy - closest_y
    return (distancia_x**2 + distancia_y**2) < (r**2)

def manejar_rebote(rect):
    global pelota_x, pelota_y, vx, vy

    # Calculamos las diferencias de penetración en cada lado
    dx_left = abs((pelota_x + radio) - rect.left)
    dx_right = abs(rect.right - (pelota_x - radio))
    dy_top = abs((pelota_y + radio) - rect.top)
    dy_bottom = abs(rect.bottom - (pelota_y - radio))

    min_penetracion = min(dx_left, dx_right, dy_top, dy_bottom)

    if min_penetracion == dx_left and vx > 0:
        pelota_x = rect.left - radio
        vx = -vx
    elif min_penetracion == dx_right and vx < 0:
        pelota_x = rect.right + radio
        vx = -vx
    elif min_penetracion == dy_top and vy > 0:
        pelota_y = rect.top - radio
        vy = -vy
    elif min_penetracion == dy_bottom and vy < 0:
        pelota_y = rect.bottom + radio
        vy = -vy

# Variables para colores dentro de funciones
amarillo = (255, 255, 0)
rojo = (255, 0, 0)

while True:
    pantalla.fill(verde)
    obstaculos.clear()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN and not en_movimiento and golpes < max_golpes:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            dx = mouse_x - pelota_x
            dy = mouse_y - pelota_y
            distancia = math.hypot(dx, dy)
            if distancia != 0:
                vx = dx / distancia * 10
                vy = dy / distancia * 10
                en_movimiento = True
                golpes += 1

    if en_movimiento:
        pelota_x += vx
        pelota_y += vy
        vx *= friccion
        vy *= friccion

        if abs(vx) < 0.1 and abs(vy) < 0.1:
            en_movimiento = False

        # Rebotar con obstáculos
        for obst in obstaculos:
            if colision_circulo_rect(pelota_x, pelota_y, radio, obst):
                # Agua: reiniciar pelota
                if obst.colliderect(pygame.Rect(250, 100, 100, 50)):
                    pelota_x, pelota_y = posicion_inicial
                    vx, vy = 0, 0
                    golpes = 0
                    en_movimiento = False
                    break
                else:
                    manejar_rebote(obst)

        # Limites campo
        if pelota_x - radio < 20:
            pelota_x = 20 + radio
            vx = -vx
        elif pelota_x + radio > ancho - 20:
            pelota_x = ancho - 20 - radio
            vx = -vx
        if pelota_y - radio < 20:
            pelota_y = 20 + radio
            vy = -vy
        elif pelota_y + radio > alto - 20:
            pelota_y = alto - 20 - radio
            vy = -vy

    dibujar_muros_y_ambiente()
    dibujar_animales()

    fuente = pygame.font.SysFont(None, 28)
    texto = fuente.render(f"Golpes: {golpes} / Max Golpes: {max_golpes}", True, blanco)
    pantalla.blit(texto, (ancho // 2 - texto.get_width() // 2, 10))

    pygame.draw.circle(pantalla, blanco, (int(pelota_x), int(pelota_y)), radio)

    pygame.display.flip()
    reloj.tick(60)