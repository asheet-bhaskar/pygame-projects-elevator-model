import pygame,sys,time
pygame.init()


width=800
height=700
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Elevator model")
screen.fill((200,200,200))
class canvas():
    def __init__(self):                     # drawing lines and writing floor number.
        
        pygame.draw.line(screen,(0,0,0),(10,0),(10,700),2)
        pygame.draw.line(screen,(0,0,0),(70,0),(70,700),2)
        pygame.draw.line(screen,(0,0,0),(110,0),(110,700),2)
        pygame.draw.line(screen,(0,0,0),(170,0),(170,700),2)
        pygame.draw.line(screen,(0,0,0),(210,0),(210,700),2)
        pygame.draw.line(screen,(0,0,0),(270,0),(270,700),2)
        pygame.draw.line(screen,(0,0,0),(310,0),(310,700),2)
        pygame.draw.line(screen,(0,0,0),(370,0),(370,700),2)
        
        i=0
        y=70
        while i<10:
            j=0
            x=10
            i+=1
            while j<4:
                pygame.draw.line(screen,(0,0,0),(x,y),(x+60,y),2)
                j+=1
                x+=100
            font  = pygame.font.Font(None , 30)
            s= str(11-i)
            text = font.render(s,1,(250,0,0))
            screen.blit(text, (x-35,y-50))
            y+=70

class button():
    def __init__(self,n):
        self.n=n
        i=0
        y=20
        x=410
        up=pygame.image.load('up.jpg')
        down=pygame.image.load('down.jpg')
        while(i<self.n):
            screen.blit(up,(x,y))
            pygame.draw.rect(screen,(250,0,0),(x,y,32,32),2)
            screen.blit(down,(x+35,y))
            pygame.draw.rect(screen,(250,0,0),(x+35,y,32,32),2)
            i+=1
            y+=70
    def pressed(self,my):# y co-ordinates given to it, then it will return at which floor button is presed is pressed.
        if my>=20 and my<=51:
            return (10)
        elif my>=90 and my<=121:
            return (9)
        elif my>=160 and my<=191:
            return (8)
        elif my>=230 and my<=261:
            return (7)
        elif my>=300 and my<=331:
            return (6)
        elif my>=370 and my<=401:
            return (5)
        elif my>=440 and my<=471:
            return (4)
        elif my>=510 and my<=541:
            return (3)
        elif my>=580 and my<=611:
            return (2)
        elif my>=650 and my<=681:
            return (1)
        


  

class elevator():
    def __init__(self,no,by,x,y=632):              #no-> number of elevator (eg. 1,2,3,4,)
        self.y=y                                   #x->  x co-rdinate of elevator
        self.x=x                                   #y->  vertical position of elevator, initially at ground floor()
        self.no=no                                 #by->  vertical position of displaying board.used in ele_pos()
        self.by=by
    def show_elev(self,v_pos):
        self.v_pos=v_pos
        img=pygame.image.load('ele.jpg')
        imgx=self.x
        imgy=self.v_pos
        screen.blit(img,(imgx,imgy))
        font  = pygame.font.Font(None , 50)
        s= str(self.no)
        text = font.render(s,1,(250,250,250))
        screen.blit(text, ((self.x)+15,(self.v_pos)+20))
    
  
        
    
    def ele_pos(self,pos):# to display position of elevator
        self.pos=pos
        pygame.draw.rect(screen,(250,250,250),(530,self.by,140,30))
        pygame.draw.rect(screen,(0,0,0),(530-2,self.by-2,144,34),2)
        pygame.draw.line(screen,(0,0,0),(630,self.by),(630,self.by+30),2)

        font  = pygame.font.Font(None , 30)
        s= "Elevator "+str(self.no)
        text = font.render(s,1,(250,0,0))
        screen.blit(text, (530,self.by+5))

        if self.pos>=0 and self.pos<72:
            s1=str(10)
            t1=font.render(s1,1,(250,0,0))
            screen.blit(t1,(640,self.by+5))
        elif self.pos>=72 and self.pos<142:
            s1=str(9)
            t1=font.render(s1,1,(250,0,0))
            screen.blit(t1,(640,self.by+5))
        elif self.pos>=142 and self.pos<212:
            s1=str(8)
            t1=font.render(s1,1,(250,0,0))
            screen.blit(t1,(640,self.by+5))
        elif self.pos>=212 and self.pos<282:
            s1=str(7)
            t1=font.render(s1,1,(250,0,0))
            screen.blit(t1,(640,self.by+5))
        elif self.pos>=282 and self.pos<352:
            s1=str(6)
            t1=font.render(s1,1,(250,0,0))
            screen.blit(t1,(640,self.by+5))
        elif self.pos>=352 and self.pos<422:
            s1=str(5)
            t1=font.render(s1,1,(250,0,0))
            screen.blit(t1,(640,self.by+5))
        elif self.pos>=422 and self.pos<492:
            s1=str(4)
            t1=font.render(s1,1,(250,0,0))
            screen.blit(t1,(640,self.by+5))
        elif self.pos>=492 and self.pos<562:
            s1=str(3)
            t1=font.render(s1,1,(250,0,0))
            screen.blit(t1,(640,self.by+5))
        elif self.pos>=562 and self.pos<632:
            s1=str(2)
            t1=font.render(s1,1,(250,0,0))
            screen.blit(t1,(640,self.by+5))
        elif self.pos>=632 and self.pos<700:
            s1=str(1)
            t1=font.render(s1,1,(250,0,0))
            screen.blit(t1,(640,self.by+5))
def floor_top(p):
    if p==10:
        return 1
    elif p==9:
        return 74
    elif p==8: 
        return 142
    elif p==7:
        return 212
    elif p==6:
        return 283
    elif p==5:
        return 353
    elif p==4:
        return 422
    elif p==3:
        return 493
    elif p==2:
        return 562
    elif p==1: 
        return 632
            
        
            
        
                    
c=canvas()
but = button(10)
elv1=elevator(1,10,12)
elv2=elevator(2,70,112)
elv3=elevator(3,130,212)
elv4=elevator(4,190,312)
list_up=[0,0,0,0,0,0,0,0,0,0];
list_down=[0,0,0,0,0,0,0,0,0,0];
FPS = 20
pixmov =3
fpsTime = pygame.time.Clock()
i=0
curr=0
imgy=632
while True:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
                mx,my=pygame.mouse.get_pos()
                st=but.pressed(my)
                if st>=1 and st<=10:
                    if mx>=410 and mx<=441:
                        list_up[st-1]=1
                        print st,"UP"
                        print list_up
                    
                    elif mx>=445 and mx<=477:
                        list_down[st-1]=1
                        print st,"Down"
                        print list_down
                    else:
                        print "yar sahi se click karo"
                    while i<10:
                        if list_up[i]==1:
                            curr=i+1
                            break
                        i+=1
                    i=0
    while i<10 and curr !=0:
        if list_up[i]==1:
            curr=i+1
            break
       
        i+=1
        
    i=0
    if curr>0 :
        top = floor_top(curr)
        screen.fill((200,200,200))
        c=canvas()
        but = button(10)
        if imgy >=top+2 :
            imgy -=pixmov
            elv1.show_elev(imgy)
            elv1.ele_pos(imgy)
        else:
            elv1.show_elev(imgy)
            elv1.ele_pos(imgy)
            time.sleep(2)
            list_up[curr-1]=0
            print list_up
            print curr
    if curr == 0:
        elv1.ele_pos(632)
        elv1.show_elev(632)
       
        
    pygame.display.update()
    fpsTime.tick(FPS)
