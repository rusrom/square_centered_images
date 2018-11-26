from PIL import Image
from os import listdir
from os import path

# Dimension of the square image
IMAGE_SIZE = (1080, 1080)

# Color of square background
BACKGROUND_COLOR = (255, 255, 255)

# Directories with images
DIR_RAW_IMAGES = 'images'
DIR_SQR_IMAGES = 'ready'

ROOT_PATH = path.dirname(path.abspath(__file__))

# Path of directory with raw images
RAW_PATH = path.join(ROOT_PATH, DIR_RAW_IMAGES)
# Path of directory with square images
SQR_PATH = path.join(ROOT_PATH, DIR_SQR_IMAGES)

# Generator of all raw images in the directory
raw_images = (img for img in listdir(RAW_PATH) if path.isfile(path.join(RAW_PATH, img)))

# Processing raw image to square image
for raw_image in raw_images:
    image = Image.open(path.join(RAW_PATH, raw_image))
    image.thumbnail(IMAGE_SIZE, Image.ANTIALIAS)

    # Square backgroud
    background = Image.new('RGB', IMAGE_SIZE, BACKGROUND_COLOR)

    # Paste image into center of square background
    background.paste(
        image, (int((IMAGE_SIZE[0] - image.size[0]) / 2), int((IMAGE_SIZE[1] - image.size[1]) / 2))
    )

    background.save(path.join(SQR_PATH, raw_image))
