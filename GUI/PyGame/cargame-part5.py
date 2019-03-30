# import necessary modules
import pygame, time, random
pygame.init() # initalize pygame
display_width, display_height = 800, 600 # initialize pygame windows wdth and height
gameDisplay = pygame.display.set_mode((display_width, display_height)) # passing width and height

# color definitions.
black, white = (0, 0, 0), (255, 255, 255)
red, green, blue = (200, 0, 0), (0, 200, 0), (0, 0, 255)
block_color, bright_red, bright_green = (53, 115, 255), (255,0,0), (0,255,0)
car_width = 73 # used to let you know when car crasing in either right/left side.

game_title = 'PyGame Car Racing Demo'
pygame.display.set_caption(game_title) # set pygame window title
clock = pygame.time.Clock()
car_image = pygame.image.load('cycle.png') # load an image

def things_dodged(count):
	font = pygame.font.SysFont(None, 25)
	text = font.render(f' Score: {str(count)}', True, blue)
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

def button(msg,x,y,width,height,inactive_color,active_color, action=None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	# print(click)
	# below if loop is for green button highligher.
	if x+width > mouse[0] > x and y+height > mouse[1] > y:
		pygame.draw.rect(gameDisplay, active_color, (x,y,width,height))
		if click[0] == 1 and action != None:
			action()
			# if action == 'play':
			# 	game_loop()
			# elif action == 'quit':
			# 	pygame.quit()
			# 	quit()
	else:
		pygame.draw.rect(gameDisplay, inactive_color, (x,y,width,height))

	smalltext = pygame.font.Font('freesansbold.ttf', 20)
	TextSurf, TextRect = text_objects(msg, smalltext)
	TextRect.center = ( (x+(width/2)), (y+(height/2)) )
	gameDisplay.blit(TextSurf, TextRect)	

# 88704484066

def quitgame():
	pygame.quit()
	quit()

def game_intro():
	# start menu
	intro = True
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quitgame()
		gameDisplay.fill(white)
		largeText = pygame.font.Font('freesansbold.ttf', 50)
		TextSurf, TextRect = text_objects(game_title, largeText)
		TextRect.center = ((display_width/2), (display_height/2))
		gameDisplay.blit(TextSurf, TextRect)
		button('Start',150,450,100,50, green, bright_green, game_loop)
		button('Stop',550,450,100,50, red, bright_red, quitgame)
		pygame.display.update()
		clock.tick(15)


def game_loop():
	#game_intro()
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

		things(thing_startx, thing_starty, thing_width, thing_height, black) # rectange object in black color
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
			thing_width += (dodged * 1.2) # increase rect obj width after cross every dodge


		if y < thing_starty + thing_height:
			# condition to tell car crash in any rectanle obj.
			# print('y crossover')
			if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
				# print('X crossover')
				crash()


		pygame.display.update() # flip() or update()
		clock.tick(100) # increase frames per sec for speed exection. eg: 60 fps.

game_intro()
game_loop() # start the game

