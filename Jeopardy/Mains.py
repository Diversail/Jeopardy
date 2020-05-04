import random,pygame,time
xb=500
yb=500
black = (0, 0, 0)
white = (255, 255, 255)
er=0
pygame.init()
pygame.mixer.init()
pygame.display.set_icon(pygame.image.load('/home/pi/Jeopardy/Images/Icon1.png'))
pygame.display.set_caption('Jeopardy')
screen=pygame.display.set_mode([xb,yb])
Icon1=pygame.image.load('/home/pi/Jeopardy/Images/Icon1.png')
Icon2=pygame.image.load('/home/pi/Jeopardy/Images/Icon1.png')
Icon3=pygame.image.load('/home/pi/Jeopardy/Images/Icon1.png')
Loading=pygame.image.load('/home/pi/Jeopardy/Images/Loading.png')
j100=pygame.image.load('/home/pi/Jeopardy/Images/100.png')
j200=pygame.image.load('/home/pi/Jeopardy/Images/200.png')
j300=pygame.image.load('/home/pi/Jeopardy/Images/300.png')
j400=pygame.image.load('/home/pi/Jeopardy/Images/400.png')
j500=pygame.image.load('/home/pi/Jeopardy/Images/500.png')
j600=pygame.image.load('/home/pi/Jeopardy/Images/600.png')
j800=pygame.image.load('/home/pi/Jeopardy/Images/800.png')
j1000=pygame.image.load('/home/pi/Jeopardy/Images/1000.png')
W1=pygame.image.load('/home/pi/Jeopardy/Images/W1.png')
W2=pygame.image.load('/home/pi/Jeopardy/Images/W2.png')
W3=pygame.image.load('/home/pi/Jeopardy/Images/W3.png')
W4=pygame.image.load('/home/pi/Jeopardy/Images/W4.png')
W5=pygame.image.load('/home/pi/Jeopardy/Images/W5.png')
W6=pygame.image.load('/home/pi/Jeopardy/Images/W6.png')
W7=pygame.image.load('/home/pi/Jeopardy/Images/W7.png')
W8=pygame.image.load('/home/pi/Jeopardy/Images/W8.png')
W9=pygame.image.load('/home/pi/Jeopardy/Images/W9.png')
W10=pygame.image.load('/home/pi/Jeopardy/Images/W10.png')
W11=pygame.image.load('/home/pi/Jeopardy/Images/W11.png')
W12=pygame.image.load('/home/pi/Jeopardy/Images/W12.png')
W13=pygame.image.load('/home/pi/Jeopardy/Images/W13.png')
W14=pygame.image.load('/home/pi/Jeopardy/Images/W14.png')
W15=pygame.image.load('/home/pi/Jeopardy/Images/W15.png')
W16=pygame.image.load('/home/pi/Jeopardy/Images/W16.png')
W17=pygame.image.load('/home/pi/Jeopardy/Images/W17.png')
W18=pygame.image.load('/home/pi/Jeopardy/Images/W18.png')
W19=pygame.image.load('/home/pi/Jeopardy/Images/W19.png')
W20=pygame.image.load('/home/pi/Jeopardy/Images/W20.png')
W21=pygame.image.load('/home/pi/Jeopardy/Images/W21.png')
W22=pygame.image.load('/home/pi/Jeopardy/Images/W22.png')
W23=pygame.image.load('/home/pi/Jeopardy/Images/W23.png')
W24=pygame.image.load('/home/pi/Jeopardy/Images/W24.png')
W25=pygame.image.load('/home/pi/Jeopardy/Images/W25.png')
W26=pygame.image.load('/home/pi/Jeopardy/Images/W26.png')
W27=pygame.image.load('/home/pi/Jeopardy/Images/W27.png')
W28=pygame.image.load('/home/pi/Jeopardy/Images/W28.png')
W29=pygame.image.load('/home/pi/Jeopardy/Images/W29.png')
W30=pygame.image.load('/home/pi/Jeopardy/Images/W30.png')
W31=pygame.image.load('/home/pi/Jeopardy/Images/W31.png')
W32=pygame.image.load('/home/pi/Jeopardy/Images/W32.png')
W33=pygame.image.load('/home/pi/Jeopardy/Images/W33.png')
W34=pygame.image.load('/home/pi/Jeopardy/Images/W34.png')
W35=pygame.image.load('/home/pi/Jeopardy/Images/W35.png')
W36=pygame.image.load('/home/pi/Jeopardy/Images/W36.png')
W37=pygame.image.load('/home/pi/Jeopardy/Images/W37.png')
W38=pygame.image.load('/home/pi/Jeopardy/Images/W38.png')
W39=pygame.image.load('/home/pi/Jeopardy/Images/W39.png')
W40=pygame.image.load('/home/pi/Jeopardy/Images/W40.png')
W41=pygame.image.load('/home/pi/Jeopardy/Images/W41.png')
W42=pygame.image.load('/home/pi/Jeopardy/Images/W42.png')
W43=pygame.image.load('/home/pi/Jeopardy/Images/W43.png')
W44=pygame.image.load('/home/pi/Jeopardy/Images/W44.png')
W45=pygame.image.load('/home/pi/Jeopardy/Images/W45.png')
W46=pygame.image.load('/home/pi/Jeopardy/Images/W46.png')
W47=pygame.image.load('/home/pi/Jeopardy/Images/W47.png')
W48=pygame.image.load('/home/pi/Jeopardy/Images/W48.png')
W49=pygame.image.load('/home/pi/Jeopardy/Images/W49.png')
W50=pygame.image.load('/home/pi/Jeopardy/Images/W50.png')
W51=pygame.image.load('/home/pi/Jeopardy/Images/W51.png')
W52=pygame.image.load('/home/pi/Jeopardy/Images/W52.png')
W53=pygame.image.load('/home/pi/Jeopardy/Images/W53.png')
W54=pygame.image.load('/home/pi/Jeopardy/Images/W54.png')
W55=pygame.image.load('/home/pi/Jeopardy/Images/W55.png')
W56=pygame.image.load('/home/pi/Jeopardy/Images/W56.png')
W57=pygame.image.load('/home/pi/Jeopardy/Images/W57.png')
W58=pygame.image.load('/home/pi/Jeopardy/Images/W58.png')
W59=pygame.image.load('/home/pi/Jeopardy/Images/W59.png')
W60=pygame.image.load('/home/pi/Jeopardy/Images/W60.png')
W61=pygame.image.load('/home/pi/Jeopardy/Images/W61.png')
#W62=pygame.image.load('/home/pi/Jeopardy/Images/W62.png')
W63=pygame.image.load('/home/pi/Jeopardy/Images/W63.png')
W64=pygame.image.load('/home/pi/Jeopardy/Images/W64.png')
W65=pygame.image.load('/home/pi/Jeopardy/Images/W65.png')
W66=pygame.image.load('/home/pi/Jeopardy/Images/W66.png')
W67=pygame.image.load('/home/pi/Jeopardy/Images/W67.png')
W68=pygame.image.load('/home/pi/Jeopardy/Images/W68.png')
W69=pygame.image.load('/home/pi/Jeopardy/Images/W69.png')
W70=pygame.image.load('/home/pi/Jeopardy/Images/W70.png')
W71=pygame.image.load('/home/pi/Jeopardy/Images/W71.png')
W72=pygame.image.load('/home/pi/Jeopardy/Images/W72.png')
W73=pygame.image.load('/home/pi/Jeopardy/Images/W73.png')
W74=pygame.image.load('/home/pi/Jeopardy/Images/W74.png')
W75=pygame.image.load('/home/pi/Jeopardy/Images/W75.png')
xstripe=pygame.image.load('/home/pi/Jeopardy/Images/x.png')
screen.fill(black)
screen.blit(Loading,(300,300))
white=0
#g= open("test","w+")
teams=[]
points=[]
W=[W1,W2,W3,W4,W5,W6,W7,W8,W9,W10,W11,W12,W13,W14,W15,W16,W17,W18,W19,W20,W21,\
   W22,W23,W24,W25,W26,W27,W28,W29,W30,W31,W32,W33,W34,W35,W36,W37,W38,W39,W40,\
   W41,W42,W43,W44,W45,W46,W47,W48,W49,W50,W51,W52,W53,W54,W55,W56,W57,W58,W59,\
   W60,W61,W63,W64,W65,W66,W67,W68,W69,W70,W71,W72,W73,W74,W75]
