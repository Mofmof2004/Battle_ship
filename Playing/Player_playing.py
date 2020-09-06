
##################################################################################################################
"""
Use to make
"""



__version__ = '1.1.1'
__author__ = 'Theophile Guillet'
__date__ = '6/12/2020'

##################################################################################################################
from math import *
import pygame
from Playing.Positioning import arrays
from Boats import Boats
import time
import numpy
def main():
    from Playing.Display import display
    pass
if __name__ == "__main__":
    main()



pygame.init()

display_width = 900
display_height = 600


grid_xattack = 38
grid_yattack = 38

grid_xview = 598
grid_yview = 318

red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
dark_white = (200, 200, 200)
green = (0,255,0)
boat_c = (0,168,243)

player_turn = 0
tries = 0
game_exit = False
##################################################################################################################
gameDisplay = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
GridImg = pygame.image.load('Playing\grid2.png')
Gridview = pygame.image.load('Playing\small_grid.png')
##################################################################################################################
Touch0 = []
Miss0 = []
Destroy0 = []
Touch1 = []
Miss1 = []
Destroy1 = []


Sb = pygame.image.load("Playing\enemy_sb.png")
Sbd = pygame.image.load("Playing\enemy_sbd.png")
Mb = pygame.image.load("Playing\enemy_mb.png")
Mbd = pygame.image.load("Playing\enemy_mbd.png")
bb = pygame.image.load("Playing\enemy_bb.png")
bbd = pygame.image.load("Playing\enemy_bbd.png")
hb = pygame.image.load("Playing\enemy_hb.png")
hbd = pygame.image.load("Playing\enemy_hbd.png")

def enemy_boat(array):
        if 1 in array:
            gameDisplay.blit(Sbd, (625, 210))
        else:
            gameDisplay.blit(Sb, (625, 210))
        if 4 in array:
            gameDisplay.blit(Mbd, (665, 210))
        else:
            gameDisplay.blit(Mb, (665, 210))
        if 7 in array:
            gameDisplay.blit(Mbd, (705, 210))
        else:
            gameDisplay.blit(Mb, (705, 210))
        if 10 in array:
            gameDisplay.blit(bbd, (745, 210))
        else:
            gameDisplay.blit(bb, (745, 210))
        if 13 in array:
            gameDisplay.blit(hbd, (785, 210))
        else:
            gameDisplay.blit(hb, (785, 210))

def text_objects(text, font, colour):
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()

def message_display(text, font_size, time_sleep, colour, x, y):
    largeText = pygame.font.Font('freesansbold.ttf', font_size)
    TextSurf, TextRect = text_objects(text, largeText, colour)
    TextRect.center = x,y
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(time_sleep)

def PLayer_show(msg,x,y,w,h,ic, size):
    pygame.draw.rect(gameDisplay, black, (x, y, w, h))
    smallText = pygame.font.Font("freesansbold.ttf", size)
    textSurf, TextRect = text_objects(msg, smallText, ic)
    TextRect.center = (x + (w / 2), y + (h / 2))
    gameDisplay.blit(textSurf, TextRect)

def grid_playing(grid_xattack,grid_yattack, grid_xview, grid_yview):
    gameDisplay.blit(GridImg, (grid_xattack, grid_yattack))
    gameDisplay.blit(Gridview , (grid_xview, grid_yview))

def highlight(rounded_x, rounded_y):

    pygame.draw.rect(gameDisplay, red, (rounded_x, rounded_y, 39, 39))


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

def ready(player_turn):
    gameDisplay.fill(black)
    if player_turn == 0:
        PLayer_show("Player 2",450, 300, 900, 600, white, 50)
    elif player_turn == 1:
        PLayer_show("Player 2", 450, 300, 900, 600, white, 50)


