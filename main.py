import pygame
from pygame.locals import *
import random
import copy
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
    pygame.init() #初期化

    #colors
    black = (0,0,0)
    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)
    white = (255,255,255)
    BG = (50,110,80) #background

    WIDTH = 800
    HEIGHT = 600
    FONTSIZE_TITLE = 50
    FONTSIZE_TOP = 30
    FONTSIZE_DEF = 20
    FONT_FILE = "AkazukiPOP.otf"

    font_title = pygame.font.Font(FONT_FILE, FONTSIZE_TITLE)
    font_top = pygame.font.Font(FONT_FILE, FONTSIZE_TOP)
    font_def = pygame.font.Font(FONT_FILE, FONTSIZE_DEF)

    clock = pygame.time.Clock()

    
    chara = []
    data = {}
    
    d = {
    "players": [
        "Player1",
        "Player2",
        "Player3"
    ],
    "colors": [
        [
        50,
        50,
        200
        ],
        [
        250,
        50,
        50
        ],
        [
        250,
        230,
        50
        ]
    ],
    "target_score": {
        "max": 600,
        "min": 400
    },
    "3size_data": {
        "高坂穂乃果": {
        "B": 78,
        "W": 58,
        "H": 82
        },
        "絢瀬絵里": {
        "B": 88,
        "W": 60,
        "H": 84
        },
        "南ことり": {
        "B": 80,
        "W": 58,
        "H": 80
        },
        "園田海未": {
        "B": 76,
        "W": 58,
        "H": 80
        },
        "星空凛": {
        "B": 75,
        "W": 59,
        "H": 80
        },
        "西木野真姫": {
        "B": 78,
        "W": 56,
        "H": 83
        },
        "東條希": {
        "B": 90,
        "W": 60,
        "H": 82
        },
        "小泉花陽": {
        "B": 82,
        "W": 60,
        "H": 83
        },
        "矢澤にこ": {
        "B": 74,
        "W": 57,
        "H": 79
        },
        "高海千歌": {
        "B": 82,
        "W": 59,
        "H": 83
        },
        "桜内梨子": {
        "B": 80,
        "W": 58,
        "H": 82
        },
        "松浦果南": {
        "B": 83,
        "W": 58,
        "H": 84
        },
        "黒澤ﾀﾞｲﾔ": {
        "B": 80,
        "W": 57,
        "H": 80
        },
        "渡辺曜": {
        "B": 82,
        "W": 57,
        "H": 81
        },
        "津島善子": {
        "B": 79,
        "W": 58,
        "H": 80
        },
        "国木田花丸": {
        "B": 83,
        "W": 57,
        "H": 83
        },
        "小原鞠莉": {
        "B": 87,
        "W": 60,
        "H": 84
        },
        "黒澤ﾙﾋﾞｨ": {
        "B": 76,
        "W": 56,
        "H": 79
        },
        "上原歩夢": {
        "B": 82,
        "W": 58,
        "H": 84
        },
        "中須かすみ": {
        "B": 76,
        "W": 55,
        "H": 79
        },
        "桜坂しずく": {
        "B": 80,
        "W": 58,
        "H": 83
        },
        "朝香果林": {
        "B": 88,
        "W": 57,
        "H": 89
        },
        "宮下愛": {
        "B": 84,
        "W": 53,
        "H": 86
        },
        "近江彼方": {
        "B": 85,
        "W": 60,
        "H": 86
        },
        "優木せつ菜": {
        "B": 83,
        "W": 56,
        "H": 81
        },
        "ｴﾏ･ｳﾞｪﾙﾃﾞ": {
        "B": 92,
        "W": 61,
        "H": 88
        },
        "天王寺璃奈": {
        "B": 71,
        "W": 52,
        "H": 75
        },
        "三船栞子": {
        "B": 79,
        "W": 56,
        "H": 78
        },
        "鐘嵐珠": {
        "B": 87,
        "W": 55,
        "H": 82
        },
        "ﾐｱ･ﾃｲﾗｰ": {
        "B": 80,
        "W": 55,
        "H": 80
        },
        "鹿角聖良": {
        "B": 85,
        "W": 59,
        "H": 84
        },
        "鹿角理亞": {
        "B": 79,
        "W": 56,
        "H": 81
        }
    }
    }

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
            
    c_list = copy.deepcopy(chara)

    using = []
    yamafuda = list(range(len(c_list))) #山札

    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("3size_game")
    allgame_running = True
    player_wins = [0,0,0] #playerの勝利数

    while allgame_running:

        using = []
        running1 = True
        while running1:
            clock.tick(60)
            await asyncio.sleep(0)
            
            #赤(255,0,0)
            screen.fill(BG)
            
            text1 = font_title.render("3サイズブラックジャック", True, black)
            text_rect = text1.get_rect(center=(WIDTH*(1/2), HEIGHT*(1/4)))
            screen.blit(text1, text_rect)
            
            text1 = font_title.render("Enterで次のゲームスタート", True, black)
            text_rect = text1.get_rect(center=(WIDTH*(1/2), HEIGHT*(2/4)))
            screen.blit(text1, text_rect)
            text1 = font_title.render("現在の勝利点", True, black)
            text_rect = text1.get_rect(center=(WIDTH*(1/2), HEIGHT*(8/12)))
            screen.blit(text1, text_rect)
            for i in range(3):
                text1 = font_title.render(f"{player_names[i]}", True, player_color[i])
                text_rect = text1.get_rect(center=(WIDTH*((1+i)/4), HEIGHT*(10/12)))
                screen.blit(text1, text_rect)
                text1 = font_title.render(f"{player_wins[i]}勝", True, player_color[i])
                text_rect = text1.get_rect(center=(WIDTH*((1+i)/4), HEIGHT*(11/12)))
                screen.blit(text1, text_rect)

            pygame.display.update()
            
            # pygame.display.update()
            for event in pygame.event.get():
                if event.type == KEYDOWN:
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
        
        targetscore = target_min + random.randrange(target_max-target_min)

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
            
            
            text = font_top.render(f"{targetscore}に近づけろ！超えたらアウト！", True, black)
            text_rect = text.get_rect(center=(WIDTH*(1/2), HEIGHT*(1/18)))
            screen.blit(text, text_rect)
            if change_power[player] == 1:
                text = font_top.render(f"Fでカード追加、Jで追加終了、CでBWHチェンジ", True, black)
            else:
                text = font_top.render(f"Fでカード追加、Jで追加終了", True, black)
            text_rect = text.get_rect(center=(WIDTH*(1/2), HEIGHT*(2/18)))
            screen.blit(text, text_rect)
            text = font_top.render(f"山札:{len(yamafuda)}枚", True, black)
            text_rect = text.get_rect(center=(WIDTH*(1/2), HEIGHT*(16/18)))
            screen.blit(text, text_rect)


            text = font_top.render(f"{player_names[player]}の番です", True, player_color[player])
            text_rect = text.get_rect(center=(WIDTH*(1/2), HEIGHT*(3/18)))
            screen.blit(text, text_rect)




            
            for p in range(3):
                text = font_def.render(f"{player_names[p]} {player_wins[p]}勝", True, player_color[p])
                text_rect = text.get_rect(center=(WIDTH*(1/6+p/3), HEIGHT*(4/18)))
                screen.blit(text, text_rect)
                for i in range(len(cards[p])):
                    text = font_def.render(f"{i+1}.{cards[p][i][0]}", True, black)
                    screen.blit(text, (WIDTH*(1/24+p/3),HEIGHT*(1/4)+i*FONTSIZE_DEF))
                    text = font_def.render(f"{cards[p][i][1]}", True, black)
                    screen.blit(text, (WIDTH*(11/48+p/3),HEIGHT*(1/4)+i*FONTSIZE_DEF))
                    if i<= 1:
                        text = font_def.render(f"{score[p][i]}", True, black)
                        screen.blit(text, (WIDTH*(25/96+p/3),HEIGHT*(1/4)+i*FONTSIZE_DEF))
                if player_skip[p] == 1:
                    text = font_def.render("追加終了", True, black)
                    screen.blit(text, (WIDTH*(4/24+p/3),HEIGHT*(1/4)+(i+1)*FONTSIZE_DEF))
                if change_power[p] == 1:
                    text = font_def.render("CP所持", True, black)
                    screen.blit(text, (WIDTH*(1/24+p/3),HEIGHT*(1/4)+(i+1)*FONTSIZE_DEF))
    
            pygame.display.update()

            for event in pygame.event.get():

                if event.type == KEYDOWN:

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
                
                

                text = font_top.render(f"{targetscore}に近づけろ！超えたらアウト！", True, black)
                text_rect = text.get_rect(center=(WIDTH*(1/2), HEIGHT*(1/18)))
                screen.blit(text, text_rect)

                text = font_def.render(f"変えるキャラを↑↓で選ぶ", True, black)
                text_rect = text.get_rect(center=(WIDTH*(1/2), HEIGHT*(2/18)))
                screen.blit(text, text_rect)
                text = font_def.render(f"BWHのいずれかでチェンジ,Cでキャンセル", True, black)
                text_rect = text.get_rect(center=(WIDTH*(1/2), HEIGHT*(3/18)))
                screen.blit(text, text_rect)

                for p in range(3):
                    text = font_def.render(f"{player_names[p]} {player_wins[p]}勝", True, player_color[p])
                    text_rect = text.get_rect(center=(WIDTH*(1/6+p/3), HEIGHT*(4/18)))
                    screen.blit(text, text_rect)

                    for i in range(len(cards[p])):
                        if selecting == i and p == player:
                            text = font_def.render(f"→{i+1}.{cards[p][i][0]}", True, black)
                        else:
                            text = font_def.render(f"{i+1}.{cards[p][i][0]}", True, black)
                        screen.blit(text, (WIDTH*(1/24+p/3),HEIGHT*(1/4)+i*FONTSIZE_DEF))
                        text = font_def.render(f"{cards[p][i][1]}", True, black)
                        screen.blit(text, (WIDTH*(11/48+p/3),HEIGHT*(1/4)+i*FONTSIZE_DEF))
                        if i<= 1:
                            text = font_def.render(f"{score[p][i]}", True, black)
                            screen.blit(text, (WIDTH*(25/96+p/3),HEIGHT*(1/4)+i*FONTSIZE_DEF))
                    if player_skip[p] == 1:
                        text = font_def.render("追加終了", True, black)
                        screen.blit(text, (WIDTH*(4/24+p/3),HEIGHT*(1/4)+(i+1)*FONTSIZE_DEF))
                    if change_power[p] == 1:
                        text = font_def.render("CP所持", True, black)
                        screen.blit(text, (WIDTH*(1/24+p/3),HEIGHT*(1/4)+(i+1)*FONTSIZE_DEF))
                pygame.display.update()
                for event in pygame.event.get():


                    if event.type == KEYDOWN:

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
            
            text = font_top.render("最終結果", True, black)
            text_rect = text.get_rect(center=(WIDTH*(1/2), HEIGHT*(2/18)))
            screen.blit(text, text_rect)
            text = font_top.render(winnertxt, True, winnercolor)
            text_rect = text.get_rect(center=(WIDTH*(1/2), HEIGHT*(3/18)))
            screen.blit(text, text_rect)
            for p in range(3):
                text = font_def.render(f"{player_names[p]} {player_wins[p]}勝", True, player_color[p])
                text_rect = text.get_rect(center=(WIDTH*(1/6+p/3), HEIGHT*(4/18)))
                screen.blit(text, text_rect)
                for i in range(len(cards[p])):
                    text = font_def.render(f"{cards[p][i][0]}", True, black)
                    screen.blit(text, (WIDTH*(1/24+p/3),HEIGHT*(1/4)+i*FONTSIZE_DEF))
                    text = font_def.render(f"{cards[p][i][1]}", True, black)
                    screen.blit(text, (WIDTH*(11/48+p/3),HEIGHT*(1/4)+i*FONTSIZE_DEF))
                    text = font_def.render(f"{score[p][i]}", True, black)
                    screen.blit(text, (WIDTH*(25/96+p/3),HEIGHT*(1/4)+i*FONTSIZE_DEF))


            
            text = font_top.render(f"目標スコア:{targetscore}", True, black)
            text_rect = text.get_rect(center=(WIDTH*(1/2), HEIGHT*(14/18)))
            screen.blit(text, text_rect)
            
            for p in range(3):
                text = font_def.render(f"{player_names[p]}のスコア:{lastscore[p]}点", True, player_color[p])
                text_rect = text.get_rect(center=(WIDTH*(p/3+1/6), HEIGHT*(15/18)))
                screen.blit(text, text_rect)
                if lastscore[p] < targetscore:
                    text = font_def.render(f"あと{targetscore-lastscore[p]}点！", True, black)
                    text_rect = text.get_rect(center=(WIDTH*(p/3+1/6), HEIGHT*(16/18)))
                    screen.blit(text, text_rect)
                elif lastscore[p] == targetscore:
                    
                    text = font_def.render(f"完璧！", True, black)
                    text_rect = text.get_rect(center=(WIDTH*(p/3+1/6), HEIGHT*(16/18)))
                    screen.blit(text, text_rect)
                else:
                    
                    text = font_def.render(f"ざこが 出直して来い", True, red)
                    text_rect = text.get_rect(center=(WIDTH*(p/3+1/6), HEIGHT*(16/18)))
                    screen.blit(text, text_rect)
            text = font_top.render("Enterで次のゲーム準備", True, black)
            text_rect = text.get_rect(center=(WIDTH*(1/2), HEIGHT*(17/18)))
            screen.blit(text, text_rect)
            pygame.display.update()
            for event in pygame.event.get():


                if event.type == KEYDOWN:

                    if event.key == K_RETURN:
                        running3 = False









if __name__ == "__main__":

    print("asyncio.run(main())")
    asyncio.run(main())