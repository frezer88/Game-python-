import pygame
from module1 import Asteroid
from module2 import Bullet
import random

pygame.init()
pygame.mixer.init()
Width = 499
Height = 600
Spawn_rate = 500 # скорость появления астероидов
FPS = 60

pygame.mixer.music.load('music2.wav')#музыка
pygame.mixer.music.play(-1) 

pygame.time.set_timer(pygame.USEREVENT,Spawn_rate)# вызов события каждые 0.4 секунды

window = pygame.display.set_mode((Width, Height))#размер окна
pygame.display.set_caption('Paper plane')

clock = pygame.time.Clock()

background_image=pygame.image.load("win.jpg")
left_image=pygame.image.load("ll.png")
right_image=pygame.image.load("rr.png")
right_Up_or_down=pygame.image.load("11.png")
bul = pygame.image.load("Bullet.png")
game_over=pygame.image.load("game_over.png")
menu_image = pygame.image.load("menu.png")
exit_menu = pygame.image.load("exit_menu.png")
play_menu = pygame.image.load("play_menu.png")

shrift = pygame.font.SysFont('arial',50)# шрифит

x = 220# начальные кординаты
y = 480 
score = 0
speed = 6# скорость
t_rect = right_Up_or_down.get_rect(centerx = Width//2,bottom = Height)# тело
window.blit(menu_image,(0,0))# задний фон начального мееню

End_game = True

mob_images = ['Asteroid.png','Asteroid2.png','Asteroid.png','Asteroid2.png']
mob_surf = [pygame.image.load(path).convert_alpha() for path in mob_images]
mob = pygame.sprite.Group()

def Mob(group):# создание рандомно падающих объектов
    index = random.randint(0,len(mob_surf)-1)
    return Asteroid(mob_surf[index],group)
Mob(mob)

def Crash():# попадание астероида в самолет
    global End_game
    for boom in mob:
        if t_rect.collidepoint(boom.rect.center):
            boom.kill()
            End_game = False

bullets = pygame.sprite.Group()
def Shoot():# создания объекта типа пули
    bullet = Bullet(x+42, y,bul)
    bullets.add(bullet)

def Draw():
    global shrift
    global score
    window.blit(background_image,(0,0))# задний фон
    #window.fill((0,0,0)) # закрашивание окно в черный
    if left:
        window.blit(left_image,(x-20,y))
    elif right:
        window.blit(right_image,(x-20,y))
    else:
        window.blit(right_Up_or_down,(x-20,y))
    window_text = shrift.render(str(score),True,(12, 0, 203))# переменная очков
    window.blit(window_text,((10,10)))# отображение очков
    mob.draw(window)
    bullets.draw(window)
    bullets.update()
    #pygame.draw.rect(window,(0,0,255), (x,y,W,H))# создание квадрата на определенных кординатах
    pygame.display.update()# обновление окна
    mob.update(600)


def Game_over():# цикл финального экрана
    global score,x,y
    global End_game
    end = True
    window.blit(game_over,(0,0))# задний фон

    pygame.mixer.music.pause()
    shrift = pygame.font.SysFont('arial',50)# шрифит
    window_text = shrift.render(str(score),True,(12, 0, 203))# переменная очков
    window.blit(window_text,((260,500)))# отображение очков
    pygame.display.update()# обновление окна
    while end:
        pygame.time.delay(10)# время задержки выполнения цикла
        for fact in pygame.event.get():# перебираем массив с событиями     
            if fact.type == pygame.QUIT:
                end = False# Конец игры
            if fact.type == pygame.K_ESCAPE:
                end = False# Конец игры

        
        keys = pygame.key.get_pressed()# отслеживание нажатых кнопок
        if keys[pygame.K_ESCAPE]:
            end = False
        if keys[pygame.K_RETURN]:
            pygame.mixer.music.play(-1) 
            end = False
            End_game = True         
            score = 0
            x = 220# начальные кординаты
            y = 480 
            t_rect.y = y
            t_rect.x = x
            Spawn_rate = 500
            pygame.time.set_timer(pygame.USEREVENT,Spawn_rate)# вызов события каждые 0.4 секунды
            mob.update(-100)
menu = True
up = False
down = False

while menu:

     for fact in pygame.event.get():# перебираем массив с событиями          
        if fact.type == pygame.QUIT:
            End_game = False# Конец игры
            menu = False
        elif fact.type == pygame.KEYDOWN:
            if fact.key == pygame.K_DOWN:
                if down == False and up == False:
                    window.blit(play_menu,(0,0))# задний фон
                    down = True
                elif down == True and up == False:
                    window.blit(exit_menu,(0,0))# задний фон
                    down = False
                    up = True
            if fact.key == pygame.K_UP:
                if up == True and down == False:
                    window.blit(play_menu,(0,0))# задний фон
                    up = False
                    down = True


     keys = pygame.key.get_pressed()# отслеживание нажатых кнопок
     if keys[pygame.K_ESCAPE]:
        menu = False
        End_game = False     
     if keys[pygame.K_RETURN]:
         if down == False and up == True:
            menu = False
            End_game = False 
         elif down == True and up == False:
            menu = False
            
     pygame.display.update()# обновление окна

while End_game:# игровой цикл
    clock.tick(FPS)
    pygame.time.delay(10)# время задержки выполнения цикла

    for fact in pygame.event.get():# перебираем массив с событиями          
        if fact.type == pygame.QUIT:
            End_game = False# Конец игры
        elif fact.type == pygame.USEREVENT:
            Mob(mob)
        elif fact.type == pygame.KEYDOWN:
            if fact.key == pygame.K_SPACE:
                Shoot()

        

    keys = pygame.key.get_pressed()# отслеживание нажатых кнопок
    left = False# направление самолета
    right = False
    if keys[pygame.K_ESCAPE]:
        End_game = False
    if keys[pygame.K_LEFT] and x > 0:# обработка определенной клавиши с выставленной границей по кординатам
        x -= speed     
        t_rect.x -= speed
        left = True
        right = False
    if keys[pygame.K_RIGHT] and x < 400:
        x += speed     
        t_rect.x += speed
        left = False
        right = True  
    if keys[pygame.K_DOWN] and y < 500:
        y += speed     
        t_rect.y += speed
        left = False
        right = False
    if keys[pygame.K_UP] and y > 0:
        y -= speed
        t_rect.y -= speed
        left = False
        right = False

    hits = pygame.sprite.groupcollide(mob, bullets, True, True)
    if len(hits) == 1:
        score += 10
        if Spawn_rate > 50:# сделать ли в обратуню сторону? 
            Spawn_rate-=10
            pygame.time.set_timer(pygame.USEREVENT,Spawn_rate)# вызов события каждые 0.4 секунды
    Crash()
    Draw()
    if End_game == False:
        Game_over()
      
pygame.quit()