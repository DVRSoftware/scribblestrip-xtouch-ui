
import pygame
import os

def createScreen(display,width,height):
    if(pygame.display.get_num_displays()>1):
        print("Open on second Monitor.")
        os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (1920*display,1080-height)
        screen = pygame.display.set_mode((1920, height), pygame.NOFRAME)
    else:
        print("Open on primary Monitor")
        os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (0,1080-height-30)
        screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
    return screen

class text:
    def __init__(self,font,text):
        self.rfont=font.render(str(text), True, (0, 0, 0))
        self.tsx, self.tsy=self.rfont.get_size()
        self.scroll=0
        self.counter=0
    
    def draw(self,surface,x,y,w,h):
        tsy=y+(h-self.tsy)/2
        if(self.tsx<=w):
            tsx=x+(w-self.tsx)/2
            sfont=self.rfont
        else:
            tsx=x
            if((self.scroll+w)>=self.tsx):
                if(self.counter>=80):
                    self.scroll=0
                    self.counter=0
                else:
                    self.counter+=1

            elif(self.scroll==0):
                if(self.counter>=80):
                    self.scroll=1
                    self.counter=0
                else:
                    self.counter+=1
            else:
                if(self.counter>=2):
                    self.scroll+=1
                    self.counter=0
                else:
                    self.counter+=1
            sfont=self.rfont.subsurface((self.scroll,0,w,self.tsy))
        surface.blit(sfont, (tsx,tsy))


class widget:
    def __init__(self,screen,color=(127,127,127),title="Channel",id=1,text1="",text2="",text3="",text4="",icon=None,iconbg=(255,255,255),mode=0):
        headfont=pygame.font.SysFont('Arial', 18)
        mainfont=pygame.font.SysFont('Arial', 16)
        self.id=text(headfont,str(id))
        self.title=text(headfont,str(title))
        self.meter=0
        self.r_meter=None
        self.screen=screen
        self.mode=mode
        self.color=color
        self.iconbg=iconbg
        self.text=[text(mainfont,text1),text(mainfont,text2),text(mainfont,text3),text(mainfont,text4)]
        if(icon!=None):
            self.icon=pygame.transform.scale(pygame.image.load(icon), (58,58))
        else:
            self.icon=None
        self.scroll_indexes=[0,0,0,0]

    def set_meter(self,level,rightlevel=None):
        self.meter=level
        if(rightlevel!=None):
            self.r_meter=rightlevel

    def draw(self,x):
        surface = pygame.Surface((174, 100), pygame.SRCALPHA)
        pygame.draw.rect(surface, (255,255,255), (0,0,174,100), 0, 0) #BG MAIN
        pygame.draw.rect(surface, self.color, (2,0,170,20),0,0) #BG FREE
        pygame.draw.rect(surface, (0,0,0), (0,20,174,2), 0, 0) #BAR TOP
        pygame.draw.rect(surface, (0,0,0), (0,0,2,100), 0, 0) #BAR LEFT
        pygame.draw.rect(surface, (0,0,0), (172,0,2,100), 0, 0) #BAR Right

        if(self.mode==0): #VU On, Icon On
            ts=24
            tw=88
            tw2=148
            vu_on=1
            pygame.draw.rect(surface, (0,0,0), (112,42,2,58), 0, 0)
            pygame.draw.rect(surface, self.iconbg, (114,42,58,58), 0, 0)

        elif(self.mode==1): #VU On, Icon Off 
            ts=24
            tw=148
            tw2=148
            vu_on=1

        elif(self.mode==2): #VU Off, Icon On
            ts=2
            tw=112
            tw2=170
            vu_on=0
            pygame.draw.rect(surface, (0,0,0), (112,42,2,58), 0, 0)
            pygame.draw.rect(surface, self.iconbg, (114,42,58,58), 0, 0)

        else:   #VU Off, Icon Off
            ts=2
            tw=170
            tw2=170
            vu_on=0

        pygame.draw.rect(surface, (0,0,0), (ts,60,tw,2), 0, 0)
        pygame.draw.rect(surface, (0,0,0), (ts,80,tw,2), 0, 0)

        if(vu_on):
            pygame.draw.rect(surface, (0,0,0), (22,0,2,100), 0, 0)
            pygame.draw.rect(surface, (0,0,0), (24,40,148,2), 0, 0)
            if(self.r_meter==None):
                vu_map1=min(max(int((self.meter/100)*78),0),78)
                pygame.draw.rect(surface, (0,255,0), (2,100-vu_map1,20,vu_map1),0,0)
            else:
                vu_map1=min(max(int((self.meter/100)*78),0),78)
                vu_map2=min(max(int((self.r_meter/100)*78),0),78)
                pygame.draw.rect(surface, (0,255,0), (2,100-vu_map1,9,vu_map1),0,0)
                pygame.draw.rect(surface, (0,255,0), (13,100-vu_map2,9,vu_map2),0,0)
                pygame.draw.rect(surface, (0,0,0), (11,22,2,78), 0, 0)
        else:
            pygame.draw.rect(surface, (0,0,0), (2,40,170,2), 0, 0)
            pygame.draw.rect(surface, (0,0,0), (22,0,2,20), 0, 0)

        if(self.icon!=None and self.mode in (0,2)):
            surface.blit(self.icon, (114,42))

        self.id.draw(surface,2,0,20,20)
        self.title.draw(surface,24,0,146,20)
        self.text[0].draw(surface,ts,22,tw2,18)
        self.text[1].draw(surface,ts,42,tw,18)
        self.text[2].draw(surface,ts,62,tw,18)
        self.text[3].draw(surface,ts,82,tw,18)
        self.screen.blit(surface, (174*x, 0))