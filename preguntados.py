import pygame
from constantes import *
from datos import *

pygame.init() #Inicia pygame.

ventana = pygame.display.set_mode([ANCHO_VENTANA, ALTO_VENTANA])
titulo = pygame.display.set_caption("Preguntados")


imagen_fondo = pygame.image.load("Laboratorio\img.jpg")
imagen_fondo_reescalada = pygame.transform.smoothscale(imagen_fondo, (800, 600))
logo = pygame.image.load("Laboratorio\img2.png")
logo_reescalado = pygame.transform.smoothscale(logo, (200, 100))

icono = pygame.image.load("Laboratorio\icono.PNG")
pygame.display.set_icon(icono)

preguntas = lista
respuesta_correcta = None
indice_pregunta_actual = 0

fuente = pygame.font.SysFont("Impact", 35)
fuente_pregunta = pygame.font.SysFont("Impact", 20)
texto_pregunta = fuente.render("PREGUNTA", True, COLOR_BLANCO)
texto_reiniciar = fuente.render("REINICIAR", True, COLOR_BLANCO)
total_preguntas = len(preguntas)

score = 0
score_formateado = ("{0}".format(score))
chances_respuesta = 0

corriendo = True

while corriendo == True:

    if indice_pregunta_actual == total_preguntas:
        # Si se han respondido todas las preguntas, reiniciar el juego
        indice_pregunta_actual = 0
        chances_respuesta = 1
        score = 0
        score_formateado = "{0}".format(score)

    ventana.blit(imagen_fondo_reescalada, (0, 0)) # IMAGEN DE FONDO
    ventana.blit(logo_reescalado, (80, 50)) # LOGO PREGUNTADOS
    
    respuesta_1 = pygame.Rect(80, 340, 200, 100)
    respuesta_2 = pygame.Rect(300, 340, 200, 100)
    respuesta_3 = pygame.Rect(520, 340, 200, 100)
    recuadro_pregunta = pygame.Rect(80, 175, 640, 140)
    reiniciar = pygame.Rect(300, 470, 200, 70)
    pregunta = pygame.Rect(300, 50, 200, 100)
    boton_score = pygame.Rect(520, 50, 200, 100)    

    pygame.draw.rect(ventana, COLOR_BLANCO, respuesta_3, 10) # BOTÓN OPCION 1
    pygame.draw.rect(ventana, COLOR_BLANCO, respuesta_2, 10) # BOTÓN OPCION 2
    pygame.draw.rect(ventana, COLOR_BLANCO, respuesta_1, 10) # BOTÓN OPCION 3
    pygame.draw.rect(ventana, COLOR_BLANCO, recuadro_pregunta, 10)
    pygame.draw.rect(ventana, COLOR_VERDE, reiniciar)
    pygame.draw.rect(ventana, COLOR_ROJO, pregunta)
    pygame.draw.rect(ventana, COLOR_NARANJA, boton_score)

    pregunta_actual = preguntas[indice_pregunta_actual]
    texto_desafio = pregunta_actual['pregunta']
    texto_desafio = fuente_pregunta.render(texto_desafio, True, COLOR_BLANCO)
    texto_score = fuente.render("SCORE:", True, COLOR_BLANCO)
    puntaje = fuente.render(score_formateado, True, COLOR_BLANCO)

    opcion_1 = pregunta_actual['a']
    opcion_2 = pregunta_actual['b']
    opcion_3 = pregunta_actual['c']
    opcion_selecccionada = None
    opcion_correcta = pregunta_actual['correcta']

    opcion_a = 'a'
    opcion_b = 'b'
    opcion_c = 'c'

    texto_opcion_a = fuente_pregunta.render(opcion_1, True, COLOR_BLANCO)
    texto_opcion_b = fuente_pregunta.render(opcion_2, True, COLOR_BLANCO)
    texto_opcion_c = fuente_pregunta.render(opcion_3, True, COLOR_BLANCO)

    ventana.blit(texto_opcion_a, (115, 375)) # "TEXTO OPCION A"
    ventana.blit(texto_opcion_b, (335, 375)) # "TEXTO OPCION B"
    ventana.blit(texto_opcion_c, (555, 375)) # "TEXTO OPCION C"
    ventana.blit(texto_pregunta, (330, 75)) # "TEXTO BOTON PREGUNTA"
    ventana.blit(texto_reiniciar, (330, 482)) # "TEXTO BOTÓN REINICIAR"
    ventana.blit(texto_score, (550, 75)) # "TEXTO SCORE"
    ventana.blit(puntaje, (655, 75)) # "NUMERO SCORE"
    ventana.blit(texto_desafio, (140, 230)) # "TEXTO PREGUNTA DESAFIO"
        
    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            
            corriendo = False

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                x, y = event.pos

                if pregunta.collidepoint(x, y):
                    
                    indice_pregunta_actual += 1
                    chances_respuesta = 1

                elif reiniciar.collidepoint(x, y):

                    indice_pregunta_actual = 0
                    score = 0
                    score_formateado = "{0}".format(score)

                elif respuesta_1.collidepoint(x, y):
                        
                        opcion_selecccionada = opcion_a

                        if opcion_selecccionada == opcion_correcta:

                            indice_pregunta_actual += 1
                            chances_respuesta = 1
                            score += 10
                            score_formateado = "{0}".format(score)

                        elif opcion_selecccionada != opcion_correcta and chances_respuesta != 0:

                            chances_respuesta -= 1

                        elif opcion_selecccionada != opcion_correcta and chances_respuesta == 0:

                            indice_pregunta_actual += 1
                            chances_respuesta = 1

                elif respuesta_2.collidepoint(x, y):

                        opcion_selecccionada = opcion_b

                        if opcion_selecccionada == opcion_correcta:
                             
                            indice_pregunta_actual += 1
                            chances_respuesta = 1
                            score += 10
                            score_formateado = "{0}".format(score)
                             
                        elif opcion_selecccionada != opcion_correcta and chances_respuesta != 0:
                             
                            chances_respuesta -= 1

                        elif opcion_selecccionada != opcion_correcta and chances_respuesta == 0:
                             
                             indice_pregunta_actual += 1
                             chances_respuesta = 1

                
                elif respuesta_3.collidepoint(x, y):

                        opcion_selecccionada = opcion_c

                        if opcion_selecccionada == opcion_correcta:
                             
                            indice_pregunta_actual += 1
                            chances_respuesta = 2
                            score += 10
                            score_formateado = "{0}".format(score)

                        elif opcion_selecccionada != opcion_correcta and chances_respuesta != 0:

                            chances_respuesta -= 1

                        elif opcion_selecccionada != opcion_correcta and chances_respuesta == 0:

                            indice_pregunta_actual += 1
                            chances_respuesta = 1


pygame.quit()

''' Corregir error de nombre de los score.

Finalizar el programa cuando se termina la lista de preguntas.'''