'''def team1(x):
    teams1.append(x)
def team2(x):
    teams2.append(x)
def name(x):
    team1name=x'''
area=0
k=0
ct=0
c=0
def Questions():
    global ac, c, ct, area
    if c==1:
        print('First Category')
        if ct==1:
            print('100')
        if ct==2:
            print('200')
        if ct==3:
            print('300')
        if ct==4:
            print('400')
        if ct==5:
            print('500')
    if c==2:
        print('Second Category')
        if ct==6:
            print('100')
        if ct==7:
            print('200')
        if ct==8:
            print('300')
        if ct==9:
            print('400')
        if ct==10:
            print('500')
    if c==3:
        print('Third Category')
        if ct==11:
            print('100')
        if ct==12:
            print('200')
        if ct==13:
            print('300')
        if ct==14:
            print('400')
        if ct==15:
            print('500')
    if c==4:
        print('Fourth Category')
        if ct==16:
            print('100')
        if ct==17:
            print('200')
        if ct==18:
            print('300')
        if ct==19:
            print('400')
        if ct==20:
            print('500')
    if c==5:
        print('Fifth Category')
        if ct==21:
            print('100')
        if ct==22:
            print('200')
        if ct==23:
            print('300')
        if ct==24:
            print('400')
        if ct==25:
            print('500')
    ct=0
    with open(ac) as f:
        data=f.readlines()
        print(data[5])
