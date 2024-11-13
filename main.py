import pygame
from pygame.locals import *
import sys
import csv
import random
import copy
import json
import asyncio


def card_use(c_list,yamafuda,using):
    randn = random.randrange(len(yamafuda))
    n = yamafuda.pop(randn)
    using.append(n)
    if len(yamafuda) == 0:
        l = list(range(len(c_list)))
        yamafuda = list(set(l) - set(using))
    return (n,yamafuda,using)






async def main():

    black = (0,0,0)
    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)
    white = (255,255,255)
    BG = (50,110,80)
    WIDTH = 800
    HEIGHT = 600
    FONTSIZE_TITLE = 50
    FONTSIZE_TOP = 30
    FONTSIZE_DEF = 20
    clock = pygame.time.Clock()

    fontname1 = '07あかずきんポップheavy'
    chara = []
    data = {}
    with open('config.json',encoding="utf-8") as f:
        d = json.load(f)
        target_max = int(d["target_score"]["max"])
        target_min = int(d["target_score"]["min"])
        player_names = d["players"]
        player_color = []
        for t in d["colors"]:

            player_color.append(tuple(t))

        for key,value in d["3size_data"].items():
            chara.append(key)
            data[key] = value
            data[key]["which"] = random.choice(["B","W","H"])
            




    #player_names = []
    #player_color = []





    c_list = copy.deepcopy(chara)

    using = []
    yamafuda = list(range(len(c_list)))
            



    pygame.init() #初期化
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("3size_game")
    allgame_running = True
    #player_names = ["キキョウ","ほわぁ","黎"]
    #player_color = [(166,100,160),(248,181,0),(216,28,47)]
    player_wins = [0,0,0]

    while allgame_running:

        

        using = []
        running1 = True
        while running1:
            clock.tick(60)
            await asyncio.sleep(0)
            
            #赤(255,0,0)
            screen.fill(BG)
            font1 = pygame.font.SysFont(fontname1, FONTSIZE_TITLE)
            text1 = font1.render("3サイズブラックジャック", True, black)
            text_rect = text1.get_rect(center=(WIDTH*(1/2), HEIGHT*(1/4)))
            screen.blit(text1, text_rect)
            font1 = pygame.font.SysFont(fontname1, FONTSIZE_TITLE)
            text1 = font1.render("Enterで次のゲームスタート", True, black)
            text_rect = text1.get_rect(center=(WIDTH*(1/2), HEIGHT*(2/4)))
            screen.blit(text1, text_rect)
            text1 = font1.render("現在の勝利点", True, black)
            text_rect = text1.get_rect(center=(WIDTH*(1/2), HEIGHT*(8/12)))
            screen.blit(text1, text_rect)
            for i in range(3):
                text1 = font1.render(f"{player_names[i]}", True, player_color[i])
                text_rect = text1.get_rect(center=(WIDTH*((1+i)/4), HEIGHT*(10/12)))
                screen.blit(text1, text_rect)
                text1 = font1.render(f"{player_wins[i]}勝", True, player_color[i])
                text_rect = text1.get_rect(center=(WIDTH*((1+i)/4), HEIGHT*(11/12)))
                screen.blit(text1, text_rect)

            pygame.display.update()
            
            # pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN:

                    if event.key == K_ESCAPE:   
                        running2 = False
                        pygame.quit()
                        sys.exit()
                    if event.key == K_RETURN:
                        running1 = False

        

        cards = []
        score = []
        for p in range(3):
            cards.append([])
            score.append([])
            for i in range(4):
                (n,yamafuda,using) = card_use(c_list,yamafuda,using)
                bwh = data[chara[n]]["which"]
                #print(n)
                cards[p].append([c_list[n],bwh])
                score[p].append(data[c_list[n]][bwh])
        
        targetscore = 400 + random.randrange(200)

        running2 = True

        player_skip = [0,0,0]
        
        start_p = random.randrange(3)
        player = start_p
        change_power = [1,1,1]
        change_running = False
        while running2:
            clock.tick(60)
            await asyncio.sleep(0)
            pygame.time.wait(30)
            screen.fill(BG)
            pygame.draw.rect(screen, white, (WIDTH*(1/36+player*(1/3)),HEIGHT*(7/36),WIDTH*(10/36),HEIGHT*(20/36)), 5)
            #赤(255,0,0)
            
            font = pygame.font.SysFont(fontname1, FONTSIZE_TOP)
            text = font.render(f"{targetscore}に近づけろ！超えたらアウト！", True, black)
            text_rect = text.get_rect(center=(WIDTH*(1/2), HEIGHT*(1/18)))
            screen.blit(text, text_rect)
            if change_power[player] == 1:
                text = font.render(f"Fでカード追加、Jで追加終了、CでBWHチェンジ", True, black)
            else:
                text = font.render(f"Fでカード追加、Jで追加終了", True, black)
            text_rect = text.get_rect(center=(WIDTH*(1/2), HEIGHT*(2/18)))
            screen.blit(text, text_rect)
            text = font.render(f"山札:{len(yamafuda)}枚", True, black)
            text_rect = text.get_rect(center=(WIDTH*(1/2), HEIGHT*(16/18)))
            screen.blit(text, text_rect)


            text = font.render(f"{player_names[player]}の番です", True, player_color[player])
            text_rect = text.get_rect(center=(WIDTH*(1/2), HEIGHT*(3/18)))
            screen.blit(text, text_rect)




            font = pygame.font.SysFont(fontname1, FONTSIZE_DEF)
            for p in range(3):
                text = font.render(f"{player_names[p]} {player_wins[p]}勝", True, player_color[p])
                text_rect = text.get_rect(center=(WIDTH*(1/6+p/3), HEIGHT*(4/18)))
                screen.blit(text, text_rect)
                for i in range(len(cards[p])):
                    text = font.render(f"{i+1}.{cards[p][i][0]}", True, black)
                    screen.blit(text, (WIDTH*(1/24+p/3),HEIGHT*(1/4)+i*FONTSIZE_DEF))
                    text = font.render(f"{cards[p][i][1]}", True, black)
                    screen.blit(text, (WIDTH*(11/48+p/3),HEIGHT*(1/4)+i*FONTSIZE_DEF))
                    if i<= 1:
                        text = font.render(f"{score[p][i]}", True, black)
                        screen.blit(text, (WIDTH*(25/96+p/3),HEIGHT*(1/4)+i*FONTSIZE_DEF))
                if player_skip[p] == 1:
                    text = font.render("追加終了", True, black)
                    screen.blit(text, (WIDTH*(4/24+p/3),HEIGHT*(1/4)+(i+1)*FONTSIZE_DEF))
                if change_power[p] == 1:
                    text = font.render("CP所持", True, black)
                    screen.blit(text, (WIDTH*(1/24+p/3),HEIGHT*(1/4)+(i+1)*FONTSIZE_DEF))
    
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:   
                        pygame.quit()
                        sys.exit()
                    if event.key == K_f:
                        (n,yamafuda,using) = card_use(c_list,yamafuda,using)
                        bwh = data[chara[n]]["which"]
                        #print(n)
                        cards[player].append([c_list[n],bwh])
                        score[player].append(data[c_list[n]][bwh])
                        if len(cards[player]) == 10:
                            player_skip[player] = 1
                        player = (player+1)%3
                    if event.key == K_c:
                        change_running = True
                        selecting = 0

                    if event.key == K_j:
                        player_skip[player] = 1
                        player = (player+1)%3
            if sum(player_skip) == 3:
                running2 = False
            else:
                while(player_skip[player]) == 1:
                    player = (player+1)%3
            
            while change_running:
                clock.tick(60)
                await asyncio.sleep(0)
                
                pygame.time.wait(30)
                screen.fill(BG)
                pygame.draw.rect(screen, white, (WIDTH*(1/36+player*(1/3)),HEIGHT*(7/36),WIDTH*(10/36),HEIGHT*(20/36)), 5)
                
                
                font = pygame.font.SysFont(fontname1, FONTSIZE_TOP)
                text = font.render(f"{targetscore}に近づけろ！超えたらアウト！", True, black)
                text_rect = text.get_rect(center=(WIDTH*(1/2), HEIGHT*(1/18)))
                screen.blit(text, text_rect)
                font = pygame.font.SysFont(fontname1, FONTSIZE_DEF)
                text = font.render(f"変えるキャラを↑↓で選ぶ", True, black)
                text_rect = text.get_rect(center=(WIDTH*(1/2), HEIGHT*(2/18)))
                screen.blit(text, text_rect)
                text = font.render(f"BWHのいずれかでチェンジ,Cでキャンセル", True, black)
                text_rect = text.get_rect(center=(WIDTH*(1/2), HEIGHT*(3/18)))
                screen.blit(text, text_rect)
                font = pygame.font.SysFont(fontname1, FONTSIZE_DEF)
                for p in range(3):
                    text = font.render(f"{player_names[p]} {player_wins[p]}勝", True, player_color[p])
                    text_rect = text.get_rect(center=(WIDTH*(1/6+p/3), HEIGHT*(4/18)))
                    screen.blit(text, text_rect)

                    for i in range(len(cards[p])):
                        if selecting == i and p == player:
                            text = font.render(f"→{i+1}.{cards[p][i][0]}", True, black)
                        else:
                            text = font.render(f"{i+1}.{cards[p][i][0]}", True, black)
                        screen.blit(text, (WIDTH*(1/24+p/3),HEIGHT*(1/4)+i*FONTSIZE_DEF))
                        text = font.render(f"{cards[p][i][1]}", True, black)
                        screen.blit(text, (WIDTH*(11/48+p/3),HEIGHT*(1/4)+i*FONTSIZE_DEF))
                        if i<= 1:
                            text = font.render(f"{score[p][i]}", True, black)
                            screen.blit(text, (WIDTH*(25/96+p/3),HEIGHT*(1/4)+i*FONTSIZE_DEF))
                    if player_skip[p] == 1:
                        text = font.render("追加終了", True, black)
                        screen.blit(text, (WIDTH*(4/24+p/3),HEIGHT*(1/4)+(i+1)*FONTSIZE_DEF))
                    if change_power[p] == 1:
                        text = font.render("CP所持", True, black)
                        screen.blit(text, (WIDTH*(1/24+p/3),HEIGHT*(1/4)+(i+1)*FONTSIZE_DEF))
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:   
                            pygame.quit()
                            sys.exit()
                        if event.key == K_UP:
                            if selecting != 0:
                                selecting -= 1
                        if event.key == K_DOWN:
                            if selecting != len(cards[player])-1:
                                selecting += 1


                        if event.key == K_c:
                            change_running = False

                        if event.key == K_b:
                            cards[player][selecting][1] = "B"
                            score[player][selecting] = data[cards[player][selecting][0]][cards[player][selecting][1]]
                            change_power[player] = 0
                            data[cards[player][selecting][0]]["which"] = "B"
                            change_running = False
                        if event.key == K_w:
                            cards[player][selecting][1] = "W"
                            score[player][selecting] = data[cards[player][selecting][0]][cards[player][selecting][1]]
                            change_power[player] = 0
                            data[cards[player][selecting][0]]["which"] = "W"
                            change_running = False
                        if event.key == K_h:
                            cards[player][selecting][1] = "H"
                            score[player][selecting] = data[cards[player][selecting][0]][cards[player][selecting][1]]
                            change_power[player] = 0
                            data[cards[player][selecting][0]]["which"] = "H"
                            change_running = False

        s = [0,0,0]
        lastscore = []
        for p in range(3):
            lastscore.append(sum(score[p]))
        for p in range(3):
            if lastscore[p] <= targetscore:
                s[p] = lastscore[p]
            else:
                s[p] = -lastscore[p]
        winscore = max(s)
        winner = []
        if winscore <0:
            winnertxt = "引き分け"
        else:
            for p in range(3):
                if s[p] == winscore:
                    winner.append(p)
            if len(winner) == 3:
                winnertxt = "引き分け"
            else:
                winners = []
                for p in range(3):
                    if p in winner:
                        winners.append(player_names[p])
                        player_wins[p] += 1
                winnertxt = "{}の勝ち".format(",".join(winners))
        if len(winner) == 1:
            winnercolor = player_color[winner[0]]
        else:
            winnercolor = black
        
                    
        running3 = True
        while running3:
            clock.tick(60)
            await asyncio.sleep(0)
            screen.fill(BG)
            font = pygame.font.SysFont(fontname1, FONTSIZE_TOP)
            text = font.render("最終結果", True, black)
            text_rect = text.get_rect(center=(WIDTH*(1/2), HEIGHT*(2/18)))
            screen.blit(text, text_rect)
            text = font.render(winnertxt, True, winnercolor)
            text_rect = text.get_rect(center=(WIDTH*(1/2), HEIGHT*(3/18)))
            screen.blit(text, text_rect)
            font = pygame.font.SysFont(fontname1, FONTSIZE_DEF)
            for p in range(3):
                text = font.render(f"{player_names[p]} {player_wins[p]}勝", True, player_color[p])
                text_rect = text.get_rect(center=(WIDTH*(1/6+p/3), HEIGHT*(4/18)))
                screen.blit(text, text_rect)
                for i in range(len(cards[p])):
                    text = font.render(f"{cards[p][i][0]}", True, black)
                    screen.blit(text, (WIDTH*(1/24+p/3),HEIGHT*(1/4)+i*FONTSIZE_DEF))
                    text = font.render(f"{cards[p][i][1]}", True, black)
                    screen.blit(text, (WIDTH*(11/48+p/3),HEIGHT*(1/4)+i*FONTSIZE_DEF))
                    text = font.render(f"{score[p][i]}", True, black)
                    screen.blit(text, (WIDTH*(25/96+p/3),HEIGHT*(1/4)+i*FONTSIZE_DEF))


            font = pygame.font.SysFont(fontname1, 15)
            text = font.render(f"目標スコア:{targetscore}", True, black)
            text_rect = text.get_rect(center=(WIDTH*(1/2), HEIGHT*(14/18)))
            screen.blit(text, text_rect)
            
            for p in range(3):
                text = font.render(f"{player_names[p]}のスコア:{lastscore[p]}点", True, player_color[p])
                text_rect = text.get_rect(center=(WIDTH*(p/3+1/6), HEIGHT*(15/18)))
                screen.blit(text, text_rect)
                if lastscore[p] < targetscore:
                    text = font.render(f"あと{targetscore-lastscore[p]}点！", True, black)
                    text_rect = text.get_rect(center=(WIDTH*(p/3+1/6), HEIGHT*(16/18)))
                    screen.blit(text, text_rect)
                elif lastscore[p] == targetscore:
                    
                    text = font.render(f"完璧！", True, black)
                    text_rect = text.get_rect(center=(WIDTH*(p/3+1/6), HEIGHT*(16/18)))
                    screen.blit(text, text_rect)
                else:
                    
                    text = font.render(f"ざこが 出直して来い", True, red)
                    text_rect = text.get_rect(center=(WIDTH*(p/3+1/6), HEIGHT*(16/18)))
                    screen.blit(text, text_rect)
            font = pygame.font.SysFont(fontname1, FONTSIZE_TOP)
            text = font.render("Enterで次のゲーム準備", True, black)
            text_rect = text.get_rect(center=(WIDTH*(1/2), HEIGHT*(17/18)))
            screen.blit(text, text_rect)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN:

                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == K_RETURN:
                        running3 = False









if __name__ == "__main__":
    #print(pygame.font.get_fonts())
    main()