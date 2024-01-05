import sys

import graph

def main():
    
    datas = open("SAVE/lang.txt", "r")
    language = int(datas.readline())
    datas.close()
    screen = graph.image(language)
    inside_game = True
    
    while inside_game:
        screen.ResetValues()
        # inside_game = screen.Menu()        
        inside_game = False
    screen.endImage()
    sys.exit()
    
if __name__ == '__main__':
    main()