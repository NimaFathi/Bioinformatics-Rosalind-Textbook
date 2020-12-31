import math
import random
import sys
import time


def euclidean_distance(data1, data2):
    d = 0.0
    for i in range(0, len(data1)):
        x = (data1[i] - data2[i]) ** 2
        d += x
    return math.sqrt(d)


def nearest_center(data, Centers):
    minVal = sys.maxsize
    index = len(Centers)
    for i, center in enumerate(Centers):
        x = euclidean_distance(data, center)
        if x < minVal:
            minVal = x
            index = i
    return [data, index]


def Lloyd(Data, k):
    centers = []

    def K_centers(Data, Centers):
        data_table = []
        for data in Data:
            data_table.append(nearest_center(data, Centers))
        return data_table

    def K_cluster(Data_table, k):
        sample = [0] * len(Data_table[0][0])
        Centers = [sample] * k
        count = [0] * k
        for data, index in Data_table:
            count[index] += 1
            Centers[index] = [sum(x) for x in zip(Centers[index], data)]
        for i in range(k):
            Centers[i] = [x / count[i] for x in Centers[i]]
        return Centers

    for i in range(0, k):
        random_choice = Data[i]
        centers.append(random_choice)

    i = 0

    while i < 1000:
        last = centers.copy()
        data_table = K_centers(Data, centers)
        centers = K_cluster(data_table, k)
        if last == centers:
            break
        i += 1
    return centers


if __name__ == '__main__':
    INPUTFILENAME = "rosalind_ba8c.txt"
    OUTPUTFILENAME = "ba8c.txt"
    start_time = time.time()
    file = open(INPUTFILENAME, "r")
    k, m = map(int, file.readline().split())
    dataPoints = []
    for line in file:
        dataPoints.append(list(map(float, line.split())))
    centers = Lloyd(Data=dataPoints, k=k)
    file = open(OUTPUTFILENAME, "w")
    for center in centers:
        X = ' '.join('{0:.3f}'.format(el) for el in center)
        file.write(str(X))
        file.write("\n")
    print("Runing Time:",time.time() - start_time)
