import sys

import pygame
from pygame.locals import *
import random
import pyperclip  # 用于操作剪贴板
import keyboard  # 用于模拟键盘操作
import time  # 用于延时操作
import msvcrt

import pygame


class Button:
    def __init__(self, x, y, width, height, text, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)


class Text:
    def __init__(self, x, y, text, size):
        self.x = x
        self.y = y
        self.text = text
        self.size = size

    def draw(self, surface):
        font = pygame.font.SysFont('Arial', self.size)
        text = font.render(self.text, True, (255, 255, 255))
        surface.blit(text, (self.x, self.y))


need_delay = False
is_copying = False
copy_completed = False
copy_as_cs = False


def virtual_kb_input():
    i = 0
    while i < 2:
        time.sleep(1)
        i = i + 1
        print("剩下" + str(2-i) + "秒复制，请把光标移动到要输入的位置")
    text = pyperclip.paste()
    print("开始粘贴")
    global copy_completed
    copy_completed = False
    global is_copying
    is_copying = True
    for char in text:
        keyboard.write(char)
        if need_delay:
            time.sleep(random.uniform(0.5, 2))
        if copy_as_cs:
            time.sleep(0.02)
    print("粘贴任务完成")
    is_copying = False
    copy_completed = True


pygame.init()
FPS = 30
DISPLAY_SURFACE = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Lagging Warrior Copy Master", "Lagging Warrior Copy Master")
# DISPLAY_SURFACE.fill((237, 101, 255))
# icon = pygame.image.load("LZX9.ico")
# DISPLAY_SURFACE.display.set_icon(icon)

# init button
button_movement_cv = Button(200, 200, 100, 50, "Mod1", (0, 255, 0))
button_cv_as_human = Button(400, 200, 100, 50, "Mod2", (0, 255, 0))
button_cv_as_cs = Button(600, 200, 100, 50, "Mod3", (0, 255, 0))
# init Img
img = pygame.image.load("_internal/Img/MSG.png")
# init Text
text_copying = Text(0, 0, "Copying", 32)
text_copy_completed = Text(0, 0, "Copy completed", 32)
software_MSG = Text(730, 0, "Version:Beta2.2", 10)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_movement_cv.rect.collidepoint(event.pos):
                need_delay = False
                copy_as_cs = False
                virtual_kb_input()
            if button_cv_as_human.rect.collidepoint(event.pos):
                need_delay = True
                copy_as_cs = False
                virtual_kb_input()
            if button_cv_as_cs.rect.collidepoint(event.pos):
                need_delay = False
                copy_as_cs = True
                virtual_kb_input()
    DISPLAY_SURFACE.fill((237, 101, 255))
    DISPLAY_SURFACE.blit(img, (0, 0))
    button_movement_cv.draw(DISPLAY_SURFACE)
    button_cv_as_human.draw(DISPLAY_SURFACE)
    button_cv_as_cs.draw(DISPLAY_SURFACE)
    software_MSG.draw(DISPLAY_SURFACE)
    # DISPLAY_SURFACE.blit(text, (0, 0))
    if is_copying:
        text_copying.draw(DISPLAY_SURFACE)
    if copy_completed:
        text_copy_completed.draw(DISPLAY_SURFACE)
    pygame.display.update()
    time.sleep(1 / FPS)

    # LZX write this code in 2024/03/10
    # LZX-TC-Pycharm2021.3-2024-03-10-001
