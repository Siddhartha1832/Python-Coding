# import necessary modules
import pygame, time, random
pygame.init() # initalize pygame
display_width, display_height = 800, 600 # initialize pygame windows wdth and height
gameDisplay = pygame.display.set_mode((display_width, display_height)) # passing width and height

# color definitions.
black = (0, 0, 0) # there is no black.
white = (255, 255, 255) # 256 choices for each color.
red = (255, 0, 0) # for green - 0,255,0. for blue - 0,0,255.
green = (0, 255, 0)
blue = (0, 0, 255)
block_color = (53, 115, 255)
car_width = 73 # used to let you know when car crasing in either right/left side.

pygame.display.set_caption('PyGame Car Racing Demo') # set pygame window title
clock = pygame.time.Clock()
car_image = pygame.image.load('cycle.png') # load an image

def things_dodged(count):
	font = pygame.font.SysFont(None, 25)
	text = font.render(f' Score: {str(count)}', True, green)
	gameDisplay.blit(text, (0,0))

def things(thingx, thingy, thingw, thingh, color):
	# rectange object will fall randomly.
	pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car(x,y):
	# blit - drawing to your background stuff whatever we're asking for.
	gameDisplay.blit(car_image, (x,y))

def text_objects(text, font):
	textSurface = font.render(text, True, red)
	return textSurface, textSurface.get_rect()

def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf', 100) # specify font style and size.
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((display_width/2), (display_height/2))
	gameDisplay.blit(TextSurf, TextRect)
	pygame.display.update()
	time.sleep(2)
	game_loop()

def crash():
	# display crash message if hit in corner or by rectangele object.
	message_display('You Crashed')

def game_loop():
	x = (display_width * 0.45)
	y = (display_height * 0.8)
	x_change = 0 # to change the location of the car.
	dodged = 0
	# below things is for rectangle object.
	thing_startx = random.randrange(0, display_width)
	thing_starty = -600
	thing_speed, thing_width, thing_height = 7, 100, 100

	gameExit = False
	while not gameExit:
		# pygame event will get any events that happen like pressing keys, moving mouse pointers.
		# list of events per frame/sec captured within pygame window
		for event in pygame.event.get(): 
			# terminate/close the pygame window if you hit X bar on top of pygame windwos screen.
			if event.type == pygame.QUIT:
				# gameExit = True
				# exit/initiate pygame window
				pygame.quit()
				quit()
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
		gameDisplay.fill(white) # fill pygame window backgrouond color as white.

		things(thing_startx, thing_starty, thing_width, thing_height, block_color) # rectange object in black color
		thing_starty += thing_speed

		car(x, y) # display car image in pygame window.
		things_dodged(dodged)

		if x > display_width - car_width or x < 0: 
			# condition to tell whether car is crashed or not.
			# gameExit = True
			crash()

		if thing_starty > display_height:
			# condition to fall rectangle object fall randomly.
			thing_starty = 0 - thing_height
			thing_startx = random.randrange(0, display_width)
			dodged += 1 # count the score dodged
			thing_speed +=1 # after every dodged, speed increased by 1
			#thing_width += (dodged * 1.2) # increase rect obj width after cross every dodge


		if y < thing_starty + thing_height:
			# condition to tell car crash in any rectanle obj.
			print('y crossover')
			if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
				print('X crossover')
				crash()


		pygame.display.update() # flip() or update()
		clock.tick(100) # increase frames per sec for speed exection. eg: 60 fps.

game_loop() # start the game