def video():
    global k,ct
    screen.fill(black)
    if area==0:
        screen.blit(j100,(0,60))
        screen.blit(j100,(100,60))
        screen.blit(j100,(200,60))
        screen.blit(j100,(300,60))
        screen.blit(j100,(400,60))
        screen.blit(j200,(0,120))
        screen.blit(j200,(100,120))
        screen.blit(j200,(200,120))
        screen.blit(j200,(300,120))
        screen.blit(j200,(400,120))
        screen.blit(j300,(0,180))
        screen.blit(j300,(100,180))
        screen.blit(j300,(200,180))
        screen.blit(j300,(300,180))
        screen.blit(j300,(400,180))
        screen.blit(j400,(0,240))
        screen.blit(j400,(100,240))
        screen.blit(j400,(200,240))
        screen.blit(j400,(300,240))
        screen.blit(j400,(400,240))
        screen.blit(j500,(0,300))
        screen.blit(j500,(100,300))
        screen.blit(j500,(200,300))
        screen.blit(j500,(300,300))
        screen.blit(j500,(400,300))
    if area==1:
        screen.blit(j200,(0,60))
        screen.blit(j200,(100,60))
        screen.blit(j200,(200,60))
        screen.blit(j200,(300,60))
        screen.blit(j200,(400,60))
        screen.blit(j400,(0,120))
        screen.blit(j400,(100,120))
        screen.blit(j400,(200,120))
        screen.blit(j400,(300,120))
        screen.blit(j400,(400,120))
        screen.blit(j600,(0,180))
        screen.blit(j600,(100,180))
        screen.blit(j600,(200,180))
        screen.blit(j600,(300,180))
        screen.blit(j600,(400,180))
        screen.blit(j800,(0,240))
        screen.blit(j800,(100,240))
        screen.blit(j800,(200,240))
        screen.blit(j800,(300,240))
        screen.blit(j800,(400,240))
        screen.blit(j1000,(0,300))
        screen.blit(j1000,(100,300))
        screen.blit(j1000,(200,300))
        screen.blit(j1000,(300,300))
        screen.blit(j1000,(400,300))
    if area==2:
        print('Final Round')
    print(ct)
    if ct>0:
        for x in range(0,len(W)):
            #print(x)
            screen.blit(W[x],(0,0))
            update()
        Questions()
    update()
def scoring():
    global teams
    for x in range(0,len(teams)):
        print('%s has %s points'% (teams[x],points[x]))
def loading():
    update()
    global er,ac
    ac='/home/pi/Jeopardy/text/test'
    b1='/home/pi/Jeopardy/text/test'
    b2='/home/pi/Jeopardy/text/test'
    b3='/home/pi/Jeopardy/text/test'
    b4='/home/pi/Jeopardy/text/test'
    b5='/home/pi/Jeopardy/text/test'
    b6='/home/pi/Jeopardy/text/test'
    b7='/home/pi/Jeopardy/text/test'
    b8='/home/pi/Jeopardy/text/test'
    b9='/home/pi/Jeopardy/text/test'
    b10='/home/pi/Jeopardy/text/test'
    lc1q=sum(1 for line in open(ac))
    lc1a=sum(1 for line in open(ac))
    lc2q=sum(1 for line in open(ac))
    lc2a=sum(1 for line in open(ac))
    lc3q=sum(1 for line in open(ac))
    lc3a=sum(1 for line in open(ac))
    lc4q=sum(1 for line in open(ac))
    lc4a=sum(1 for line in open(ac))
    lc5q=sum(1 for line in open(ac))
    lc5a=sum(1 for line in open(ac))
    lc6q=sum(1 for line in open(ac))
    lc6a=sum(1 for line in open(ac))
    if lc1q!=lc1a:
        print('Error for cat 1')
        er+=1
    if lc2q!=lc2a:
        print('Error for cat 2')
        er+=1
    if lc3q!=lc3a:
        print('Error for cat 3')
        er+=1
    if lc4q!=lc4a:
        print('Error for cat 4')
        er+=1
    if lc5q!=lc5a:
        print('Error for cat 5')
        er+=1
    if lc6q!=lc6a:
        print('Error for cat 6')
        er+=1
    Theme=pygame.mixer.music.load('/home/pi/Jeopardy/Music/Theme.mp3')
    Win=pygame.mixer.music.load('/home/pi/Jeopardy/Music/Win.mp3')
    Lose=pygame.mixer.music.load('/home/pi/Jeopardy/Music/Lose.mp3')
    print('All files loaded, there were %s errors.'% er)
    Main()
