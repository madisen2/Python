"""Script usage:

# To show the 0th training image with its label data
python dataset_example.py show 0
python dataset_example.py count
"""

import click

## Utility functions
def count_frames(is_test):
    """This function should return the number of sample frames 
    in either the training set (is_test == False) or test set
    (is_test == True).
    """
    raise NotImplementedError()
    return 0


def get_image(is_test, n):
    """Returns the nth image from the training or test set.
    
    Should return the image as an array of floats.
    """
    raise NotImplementedError()
    # im_w is image width, im_h is image height.  The number of 
    # channels is 1 because the images are grayscale.
    return np.zeros((im_h, im_w, 1), dtype=np.float32)


def get_subject(n):
    """For the training set, returns the subject ID number 
    (training set images are named subject_imageNum.tif).
    """
    raise NotImplementedError()
    return 0

                    
def get_target(n):
    """Returns the target for the nth image from the training set.
    
    Note that you do not have targets from the test set.
    
    Should return an array of bytes.
    """
    raise NotImplementedError()
    return np.zeros((im_h, im_w, 1), dtype=np.uint8)
    
    
## Demo functions
def demo_combine(image, target):
    """Blend target into image to highlight the target region.
    """
    raise NotImplementedError()
    
    
def demo_show(image):
    """Shows the image.
    """
    raise NotImplementedError()


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