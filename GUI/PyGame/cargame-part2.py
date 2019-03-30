import pygame # import pygame module
pygame.init() # initalize pygame
display_width, display_height = 800, 600 # initialize pygame windows wdth and height
gameDisplay = pygame.display.set_mode((display_width, display_height)) # passing width and height

# color definitions.
black = (0, 0, 0) # there is no black.
white = (255, 255, 255) # 256 choices for each color.
red = (255, 0, 0) # for green - 0,255,0. for blue - 0,0,255.

pygame.display.set_caption('PyGame Demo') # set pygame window title
clock = pygame.time.Clock()

car_image = pygame.image.load('racecar.png') # load an image

def car(x,y):
	gameDisplay.blit(car_image, (x,y)) # blit - drawing to your background stuff whatever we're asking for.

x = (display_width * 0.45)
y = (display_height * 0.8)

x_change = 0 # to change the location of the car.

crashed = False

while not crashed:
	# pygame event will get any events that happen like pressing keys, moving mouse pointers.
	# list of events per frame/sec captured within pygame window
	for event in pygame.event.get(): 
		# terminate/close the pygame window if you hit X bar on top of pygame windwos screen.
		if event.type == pygame.QUIT:
			crashed = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x_change = -5
			if event.key == pygame.K_RIGHT:
				x_change = 5

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				x_change = 0

		# print(f' Event : {event}') # collecting events
	x += x_change
	gameDisplay.fill(white)
	car(x, y)
	pygame.display.update() # flip() or update()
	clock.tick(100) # increase frames per sec for speed exection. eg: 60 fps.

# exit/initiate pygame window
pygame.quit()
quit()
