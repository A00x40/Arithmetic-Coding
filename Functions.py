# Importing numpy a General-purpose array-processing package
import numpy as np

import collections


# Function to count frequency of each element
# it returns a dictionary data structure whose
# keys are array elements and values are their  corresponding frequencies
def CalculateProbability(arr):
    Dict = collections.Counter(arr)
    for k in Dict.keys():
        Dict[k] = round(Dict[k] / arr.size, 5)
    return Dict


def ImageEncoding(pixelsArr, Dict, blockSize):
    j = 0

    if pixelsArr.size % blockSize == 0:
        EncodedArr = np.zeros(int(pixelsArr.size / blockSize))
    else:
        EncodedArr = np.zeros(int(pixelsArr.size / blockSize) + 1)

    while j < int(pixelsArr.size / blockSize):
        i = j * blockSize + 1
        Upper = Dict[pixelsArr[i - 1]]
        Lower = 0.0
        while i < blockSize:
            if Scale(Upper, Lower) == 0:
                Upper = 2 * Upper
                Lower = 2 * Lower
            elif Scale(Upper, Lower) == 1:
                Upper = 2 * (Upper - 0.5)
                Lower = 2 * (Lower - 0.5)
            Lower = Lower + round((Upper - Lower) * Dict[pixelsArr[i - 1]], 5)
            Upper = Lower + round((Upper - Lower) * Dict[pixelsArr[i]], 5)

            i = i + 1
        Tag = (Upper + Lower) / 2
        EncodedArr[j] = Tag
        j = j + 1

    if pixelsArr.size % blockSize != 0:
        i = blockSize * int(pixelsArr.size / blockSize)
        while i < pixelsArr.size:
            if Scale(Upper, Lower) == 0:
                Upper = 2 * Upper
                Lower = 2 * Lower
            elif Scale(Upper, Lower) == 1:
                Upper = 2 * (Upper - 0.5)
                Lower = 2 * (Lower - 0.5)
            Lower = Lower + (Upper - Lower) * Dict[pixelsArr[i - 1]]
            Upper = Lower + (Upper - Lower) * Dict[pixelsArr[i]]

            i = i + 1
        Tag = (Upper + Lower) / 2
        EncodedArr[j] = Tag
    return EncodedArr

def Scale(Upper, Lower):
    if Lower >= 0 and Upper <= 0.5:
        return 0
    elif Lower >= 0.5 and Upper <= 1:
        return 1
    else:
        return 2
