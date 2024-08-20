import time, sys
indent = 0 # How many spaces to indent.
indentIncreasing = True # Whether the indentation is increasing or not.

def zig_zag_game(name):
    try:
        while True: 
            global indent
            global indentIncreasing
            print(' ' * indent, end='')
            print(f'{name}')
            time.sleep(0.1) 

            if indentIncreasing:
                indent = indent + 1
                if indent == 20:
                    indentIncreasing = False

            else:
                indent = indent - 1
                if indent == 0:
                    indentIncreasing = True
    except KeyboardInterrupt:
        sys.exit()