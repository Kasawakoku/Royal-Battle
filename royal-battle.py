# Bruce Qiu, Jonathan Fong
# CPT: Royal Battle
import pygame
import pygame.event
import random
import time
from pygame.locals import MOUSEBUTTONDOWN

# Bruce
# Global Variables
WIDTH = 400
HEIGHT = 400
SIZE = (WIDTH, HEIGHT)

SCREEN = pygame.display.set_mode(SIZE)
CLOCK = pygame.time.Clock()


TILES = {}
for x in range(0,400):
            for y in range(0,400):
                if x % 50 == 0 and y % 50 == 0:
                    TILES[str(int((x/50+1)))+str(int((y/50+1)))] = (x,y,50,50)

PIECES = {}
for i in range (1,9):
    PIECES["bp"+str(i)] = str(i)+"7"
    PIECES["wp"+str(i)] = str(i)+"2"
BACK_POS_LIST = [1,2,3,4,5,6,7,8]
BACK_PIECE_LIST = ["k","n1","n2","t1","t2","m","g1","g2"]
for p in BACK_PIECE_LIST:
    pos = random.choice(BACK_POS_LIST)
    BACK_POS_LIST.remove(pos)
    PIECES["b"+p] = str(pos) + "8"
    PIECES["w"+p] = str(pos) + "1"
    


TILE_CLICKED = None
WHITE_MOVE = True
def display_text(message,colour,font):
    text = font.render(message,True,colour)
    SCREEN.blit(text, (150,150))

# Bruce
# Pawn Move
def pawn_move(pawn):
    pos = PIECES[pawn]
    pos_list = []
    global WHITE_MOVE
    if not WHITE_MOVE and pos[1] != "1":
        pos_list.append(pos[0]+str(int(pos[1])-1))
    elif WHITE_MOVE and pos[1] != "8":
        pos_list.append(pos[0]+str(int(pos[1])+1))

    for piece in PIECES:
        if WHITE_MOVE:
            if piece[0] == "b": 
                if int(PIECES[piece]) == int(PIECES[pawn])+10 or int(PIECES[piece]) == int(PIECES[pawn])-10:
                    pos_list.append(PIECES[piece])
        else:
            if piece[0] == "w": 
                if int(PIECES[piece]) == int(PIECES[pawn])+10 or int(PIECES[piece]) == int(PIECES[pawn])-10:
                    pos_list.append(PIECES[piece])
    
    for p in pos_list.copy():
        for piece in PIECES:
            if PIECES[piece] == p:
                if pawn[0] == piece[0]:
                    pos_list.remove(p)

    for p in pos_list:
        ppos = TILES[p]
        pygame.draw.circle(SCREEN,(110,110,110),(ppos[0] + 25,ppos[1] + 25),10)
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for tile in TILES:
                if pygame.Rect(TILES[tile]).collidepoint(x,y):
                    for p in pos_list: 
                        if tile == p:
                            for piece in PIECES.copy():
                                if PIECES.copy()[piece] == tile:
                                    PIECES.pop(piece,None)
                            PIECES[pawn] = p
                            if WHITE_MOVE:
                                WHITE_MOVE = False
                            else:
                                WHITE_MOVE = True
                            global TILE_CLICKED
                            TILE_CLICKED = None
                            pass
                        elif tile not in pos_list:
                            TILE_CLICKED = None
                            pass

