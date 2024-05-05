import pgzrun
import os
#................................
TITLE = 'race game'
WIDTH = 610
HIGHT = 417
os.environ["SDL_VIDEO_CENTERED"] = '1'
#...............................





gameMap = Actor("back")
icons = Actor("icons",(320,520))
car1 = Actor("car1",(355,320))
car2 = Actor("car2",(345,350))
start = Actor("start")
menu = Actor("menu",(580,40))
#----------------
pointPic1 = Actor("point",(457,169))
pointPic2 = Actor("point",(427,134))
pointPic3 = Actor("point",(458,62))
pointPic4 = Actor("point",(501,25))
pointPic5 = Actor("point",(267,139))
pointPic6 = Actor("point",(244,170))
pointPic7 = Actor("point",(272,286))
pointPic8 = Actor("point",(241,394))
pointPic9 = Actor("point",(170,396))
pointPic10 = Actor("point",(91,360))
pointPic11 = Actor("point",(310,568))
pointPic12 = Actor("point",(132,540))
#----------------





car1Nfs = True
car2Nfs = True
gameMenu = False
car1Score = 0 #yellow
car2Score = 0 #white



def draw():
    global gameMenu
    screen.clear()
    start.draw()
    icons.draw()
    menu.draw()
    if gameMenu == True :
        screen.clear()
        gameMap.draw()
        car1.draw()
        car2.draw()
        pointPic1.draw()
        pointPic2.draw()
        pointPic3.draw()
        pointPic4.draw()
        pointPic5.draw()
        pointPic6.draw()
        pointPic7.draw()
        pointPic8.draw()
        pointPic9.draw()
        pointPic10.draw()
        pointPic11.draw()
        pointPic12.draw()
        screen.draw.text(f"white car score : {car1Score}",(0,0),fontsize = 40 ,color = "red")
        screen.draw.text(f"yellow car score : {car2Score}",(0,27),fontsize = 40 ,color = "red")

def update():
    global car1Nfs , car2Nfs , car1Score , car2Score
    if keyboard.up :
        car1.y -= 2
    if keyboard.down :
        car1.y += 2
    if keyboard.left :
        car1.x -= 2
    if keyboard.right :
        car1.x += 2
    if keyboard.p and car1Nfs != False :
        car1.y -= 50
        car1Nfs = False
    

    if keyboard.w :
        car2.y -= 2
    if keyboard.s :
        car2.y += 2
    if keyboard.a :
        car2.x -= 2
    if keyboard.d :
        car2.x += 2
    if keyboard.z and car2Nfs != False :
        car2.y -= 50
        car2Nfs = False

#--car 1--
    if car1.colliderect(pointPic1) :
        car1Score += 2
    if car1.colliderect(pointPic2) :
        car1Score += 2
    if car1.colliderect(pointPic3) :
        car1Score += 2
    if car1.colliderect(pointPic4) :
        car1Score += 2
    if car1.colliderect(pointPic5) :
        car1Score += 2
    if car1.colliderect(pointPic6) :
        car1Score += 2
    if car1.colliderect(pointPic7) :
        car1Score += 2
    if car1.colliderect(pointPic8) :
        car1Score += 2
    if car1.colliderect(pointPic9) :
        car1Score += 2
    if car1.colliderect(pointPic10) :
        car1Score += 2
    if car1.colliderect(pointPic11) :
        car1Score += 2
    if car1.colliderect(pointPic12) :
        car1Score += 2
#--car 2--
    if car2.colliderect(pointPic1) :
        car2Score += 2
    if car2.colliderect(pointPic2) :
        car2Score += 2
    if car2.colliderect(pointPic3) :
        car2Score += 2
    if car2.colliderect(pointPic4) :
        car2Score += 2
    if car2.colliderect(pointPic5) :
        car2Score += 2
    if car2.colliderect(pointPic6) :
        car2Score += 2
    if car2.colliderect(pointPic7) :
        car2Score += 2
    if car2.colliderect(pointPic8) :
        car2Score += 2
    if car2.colliderect(pointPic9) :
        car2Score += 2
    if car2.colliderect(pointPic10) :
        car2Score += 2
    if car2.colliderect(pointPic11) :
        car2Score += 2
    if car2.colliderect(pointPic12) :
        car2Score += 2  




















def on_mouse_down(pos,button) :
    global gameMenu
    if icons.collidepoint(pos) and button == mouse.LEFT :
        gameMenu = True
    print(pos)



pgzrun.go()
