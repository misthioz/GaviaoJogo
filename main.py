import pygame
import os
import time
import random
pygame.font.init()

WIDTH = 975
HEIGHT = 688
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Gaviao Game')

#carregando imagens
GAVIAO = pygame.image.load(os.path.join('assets','gaviao.png')) #player
GAVIAO = pygame.transform.scale(GAVIAO, (180,160))
BG = pygame.image.load(os.path.join('assets','background.jpg')) #fundo
BG2 = pygame.image.load(os.path.join('assets','bg2.jpg'))
BG2 = pygame.transform.scale(BG2, (975,688))
TIRO = pygame.image.load(os.path.join('assets','tiro.png'))#tiro
#pode comer:
COELHO = pygame.image.load(os.path.join('assets','coelho.png'))
ESQUILO = pygame.image.load(os.path.join('assets','esquilo.png'))
PASSARO = pygame.image.load(os.path.join('assets','passaro.png'))
RATO = pygame.image.load(os.path.join('assets','rato.png'))
SAPO = pygame.image.load(os.path.join('assets','sapo.png'))
#nao pode comer:
FRUTAS = pygame.image.load(os.path.join('assets','frutas.png'))
MACA = pygame.image.load(os.path.join('assets','maca.png'))
UVA = pygame.image.load(os.path.join('assets','uva.png'))
SAPO_VENENOSO = pygame.image.load(os.path.join('assets','sapo_venenoso.png'))
RA_VENENOSA = pygame.image.load(os.path.join('assets','ra_venenosa.png'))

#cores:
GREEN = (0,100,0)

#fontes:
font = pygame.font.SysFont("comicsans", 40)
fontS = pygame.font.SysFont("comicsans", 25)

class Personagem:
	def __init__(self,x,y,health):
		self.x = x
		self.y = y
		self.health = health
		self.sprite = None
		#apenas do player
		self.tiroImg = None
		self.tiro = []
		self.cooldownCounter = 0

	def draw(self, screen):
		screen.blit(self.sprite, (self.x, self.y))

class Player(Personagem):
	def __init__(self,x,y,health):
		super().__init__(x,y,health) 
		self.sprite = GAVIAO
		self.tiroImg = TIRO
		self.mask = pygame.mask.from_surface(self.sprite)
		self.maxHealth = health

player = Player(400,500,0)


def main():
	run = True
	FPS = 60

	level = 1
	vidas = 5
	speed = 3

	clock = pygame.time.Clock()

	def redrawWindow(): #funciona como uma função normal, mas como e definido dentro da main so pode ser chamado a partir da main
		SCREEN.blit(BG2, (0,0)) #recria a imagem do bg em cima de tudo que foi desenhado antes 

		#texto
		vidaTexto = font.render(f'Vidas: {vidas}',1,GREEN)
		levelTexto = font.render(f'Nivel: {level}',1,GREEN)
		speedTexto = fontS.render(f'Velocidade: {speed}',1,GREEN)

		SCREEN.blit(vidaTexto,(30,25))
		SCREEN.blit(levelTexto,(830,25))
		SCREEN.blit(speedTexto,(830,60))

		#personagens
		player.draw(SCREEN)

		pygame.display.update()

	while run:
		clock.tick(FPS)
		redrawWindow()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		keys = pygame.key.get_pressed()
		if keys[pygame.K_a] and player.x - speed > 0 : #esquerda
			player.x -= speed
		if keys[pygame.K_d] and player.x + speed + 140< WIDTH : #direita
			player.x += speed
		if keys[pygame.K_w] and player.y - speed > 0 : #cima
			player.y -= speed
		if keys[pygame.K_s] and player.y + speed + 140 < HEIGHT : #baixo
			player.y += speed


main()
		

