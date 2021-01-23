import os 



def recc(dire,old,b,c):
    if b != 0:
        path = old+ "/" + dire
    else:
        path = dire
    #print(path)
    for filename in os.listdir(path):
        if os.path.isdir(path + "/" + filename):
            if filename != "res":
                recc(filename, path,1,c)
        elif filename[-3:] == "avi" or filename[-3:] == "mp4" or filename[-3:] == "mts":
            print(path.split("/vol"))
            os.system("mkdir -p ../vol/res" + path.split("/vol")[1] + '/' + filename.split('.')[0])
            os.system("./build/examples/openpose/openpose.bin --video " + str(path) + "/" + str(filename) +\
                " -face -hand --part_candidates --number_people_max 1 --write_json ../vol/res" + path.split("/vol")[1] + '/' + filename.split('.')[0])
	    os.system("python data_proc.py -p  ../vol/res" + path.split("/vol")[1] + '/' + filename.split('.')[0] + " -n "+ filename.split('.')[0])
            c +=1
    print("$$$$$$$$$$$$$$$$")
    print(c)

b=0
c = 0
os.system("mkdir ../vol/res")
#os.system("nvidia-settings -a '[gpu:0]/GPUFanControlState=1' -a '[fan:0]/GPUTargetFanSpeed=99'")
recc("../vol","",b,c)
print(c)

#--disable_multi_thread
#--number_people_max