def Main():
    global dd,k,c,ct
    p=0
    print('Welcome to Jeopardy!')
    print('Again there were %s errors.'% er)
    while p==0:
        teams.append(input('Add player names '))
        dd=input('Anymore? Enter no to quit ')
        if dd=='no':
            print('The players are %s'% teams)
            ee=input('Are you sure you want to exit the player appending? ')
            if ee=='yes' or ee=='y':
                p=1
            else:
                continue
        else:
            continue
        for x in range(0,len(teams)):
            points.append(0)
        scoring()
    print('Okay, we have %s as our players.'% teams)
    video()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            k=0
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                mousex, mousey = pygame.mouse.get_pos()
                print(mousex)
                print(mousey)
                '''if 100>mousex>0 and 120>mousey>60:
                    k=1
                if 100>mousex>0 and 180>mousey>120:
                    k=1
                if 100>mousex>0 and 240>mousey>180:
                    k=1
                if 100>mousex>0 and 300>mousey>240:
                    k=1
                if 100>mousex>0 and 360>mousey>300:
                    k=1'''
                if 100>mousex>0:
                    print('First Column')
                    c=1
                    #k=1
                    if 120>mousey>60:
                        ct=1
                    if 180>mousey>120:
                        ct=2
                    if 240>mousey>180:
                        ct=3
                    if 300>mousey>240:
                        ct=4
                    if 360>mousey>300:
                        ct=5
                    print(ct)
                if 200>mousex>100:
                    print('Second Column')
                    c=2
                    #k=1
                    if 120>mousey>60:
                        ct=6
                    if 180>mousey>120:
                        ct=7
                    if 240>mousey>180:
                        ct=8
                    if 300>mousey>240:
                        ct=9
                    if 360>mousey>300:
                        ct=10
                if 300>mousex>200:
                    print('Third Column')
                    c=3
                    #k=1
                    if 120>mousey>60:
                        ct=11
                    if 180>mousey>120:
                        ct=12
                    if 240>mousey>180:
                        ct=13
                    if 300>mousey>240:
                        ct=14
                    if 360>mousey>300:
                        ct=15
                if 400>mousex>300:
                    print('Fourth Column')
                    c=4
                    #k=1
                    if 120>mousey>60:
                        ct=16
                    if 180>mousey>120:
                        ct=17
                    if 240>mousey>180:
                        ct=18
                    if 300>mousey>240:
                        ct=19
                    if 360>mousey>300:
                        ct=20
                if 500>mousex>400:
                    print('Fifth Column')
                    c=5
                    #k=1
                    if 120>mousey>60:
                        ct=21
                    if 180>mousey>120:
                        ct=22
                    if 240>mousey>180:
                        ct=23
                    if 300>mousey>240:
                        ct=24
                    if 360>mousey>300:
                        ct=25
                '''if 200>mousex>100 and 120>mousey>60:
                    k=1
                if 200>mousex>100 and 180>mousey>120:
                    k=1
                if 200>mousex>100 and 240>mousey>180:
                    k=1
                if 200>mousex>100 and 300>mousey>240:
                    k=1
                if 200>mousex>100 and 360>mousey>300:
                    k=1
                if 300>mousex>200 and 120>mousey>60:
                    k=1
                if 300>mousex>200 and 180>mousey>120:
                    k=1
                if 300>mousex>200 and 240>mousey>180:
                    k=1
                if 300>mousex>200 and 300>mousey>240:
                    k=1
                if 300>mousex>200 and 360>mousey>300:
                    k=1
                if 400>mousex>300 and 120>mousey>60:
                    k=1
                if 400>mousex>300 and 180>mousey>120:
                    k=1
                if 400>mousex>300 and 240>mousey>180:
                    k=1
                if 400>mousex>300 and 300>mousey>240:
                    k=1
                if 400>mousex>300 and 360>mousey>300:
                    k=1
                if 500>mousex>400 and 120>mousey>60:
                    k=1
                if 500>mousex>400 and 180>mousey>120:
                    k=1
                if 500>mousex>400 and 240>mousey>180:
                    k=1
                if 500>mousex>400 and 300>mousey>240:
                    k=1
                if 500>mousex>400 and 360>mousey>300:
                    k=1'''
                video()
                #if j200.get_rect().collidepoint(pygame.mouse.get_pos()):
                #print("mouse is over 'newGameButton'")
def delay(x):
    pygame.time.delay(x)
def update():
    pygame.display.update()
loading()
#screen.blit(Icon1 ,(0,0))
#screen.blit(Icon2 ,(40,0))
#screen.blit(Icon3 ,(80,0))
update()   
