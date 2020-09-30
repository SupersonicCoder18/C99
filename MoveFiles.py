import os
import shutil

source = input("Enter the source folder path :- ")
destination = input("Enter destination path name:- ")

source = source + "/"
destination = destination + "/"

files = os.listdir(source)
for file in files:
    shutil.move((source + file), destination)
