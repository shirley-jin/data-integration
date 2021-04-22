import pandas as pd

file = pd.read_excel("/Users/qianjin/Dropbox/PhD Project/OpenRiceData/Network data/Network_April21/network_user.xlsx")

user_id = []
topic=[]
gamma=[]
l=0

def unique_index(L,e):
    return [i for (i,j) in enumerate(L) if j == e][-1]

for i in range(1,21):
    for j in range(0,len(file[file["topic"]==i])):
        if file[file["topic"]==i].loc[j+l]["user_id"] in user_id:
            if topic[unique_index(user_id,file[file["topic"]==i].loc[j+l]["user_id"])] == i:
                gamma[unique_index(user_id,file[file["topic"]==i].loc[j+l]["user_id"])]+=file[file["topic"]==i].loc[j+l]["gamma"]
            else:
                user_id.append(file[file["topic"]==i].loc[j+l]["user_id"])
                topic.append(i)
                gamma.append(file[file["topic"]==i].loc[j+l]["gamma"])     
        else:
            user_id.append(file[file["topic"]==i].loc[j+l]["user_id"])
            topic.append(i)
            gamma.append(file[file["topic"]==i].loc[j+l]["gamma"])     
    
    print(i,len(file[file["topic"]==i]))
    l+=len(file[file["topic"]==i])
    
cb = pd.DataFrame({"user_id":user_id,"topic":topic,"gamma":gamma})

cb.to_csv("/users/qianjin/desktop/network_user.csv")
