import sys

import graph
import objects
def main():
    
    datas = open("SAVE/lang.txt", "r")
    language = int(datas.readline())
    datas.close()
    screen = graph.image(language)
    inside_game = True
    
    while inside_game:
        inside_game = screen.Menu()        

        inside_game = False
    
    input()
        
    screen.endImage()
    sys.exit()
    
if __name__ == '__main__':
    main()