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
    left = 0
    right = w-1
    up = 0
    down = h-1

    checkinputx = False
    checkinputy = False
    sc = True #secondcorner
    xy = True
    turn = 0
    while True:
        eprint("left: " + str(left))
        eprint("right: " + str(right))
        eprint("up: " + str(up))
        eprint("down: " + str(down))
        bomb_dir = input()  # Current distance to the bomb compared to previous distance (COLDER, WARMER, SAME or UNKNOWN)
        turn+=1
        if(turn == 1):
            print(0,0)
            continue
        
        if(checkinputx):#adjust search boundaries in x
            checkinputx = False
            halfwidth = int((right-left)/2)
            if(bomb_dir== "WARMER"):
                left+=halfwidth+1
            if(bomb_dir== "COLDER"):
                right-=(halfwidth+1)
            if(bomb_dir== "SAME"):
                left+=halfwidth
                right-=halfwidth
            if(left==right):
                xy = False
                sc = True
                x = left
            
        if(checkinputy): #adjust search bounderies in y
            checkinputy = False
            halfwidth = int((down-up)/2)
            if(bomb_dir== "WARMER"):
                up+=halfwidth+1
            if(bomb_dir== "COLDER"):
                down-=(halfwidth+1)
            if(bomb_dir== "SAME"):
                up+=halfwidth
                down-=halfwidth
            
            if(up==down):
                xy = False
                y = up
                
                print(x,y)
        if(xy):#closer in x
            if(sc):
                checkinputx = True
                sc = not sc
                print(right,0)
            else:
                sc = not sc
                print(left,0)
        else: #closer in y
            if(sc):
                checkinputy = True
                sc = not sc
                print(x,down)
            else:
                sc = not sc
                print(x,up)
        #else:
            
        
def eprint(*args,**kwargs):
    print(*args,file=sys.stderr,**kwargs)

if __name__ == "__main__":
    main()