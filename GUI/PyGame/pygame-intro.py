import pygame # import pygame module
pygame.init() # initalize pygame
gameDisplay = pygame.display.set_mode((800,600)) # passing width and height
pygame.display.set_caption('PyGame Demo') # set pygame window title
clock = pygame.time.Clock()
crashed = False

while not crashed:
	# pygame event will get any events that happen like pressing keys, moving mouse pointers.
	# list of events per frame/sec captured within pygame window
	for event in pygame.event.get(): 
		# terminate/close the pygame window if you hit X bar on top of pygame windwos screen.
		if event.type == pygame.QUIT:
			crashed = True
		print(f' Event : {event}') # collecting events
	pygame.display.update()
	clock.tick(60) # increase frames per sec for speed exection. eg: 60 fps.

# exit/initiate pygame window
pygame.quit()
quit()