# Jonathan
# King Move
def king_move(king):
    pos = PIECES[king]
    pos_list = []
    global WHITE_MOVE
    
    pos_list.append(pos[0]+str(int(pos[1])-1))
    pos_list.append(pos[0]+str(int(pos[1])+1))
    pos_list.append(str(int(pos[0])+1)+pos[1])
    pos_list.append(str(int(pos[0])-1)+pos[1])
    pos_list.append(str(int(pos[0])+1)+str(int(pos[1])+1))
    pos_list.append(str(int(pos[0])+1)+str(int(pos[1])-1))
    pos_list.append(str(int(pos[0])-1)+str(int(pos[1])+1))
    pos_list.append(str(int(pos[0])-1)+str(int(pos[1])-1))
    
    for p in pos_list.copy():
        if p not in TILES:
            pos_list.remove(p)
            
    for p in pos_list.copy():
        for piece in PIECES:
            if PIECES[piece] == p:
                if king[0] == piece[0]:
                    pos_list.remove(p)
        

    for p in pos_list:
        ppos = TILES[p]
        pygame.draw.circle(SCREEN,(110,110,110),(ppos[0] + 25,ppos[1] + 25),10)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for tile in TILES:
                if pygame.Rect(TILES[tile]).collidepoint(x,y):
                    for p in pos_list: 
                        if tile == p:
                            for piece in PIECES.copy():
                                if PIECES.copy()[piece] == tile:
                                    PIECES.pop(piece,None)
                            PIECES[king] = p
                            if WHITE_MOVE:
                                WHITE_MOVE = False
                            else:
                                WHITE_MOVE = True
                            global TILE_CLICKED
                            TILE_CLICKED = None
                            pass
                        elif tile not in pos_list:
                            TILE_CLICKED = None
                            pass
                            
# Jonathan                 
# Super Soldier Move
def super_move(super):
    pos = PIECES[super]
    pos_list = []
    global WHITE_MOVE

    pos_list.append(pos[0]+str(int(pos[1])-1))
    pos_list.append(pos[0]+str(int(pos[1])+1))
    pos_list.append(str(int(pos[0])+1)+pos[1])
    pos_list.append(str(int(pos[0])-1)+pos[1])
    pos_list.append(pos[0]+str(int(pos[1])-2))
    pos_list.append(pos[0]+str(int(pos[1])+2))
    pos_list.append(str(int(pos[0])+2)+pos[1])
    pos_list.append(str(int(pos[0])-2)+pos[1])
    
    for p in pos_list.copy():
        if p not in TILES:
            pos_list.remove(p)
            
    for p in pos_list.copy():
        for piece in PIECES:
            if PIECES[piece] == p:
                if super[0] == piece[0]:
                    pos_list.remove(p)
        
    for p in pos_list:
        ppos = TILES[p]
        pygame.draw.circle(SCREEN,(110,110,110),(ppos[0] + 25,ppos[1] + 25),10)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for tile in TILES:
                if pygame.Rect(TILES[tile]).collidepoint(x,y):
                    for p in pos_list: 
                        if tile == p:
                            for piece in PIECES.copy():
                                if PIECES.copy()[piece] == tile:
                                    PIECES.pop(piece,None)
                            PIECES[super] = p
                            if WHITE_MOVE:
                                WHITE_MOVE = False
                            else:
                                WHITE_MOVE = True
                            global TILE_CLICKED
                            TILE_CLICKED = None
                            pass
                        elif tile not in pos_list:
                            TILE_CLICKED = None
                            pass
# Jonathan
# Tank Move
def tank_move(tank):
    pos = PIECES[tank]
    pos_list = []
    global WHITE_MOVE
  
    pos_list.append(str(int(pos[0])-1)+str(int(pos[1])-1))
    pos_list.append(str(int(pos[0])+1)+str(int(pos[1])-1))
    pos_list.append(str(int(pos[0])-1)+str(int(pos[1])+1))
    pos_list.append(str(int(pos[0])+1)+str(int(pos[1])+1))
    pos_list.append(str(int(pos[0])-2)+str(int(pos[1])-2))
    pos_list.append(str(int(pos[0])+2)+str(int(pos[1])-2))
    pos_list.append(str(int(pos[0])-2)+str(int(pos[1])+2))
    pos_list.append(str(int(pos[0])+2)+str(int(pos[1])+2))
    
    for p in pos_list.copy():
        if p not in TILES:
            pos_list.remove(p)
            
    for p in pos_list.copy():
        for piece in PIECES:
            if PIECES[piece] == p:
                if tank[0] == piece[0]:
                    pos_list.remove(p)

    
    for p in pos_list:
        ppos = TILES[p]
        pygame.draw.circle(SCREEN,(110,110,110),(ppos[0] + 25,ppos[1] + 25),10)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for tile in TILES:
                if pygame.Rect(TILES[tile]).collidepoint(x,y):
                    for p in pos_list: 
                        if tile == p:
                            for piece in PIECES.copy():
                                if PIECES.copy()[piece] == tile:
                                    PIECES.pop(piece,None)
                            PIECES[tank] = p
                            if WHITE_MOVE:
                                WHITE_MOVE = False
                            else:
                                WHITE_MOVE = True
                            global TILE_CLICKED
                            TILE_CLICKED = None
                            pass
                        elif tile not in pos_list:
                            TILE_CLICKED = None
                            pass

