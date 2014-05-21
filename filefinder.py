__author__ = 'thomas, steve'

import os
import fnmatch
# Any kind of file you are looking for
fileTypes = ["png", "jpg", "doc", " docx", "psd", "mp3", "mp4", "m4a", "pdf", "mov"]
rootdir = os.getcwd
#The root folder of where youd like to look
workingdir = "/home/thomas/folder"

def file_move(tobemoved, typeof):
    os.system("cp %s %s" % (tobemoved, (rootdir + "/RESTORED/" + typeof)))


def find_files():
    currentdir = os.getcwd
    print("Working in" + currentdir + "\n")

    for rootdir, dirdir, filedir in os.walk(workingdir):
        for folder in dirdir:
            print(folder + "\n")
            if folder == "RESTORED" or folder in fileTypes:
                print("Skipping folders: " + folder + "\n")
            else:
                print("Moving to %s \n" % folder)
                os.chdir(folder)
                for typeof in fileTypes:
                    pat = "*." + typeof
                    for root, dirs, files in os.walk("."):
                        for name in files:
                            if fnmatch.fnmatch(name, pat):
                                print(workingdir + folder + "/" + name)
                                filepath = workingdir + folder + "/" + name
                                file_move(filepath, typeof)
                            else:
                                print("Nothing found")
                os.system("pwd")
                os.system("../")
                os.system("pwd")


def premade_dir():
    print("Making dir for file types in folder RESTORED\n")
    os.system("test -d RESTORED; if( test $? -eq 1) then mkdir RESTORED; fi")
    os.chdir("RESTORED")

    for extension in fileTypes:
        os.system("test -d %s; if( test $? -eq 1) then mkdir %s; fi" % (extension, extension))
        print(" " + extension + " ")


def main():
    print("Starting up \n")
    premade_dir()
    os.chdir(workingdir)
    find_files()

if __name__ == "__main__":
    main()