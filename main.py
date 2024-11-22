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
pta_mode = False


def virtual_kb_input():
    #print(need_delay.__str__() + " " + copy_as_cs.__str__() + " " + pta_mode.__str__())
    i = 0
    while i < 2:
        time.sleep(1)
        i = i + 1
        print("剩下" + str(3 - i) + "秒复制，请把光标移动到要输入的位置")
    text = pyperclip.paste()
    if pta_mode:
        text = text.replace("    ","")
    print("开始粘贴")
    global copy_completed
    copy_completed = False
    global is_copying
    is_copying = True
    for char in text:
        if pta_mode:
            if char == '/t':
                print("t")
                continue
        keyboard.write(char)
        if need_delay:
            time.sleep(random.uniform(0.5, 2))
        if copy_as_cs:
            time.sleep(0.02)
    print("粘贴任务完成")
    if pta_mode:
        keyboard.write("\n\n\n\n/*请手动删除本行以下的文本*/")
    is_copying = False
    copy_completed = True


def main():
    pygame.init()
    print("LoongLy Paste Master Beta3.1")
    print("Mode1:瞬间粘贴\nMode2:模仿人手输入(0.5-2秒输入一个字)\nMode3:每隔0.05秒输入一个字\nPTA Mode:针对类C在PTA平台的粘贴")
    FPS = 30
    DISPLAY_SURFACE = pygame.display.set_mode((520, 150))
    pygame.display.set_caption("Loongly(Lagging Warrior) Copy Master", "Loongly(Lagging Warrior) Copy Master")
    # DISPLAY_SURFACE.fill((237, 101, 255))
    # icon = pygame.image.load("LZX9.ico")
    # DISPLAY_SURFACE.display.set_icon(icon)

    # init button
    button_movement_cv = Button(10, 10, 150, 50, "Mode1", (76, 90, 88))
    button_cv_as_human = Button(180, 10, 150, 50, "Mode2", (76, 90, 88))
    button_cv_as_cs = Button(350, 10, 150, 50, "Mode3", (76, 90, 88))
    button_pta_mode_cv = Button(10, 70, 490, 50, "PTA Mode:OFF", (76, 90, 88))
    # init Img
    img = pygame.image.load("_internal/Img/MSG.png")
    # init Text
    text_copying = Text(0, 0, "Copying", 32)
    text_copy_completed = Text(0, 0, "Copy completed", 32)
    software_MSG = Text(730, 0, "Version:Beta3.1", 10)

    global need_delay
    global copy_as_cs
    global pta_mode
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
                if button_pta_mode_cv.rect.collidepoint(event.pos):
                    pta_mode = not pta_mode
                    #print(pta_mode.__str__())
                    if pta_mode:
                        button_pta_mode_cv.text = "PTA Mode:ON"
                    else:
                        button_pta_mode_cv.text = "PTA Mode:OFF"
                    #virtual_kb_input()
        DISPLAY_SURFACE.fill((237, 101, 255))
        DISPLAY_SURFACE.blit(img, (0, 0))
        button_movement_cv.draw(DISPLAY_SURFACE)
        button_cv_as_human.draw(DISPLAY_SURFACE)
        button_cv_as_cs.draw(DISPLAY_SURFACE)
        button_pta_mode_cv.draw(DISPLAY_SURFACE)
        software_MSG.draw(DISPLAY_SURFACE)
        # DISPLAY_SURFACE.blit(text, (0, 0))
        if is_copying:
            text_copying.draw(DISPLAY_SURFACE)
        if copy_completed:
            text_copy_completed.draw(DISPLAY_SURFACE)
        pygame.display.update()
        time.sleep(1 / FPS)


if __name__ == '__main__':
    main()

# LZX write this code in 2024/03/10
# LZX-TC-Pycharm2021.3-2024-03-10-001