def destroy_func(destroy_array, boat_array, player_turn):
    count = 1
    for index in range(5):
        if count not in boat_array:
            k_count = 0
            positions = numpy.where(boat_array == (count+1))
            for index in range(len(positions[0])):
                print(len(positions[0]))
                # positionsy = numpy.where(boat_array == (count+1))[1][1]
                positionsx = (numpy.array(positions)[1, k_count])
                positionsy = (numpy.array(positions)[0, k_count])
                posx = int((positionsx * 40) + 40)
                posy = int((positionsy * 40) + 40)
                destroy_array.append(posx)
                destroy_array.append(posy)
                positionsx = count + 2
                positionsy = count + 2
                k_count += 1
                print(boat_array)
                print(positions)
                print(positionsy)
                print(positionsx)
                print(destroy_array)
                print(posx)
                print(posy)

            # posx = int((positions[0][0] + 40) * 40)
            # posy = int((positions[0][1] + 40) * 40)
            # print(posx + posy)
            count += 3

        else:
            count += 3



def touch(listt):
    blocks = 0
    blockg = 0
    try:
        for index in range(int(ceil((len(listt) / 2)))):

            pygame.draw.rect(gameDisplay, red, (listt[blockg], listt[blockg + 1], 39, 39))

            blockg += 2


    except:
        print("what")



def miss(listm):
    blocks1 = 0

    try:
        for index in range(int(ceil(len(listm) / 2))):
            # PLayer_show("Miss", 450, 10, 100, 20, white)
            # pygame.display.update()
            pygame.draw.rect(gameDisplay, white, (listm[blocks1], listm[blocks1 + 1], 39, 39))
            blocks1 += 2
            # print(listm)
            # print(blocks1)
            # print(player_turn)

    except:
        pass

def destroy(destroy_array):
    blocks1 = 0
    list_length = len(destroy_array)
    try:
        for index in range(int(ceil((list_length / 2)))):
            # PLayer_show("Destroy", 450, 10, 100, 20, white)
            # pygame.display.update()
            pygame.draw.rect(gameDisplay, boat_c, (destroy_array[blocks1], destroy_array[blocks1 + 1], 39, 39))
            blocks1 += 2
            # print(destroy_array)
            # print(blocks1)
            # print(player_turn)

    except:
        pass

def Sgrid(listg, listt, listd, boat_array):
    blocks1 = 0
    count = 1
    for index in range(int(ceil(len(listg) / 2))):
        pygame.draw.rect(gameDisplay, white,(((listg[blocks1] / 2) + 580), ((listg[blocks1 + 1] / 2) + 300), 18, 18))
        blocks1 += 2
    blocks1 = 0
    for index in range(int(ceil(len(listt) / 2))):
        pygame.draw.rect(gameDisplay, red, (((listt[blocks1] / 2) + 580), ((listt[blocks1 + 1] / 2) + 300), 18, 18))
        blocks1 += 2
    blocks1 = 0
    for index in range(int(ceil(len(listd) / 2))):
        pygame.draw.rect(gameDisplay, boat_c, (((listd[blocks1] / 2) + 580), ((listd[blocks1 + 1] / 2) + 300), 18, 18))
        blocks1 += 2
    for index in range(5):
        if count in boat_array:
            k_count = 0
            positions = numpy.where(boat_array == (count))
            for index in range(len(positions[0])):
                print(len(positions[0]))
                # positionsy = numpy.where(boat_array == (count+1))[1][1]
                positionsx = (numpy.array(positions)[1, k_count])
                positionsy = (numpy.array(positions)[0, k_count])
                posx = int((positionsx * 20) + 600)
                posy = int((positionsy * 20) + 320)
                print(posx)
                print(posy)
                print(count)
                Sboat = pygame.image.load("Playing\Sgrid.png")
                gameDisplay.blit(Sboat, (posx , posy))


                k_count += 1
            count += 3


