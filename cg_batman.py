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
    
   
    while True:
       
        bomb_dir = input()  # Current distance to the bomb compared to previous distance (COLDER, WARMER, SAME or UNKNOWN)
        turn+=1
            
        
def eprint(*args,**kwargs):
    print(*args,file=sys.stderr,**kwargs)

if __name__ == "__main__":
    main()