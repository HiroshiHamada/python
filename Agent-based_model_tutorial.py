# -*- coding: utf-8 -*-
# ライブラリの導入
import random
import matplotlib.pyplot as plt
#import numpy.random as rd

# define class of Agent
class Agent:
    def __init__(self, unique_id):
        self.unique_id = unique_id #agentのid番号を記録する
        self.wealth = 1 #初期資産の定義

# define functions
def giving_money():
    agent1 = random.choice(agents)# 1人ランダムに選ぶ
    agent2 = random.choice(agents)# 1人ランダムに選ぶ
    if agent1.wealth > 0:
        agent2.wealth +=1 # 2の資産を1単位増やす
        agent1.wealth -=1 #　1の資産が1減る

n = 50 # define No.of agents
time = 500 # define No. of interaction　

# define agents (instance of Agent)
agentｓ = [Agent(i) for i in range(n)] 

# compute interactions    
for i in range(time):
    giving_money()
     
# analyze statistics                
agent_wealth = [x.wealth for x in agents]# 各自の資産を取り出す．
#%matplotlib inline
plt.hist(agent_wealth)#plot a histogram