import pandas as pd
import numpy as np
from collections import OrderedDict


f=pd.read_csv('C:/Users/ASUS/Desktop/upgrad/2018wc/result18.csv',',',)

v=pd.read_csv('C:/Users/ASUS/Desktop/upgrad/2018wc/index18.csv',',')
h=np.array(v)
Point={}
#dic={"Brazil":2,"England":3,"Portugal":4,"France":1,"Iran":4,"Sweden":4,"Denmark":7,"Australia":4,"Russia":4,"Paraguay":4,"Colombia":4}
list1=["Egypt","Spain","Belgium","Brazil","England","Portugal","France","Iran","Sweden","Denmark","Australia","Russia","Colombia","Morocco","Mexico","Uruguay","Germany","SaudiArabia","Morocco","Peru","Croatia","Nigeria","Iceland","Argentina","Switzerland","Serbia","CostaRica","SouthKorea","Tunisia","Panama","Japan","Senegal","Poland"]
groupingsasTeam1 = f.groupby(['Team1']) [['Team1Goals','Team2Goals']].sum()
#print(groupingsasTeam1)
groupingsasTeam2 = f.groupby(['Team2']) [['Team1Goals','Team2Goals']].sum() 
#print(groupingsasTeam2)  
for item in list1:
    play=f[f.Team2==item]+f[f.Team1==item]
   # print("number of play matchs of",item,len(play))
    draw=f[f.Winner==item]+f[f.Losser==item]
    
    d=len(play)-len(draw)
   # print("number of draw matchs of",item,d)
    win=f[f.Winner==item]
    dm=0
    #print("number of Win matchs of",item,len(win))
    los=f[f.Losser==item]
    p=1
   # print("number of losses matchs of",item,len(los))
    i1=item 
    hoo=f[f.Winner==f.Losser]
    ho1=hoo[hoo.Team1==item]
    ho=hoo[hoo.Team2==item]
    listofdraw=list(ho.Team1)+list(ho1.Team2)
   # print(listofdraw)
    
   # Point[i1]= round((len(win)*6+y*2)/len(play),2 )
    goalsgiven=groupingsasTeam1.Team1Goals[groupingsasTeam1.index==item] + groupingsasTeam2.Team2Goals[groupingsasTeam2.index==item]
   # print(goalsgiven.dtypes)
  #  goalsgiven=goalsgiven.astype('int')
#    print(goalsgiven.dtypes)
 #   print(goalsgiven+4)
    goalsagainst=groupingsasTeam1.Team2Goals[groupingsasTeam1.index==item] + groupingsasTeam2.Team1Goals[groupingsasTeam2.index==item]
    goaldiff=goalsgiven-goalsagainst
 #   print("number of goaldiff of",goaldiff)
    l=list(win.Losser)
    lost=list(los.Winner)
    gd=goaldiff.item()
    lp=0
    u=t=y=0
    for i in range(0,len(l)):
        for j in range(0,206):
                     
              if (l[i]==(h[j][1])):
                  p=p+(h[j][2])
                  
              
                  
                  
                 
    for i in range(0,len(listofdraw)):
        for j in range(0,206):
                     
             if (listofdraw[i]==(h[j][1])):
                 dm=dm+h[j][2]
                 
    for i in range(0,len(lost)):
        for j in range(0,206):
                     
             if (lost[i]==(h[j][1])):
                 lp=lp+1.5-(h[j][2])
                 
     #            print(h[j][1])
   
    Point[i1]= round(((dm*2+p*6-lp+(gd/10))/len(play)),2 )
    
    
#print(Point)
Point_new = OrderedDict(sorted(Point.items(), key=lambda x: x[1]))
print(Point_new)
tndg1=[]
sndg1= []
tndg2=[]
sndg2= []
group1=["Uruguay","Portugal","France","Argentina","Brazil","Mexico","Belgium","Japan"]
group2=["Spain","Russia","Croatia","Denmark","Sweden","Switzerland","Colombia","England"]
for i in range(0,8,2):
    if Point_new[group1[i]] > Point_new[group1[i+1]]:
        sndg1.append(group1[i])
    else:
        sndg1.append(group1[i+1])
        
for i in range(0,4,2):
    if Point_new[sndg1[i]] > Point_new[sndg1[i+1]]:
        tndg1.append(sndg1[i])
    else:
        tndg1.append(sndg1[i+1])
      
        
for i in range(0,8,2):
    if Point_new[group2[i]] > Point_new[group2[i+1]]:
        sndg2.append(group2[i])
    else:
        sndg2.append(group2[i+1])
        
for i in range(0,4,2):
    if Point_new[sndg2[i]] > Point_new[sndg2[i+1]]:
        tndg2.append(sndg2[i])
    else:
        tndg2.append(sndg2[i+1])       
    
print("\n After round of 16 winning teams are:\n",sndg1+sndg2)    
print("\n After round of 8 winning teams are:\n",tndg1+tndg2)    
print("\n\n          Our Semi-finalist are \n",tndg1+tndg2)

semi=tndg1+tndg2
final=[]
for i in range(0,4,2):
    if Point_new[semi[i]] > Point_new[semi[i+1]]:
        final.append(semi[i])
    else:
        final.append(semi[i+1])  

print("\n\n       Our finalist are \n    ",final)

if Point_new[final[0]] > Point_new[final[1]]:
    print("\n    2018 worldcup champion is\n             ",final[0])
else:
    print("\n    2018 worldcup champion is\n             ",final[1])



#from heapq import nlargest

#two_largest = nlargest(2, Point_new, key=Point_new.get)
#print("As this teams are not intersect before semi-final so 2 semi-finalists are",two_largest)
 

    
    