def game_playing(player_turn, tries):

    while not game_exit:

        mx, my = pygame.mouse.get_pos()
        rounded_x = (40 * round((mx - 20) / 40))
        rounded_y = (40 * round((my - 20) / 40))






        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            click = pygame.mouse.get_pressed()

            if (click[0] == 1) and (mx > grid_xattack  and mx < grid_xattack + 480 and my > grid_yattack and my < grid_yattack + 480):
                indexx = int((rounded_x - 40) / 40)
                indexy = int((rounded_y - 40) / 40)


                if player_turn == 0:
                    if arrays.boat_location2[indexy][indexx] in (1,4,7,10,13):
                        # print(arrays.boat_location2)
                        print("yhe")
                        tries += 1
                        Touch0.append(rounded_x)
                        Touch0.append(rounded_y)
                        arrays.boat_location2[indexy][indexx] += 1
                        pygame.draw.rect(gameDisplay, black, (rounded_x, rounded_y, 39, 39))
                        message_display("Touch", 50, 1, white, 725, 150)
                        destroy_func(Destroy1, arrays.boat_location2, player_turn)





                    elif arrays.boat_location2[indexy][indexx] == 0:
                        pygame.display.update()
                        player_turn = 1
                        tries += 1
                        Miss0.append(rounded_x)
                        Miss0.append(rounded_y)

                        arrays.boat_location2[indexy][indexx] += -1
                        pygame.draw.rect(gameDisplay, black, (rounded_x, rounded_y, 39, 39))
                        message_display("Miss", 50, 2, white, 725, 150)
                        for index in range(1):
                            gameDisplay.fill(black)
                            message_display("Player 2",50,3,white,450,300)
                            pygame.display.update()




                elif player_turn == 1:
                    if arrays.boat_location[indexy][indexx] in (1,4,7,10,13):
                        print("Yhe")
                        tries += 1
                        Touch1.append(rounded_x)
                        Touch1.append(rounded_y)
                        arrays.boat_location[indexy][indexx] += + 1
                        destroy_func(Destroy0, arrays.boat_location, player_turn)
                        pygame.draw.rect(gameDisplay, black, (rounded_x, rounded_y, 39, 39))
                        message_display("Touch", 50, 1, white, 725, 150)



                    elif arrays.boat_location[indexy][indexx] == 0:
                        pygame.display.update()
                        player_turn = 0
                        tries += 1
                        Miss1.append(rounded_x)
                        Miss1.append(rounded_y)
                        arrays.boat_location[indexy][indexx] += -1
                        pygame.draw.rect(gameDisplay, black, (rounded_x, rounded_y, 39, 39))
                        message_display("Miss", 50, 1, white, 725, 150)
                        for index in range(1):
                            gameDisplay.fill(black)
                            message_display("Player 1", 50, 3, white, 450, 300)
                            pygame.display.update()



        gameDisplay.fill(black)
        grid_playing(grid_xattack, grid_yattack, grid_xview, grid_yview)
        if mx > grid_xattack  and mx < grid_xattack + 480 and my > grid_yattack and my < grid_yattack + 480:
            highlight(rounded_x, rounded_y)

        if player_turn == 0:
            PLayer_show("Player 1", 20, 10, 870, 20, white, 20)
            Sgrid(Miss1, Touch1, Destroy0, arrays.boat_location)
            touch(Touch0)
            miss(Miss0)
            destroy(Destroy1)
            enemy_boat(arrays.boat_location2)


            #
            # if (1 and 4 and 7 and 10 and 13) not in arrays.boat_location2:
            #     gameDisplay.fill(black)
            #     message_display("Player 1 is the Winner", 50, 5, white, 450, 300)


            # message_display("Player 2", 50, 2, white)
        elif player_turn == 1:
            PLayer_show("Player 2", 20, 10, 870, 20, white, 20)
            Sgrid(Miss0, Touch0, Destroy1, arrays.boat_location2)
            touch(Touch1)
            miss(Miss1)
            destroy(Destroy0)
            enemy_boat(arrays.boat_location)


            # if (1 and 4 and 7 and 10 and 13) not in arrays.boat_location:
            #     gameDisplay.fill(black)
            #     message_display("Player 2 is the Winner", 50, 5, white, 450, 300)


        pygame.display.update()
        clock.tick(60)
game_playing(player_turn, tries)
pygame.quit()
quit()