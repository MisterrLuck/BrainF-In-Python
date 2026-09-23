import readline

class Brain:
    def __init__(self, eof='\0'):
        self.loopStack = []
        self.cells = [0]
        self.lexed = []
        self.currCell = 0
        self.buffer = ""
        if len(eof) != 1:
            raise Exception(f"EOF must be a char, not {eof}")
        self.EOF = eof

    def reset(self):
        self.__init__()

    def lexer(self, code):
        self.lexed = []
        
        for char in code:
            if char in "+-<>.,[]":
                self.lexed.append(char)
    
    def interpret(self):
        index = 0
        endLoop = 0;

        try:
            while index < len(self.lexed):
                if endLoop:
                    if (self.lexed[index] == ']'):
                        endLoop -= 1
                    if (self.lexed[index] == '['):
                        endLoop += 1
                else:
                    match (self.lexed[index]):
                        case '+':
                            self.cells[self.currCell] += 1
                            self.cells[self.currCell] %= 256
                        case '-':
                            self.cells[self.currCell] -= 1
                            self.cells[self.currCell] %= 256
                        case '<':
                            if self.currCell > 0:
                                self.currCell -= 1
                            else:
                                raise Exception("Cell location must be positive. Attempt to go to the left too much!")
                        case '>':                    
                            self.currCell += 1
                            if len(self.cells) <= self.currCell:
                                self.cells.append(0)
                        case '[':
                            if self.cells[self.currCell] == 0:
                                endLoop += 1
                            else:
                                self.loopStack.append(index)

                        case ']':
                            if self.cells[self.currCell] == 0:
                                self.loopStack.pop()
                            else:
                                index = self.loopStack[-1]
                        case '.':
                            print(chr(self.cells[self.currCell]), end="")
                        case ',':
                            
                            inp = ""
                            if self.buffer:
                                inp = self.buffer[0]
                                self.buffer = self.buffer[1::]
                            else:
                                inp = input()+self.EOF
                                self.buffer += inp[1::]
                                inp = inp[0]
                            self.cells[self.currCell] = ord(inp)
                            
                            #self.cells[self.currCell] = ord((input()+self.EOF)[0])
                            
                index += 1
        except KeyboardInterrupt as ki:
            pass
                

    def run_file(self, file):
        with open(file, "r") as f:
            code = f.read()
            self.run(code)
            f.close()

    def run(self, code):
        self.lexer(code)
        self.interpret()

    def debug(self, offset=5, full=False):
        print()
        if full:
            rnge = [0, len(self.cells)]
        else:
            index = self.currCell
            rnge = [max(index-offset, 0), min(index+offset+1, len(self.cells))]
            if rnge[0] != 0:
                print("...", end=" ")
        for i in range(rnge[0], rnge[1]):
            if i == self.currCell:
                print(f"[{self.cells[i]}]", end=" ")
            else:
                print(f"{self.cells[i]}", end=" ")
        if rnge[-1] != len(self.cells):
            print("...", end=" ")
        print()

if __name__ == "__main__":
    brain = Brain()
    brain.run("+[>,]<-[+<-]>[.>]")
    brain.debug()

    
