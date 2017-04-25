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
    testingx = True
    eprint(xmin)
    eprint(xmax)
    turn = 0
    x = x0
    '''
    while True:
        
        bomb_dir = input()  # Current distance to the bomb compared to previous distance (COLDER, WARMER, SAME or UNKNOWN)
        eprint("current x: " + str(x))
        turn+=1
        if(turn==1):
            m = (xmin+xmax-1)/2
            xold = x
            x = x + 2*(m-x)
            eprint("initially jumpint to: " + str(x))
            print(int(x),int(y0))

        
        if(testingx == True and turn>1):
            m = (x + xold)/2 #The actual divider line
            
            if(bomb_dir == "SAME"):
                
                xcorrect = m
                eprint("correct x at: " + str(x))
                testingx = False
            if(bomb_dir == "COLDER"):
                if(x < xold): xmin = int(m)
                if(x > xold): xmax = int(m)
            if(bomb_dir == "WARMER"):
                if(x < xold): xmax = int(m)
                if(x > xold): xmin = int(m)
            eprint("new limits: " + str(xmin) +  " to " + str(xmax))
            m = (xmin + xmax)/2 #Tentative m for the best cut
            eprint("best cut at " + str(m))
            xold = x
            x = x + 2*(m - x)#Tentative x
            eprint("best x: " + str(x))
            if(x < 0): x = 0
            if(x > w - 1): x = w-1 
            eprint("corrected x: " + str(x))
            print(int(x),int(y0))
    '''
    while True:
        
        bomb_dir = input()  # Current distance to the bomb compared to previous distance (COLDER, WARMER, SAME or UNKNOWN)
        eprint("current x: " + str(x))
        turn+=1
        if(turn==1):
            #m = (xmin+xmax)/2
            m = xmin + (xmax-xmin)/2
            xold = x
            x = x + 2*(m-x)
            eprint("initially jumpint to: " + str(x))
            print(int(x),int(y0))
            continue

        
        if(testingx == True and turn>1):
            #m = (x + xold-1)/2 #The actual divider line
            dist = abs(x-xold)
            if(dist%2 == 1):
                dist -=1
            m = min(x,xold) + (dist)/2
            eprint("actual divider line: " + str(m))
            if(bomb_dir == "SAME"):
                
                xcorrect = m
                eprint("correct x at: " + str(x))
                testingx = False
            if(bomb_dir == "COLDER"):
                if(x < xold): xmin = int(m)
                if(x > xold): xmax = int(m)
            if(bomb_dir == "WARMER"):
                if(x < xold): xmax = int(m)
                if(x > xold): xmin = int(m)
            eprint("new limits: " + str(xmin) +  " to " + str(xmax))
            m = (xmin + xmax)/2 #Tentative m for the best cut
            eprint("best cut at " + str(m))
            xold = x
            x = x + 2*(m - x)#Tentative x
            eprint("best x: " + str(x))
            if(x < 0): x = 0
            if(x > w - 1): x = w-1 
            eprint("corrected x: " + str(x))
            print(int(x),int(y0))        
    
def eprint(*args,**kwargs):
    print(*args,file=sys.stderr,**kwargs)

if __name__ == "__main__":
    main()