# Jonathan                     
# Miner Move

def miner_move(miner):
    pos = PIECES[miner]
    pos_list = []
    global WHITE_MOVE

    pos_list.append(pos[0]+str(int(pos[1])-2))
    pos_list.append(pos[0]+str(int(pos[1])+2))
    pos_list.append(pos[0]+str(int(pos[1])-4))
    pos_list.append(pos[0]+str(int(pos[1])+4))
    pos_list.append(pos[0]+str(int(pos[1])-6))
    pos_list.append(pos[0]+str(int(pos[1])+6))
    pos_list.append(str(int(pos[0])-2)+pos[1])
    pos_list.append(str(int(pos[0])+2)+pos[1])
    pos_list.append(str(int(pos[0])-4)+pos[1])
    pos_list.append(str(int(pos[0])+4)+pos[1])
    pos_list.append(str(int(pos[0])-6)+pos[1])
    pos_list.append(str(int(pos[0])+6)+pos[1])
    
    for p in pos_list.copy():
        if p not in TILES:
            pos_list.remove(p)
            
    for p in pos_list.copy():
        for piece in PIECES:
            if PIECES[piece] == p:
                if miner[0] == piece[0]:
                    pos_list.remove(p)
        
    for p in pos_list:
        ppos = TILES[p]
        pygame.draw.circle(SCREEN,(110,110,110),(ppos[0] + 25,ppos[1] + 25),10)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for tile in TILES:
                if pygame.Rect(TILES[tile]).collidepoint(x,y):
                    for p in pos_list: 
                        if tile == p:
                            for piece in PIECES.copy():
                                if PIECES.copy()[piece] == tile:
                                    PIECES.pop(piece,None)
                            PIECES[miner] = p
                            if WHITE_MOVE:
                                WHITE_MOVE = False
                            else:
                                WHITE_MOVE = True
                            global TILE_CLICKED
                            TILE_CLICKED = None
                            pass
                        elif tile not in pos_list:
                            TILE_CLICKED = None
                            pass

# Jonathan
# Goat Move
def goat_move(goat):
    pos = PIECES[goat]
    pos_list = []
    global WHITE_MOVE

    pos_list.append(pos[0]+str(int(pos[1])-1))
    pos_list.append(pos[0]+str(int(pos[1])+1))
    pos_list.append(str(int(pos[0])-1)+pos[1])
    pos_list.append(str(int(pos[0])+1)+pos[1])
    pos_list.append(str(int(pos[0])-1)+str(int(pos[1])-1))
    pos_list.append(str(int(pos[0])+1)+str(int(pos[1])-1))
    pos_list.append(str(int(pos[0])-1)+str(int(pos[1])+1))
    pos_list.append(str(int(pos[0])+1)+str(int(pos[1])+1))
    
    for p in pos_list.copy():
        if p not in TILES:
            pos_list.remove(p)
            
    for p in pos_list.copy():
        for piece in PIECES:
            if PIECES[piece] == p:
                if goat[0] == piece[0]:
                    pos_list.remove(p)
        
    for p in pos_list:
        ppos = TILES[p]
        pygame.draw.circle(SCREEN,(110,110,110),(ppos[0] + 25,ppos[1] + 25),10)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for tile in TILES:
                if pygame.Rect(TILES[tile]).collidepoint(x,y):
                    for p in pos_list: 
                        if tile == p:
                            for piece in PIECES.copy():
                                if PIECES.copy()[piece] == tile:
                                    PIECES.pop(piece,None)
                            PIECES[goat] = p
                            if WHITE_MOVE:
                                WHITE_MOVE = False
                            else:
                                WHITE_MOVE = True
                            global TILE_CLICKED
                            TILE_CLICKED = None
                            pass
                        elif tile not in pos_list:
                            TILE_CLICKED = None
                            pass
                          

