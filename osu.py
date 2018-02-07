import math, pygame, sys, time
from random import randint

resolution = [1000, 800]
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode(resolution)

circle_radius = 50
bg = pygame.image.load("image.jpg")

pygame.mixer.init()
pygame.mixer.music.load("Meie Mees - Moskva.mp3")
pygame.mixer.music.play()

hit_text = ""

circles = [{"time":1}, 
			{"time":1.2}, 
			{"time":1.5}, 
			{"time":3}]

score_bar = 900

def pygame_event():
	global score_bar, circles, inactive_circles, hit_text
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			if len(inactive_circles) > 0:
				for i in range(len(circles)):
					if math.sqrt(pow(circles[i]["pos"][0]-pos[0], 2) + pow(circles[i]["pos"][1]-pos[1], 2)) < circle_radius:
						if circles[i]["index"] == min(inactive_circles):
							if circles[i]["radius"]-circle_radius < 5:
								hit_text = "Perfect!"
								score_bar += 40
							elif circles[i]["radius"]-circle_radius < 10:
								hit_text = "Good"
								score_bar += 30
							elif circles[i]["radius"]-circle_radius < 15:
								hit_text = "Meh"
								score_bar += 20
							else:
								hit_text = "Shit!!!"
								score_bar += 10
							del circles[i]
							break
							break

		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
			pygame.quit()
			sys.exit()

score_bar = 900

for i in range(len(circles)):
	circles[i]["pos"] = [randint(circle_radius, resolution[1]-circle_radius), randint(circle_radius, resolution[1]-circle_radius)]
	circles[i]["radius"] = 75
	circles[i]["index"] = i+1
	circles[i]["duration"] = 2

start_time = time.time()
inactive_circles = []
while True:
	pygame_event()
	inactive_circles = []
	screen.fill((0, 0, 0))
	screen.blit(bg,(0,0))

	if score_bar > 900:
		score_bar = 900
	if score_bar < 0:
		if abs(score_bar) > resolution[1]/2:
			score_bar = -resolution[1]/2
		render = pygame.font.SysFont('Comic Sans MS', 100).render("Game Over", False, (0, 255, 0))
		screen.blit(render, (resolution[0]//2-render.get_width()/2, abs(score_bar)*2-render.get_height()))
	else:
		screen.fill((255, 192, 203), pygame.Rect(55, 755, score_bar, 25))
		pygame.draw.rect(screen, (255, 192, 203), (50, 750, 910, 35), 1)
		screen.fill((255, 192, 203), pygame.Rect(55, 755, score_bar, 25))
		render = pygame.font.SysFont('Comic Sans MS', 100).render(hit_text, False, (0, 255, 255))
		screen.blit(render, (resolution[0]/2-render.get_width()/2, resolution[1]/2-render.get_height()/2))
	score_bar -= 1

	for i in range(len(circles)):
		if circles[i]["time"] < time.time() - start_time:
			if circles[i]["radius"] == circle_radius:
				circles[i]["radius"] -= 1/circles[i]["duration"]
				hit_text = ""
				score_bar -= 30
			if circles[i]["radius"] > circle_radius:
				circles[i]["radius"] -= 1/circles[i]["duration"]
				inactive_circles.append(circles[i]["index"])
				pygame.draw.circle(screen, (0, 255, 0), circles[i]["pos"], circle_radius, 0)
				pygame.draw.circle(screen, (255, 255, 255), circles[i]["pos"], int(circles[i]["radius"]), 2)
				render = pygame.font.SysFont('Comic Sans MS', 30).render(str(circles[i]["index"]), False, (0, 0, 255))
				screen.blit(render, (circles[i]["pos"][0]-render.get_width()/2, circles[i]["pos"][1]-render.get_height()/2))

	pygame.display.update()
	time.sleep(0.01)