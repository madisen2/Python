"""Script usage:

# To show the 0th training image with its label data
python dataset_example.py show 0
python dataset_example.py count
"""
import os
import click
from PIL import Image
import numpy as np
from natsort import natsorted

REAL_PATH_TEST="/u/madisen2/Python/Nerve_Segmentation/test"
REAL_PATH_TRAIN="/u/madisen2/Python/Nerve_Segmentation/train"



def get_imlist(path):

    """Returns a list or filenames for all tif images in a directory."""
    imlist=get_imlist(path)

     return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.tif')




def count_frames(is_test):
    """This function should return the number of sample frames
    in either the training set (is_test == False) or test set
    (is_test == True).
    """

    if is_test:

        images=get_imlist(REAL_PATH_TEST)

    else:
        images=get_imlist(REAL_PATH_TRAIN)


    im=array(Image.open(images[0])) #open one image to get size

    im_h,im_w=im.shape[0:2] #get the size of the images

    imnbr=len(images) #get the number of images

    #create matrix to store all flattened images
    immatrix=array([array(Image.open(im)).flatten()
            for im in images],'f'

    return 0


def get_image(is_test, n):
    """Returns the nth image from the training or test set.

    Should return the image as an array of floats.
    """
    # im_w is image width, im_h is image height.  The number of
    # channels is 1 because the images are grayscale.
    if is_test:
        im_sort=natsorted(REAL_PATH_TEST)
    else:
        im_sort=natsorted(REAL_PATH_TRAIN)

    image = Image.open(im_sort)
    image.load()
    data = np.asarray ( image, dtype="int32" )
    return data

def get_subject(n):
    """For the training set, returns the subject ID number
    (training set images are named subject_imageNum.tif).
    """
    subject_ID=os.path.basename(im_sort).split('_')[0]

    """uses the same filename as get_image"""

    raise NotImplementedError()
    return 0


def get_target(n):
    """Returns the target for the nth image from the training set.

    Note that you do not have targets from the test set.

    Should return an array of bytes.
    """
"""need to load the mask data"""

    return np.zeros((im_h, im_w, 1), dtype=np.uint8)

## Demo functions
def demo_combine(image, target):
    """Blend target into image to highlight the target region.
    """
    image=Image.fromarray(data, 'RGB')
    image = Image.composite(image,target)



def demo_show(image):
    """Shows the image.
    """
    image.show()

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
    result.
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
