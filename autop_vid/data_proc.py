import os
import json 
import csv
import numpy as np
import pandas as pd
import argparse



parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", type=str, action="store")
parser.add_argument("-n", "--name", type=str, action="store")
args = parser.parse_args()
path = args.path
print(path)

df = pd.DataFrame([])
d = np.array([])
dd = np.array([[-1]*(75+70*3+63*2)]) #*3 if prob taken into account
#print(dd)

#get filenames and sort so that the movement is int the right order
for filename in os.listdir(path):
    if filename.endswith("json"):
        d = np.append(d, filename)
d = np.sort(d)

#main loop
#extract part pose and stor them in a csv 
#question do we store the probability of the pose of each point?
#for now no but we put the code commented just in case

c =1
for i in d:
    with open(path + "/" + i) as json_file:
        #print(json_file)
        temp = json.load(json_file)
        #print(temp)
        temp2 = []
        #for key,value in temp['part_candidates'][0].items():
        for key in range(25):
            # if c ==1:
            #     sorted(temp['part_candidates'][0][str(key)])
            #     print(key)
                
            #print(key,value)
            if temp['part_candidates'][0][str(key)] == []:
                temp2.append(0)
                temp2.append(0)
                temp2.append(0)
            else:
                """temp2.append(value[0])
                temp2.append(value[1]) """
                temp2.append(temp['part_candidates'][0][str(key)][0])
                temp2.append(temp['part_candidates'][0][str(key)][1])
                temp2.append(temp['part_candidates'][0][str(key)][2])
            #print(temp2)
            exp = np.expand_dims(temp2,axis=0)
            #print(exp)
	for j in range(len(temp["people"])):
		if temp["people"][j]["face_keypoints_2d"] != []:
			exp = np.concatenate((exp,temp["people"][j]["face_keypoints_2d"]),axis=None)
		else:
			exp = np.concatenate((exp,[0]*70*3),axis=None)

		if temp["people"][j]["hand_left_keypoints_2d"] != []:
			exp = np.concatenate((exp,temp["people"][j]["hand_left_keypoints_2d"]),axis=None)
		else:
			exp = np.concatenate((exp,[0]*21*3),axis=None)

		if temp["people"][j]["hand_right_keypoints_2d"] != []:
			exp = np.concatenate((exp,temp["people"][j]["hand_right_keypoints_2d"]),axis=None)
		else:
			exp = np.concatenate((exp,[0]*21*3),axis=None)
	exp = np.expand_dims(exp,axis=0)
	#print(np.shape(exp))
	#print(np.shape(dd))
        dd = np.append(dd,exp,axis = 0)
        #if c == 1:
            #print(dd)
            #print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
            #print(exp)
        #c+=1
#print(dd)
    
#print(dd.shape)
#print(type(dd))
df = pd.DataFrame(dd[1:])
print(dd[1:].shape)
print(d.shape)
#print(df)
df.to_csv(path + "/../" + args.name + ".csv",index=False)

