#main.py
import pygame
import ui
from tools import counter
from random import randint

WINHEIGHT=100
WINWIDTH=1920
WIDGETSPACING=1
WIDGETOFFSET=10

running = True
widgets=[]

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

screen=ui.createScreen(1,WINWIDTH,WINHEIGHT)
pygame.display.set_caption("Test-Meterbridge")

#UI initialisieren
BLUE=(0,0,255)
RED=(255,0,0)
YELLOW=(255,255,0)
GREEN=(0,255,0)
MAGENTA=(255,0,100)
CYAN=(100,100,255)
WHITE=(255,255,255)
BLACK=(0,0,0)
GREY=(100,100,100)

channel_widgets=[
ui.widget(screen, GREY, "Mic 1", 1, "XLR 1","Funk A",icon="ui_icons/wireless_microphone_L.png",iconbg=RED),
ui.widget(screen, GREY, "Mic 2", 2, "XLR 2","Funk B",icon="ui_icons/wireless_microphone_R.png",iconbg=BLUE),
ui.widget(screen, GREY, "Mic 3", 3, "XLR 3","EXT A",icon="ui_icons/microphone.png",iconbg=YELLOW),
ui.widget(screen, GREY, "Mic 4", 4, "XLR 4","EXT B",icon="ui_icons/microphone.png",iconbg=MAGENTA),
ui.widget(screen, GREY, "Mic 5", 5, "XLR 5","EXT C",icon="ui_icons/microphone.png",iconbg=GREEN),
ui.widget(screen, GREY, "Mic 6", 6, "XLR 6","EXT D",icon="ui_icons/microphone.png",iconbg=CYAN),
ui.widget(screen, BLUE, "AV-System", 7, "XLR 13/14","HDMI",icon="ui_icons/hdmi.png",iconbg=RED),
ui.widget(screen, BLUE, "Bluetooth", 8, "AUX","Bluetooth",icon="ui_icons/smartphone_bluetooth.png",iconbg=YELLOW),

ui.widget(screen, RED, "Rausgang", "M", "OUT L/R","A/B",icon="ui_icons/loudspeaker.png",iconbg=CYAN),
ui.widget(screen, GREY, "Player Status", "P", "Interpret XY - Irgend ein Lied von dem Interpret XY", "State: Play",icon="ui_icons/player_play.png",iconbg=GREEN),
ui.widget(screen, GREY, "Layer Control", "L", "Layer: Physical Inputs", "No. 1", "", mode=3)
]

a=counter(2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
    if(a.expired()):
        for i in range(len(channel_widgets)):
            channel_widgets[i].set_meter(randint(0,100))
    screen.fill((0,0,0))
    for i in range(len(channel_widgets)):
        channel_widgets[i].draw(i)
    pygame.display.flip()
    clock.tick(60)
