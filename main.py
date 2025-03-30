from pygame import *

init()

def intesec_rects(rectA,rectB,dire):
    mirol_ = rectA.copy()
    mirol_.x += dire.x
    mirol_.y += dire.y
    if mirol_.colliderect(rectB):
        return True
    return False



class PLAYER():
    def __init__(self,x,y):
        self.img = Surface((16,16))
        self.img.fill((200,0,0))
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def updade(self):
        keys = key.get_pressed()
        dire = Vector2(keys[K_d]-keys[K_a],keys[K_s]-keys[K_w])
        if intesec_rects(self.rect,caho,Vector2(keys[K_d]-keys[K_a],0)):
            dire.x = 0
        if intesec_rects(self.rect,caho,Vector2(0,keys[K_s]-keys[K_w])):
            dire.y = 0
        
        self.rect.x += dire.x
        self.rect.y += dire.y
    def draw(self,surfac):
        surfac.blit(self.img,self.rect)
    
class CHAO():
    def __init__(self,x,y):
        self.img = Surface((16,16))
        self.img.fill((200,0,200))
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def draw(self,surfac):
        surfac.blit(self.img,self.rect)

class WALL():
    def __init__(self,x,y):
        self.img = Surface((16,16))
        self.img.fill((200,0,200))
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def draw(self,surfac):
        surfac.blit(self.img,self.rect)

player = PLAYER(0,0)
caho = WALL(100,100)

list_spr = [player,caho]
class CAMERA():
    def __init__(self):
        self.tela_img = display.get_surface()
        self.pos = Vector2(0,0)
    def draw_screen(self,surfac):
        self.pos = Vector2(player.rect.x+8-384/2,player.rect.y+8-216/2)

        for spr in list_spr:
            pos = list(spr.rect.topleft)
            pos[0] -= self.pos.x
            pos[1] -= self.pos.y
            surfac.blit(spr.img,pos)

cam = CAMERA()
fps = time.Clock()
screen = display.set_mode((384,216),RESIZABLE | SCALED)
canva = Surface((384,216))
LOOP = True

while LOOP:
    for evente in event.get():
        if evente.type == QUIT:
            LOOP = False

    screen.fill((0, 0, 0))
    canva.fill((20,0,20))
    player.updade()
    cam.draw_screen(canva)
    screen.blit(canva,(0,0))

    display.flip()
    fps.tick(60)
quit()
