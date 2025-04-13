from pygame import *
from math import *

init()
#============================#
#============================#
tile_map = [
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            [1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1,1,0],
            [1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
            [1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            [1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
            [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,1,1,1,1,1,0,1,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0],
            [1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0],
            [1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0],
            [1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,0,1,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,0,1,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0],
            [1,1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            ]

list_spr = []
list_colider = []
list_bullet = []
def intesec_rects(rectA,rectB,dire):
    mirol_ = rectA.copy()
    mirol_.x += dire.x
    mirol_.y += dire.y
    if mirol_.colliderect(rectB):
        return True
    return False

def lerp(x,y,peso):
    dists = y-x
    return x + dists*peso

def direct(Vec01: Vector2,Vec02: Vector2):
    dire = Vector2(0,0)
    dist = sqrt((Vec02.x - Vec01.x)*(Vec02.x - Vec01.x)+(Vec02.y - Vec01.y)*(Vec02.y - Vec01.y ))
    dire.x = (Vec02.x - Vec01.x)/dist 
    dire.y = (Vec02.y - Vec01.y)/dist
    return dire

def intsec_listRect(rectA,listRec,dire):
    for i in listRec:
        if intesec_rects(rectA,i.rect,dire):
            return True
    return False

class TEMPORIZADOR():
    def __init__(self,frames):
        self.frame = frames
        self.temp = frames
    def rodar(self):
        if self.frame >= 0:
            self.frame -= 1
    def is_finish(self):
        if self.frame <=0:
            return True
        return False
    def reniciar(self):
        self.frame = self.temp

class Bullet():
    def __init__(self,x,y,dire_x,dire_y):
        self.img = image.load("bullet_spr.png")
        self.rect = self.img.get_rect()
        self.pos = math.Vector2(Vector2(x,y))
        self.rect.center = self.pos
        self.dire = Vector2(dire_x,dire_y)
        
    def updade(self):
        self.pos.y += self.dire.y*2.5
        self.pos.x += self.dire.x*2.5
        self.rect.center = self.pos
        if intsec_listRect(self.rect,list_colider,Vector2(0,0)):
            list_spr.remove(self)
            list_bullet.remove(self)
    def draw(self,surfac):
        surfac.blit(self.img,self.rect)

class PLAYER():
    def __init__(self,x,y):
        self.imgs = [image.load("robo_and2.png"),image.load("robo_and.png"),image.load("robo_and03.png")]
        self.img = self.imgs[0]
        self.img_index = 0
        
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.time_shotter = TEMPORIZADOR(15)
        self.ref_ani = 1
    def updade(self):
        self.img_index += 0.2*self.ref_ani
        if int(self.img_index) >= 3 or self.img_index <= 0:
            self.ref_ani *= -1
            self.img_index += 0.2*self.ref_ani

        
        keys = key.get_pressed()
        dire = Vector2(keys[K_d]-keys[K_a],keys[K_s]-keys[K_w])
        self.img = transform.flip(self.imgs[int(self.img_index)],keys[K_a],False)

        if intsec_listRect(self.rect,list_colider,Vector2(dire.x*2,0)):
            dire.x = 0
        if intsec_listRect(self.rect,list_colider,Vector2(0,dire.y*2)):
            dire.y = 0
        
        Mous = mouse.get_pressed()
        self.time_shotter.rodar()

        if Mous[0] == True and self.time_shotter.is_finish():
            mouse_pos = list(mouse.get_pos())
            mouse_pos[0] += -384/2 + self.rect.x
            mouse_pos[1] += -216/2 + self.rect.y
            
            diret = direct(Vector2(self.rect.x,self.rect.y),Vector2(mouse_pos[0],mouse_pos[1]))
            
            bullet = Bullet(self.rect.x+8,self.rect.y+8,diret.x,diret.y)
            list_bullet.append(bullet)
            list_spr.append(bullet)
            self.time_shotter.reniciar()

        self.rect.x += dire.x*2
        self.rect.y += dire.y*2
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
    def __init__(self,x,y,w,h):
        self.img = Surface((w,h))
        self.img.fill((200,0,200))
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def draw(self,surfac):
        surfac.blit(self.img,self.rect)

player = PLAYER(32,32)
caho = WALL(100,100,16,16)

def inter_tile(TileMap : list):
    tilemap = list(TileMap)
    Tx = -1
    Ty = -1
    Bx = -1
    By = -1
    pos_y = 0
    for list_x in tilemap:
        pos_x = 0
        for i in list_x:
            if i == 1:
                tilemap[pos_y][pos_x] = 0
            if Tx == -1:
                if i == 1:
                    Ty = pos_y
                    Tx = pos_x
            if Tx != -1:
                if i == 0:
                    Bx = pos_x -1
            if Tx !=-1 and Bx != -1:
                ye = Ty+1
                while(By ==-1):
                    for a in range(Tx,Bx+1):
                        if tilemap[ye][a] != 1:
                            By = ye-1
                            w_ = Bx+1 - Tx
                            h_ = By+1 - Ty
                            list_spr.append(WALL(Tx*16,Ty*16,w_*16,h_*16))
                            list_colider.append(WALL(Tx*16,Ty*16,w_*16,h_*16))

                    if By == -1:
                        for a in range(Tx,Bx+1):
                            tilemap[ye][a] = 0
                    if By != -1:
                        Tx = -1
                        Ty = -1
                        Bx = -1
                        By = -1
                        break
                    ye += 1 
            pos_x += 1
        pos_y += 1
list_spr.append(player)

# list_spr = [player,caho]
class CAMERA():
    def __init__(self):
        self.tela_img = display.get_surface()
        self.pos = Vector2(0,0)
    def draw_screen(self,surfac):
        x_ = lerp(self.pos.x,(player.rect.x+8-384/2),0.06)
        y_ = lerp(self.pos.y,(player.rect.y+8-216/2),0.06)
        self.pos = Vector2(x_,y_)
        
        for spr in list_spr:
            # rec = spr.rect
            pos = [spr.rect.x,spr.rect.y]
            pos[0] -= self.pos.x
            pos[1] -= self.pos.y
            surfac.blit(spr.img,pos)

cam = CAMERA()
fps = time.Clock()
screen = display.set_mode((384,216),RESIZABLE | SCALED)
canva = Surface((384,216))
LOOP = True
inter_tile(tile_map)
while LOOP:
    for evente in event.get():
        if evente.type == QUIT:
            LOOP = False
    

    for i in list_bullet:
        i.updade()

    screen.fill((0, 0, 0))
    canva.fill((0,50,100))
    player.updade()
    cam.draw_screen(canva)
    screen.blit(canva,(0,0))

    display.flip()
    fps.tick(60)
quit()
