import pygame
pygame.init()

white, black = (255,255,255), (0,0,0)
red, green, blue = (255,0,0), (0,255,0), (0,0,255)
display_width, display_height = 800, 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
gameDisplay.fill(black)

pixAr = pygame.PixelArray(gameDisplay) # convert gameDisplay to pixel array.
pixAr[10][20] = green # plot pixel in x,y coordinate (10,20)

pygame.draw.line(gameDisplay, blue, (100,200), (300,450), 5) # draw line x1,y1,x2,y2,thickness.
pygame.draw.rect(gameDisplay, red, (400,400,50,20)) # draw rectangle x,y,width,height.
pygame.draw.circle(gameDisplay, white, (150,150),75) # draw circle x,y,radius.
pygame.draw.polygon(gameDisplay, green, ((225,275),(275,400),(300,450),(400,400))) # draw polygon with list of tuples with x,y.

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

	pygame.display.update()