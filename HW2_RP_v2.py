"""
Created on Mon Oct  7 19:03:23 2013

@author: raghavendrashanbhogue
"""
#from random import randint

import numpy as np
from HW1_Perceptron_RP_v3 import target_function,generate_trainingData
from numpy.linalg import pinv
from random import choice
from math import copysign
import random

'''
def hoeffding_inequality_hw2_prob1(numOfCoins):
 
    coin_toss = [[]]  
    
    vmin = 10
    
    for i in range(numOfCoins):
        coinsample = []
        for j in range(10):
            coinsample.append(randint(0,1)) #0 if Tails; 1 if Heads
        if i == 0:
            coin_toss = [coinsample]
        else:
            coin_toss.append(coinsample)
        vmin = min (vmin,sum(coinsample))
 
    print coin_toss
   
    return vmin
    

def outer_looping_function(outerloopCount,numOfCoins):
    
    sumOfVmin = 0
    
    for k in range(outerloopCount):
        sumOfVmin = sumOfVmin + hoeffding_inequality_hw2_prob1(numOfCoins)
    
    print " The average vmin is %f" %(float(sumOfVmin)/(outerloopCount*10))
    
    return
'''

def linearRegression(sampleCount,trainingData_x,y):
    
    linearReg_betas = [0,0,0,0,0,0]
    
    moorePenroseInverse = pinv(trainingData_x)
    
  #  print moorePenroseInverse
    
    linearReg_betas = np.dot(moorePenroseInverse,y)
    
    
    return linearReg_betas
    
def transformed_trainingData(sampleCount,x1rand_1,x2rand_1,x1rand_2,x2rand_2):
    
    x0 = [1]
    x1 = [0]
    x2 = [0]
    x3 = [0]
    x4 = [0]
    x5 = [0]
    y  = [0]
    for i in range(sampleCount):
        
        temp_x1 = random.uniform(-1,1)
        temp_x2 = random.uniform(-1,1)
#        temp_y  = isLeft(x1rand_1,x2rand_1,x1rand_2 ,x2rand_2,temp_x1,temp_x2)
        
        temp_x12 = temp_x1*temp_x2
        temp_x1sqr = temp_x1*temp_x1
        temp_x2sqr = temp_x2*temp_x2
        
        temp_y = copysign(1,temp_x1**2 + temp_x2**2 - 0.6)
        
        if i==0:            
            x1[0] = temp_x1
            x2[0] = temp_x2
            x3[0] = temp_x12
            x4[0] = temp_x1sqr
            x5[0] = temp_x2sqr
            y[0] =  temp_y
        else:
            x0.append(1)
            x1.append(temp_x1)
            x2.append(temp_x2)
            x3.append(temp_x12)
            x4.append(temp_x1sqr)
            x5.append(temp_x2sqr)
            y.append(temp_y)
        
    trainingData_x = zip(x0,x1,x2,x3,x4,x5)
    return trainingData_x,y


def linearRegression_calling_function(sampleCount,simulationRunCount):

#    iterationCounter = []
#    Ein = 0.0
    Eout = 0.0

        
    
    for simulationCounter in range(simulationRunCount):
        
        x1rand_1,x2rand_1,x1rand_2 ,x2rand_2 = target_function()        
        trainingData_x,y = transformed_trainingData(sampleCount,x1rand_1,x2rand_1,x1rand_2,x2rand_2)
        
        yNoise = y

        for i in range(int(sampleCount*0.1)):
            randomNoise = choice(range(sampleCount))
            yNoise[randomNoise] = y[randomNoise]*(-1)
        

        linearReg_betas = linearRegression(sampleCount,trainingData_x,yNoise)
        
        testData_x,y_testdata = transformed_trainingData(1000,x1rand_1,x2rand_1,x1rand_2,x2rand_2)
        yNoise_testdata = y_testdata
        for i in range(int(100)):
            randomNoise = choice(range(sampleCount))
            yNoise_testdata[randomNoise] = y_testdata[randomNoise]*(-1)
            
        for i in range(1000):
            if (yNoise_testdata[i] != copysign(1,linearReg_betas[0] + linearReg_betas[1]*testData_x[i][1] + linearReg_betas[2]*testData_x[i][2]
                                                 + linearReg_betas[3]*testData_x[i][3] + linearReg_betas[4]*testData_x[i][4] + linearReg_betas[5]*testData_x[i][5])):
               Eout += 1

    print "The probability of Eout when test data = %d is %f" %(1000,Eout/(1000*simulationRunCount))         

#    print linearReg_betas                   

#    main_calling_function(sampleCount,simulationRunCount,linearReg_betas,trainingData_x,y,x1rand_1,x2rand_1,x1rand_2 ,x2rand_2)        
    return

 #linearRegression_calling_function (1000,1000)
#[-1.00903354 -0.0442585  -0.05639549 -0.1326681   1.54333884  1.59105149]
