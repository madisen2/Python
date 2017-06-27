"""Script usage:# To show the 0th training image with its label
python dataset_example.py show 0
python dataset_example.py count"""

import os
import click
from PIL import Image
import numpy as np
from natsort import natsorted
import PIL.ImageOps

REAL_PATH_TRAIN="/u/madisen2/tlab/Nerve_Segmentation/train"

#_______________________________________________________________________#

def get_imlist(is_test):

    """Returns a list of file names based off of the path provided."""

    if is_test:#setting path to test files
        path="/u/madisen2/tlab/Nerve_Segmentation/test"

    else:#setting path to train files, filtering out the masks
        path="/u/madisen2/tlab/Nerve_Segmentation/train"


    #sorting the selected files naturally
    file_names=os.listdir(path)
    file_names=[
            os.path.join(path,p)
            for p in file_names
            if not p.endswith('mask.tif')]
    file_names=natsorted(file_names)

    return file_names

#_________________________________________________________________________#


def count_frames(is_test):

    """Counts the number of sample frames in either the training
    set or test set."""

    number_frames=len(get_imlist(is_test))
    return number_frames


#_________________________________________________________________________#


def get_image(n,is_test):

    """Returns the nth image from the training or test set.
    Should return the image as an array of floats."""

    subject = Image.open((get_imlist(is_test))[n]).convert("RGB")
    subject_array=np.asarray(subject,dtype=np.float32)

    return subject_array/255

#_______________________________________________________________________#


def get_subject(n):

    """For the training set, returns the subject ID number
    (training set images are named subject_imageNum.tif)."""

    subject_ID=os.path.basename((get_imlist(False)[n])).split('_')[0]

    return subject_ID


#_______________________________________________________________________#


def get_target(n):

    """Returns the target for the nth image from the training set.
    Note that you do not have targets from the test set.
    Should return an array of bytes.
    need to load the mask data"""


#    mask=Image.open(str(get_imlist(n)+'mask.tif').convert("RGB")

    mask=Image.open(REAL_PATH_TRAIN+'/'+os.path.basename((get_imlist(False)[n])).split('.')[0]+'_mask.tif').convert("RGB")

   # mask=Image.open(REAL_PATH_TRAIN+'/'+
   #str(get_subject(n))+'_'+str(n)+'_mask.tif').convert("RGB")
    mask_array=np.array(mask, dtype='float32')

    return mask_array/255

#_______________________________________________________________________#


def demo_combine(n):

    """Blend target into image to highlight the target region."""


    subject=Image.fromarray(np.asarray(get_image(n,False)*255,dtype=np.uint8),"RGB"
            ).show()
    #calling the get_image function to retrieve the subject image

    #grabbing dimensions that will define the size of the highlight image

    highlight=Image.new("RGB",(580,420),(255))
    #creating an image that will have the color we want to highlight with

    mask=Image.fromarray(np.asarray(get_target(n)*255,dtype=np.uint8),"RGB")
    mask=PIL.ImageOps.invert(mask)
    #calling get_image to retrieve the mask image for the associated subject


    mask=mask.convert('L')
    mask=Image.eval(mask,lambda p:(255-(255-p)//3))

    combined= Image.composite(#combining all 3 images above together
            subject,
            highlight,mask).show()


    return combined

#_______________________________________________________________________#


def demo_show(image):

    return image.show()


#________________________________________________________________________#


@click.group()
def main(**kwargs):
    """Don't worry about this function; it is a placeholder for the
    click framework.
    """
    pass


@main.command()
@click.option('--test/--train', default=False)
def count(**kwargs):
    """Counts the number of frames in either the training or testing set.
    """
    print(count_frames(kwargs['test']))


@main.command()
@click.option('--test/--train', default=False)  # is_test
@click.argument('n', type=int)
def show(**kwargs):
    """Loads and combines the image and target data and shows the
    result.https://mail.google.com/mail/u/0/
    """
    is_test = kwargs['test']
    n = kwargs['n']
    image = get_image(is_test, n)
    if not is_test:
        target = get_target(is_test, n)
        demo_combine(image, target)
    demo_show(image)

if __name__ == '__main__':
    main()

