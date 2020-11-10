# PyMad a201105
def run():
    files = ["a.txt", "b.txt", "c.txt", "dir: d"]
    error = 0
    while True:
        위치 = ["P: ", "files"]
        shellInput1 = input("$ ")
        directories = 1
        if error == 5:
            print("Your Pyshell is locked.")
            break
        if shellInput1 == "ls":
            print(files)
        elif shellInput1 == "pwd":
            print(위치)
        elif shellInput1 == "touch":
            shellInput2 = input("$ touch ")
            if shellInput2 != "cancel":
                files.append(shellInput2)
        elif shellInput1 == "rm":
            shellInput2 = input("$ rm ")
            if shellInput2 != "cancel":
                try:
                    del files[files.index(shellInput2)]
                except:
                    print("Invalid file or directory.")
                    error += 1
        elif shellInput1 == "mkdir":
            shellInput2 = input("$ mkdir ")
            if shellInput2 != "cancel":
                files.append("dir: {}".format(shellInput2))
        elif shellInput1 == "exit":
            print("Bye!")
            break
        else:
            print("Invalid command.")
            error += 1
# 실행: python AlphaPyShell_-5.-5.-3.py
# codecademy.com
# codecademy.com
#codecademy.commoc.ymedacedoc
# codecademy.com
# freesam.commoc.maseerf