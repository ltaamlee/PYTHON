import os
def GetFileName(path):
    return os.path.basename(path)

def GetFileNameWithoutExtension(path):
    return os.path.splitext(os.path.basename(path))[0]

exPath = "D:\\music\\muabui.mp3"
print('VD:', exPath)

print(GetFileName(exPath))  
print(GetFileNameWithoutExtension(exPath))  

path=input("Nhap duong dan tep tin: ")

file=GetFileName(path)
fileW=GetFileNameWithoutExtension(path)

print(f"Ten tep tin: {file}")  
print(f"Ten tep tin khong co phan mo rong: {fileW}")  

