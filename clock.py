import pygame
import time
import math

pygame.init()

screen = pygame.display.set_mode((500,600))

GREY = (150,150,150)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
start = False

running = True

total_secs = 0
total = 0

sound = pygame.mixer.Sound("alarm.wav") #download from internet !!!!!!!!!!

clock = pygame.time.Clock()

while running:
	clock.tick(60)

	font = pygame.font.SysFont('sans', 60)
	text_1 = font.render('+', True, BLACK)
	text_2 = font.render('+', True, BLACK)
	text_3 = font.render('-', True, BLACK)
	text_4 = font.render('-', True, BLACK)

	font_letter = pygame.font.SysFont('sans', 50)
	text_5 = font_letter.render('START', True, BLACK)
	text_6 = font_letter.render('RESET', True, BLACK)


	screen.fill(GREY)
	mouse_x, mouse_y = pygame.mouse.get_pos()

	pygame.draw.rect(screen, WHITE, (100,50,50,50))
	pygame.draw.rect(screen, WHITE, (200,50,50,50))
	pygame.draw.rect(screen, WHITE, (300,50,150,50))
	pygame.draw.rect(screen, WHITE, (100,200,50,50))
	pygame.draw.rect(screen, WHITE, (200,200,50,50))
	pygame.draw.rect(screen, WHITE, (300,150,150,50))

	screen.blit(text_1, (110,40))
	screen.blit(text_2, (210,40))
	screen.blit(text_3, (115,185))
	screen.blit(text_4, (215,185))
	screen.blit(text_5, (305,45))
	screen.blit(text_6, (305,145))


	pygame.draw.rect(screen, BLACK, (57,527,386,36))
	pygame.draw.rect(screen, WHITE, (60,530,380,30))

	pygame.draw.circle(screen, BLACK, (240,400), 100)
	pygame.draw.circle(screen, WHITE, (240,400), 97)
	pygame.draw.circle(screen, BLACK, (240,400), 3)


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				pygame.mixer.pause()
				if 100<mouse_x<150 and 50<mouse_y<100:
					print(" press + min ")
					total_secs += 60
					total = total_secs
				if 200<mouse_x<250 and 50<mouse_y<100:
					print(" press + second ")
					total_secs += 1
					total = total_secs
				if 100<mouse_x<150 and 200<mouse_y<250:
					print(" press - min ")
					total_secs -= 60
					total = total_secs
				if 200<mouse_x<250 and 200<mouse_y<250:
					print(" press - second ")
					total_secs -=1
					total = total_secs
				if 300<mouse_x<450 and 50<mouse_y<100:
					start = True
					total = total_secs
					print(" press START ")
				if 300<mouse_x<450 and 150<mouse_y<200:
					total_secs = 0
					total = total_secs
					print(" press RESET ")


	if start:
		if total_secs == 0:
			print("DONE")
			start = False
			pygame.mixer.Sound.play(sound)
		total_secs -= 1
		time.sleep(1)

	mins = int(total_secs/60)
	secs = total_secs - mins*60
	time_now = str(mins) + ":" + str(secs)
	text_time = font_letter.render(time_now, True, BLACK)
	screen.blit(text_time, (147,125))

	if total_secs < 0:
		total_secs = 0

	pygame.draw.line(screen, BLACK, (240,400), (240+90*math.sin((6*math.pi/180)*secs), 400-90*math.cos(6*math.pi/180*secs)))
	pygame.draw.line(screen, RED, (240,400), (240+45*math.sin((6*math.pi/180)*mins), 400-45*math.cos(6*math.pi/180*mins)))

	if total != 0:
		pygame.draw.rect(screen, RED, (60,530,380*(total_secs/total),30))

	pygame.display.flip()

pygame.quit()





































