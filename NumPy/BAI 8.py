import numpy as np

def combine_rooms(room_1, room_2):
    res=[]
    for i,j in zip(room_1, room_2):
        if (i>0):
            res.append(int(i))
        elif (j>0):
            res.append(int(j))
        else:
            res.append("None")
    return res

room_1=np.array([1,2,-3,4,5,6,-7])
room_2=np.array([8,9,10,11,12,-13,-14])

res=combine_rooms(room_1,room_2)

print("Danh sach cac thi sinh cuoi cung :\n",res)