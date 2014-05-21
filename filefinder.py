__author__ = 'thomas, steve'

import os
import fnmatch

#The root folder of where youd like to look
WORKING_DIR = "/home/thomas/folder"

# Any kind of file you are looking for
FILE_TYPES = [
    "png", 
    "jpg", 
    "jpeg", 
    "gif", 
    "doc", 
    "docx", 
    "psd", 
    "mp3", 
    "mp4", 
    "m4a", 
    "pdf", 
    "mov", 
    "zip", 
    "rar", 
    "csv", 
    "ppt", 
    "wav", 
    "xls", 
    "qt", 
    "avi"
]

rootdir = os.getcwd

def file_move(tobemoved, typeof):
    os.system("cp %s %s" % (tobemoved, (rootdir + "/RESTORED/" + typeof)))

def find_files():
    currentdir = os.getcwd
    print("Working in" + currentdir + "\n")

    for rootdir, dirdir, filedir in os.walk(WORKING_DIR):
        for folder in dirdir:
            print(folder + "\n")
            if folder == "RESTORED" or folder in FILE_TYPES:
                print("Skipping folders: " + folder + "\n")
            else:
                print("Moving to %s \n" % folder)
                os.chdir(folder)
                for typeof in FILE_TYPES:
                    pat = "*." + typeof
                    for root, dirs, files in os.walk("."):
                        for name in files:
                            if fnmatch.fnmatch(name, pat):
                                print(WORKING_DIR + folder + "/" + name)
                                filepath = WORKING_DIR + folder + "/" + name
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

    for extension in FILE_TYPES:
        os.system("test -d %s; if( test $? -eq 1) then mkdir %s; fi" % (extension, extension))
        print(" " + extension + " ")


def main():
    if os.path.isdir(WORKING_DIR):
        premade_dir()
        os.chdir(WORKING_DIR)
        find_files()
    else:
        print 'Directory: ' + WORKING_DIR + ' does not exist.'

if __name__ == "__main__":
    main()
