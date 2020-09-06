
##################################################################################################################
"""
Use to create the display game for placing the boats
"""



__version__ = '1.1.1'
__author__ = 'Theophile Guillet'
__date__ = '5/29/2020'

##################################################################################################################


import pygame
from Boats import Boats
from Playing.Positioning import arrays
import time

##################################################################################################################




pygame.init()

display_width = 900
display_height = 600

black = (0, 0, 0)
dark_white = (240, 240, 240)
white = (200, 240, 240)
bright_white = (250, 250, 250)
red = (255, 0, 0)


grid_x = 358
grid_y = 38


##################################################################################################################
gameDisplay = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
GridImg = pygame.image.load('Playing\grid2.png')


##################################################################################################################
# Creating the boats

Sb = Boats("Playing\g.2.png", 2, 40, 40,40,40, 40, 1)
Mb = Boats("Playing\g.3.png", 3, 100, 40, 100, 40, 40, 4)
MbII = Boats("Playing\g.3.png", 3, 40, 240, 40, 240, 40, 7)
bb = Boats("Playing\g.4.png", 4, 100, 240, 100, 240, 40, 10)
hb = Boats("Playing\g.5.png", 5, 170, 100, 160, 100, 40, 13)

def boat(Sb, Mb, MbII, bb, hb):
    imgs = pygame.image.load(Sb.name)
    imgm = pygame.image.load(Mb.name)
    imgmII = pygame.image.load(MbII.name)
    imgb = pygame.image.load(bb.name)
    imgh = pygame.image.load(hb.name)

    gameDisplay.blit(imgs, (Sb.x, Sb.y))
    gameDisplay.blit(imgm, (Mb.x, Mb.y))
    gameDisplay.blit(imgmII, (MbII.x, MbII.y))
    gameDisplay.blit(imgb, (bb.x, bb.y))
    gameDisplay.blit(imgh, (hb.x, hb.y))

##############################################################################
boats = [Sb, Mb, MbII, bb, hb]


##############################################################################

def grid(grid_x,grid_y):
    gameDisplay.blit(GridImg, (grid_x, grid_y))

def text_objects(text, font, colour):
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()

def message_display(text, font_size, time_sleep, colour):
    largeText = pygame.font.Font('freesansbold.ttf', font_size)
    TextSurf, TextRect = text_objects(text, largeText, colour)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(time_sleep)

def PLayer_show(msg,x,y,w,h,ic):
    pygame.draw.rect(gameDisplay, black, (x, y, w, h))
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, TextRect = text_objects(msg, smallText, ic)
    TextRect.center = (x + (w / 2), y + (h / 2))
    gameDisplay.blit(textSurf, TextRect)


def find_boat(function, mouse, click):
    count = 0
    found = False
    while found == False:
        same = boats[count]
        if count <= 4 and same.x + 60 > mouse[0] > same.x and same.y + same.block_size * 40 > mouse[1] > same.y:
            function(same)
            found = True

            # print(count)
            count = 0
        else:
            if count <= 3:
                count += 1

            else:
                count = 0
                found = True



