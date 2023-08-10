from cmd import Cmd
import os
import subprocess
def eva(o):
    subprocess.call(o,shell=True)

set=[]
path="C:\\"

class TrojanHorse(Cmd):
    """just try try"""

    prompt = "┌──(\x1b[38;2;255;0;0mhacker\x1b[0m)-[\x1b[38;2;16;150;220m"+path+"\x1b[0m]\n└─\x1b[38;2;255;0;0m#\x1b[0m "
    intro = "Welcome to \x1b[38;2;16;150;220mHacker\x1b[0m cli tool"

    def do_exit(self):
        return True
    def do_cd(self,argv):
        global path
        path=os.path.join(path,argv)
        self.prompt = "┌──(\x1b[38;2;255;0;0mhacker\x1b[0m)-[\x1b[38;2;16;150;220m"+path+"\x1b[0m]\n └─\x1b[38;2;255;0;0m#\x1b[0m "
    def default(self,line):
        global set
        if line[-1]=="\\" or line[-1]=="^":
            set.append(line)
            ah="^"
            while ah[-1]=="^" or ah[-1]=="\\" :
                if len(set):
                    set[-1]=set[-1][0:-1]
                ah=input("└─\x1b[38;2;255;0;0m#\x1b[0m ")
                set.append(ah)
            eva(" ".join(set))
            set=[]
        else:
            eva(line)

    def preloop(self):
        eva("cls")

    def postloop(self):
        print("Exiting HackerTool")


if __name__ == "__main__":
    try:
        TrojanHorse().cmdloop()
    except KeyboardInterrupt:
        print("\nExiting HackerTool")
