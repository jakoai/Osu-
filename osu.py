import math, pygame, sys, time
from random import randint

resolution = [1000, 800]
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode(resolution)

font = pygame.font.SysFont('Comic Sans MS', 20)

circle_radius = 50
bg = pygame.image.load("image.jpg")

pygame.mixer.init()
pygame.mixer.music.load("Meie Mees - Moskva.mp3")
pygame.mixer.music.play()

def pygame_event():
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			for i in range(len(inactive_circles)):
				if math.sqrt(pow(inactive_circles[i]["pos"][0]-pos[0], 2) + pow(inactive_circles[i]["pos"][1]-pos[1], 2)) < circle_radius:
					mini = []
					for j in inactive_circles:
						mini.append(j["n"])
					if inactive_circles[i]["n"] == min(mini):
						del circles[i]
						if inactive_circles[i]["radius"]-circle_radius < 5:
							print("perfect")
						elif inactive_circles[i]["radius"]-circle_radius < 10:
							print("good")
						elif inactive_circles[i]["radius"]-circle_radius < 15:
							print("meh")
						else:
							print("shit")
						break

		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
			pygame.quit()
			sys.exit()

circles = [{"time":1}, 
			{"time":1.2}, 
			{"time":1.5}, 
			{"time":3}]

for i in range(len(circles)):
	circles[i]["pos"] = [randint(circle_radius, resolution[1]-circle_radius), randint(circle_radius, resolution[1]-circle_radius)]
	circles[i]["radius"] = 75
	circles[i]["n"] = i+1

start_time = time.time()
inactive_circles = []
while True:
	pygame_event()
	inactive_circles = []
	screen.fill((0, 0, 0))
	screen.blit(bg,(0,0))

	for i in range(len(circles)):
		if circles[i]["time"] < time.time() - start_time:
			if circles[i]["radius"] == circle_radius:
				circles[i]["radius"] -= 1
				print("missed")
			if circles[i]["radius"] > circle_radius:
				circles[i]["radius"] -= 1
				inactive_circles.append(circles[i])
				pygame.draw.circle(screen, (0, 255, 0), circles[i]["pos"], circle_radius, circle_radius)
				pygame.draw.circle(screen, (255, 255, 255), circles[i]["pos"], circles[i]["radius"], 2)
				screen.blit(font.render(str(circles[i]["n"]), False, (0, 0, 255)), circles[i]["pos"])


	pygame.display.update()
	time.sleep(0.05)