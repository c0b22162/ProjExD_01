import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ProjExD2023/ex01/fig/pg_bg.jpg")
    kk_img = pg.image.load("ProjExD2023/ex01/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_img = [kk_img, pg.transform.rotozoom(kk_img, 10, 1.0)]
    tmr = 0
    x = 0
    while True:
        x += 1
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        # for x in range(1600):
        #     if x == 1599: 
        #         x = 1 
        #         return
        screen.blit(bg_img, [-x, 0])
        screen.blit(kk_img[tmr % 2], [300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(100)
        
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()