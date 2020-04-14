from Functions import *
from tempfile import TemporaryFile
import cv2  # Import openCV
import \
    sys  # import Sys. Sys will be used for reading from the command line.

# We give Image name parameter with  extension when we will run python script


# Read the image. The first Command line argument is the image
# Image read Grayscale specifies to load an image in grayscale mode
image = cv2.imread(sys.argv[1], cv2.IMREAD_GRAYSCALE)

# Read number from Command Line
blockSize = int(input())

# Create Image array

imageArr = np.array(image)

# Flatten 2D numpy array to 1D
pixelsArr = imageArr.flatten()


# Call CountFrequency to get probability
GrayDict = CalculateProbability(pixelsArr)

# Call ImageEncoding to encode pixels array
EncodedArr = ImageEncoding(pixelsArr, GrayDict, blockSize)

outfile = TemporaryFile()
np.save('outfile', EncodedArr)
