import numpy as np


#остров
Island =np.array([2,4,2,6,4,2,1,4,5,3,1])


water = 0
while( len( Island) > 0 ):
    # его края
    edges = Island[0:len(Island):len(Island) - 1]
   # print(water, Island,np.where(edges == 0)[0]==0)
    if(np.count_nonzero(edges <= 0) > 0):
        Island = Island[1:] if  np.where(edges <= 0)[0]==0 else Island[:-2]
        continue
    if(np.count_nonzero(Island <= 0) > 0):
        water+=np.count_nonzero(Island <= 0)
        Island -= 1
    else:
        Island -= 1
print(water)