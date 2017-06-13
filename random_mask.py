#Madisen Phillips
#Teuscher Labs
#Spring 2017

"""This file is used to generate random masks to test the least squares error
between the result and given mask data."""

import os
import click
from PIL import Image
import numpy as np
from natsort import natsorted
import  PIL.ImageOps
import dataset_example
import matplotlib.pyplot as plt
import math

#Utility Functions
#____________________________________________________________________#

def get_test(n):
    """This function takes a real image target and creates an array
    of random floats (between 0 and 1) of the same size"""

    #loading a mask from the training set to get initial data
    real_mask=dataset_example.get_target(n)

    #finding the size of the initial image
    size=np.shape(real_mask)

    #creating an array of random numbers between 0 and 1
    random_array=np.random.uniform(0,1,(size))

    return random_array
#____________________________________________________________________#

def get_dice(threshold):
    """This function takes the dice coefficient of the test array and the
    real image target array, where real target image array is an array
    collected from get_target"""

    range=dataset_example.count_frames(False)#amount of trianing images
    n=np.random.randint(range)#n is a random image # in rangeof images

    #loading a random array
    random_array=get_test(n)
    #loading a real, but randomly chosen mask
    real_mask=dataset_example.get_target(n)
    #copying the size of the array
    athresh = np.zeros_like(random_array)

    #creating an array that can be used as a threshold
    athresh[:]=0
    athresh[random_array > threshold] = 1


    #function to compare pixel-wise agreement between a and b.
    #When both a and b are empty the Dice coefficient is 1.
    a=(2*(athresh*real_mask).sum())
    b=(athresh.sum()+real_mask.sum())
    dice=a/b

    return dice
#____________________________________________________________________#

def get_plot(N):
    """This function plots the result of the dice coefficient vs. the

    threshold."""
    threshold=np.linspace(0.001,0.99,num=10)#set this to any frequency 0-1
    dice=[]
    plt.figure()
    count=1
    while (count<=N):
        dice=[]
        #at each threshold value, we are taking the dice coefficient
        for i in threshold:
            dice.append(get_dice(i))

       # std=np.asarray(dice).std()
       # yerr=0.1+0.1*std

        plt.errorbar(threshold, dice,fmt='o')
       # plt.plot(threshold,dice,'ro')
       # plt.show()

        #plotting
        plt.xlabel('Threshold (with linspace)')
        plt.ylabel('Dice Coefficient')
        plt.title('Threshold v. Dice Coefficient')
        count=count+1
    plt.show()

    return 0
#______________________________________________________________________#

def get_squares():

    #create a random array for x
    x=np.array((np.random.randint(10,size=10))/10)
    #create an equal length array of equal values of y
    y=np.linspace(0,1,num=len(x))

    #create a coefficient matrix
    A=np.vstack([x,np.ones(len(x))]).T

    #solve for slope and intercept
    m,c=np.linalg.lstsq(A,y)[0]
    #print slope and intercept
    print(m,c)

    #plot original x & y
    #plt.plot(x,y,'o', label='Original data',markersize=10)

    #create an empty array for what will be the best fit line
    e=[]

    #create a best fit line of random data
    for i in x:
        e.append(m*i+c)

    plt.figure()
    #create a plot with error bars to best fit line
    plt.errorbar(y,x,e, marker='^')

    #labels
    plt.xlabel('Threshold (with linspace)')
    plt.ylabel('Random Ints')
    plt.title('Error bars with random ints')


   #plt.plot(x,m*x+c,'r',label='Fitted line')
    #plt.legend()
    plt.show()







   # a=dataset_example.get_target(n)
   # b=get_test(n)

   # h,w=a.shape
   # print(h,w)

   # a.flatten()
   # print(a.shape)

   # h,w=a.shape
   # b.flatten()
   # print(h,w)
   # b=np.vstack([b,np.ones(len(b))]).T
   # print(b.size)
   # print(a.size)
   # a=np.array([0.1,0.2,0.3,0.4,0.5])

   # b=np.array([0.2,0.6,0.8,0.3,0.1])
   # a=np.vstack([a,np.ones(len(a))]).T
   # print(a.size)
   # m,c=np.linalg.lstsq(a,b)[0]
    return 0
#______________________________________________________________________#













@click.command()
def main(**kwargs):
    """Used for file framework"""
    pass


if __name__ == '__main__':
    main()
