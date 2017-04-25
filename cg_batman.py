import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def main():

    # w: width of the building.
    # h: height of the building.
    w, h = [int(i) for i in input().split()]
    n = int(input())  # maximum number of turns before game over.
    x0, y0 = [int(i) for i in input().split()]
    
    xmin = 0
    xmax = w-1
    if(xmin == xmax):
        testingx = False
        xcorrect = xmin
    else:
        testingx = True
    ymin = 0
    ymax = h-1
    
    starty = True
        
    
    eprint(xmin)
    eprint(xmax)
    turn = 0
    x = x0
    y = y0

    while True:
        
        bomb_dir = input()  # Current distance to the bomb compared to previous distance (COLDER, WARMER, SAME or UNKNOWN)
        eprint("current x: " + str(x))
        eprint("current y: " + str(y))
        turn+=1
        if(turn==1):
            #m = (xmin+xmax)/2
            m = xmin + (xmax-xmin)/2
            xold = x
            x = x + 2*(m-x)
            eprint("initially jumping to x: " + str(x))
            print(int(x),int(y0))
            continue

        
        if(testingx == True and turn>1):
            m = min(x,xold) + (max(x,xold) - min(x,xold))/2         
            mint = int(2*m)%2==0   
            eprint("actual divider line x: " + str(m))
            eprint("mint x" + str(mint))
            if(bomb_dir == "SAME"):
                
                xcorrect = m
                eprint("correct x at: " + str(xcorrect))
                testingx = False
            if(bomb_dir == "COLDER"):
                if(x < xold): #moved left
                    if(mint):
                        xmin = int(m+1)
                    if(not mint):
                        xmin = int(m+0.5)
                if(x > xold): #moved right
                    if(mint):
                        xmax = int(m-1)
                    if(not mint):    
                        xmax = int(m-0.5)
            if(bomb_dir == "WARMER"):
                if(x < xold): #moved left
                    if(mint):    
                        xmax = int(m-1)
                    if(not mint):
                        xmax = int(m-0.5)
                if(x > xold): #moved right
                    if(mint):                
                        xmin = int(m+1)
                    if(not mint):
                        xmin = int(m+0.5)
            if(xmin == xmax):
                xcorrect = xmin
                testingx = False
            if(testingx == True):
                eprint("new limits x: " + str(xmin) +  " to " + str(xmax))
                m = (xmin + xmax)/2 #Tentative m for the best cut
                eprint("best cut at x: " + str(m))
                xold = x
                x = x + 2*(m - x)#Tentative x
                eprint("best x: " + str(x))
                if(x < 0): x = 0
                if(x > w - 1): x = w-1 
                eprint("corrected x: " + str(x))
                print(int(x),int(y0))
                
            
        if(testingx == False):
            eprint("FOUND CORRECT X AT " + str(xcorrect))
            if(starty):
                starty = False
                m = ymin + (ymax-ymin)/2
                yold = y
                y = y + 2*(m-y)
                eprint("initially jumping to y: " + str(y))
                print(int(x),int(y))
                continue
            else:
                m = min(y,yold) + (max(y,yold) - min(y,yold))/2         
                mint = int(2*m)%2==0   
                eprint("actual divider line y: " + str(m))
                eprint("mint y: " + str(mint))
                if(bomb_dir == "SAME"):

                    eprint("correct y at: " + str(m))
                    print(int(xcorrect),int(m))
                if(bomb_dir == "COLDER"):
                    if(y < yold): #moved left
                        if(mint):
                            ymin = int(m+1)
                        if(not mint):
                            ymin = int(m+0.5)
                    if(y > yold): #moved right
                        if(mint):
                            ymax = int(m-1)
                        if(not mint):    
                            ymax = int(m-0.5)
                if(bomb_dir == "WARMER"):
                    if(y < yold): #moved left
                        if(mint):    
                            ymax = int(m-1)
                        if(not mint):
                            ymax = int(m-0.5)
                    if(y > yold): #moved right
                        if(mint):                
                            ymin = int(m+1)
                        if(not mint):
                            ymin = int(m+0.5)
                if(ymin == ymax):
                    print(int(xcorrect),int(ymin))
                    
                eprint("new limits y: " + str(ymin) +  " to " + str(ymax))
                m = (ymin + ymax)/2 #Tentative m for the best cut
                eprint("best cut at " + str(m))
                yold = y
                y = y + 2*(m - y)#Tentative x
                eprint("best y: " + str(y))
                if(y < 0): y = 0
                if(y > h - 1): y = h-1 
                eprint("corrected y: " + str(y))
                print(int(x),int(y))
             
def eprint(*args,**kwargs):          
   print(*args,file=sys.stderr,**kwargs)

if __name__ == "__main__":
    main()