def button(msg, x, y, w, h, ic, ac,inf, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action(inf)

    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, TextRect = text_objects(msg, smallText, black)
    TextRect.center = (x + (w / 2), y + (h / 2))
    gameDisplay.blit(textSurf, TextRect)

def display():
    player_2 = 1

    def Positioning(player_2):
        game_exit = False
        print(player_2)

    ##################################################################################################################
        while not game_exit:
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            mx, my = pygame.mouse.get_pos()



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                def mouvment(name):
                        if click[0] == 1:
                            name.x = 40 * round((mx - 25) / 40)
                            name.y = 40 * round((my - name.block_size*20) / 40)


                        if (name.x + name.angle) > mouse[0] > name.x and name.y + name.block_size*40 > mouse[1] > name.y and click[2]:
                            print(name.angle)
                            if "r" in name.name:
                                name.name = "Playing\g."+ str(name.block_size) +".png"
                                rotate = pygame.image.load(name.name)
                                name.angle += - name.block_size*80
                                gameDisplay.blit(rotate, (name.x, name.y))



                            else:
                                name.name = "Playing\g."+ str(name.block_size) +"r.png"
                                rotate = pygame.image.load(name.name)
                                name.angle += name.block_size*80
                                gameDisplay.blit(rotate, (name.x, name.y))



                        if click[0] == 0:
                            if name.x > grid_x or name.x == grid_x and name.x < grid_x + 480 and name.y > grid_y or name.y == grid_y and name.y < grid_y + 480:
                                # indexx = (name.x - 358)/40
                                # indexy = (name.y - 78)/40
                                # arrays.boat_location[int(indexy)][int(indexx)] = 1
                                # print(indexx)
                                # print(indexy)
                                bob = "b"


                            else:
                                if "r" in name.name:
                                    name.name = "Playing\g." + str(name.block_size) + ".png"
                                    rotate = pygame.image.load(name.name)
                                    name.angle += - name.block_size * 40
                                    gameDisplay.blit(rotate, (name.x, name.y))

                                name.x = name.xstart
                                name.y = name.ystart
                                return


                find_boat(mouvment, mouse, click)


            gameDisplay.fill(black)
            boat(Sb, Mb, MbII, bb, hb)
            grid(grid_x,grid_y)
            if player_2 == 1:
                PLayer_show("Player 1", 20, 10, 870, 20, bright_white)
                button("Ready", 20, 530, 860, 50, dark_white, white, player_2, done)
            elif player_2 == 2:
                PLayer_show("Player 2", 20, 10, 870, 20, bright_white)
                button("Play", 20, 530, 860, 50, dark_white, white,player_2, done)
            elif player_2 == 3:
                gameDisplay.fill(black)
                message_display("Player 1 turn", 50, 2, bright_white)
                from Playing.Player_playing import game_playing
                game_playing()





            pygame.display.update()
            clock.tick(60)


    def done(player_2):
        array = None
        if player_2 == 1:

            array = arrays.boat_location
        elif player_2 == 2:

            array = arrays.boat_location2



        def saving(name, player_2, array):
            if name.x > grid_x or name.x == grid_x and name.x < grid_x + 480 and name.y > grid_y or name.y == grid_y and name.y < grid_y + 480:
                indexx = (name.x - 360)/40
                indexy = (name.y - 40)/40

                for index in range(name.block_size):
                    if "r" in name.name:
                        array[int(indexy)][int(indexx)] = name.array
                        indexx += 1
                        print(array)
                    else:
                        array[int(indexy)][int(indexx)] = name.array
                        indexy += 1
                        print(array)
                if save_count == 4:

                    player_2 += 1
                    print(player_2)
                    Sb.x = Sb.xstart
                    Sb.y = Sb.ystart
                    Mb.x = Mb.xstart
                    Mb.y = Mb.ystart
                    MbII.x = MbII.xstart
                    MbII.y = MbII.ystart
                    bb.x = bb.xstart
                    bb.y = bb.ystart
                    hb.x = hb.xstart
                    hb.y = hb.ystart
                    gameDisplay.fill(black)
                    if player_2 == 2:
                        message_display("Player 2", 50, 2, bright_white)
                        Positioning(player_2)
                    else:
                        Positioning(player_2)

            else:
                gameDisplay.fill(black)
                message_display("Not all boats are positioned!!!", 50, 2, bright_white)
                Positioning(player_2)


        save_count = 0
        for index in range(5):
            all_boats = boats[save_count]
            saving(all_boats, player_2, array)
            save_count += 1
            print(save_count)

            pygame.display.update()
            clock.tick(60)


    ##################################################################################################################

    Positioning(player_2)
    done(player_2)
    pygame.quit()
    quit()

