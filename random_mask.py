#Madisen Phillips
#Teuscher Labs
#Spring 2017

"""This file is used to generate random masks to test the least squares error
between the result and given mask data."""



import os,click,PIL, numpy as np, natsort,PIL.ImageOps,dataset_example
import matplotlib.pyplot as plt, math, tkinter
from PIL import Image

def init_ipython():
    return {
            'np': np,
            'os': os,
            }

#import scipy.stats as stats
#Utility Functions
#____________________________________________________________________#

def get_random_array():
    """This function takes a real image target and creates an array
    of random floats (between 0 and 1) of the same size"""

    #loading a mask from the training set to get initial data
    real_mask=dataset_example.get_target(get_random())

    #finding the size of the initial image
   # size=np.shape(real_mask)
    size=(420,580)
    #creating an array of random numbers between 0 and 1
    random_array=np.random.uniform(0,1,(size))

    return random_array
#____________________________________________________________________#

def get_random():
    """This function loads a random mask and random threshold to be"""
    """evaluated in get dice."""

    range=dataset_example.count_frames(False)#amount of trianing images
    n=np.random.randint(range)#n is a random image # in rangeof images
    n=43
    return n
#___________________________________________________________________#


def get_real_mask():

    #loading a real, but randomly chosen mask
    real_mask=dataset_example.get_target(get_random())

    return real_mask

#_____________________________________________________________________#

def get_dice(random_array,real_mask,threshold):
    """This function takes the dice coefficient of the test array and the
    real image target array, where real target image array is an array
    collected from get_target"""

    #copying the size of the array
    athresh = np.zeros_like(random_array)

    #creating an array that can be used as a threshold
    athresh[:]=0
    athresh[random_array > threshold] = 1

    #function to compare pixel-wise agreement between a and b.
    #When both a and b are empty the Dice coefficient is 1.
    a=(2*(athresh*real_mask).sum())
    b=(athresh.sum()+real_mask.sum())+1e-6
    dice=a/b

    return dice
#____________________________________________________________________#

def get_plot(random_array,real_mask,N):#N):
    """This function plots the result of the dice coefficient vs. the
    threshold."""

    thresholds=1000
    #setting threshold values, starting small, can manipulate later
    threshold=np.linspace(-0.5,0.5,num=thresholds)#set this to any frequency 0-1

    #initializing loop variables
    count=0
    dice=[]

    #initializing function variables
    #real_mask=get_real_mask()
    #random_array=get_random_array()

    while (count<N):

        dice.append([])#priming the dice array to store values

        for i in threshold:
            dice[count].append(get_dice(random_array,real_mask,i))
        count=count+1

    print(dice)


    plt.figure()#beginning figure
    dice=np.asarray(dice)#dice becomes a numpy array

    #initializing loop variables
    means=[]
    stds=[]
    count=0

    #getting mean and standard deviations
    while (count<thresholds):

        means.append(dice[:,count].mean())
        stds.append(dice[:,count].std())
        count=count+1

    #plotting with caps on the standard deviation error bars
    (_, caps, _)=plt.errorbar(threshold,means,yerr=stds)

    #labels for plotting

    plt.xlabel('Threshold (with linspace)')
    plt.ylabel('Dice Coefficient')
    plt.title('Threshold v. Dice Coefficient with '+str(N)+' images')
    plt.show()

    return dice
#_____________________________________________________________________#

def get_subject(n):
    subject_image=dataset_example.get_image(n,False)

    return subject_image

#____________________________________________________________________#


def get_subject_mask(n):
    subject_mask=dataset_example.get_target(n)

    return subject_mask

#______________________________________________________________________#

def make_image():

    image=np.zeros((420,580))
    image[0:210,0:290]=1
    image[210:420,290:580]=1


    return image

#______________________________________________________________________#

def make_mask():

    mask=np.zeros((420,580))
    mask[0:210,0:290]=1
    mask[210:420,290:580]=1

    return mask



#___________________________________________________________________#

def get_padding(image_pad):

    """This function pads images with zeros on all sides"""

    image_pad=np.pad(image_pad,(10,10),'constant',constant_values=0)

    return image_pad


#_____________________________________________________________________#

def get_rc(n):

    subject_image=get_subject(n)
    rows=np.linspace(0,len(subject_image)-1,len(subject_image))
    cols=np.linspace(0,len(subject_image[0])-1,len(subject_image[0]))
    rows=rows.astype(int)
    cols=cols.astype(int)

    return rows, cols

#____________________________________________________________________#


def get_b(n):#(subject_image,subject_mask):#n):

    #loading the images that will be used in least squares method
    subject_image=get_subject(n)
    subject_mask=get_subject_mask(n)

    #padding the images
    subject_image=get_padding(subject_image)
    subject_mask=get_padding(subject_mask)

    #loop variables
    rows,cols=get_rc(n)#subject_image)#n)
    b=[]
    for i in rows:
        for j in cols:
            if (1==subject_mask[i,j].mean()):
                b.append(1)
            else:
                b.append(0)

    b=np.asarray(b)
    return b
#______________________________________________________________________#


def get_squares(areas,b):

    least_squares=np.linalg.lstsq(areas,b)


    return least_squares

#_____________________________________________________________________#

def get_areas(n):

    #loading and padding the image
    subject_image=get_subject(n)
    subject_image=get_padding(subject_image)

    #setting loop varibles
    rows,cols=get_rc(n)
    areas=[]

    for i in rows:
        for j in cols:
            areas.append(subject_image[i:i+21,j:j+21])

    length=len(areas)
    count=0

    while count<length:
        areas[count]=areas[count].flatten()
        count=count+1

    return areas#np.asarray(areas)
#_____________________________________________________________________#

def get_estimated(subject_image,subject_mask):#n):


    x_b=get_b(subject_image,subject_mask)#n)
    areas=get_areas(subject_image)#n)
    coefficients=get_squares(areas,x_b)[0]
    b_new=[]
    count=0


    while count<len(areas):#dataset_example.count_frames(False):#5636:#243600:

        b_new.append((coefficients*areas[count]).sum())
        count=count+1

    b_new=np.asarray(b_new)
    b_new=b_new/(b_new.max())

    count=0

#    while count<len(b_new):
 #       if b_new[count]<0:
  #          b_new[count]=0
   #     count=count+1
   # count=0


    b_new=np.reshape(b_new,(420,580))
   # temp=Image.fromarray(np.asarray(b_new*255,dtype=np.uint8),"L").show()

    return b_new

#______________________________________________________________________#

def stitch(mask,estimated_mask):

    mask=Image.fromarray(np.asarray(mask*255,dtype=np.uint8),"L")
    estimated_mask=Image.fromarray(np.asarray(estimated_mask*255,dtype=np.uint8),"L")
    mask.save("mask.png")
    estimated_mask.save("estimated_mask.png")
    image1=Image.open("mask.png")
    image2=Image.open("estimated_mask.png")

    (width1,height1)=image1.size
    (width2,height2)=image2.size

    result_width=width1+width2
    result_height=max(height1,height2)

    result=Image.new("L",(result_width,result_height))
    result.paste(im=image1,box=(0,0))
    result.paste(im=image2,box=(width1,0))
    result.show()
    result.save("stitch.png")

    return 0


#_______________________________________________________________________#


    array=np.asarray([0,1,0,1])
    array=np.reshape(array,(2,2))

    return array

#_________________________________________________________________________



@click.command()
def main(**kwargs):
    """Used for file framework"""
    pass


if __name__ == '__main__':
    main()
