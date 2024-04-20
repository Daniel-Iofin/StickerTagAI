from numpy import random as RandNorm
from numpy import array, mean, std
from random import random
from Agent import Agent
import json


def simulation(taggingFactor):
    agentList = []
    aliveCount = 100
    for i in range(100):
        agentList.append(Agent((i+1)%100))


    distances = []
    iterations = 0
    iterationsBetweenTags = []
    lastTagAt = 0

    while aliveCount>5:
        iterations+=1
        for i in range(100):
            agent = agentList[i]
            rotation = abs(RandNorm.normal()*10)
            distance = agent.velocity
            velocity = abs(RandNorm.normal()*5)
            agent.move(rotation, distance)
            agent.changeVelocity(velocity)

        for hunter in agentList:
            if hunter.alive:
                target = agentList[hunter.target]
                distance = ((hunter.x-target.x)**2+(hunter.x-target.y)**2)**0.5
                tagProbability = 1-taggingFactor*(distance/100)**2
                if random()<tagProbability:
                    hunter.tag()
                    hunter.updateTarget(target.target)
                    target.tagged()
                    aliveCount-=1
                    iterationsBetweenTags.append(iterations-lastTagAt)
                    print(str(iterations-lastTagAt)+"".join([" "]*(10-len(str(iterations-lastTagAt))))+str(aliveCount))
                    lastTagAt = iterations

    print(iterationsBetweenTags, iterations)
    print([agent.tags for agent in agentList])
    with open("simulationResult.txt", "w") as output:
        output.write(json.dumps(iterationsBetweenTags))

simulation(1000000)