# Main
def main():
    pygame.init()
    running = True
    font = pygame.font.SysFont("Times New Roman", 20)
    
    while running:
        # Bruce
        # Event
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for tile in TILES:
                    if pygame.Rect(TILES[tile]).collidepoint(x,y):
                        global TILE_CLICKED
                        TILE_CLICKED = tile
                        for piece in PIECES:
                            if PIECES[piece] == tile:
                                global PIECE_SELECTED
                                
                                PIECE_SELECTED = True
                            else:
                                PIECE_SELECTED = False
                                
        # Bruce
        # Board Setup
        SCREEN.fill((255,255,255))
        for x in range(0,400):
            for y in range(0,400):
                if x % 50 == 0 and y % 50 == 0:      
                    if x % 100 == 0 and y % 100 == 0:
                        pygame.draw.rect(SCREEN, (0,0,130),(x,y,50,50))
                    elif x % 100 == 50 and y % 100 == 50:
                        pygame.draw.rect(SCREEN, (0,0,130),(x,y,50,50)) 
        # Jonathan
        # Pieces
        for piece in PIECES:
            pos = TILES[PIECES[piece]]
            
            if piece[1] == "p": # pawn
                if piece[0] == "b":
                    pygame.draw.circle(SCREEN,(0,0,0),(pos[0] + 25,pos[1] + 25),20)
                elif piece[0] == "w": 
                    pygame.draw.circle(SCREEN,(255,255,255),(pos[0] + 25,pos[1] + 25),20)
                    pygame.draw.circle(SCREEN,(0,0,0),(pos[0] + 25,pos[1] + 25),20,2)
            elif piece[1] == "k": # king
                if piece[0] == "b":
                    pygame.draw.polygon(SCREEN,(0,0,0),((pos[0]+10,pos[1]+40),(pos[0]+5,pos[1]+10),(pos[0]+15,pos[1]+25),
                                                       (pos[0]+25,pos[1]+5),(pos[0]+35,pos[1]+25),(pos[0]+45,pos[1]+10),(pos[0]+40,pos[1]+40)))
                elif piece[0] == "w":
                    pygame.draw.polygon(SCREEN,(255,255,255),((pos[0]+10,pos[1]+40),(pos[0]+5,pos[1]+10),(pos[0]+15,pos[1]+25),
                                                       (pos[0]+25,pos[1]+5),(pos[0]+35,pos[1]+25),(pos[0]+45,pos[1]+10),(pos[0]+40,pos[1]+40)))
                    pygame.draw.polygon(SCREEN,(0,0,0),((pos[0]+10,pos[1]+40),(pos[0]+5,pos[1]+10),(pos[0]+15,pos[1]+25),
                                                       (pos[0]+25,pos[1]+5),(pos[0]+35,pos[1]+25),(pos[0]+45,pos[1]+10),(pos[0]+40,pos[1]+40)),2)
            elif piece[1] == "n": # super soldier
                if piece[0] == "b":
                    pygame.draw.polygon(SCREEN,(0,0,0),((pos[0]+40,pos[1]+5),(pos[0]+15,pos[1]+30),(pos[0]+20,pos[1]+35)))
                    pygame.draw.line(SCREEN,(0,0,0),(pos[0]+8,pos[1]+45),(pos[0]+18,pos[1]+33),2)
                elif piece[0] == "w":
                    pygame.draw.polygon(SCREEN,(255,255,255),((pos[0]+40,pos[1]+5),(pos[0]+15,pos[1]+30),(pos[0]+20,pos[1]+35)))
                    pygame.draw.polygon(SCREEN,(0,0,0),((pos[0]+40,pos[1]+5),(pos[0]+15,pos[1]+30),(pos[0]+20,pos[1]+35)),2)
                    pygame.draw.line(SCREEN,(0,0,0),(pos[0]+8,pos[1]+45),(pos[0]+18,pos[1]+33),2)
            elif piece[1] == "t": # tank
                if piece[0] == "b":
                    pygame.draw.rect(SCREEN,(0,0,0), (pos[0]+5,pos[1]+5,40,40))
                elif piece[0] == "w":
                    pygame.draw.rect(SCREEN,(255,255,255), (pos[0]+5,pos[1]+5,40,40))
                    pygame.draw.rect(SCREEN,(0,0,0), (pos[0]+5,pos[1]+5,40,40), 2)
            elif piece[1] == "m": # miner
                if piece[0] == "b":
                    pygame.draw.polygon(SCREEN,(0,0,0), ((pos[0]+25,pos[1]+5),(pos[0]+45,pos[1]+25),(pos[0]+25,pos[1]+45),(pos[0]+5,pos[1]+25)))
                elif piece[0] == "w":
                    pygame.draw.polygon(SCREEN,(255,255,255), ((pos[0]+25,pos[1]+5), (pos[0]+45,pos[1]+25), (pos[0]+25,pos[1]+45),(pos[0]+5,pos[1]+25)))
                    pygame.draw.polygon(SCREEN,(0,0,0), ((pos[0]+25,pos[1]+5), (pos[0]+45,pos[1]+25), (pos[0]+25,pos[1]+45),(pos[0]+5,pos[1]+25)), 2)
            elif piece[1] == "g": # goat
                if piece[0] == "b":
                  pygame.draw.polygon(SCREEN,(0,0,0), ((pos[0]+5,pos[1]+5),(pos[0]+5,pos[1]+45),(pos[0]+45,pos[1]+45),(pos[0]+45,pos[1]+5),(pos[0]+25,pos[1]+25)))
                elif piece[0] == "w":
                    pygame.draw.polygon(SCREEN,(255,255,255), ((pos[0]+5,pos[1]+5),(pos[0]+5,pos[1]+45),(pos[0]+45,pos[1]+45),(pos[0]+45,pos[1]+5),(pos[0]+25,pos[1]+25)))
                    pygame.draw.polygon(SCREEN,(0,0,0), ((pos[0]+5,pos[1]+5),(pos[0]+5,pos[1]+45),(pos[0]+45,pos[1]+45),(pos[0]+45,pos[1]+5),(pos[0]+25,pos[1]+25)), 2)    
        # Move
        for key in PIECES.copy():
            if PIECES.copy()[key] == TILE_CLICKED:
                global WHITE_MOVE
                if WHITE_MOVE:
                    if key[0] == "w":
                        if key[1] == "p":
                            pawn_move(key)
                            break
                        elif key[1] == "k":
                            king_move(key)
                            break
                        elif key[1] == "n":
                            super_move(key)
                            break
                        elif key[1] == "t":
                            tank_move(key)
                            break
                        elif key[1] == "m":
                            miner_move(key)
                            break
                        elif key[1] == "g":
                            goat_move(key)
                            break
                    else:
                        pass
                else:
                    if key[0] == "b":
                        if key[1] == "p":
                            pawn_move(key)
                            break
                        elif key[1] == "k":
                            king_move(key)
                            break
                        elif key[1] == "n":
                            super_move(key)
                            break
                        elif key[1] == "t":
                            tank_move(key)
                            break
                        elif key[1] == "m":
                            miner_move(key)
                            break
                        elif key[1] == "g":
                            goat_move(key)
                            break
                    else:
                        pass

        # Bruce
        # Game End
        if "wk" not in PIECES:
            pygame.draw.rect(SCREEN,(215,215,215),(0,0,400,400))
            display_text("Black wins!", (0,0,0),font)
        elif "bk" not in PIECES:
            pygame.draw.rect(SCREEN,(215,215,215),(0,0,400,400))
            display_text("White wins!", (0,0,0),font)
        
        pygame.display.flip()
        CLOCK.tick(60)
        
    pygame.quit()

if __name__ == "__main__":
    main()