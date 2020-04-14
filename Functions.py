# Importing numpy a General-purpose array-processing package
import numpy as np

import collections


# Function to count frequency of each element
# it returns a dictionary data structure whose
# keys are array elements and values are their  corresponding frequencies
def CalculateProbability(arr):
    Dict = collections.Counter(arr)
    for k in Dict.keys():
        Dict[k] = Dict[k] / arr.size
    return Dict


def ImageEncoding(pixelsArr, Dict, blockSize):
    j = 0
    Lower = 0
    if pixelsArr.size % blockSize == 0:
        EncodedArr = np.zeros(int(pixelsArr.size / blockSize))
    else:
        EncodedArr = np.zeros(int(pixelsArr.size / blockSize) + 1)

    while j < int(pixelsArr.size / blockSize):
        i = j * blockSize + 1
        Upper = Dict[pixelsArr[i - 1]]
        k = 1
        while k < blockSize:
            Lower = Lower + (Upper - Lower) * Dict[pixelsArr[i - 1]]
            Upper = Lower + (Upper - Lower) * Dict[pixelsArr[i]]
            i = i + 1
            k = k + 1
        Tag = (Upper + Lower) / 2
        EncodedArr[j] = Tag
        j = j + 1

    if pixelsArr.size % blockSize != 0:
        Upper = Dict[pixelsArr[i]]
        i = i + 1
        while i < pixelsArr.size:
            Lower = Lower + (Upper - Lower) * Dict[pixelsArr[i - 1]]
            Upper = Lower + (Upper - Lower) * Dict[pixelsArr[i]]
            i = i + 1
            print(i)
        Tag = (Upper + Lower) / 2
        EncodedArr[j] = Tag
    return EncodedArr
