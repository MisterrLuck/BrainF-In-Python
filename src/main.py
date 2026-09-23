# from interpreter import run, lexer, lstNum
# import sys
#
# code = sys.argv[1]
#
# with open(code, 'r') as file:
# 	lexed, loops = lexer(file)
#
# cells, currentCell = run(lexed, loops)
# cells = lstNum(cells, currentCell)
# print(f'\n\033[1;32m=> {cells}\033[0m')

import readline
from brain import Brain
import sys

brain = Brain()

args = sys.argv

# File mode
if len(args) >= 2:
    brain.run_file(args[1])
    brain.debug()

# Shell Mode
else:
    try:
        while (1):
            code = input(": ")
            if code in ["quit", "exit", "quit()", "exit()"]:
                break

            brain.run(code)
            brain.debug()
    except KeyboardInterrupt:
        pass
