import math
import sys
import time


def euclidean_distance(data1, data2):
    d = 0.0
    for i in range(0, len(data1)):
        x = (data1[i] - data2[i]) ** 2
        d += x
    return math.sqrt(d)


def minimum_d(datapoint, Centers):
    mindistance = sys.maxsize
    for center in Centers:
        x = euclidean_distance(datapoint, center)
        if (x < mindistance):
            mindistance = x
    return mindistance


def Distortion(Data, Centers):
    distortion = 0
    for data in Data:
        distortion += minimum_d(data, Centers) ** 2

    return 1 / len(Data) * distortion


if __name__ == '__main__':
    start_time = time.time()
    INPUTFILE = "rosalind_ba8b.txt"
    OUTPUTFILE = "ba8b.txt"
    file = open(INPUTFILE, "r")
    k, m = map(int, file.readline().split())
    centers = []
    datapoints = []
    mode = 0
    for line in file:
        if line.__contains__("-"):
            mode = 1
            continue
        if mode == 0:
            centers.append(list(map(float, line.split())))
        else:
            datapoints.append(list(map(float, line.split())))
    file.close()
    file = open(OUTPUTFILE, "w")
    file.write(str(round(Distortion(datapoints, centers), 3)))
    print(time.time() - start_time)
