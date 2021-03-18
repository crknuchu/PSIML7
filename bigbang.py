import math
import sys
# N S T P
particle_info = []


N,S,T,P = input().split() #probability of not bouncing of edge
N = int(N)
S = int(S)
T = int(T)
P = float(P)

def reflectXAxis(x,S):
    d = abs(S-x)
    tempx = S-d
    return tempx

def reflectXAxisNeg(x,S):
    d = abs(S-x)
    tempx = S+d
    return tempx

def reflectYAxis(y,S):
    d = abs(S-y)
    tempy = S-d
    return tempy

def reflectYAxisNeg(y,S):
    d = abs(S-y)
    tempy = S+d
    return tempy
#print(reflectXAxis(11,8,10))

def numBounce(Px,Py,Vx,Vy):
    bounce = 0
    sec=0
    while True:
        
        sec+=1
        Px += Vx
        Py += Vy
        #print("Px,Py ",Px,Py)
        
        if(Px>0):
            if(Px > S):
                bounce+=1
                Px = reflectXAxis(Px,S)
                Vx = -1*Vx
        else:
            if(Px < (-S)):
                bounce+=1
                Px = reflectXAxisNeg(Px,-S)
                Vx = -1*Vx
                
        if(Py>0):    
            if(Py > S):
                bounce+=1
                Py = reflectYAxis(Py,S)
                Vy = -1*Vy
        else:
            if(Py < (-S)):
                bounce+=1
                Py = reflectYAxisNeg(Py,-S)
                Vy = -1*Vy
        
        
        if(sec==int(T)):
            break
    #print(Px,Py)    
    return bounce

for i in range(0,int(N)):
    particle_info.append(input().split())


def distToOrigin(Px,Py):
    dist = abs(math.hypot(Px,Py))
    return dist


def particleMinDist(Px,Py,Vx,Vy):
    
    minDist = round(distToOrigin(Px,Py),6)
    
    while True:
    
        Px = round(Px - Vx,6)
        Py = round(Py - Vy,6)
        dist = round(distToOrigin(Px,Py),6)
    
        if(dist<minDist):
            minDist=dist
        else:
            break
    return minDist



particle_info_float = []
for sublist in particle_info:
    float_sublist=[]
    for x in sublist:
        float_sublist.append(float(x))
    particle_info_float.append(float_sublist)

def probability(bounce,P):
    for i in range (0,bounce):
        
    

bounce =0
#prob = 0
#for particle in particle_info_float:
#    prob += probability(numBounce(particle[0],particle[1],particle[2],particle[3]),P)
#    bounce+=numBounce(particle[0],particle[1],particle[2],particle[3])
    
    
minDist =0

for particle in particle_info_float:
    minDist += round(distToOrigin(particle[0],particle[1]),6)
#print(minDist)
# minDist je zbir svih razdaljina od centra
currDist = 0
sec=0
while True:
    currDist = 0
    for particle in particle_info_float:
        particle[0]-=particle[2]
        particle[1]-=particle[3]
        currDist += round(distToOrigin(particle[0],particle[1]),6)
#print(currDist)
    if(currDist < minDist):
        minDist=currDist
        sec+=1
    else:
        break


print(sec,bounce,-1)
    
  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
