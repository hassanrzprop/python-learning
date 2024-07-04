import os 
currentDirectory= os.getcwd()
print("PRESENT DIR: ",currentDirectory)
getFiles=os.listdir(currentDirectory)
print("PRESENT FILES:",getFiles)