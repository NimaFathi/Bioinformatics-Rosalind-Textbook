import math
import sys
import time


def FarthestFirstTraversal(Data, k):
    def euclidean_distance(data1, data2):
        d = 0.0
        for i in range(0, len(data1)):
            x = (data1[i] - data2[i]) ** 2
            d += x
        return math.sqrt(d)

    def maximizing_d(Data, Centers):
        datas = list([])
        dataa = []
        for data in Data:
            mindata = sys.maxsize
            for center in Centers:
                x = euclidean_distance(data, center)
                if (x < mindata):
                    mindata = x
                    dataa = data
            datas.append([mindata, dataa])
        x = sorted(datas, reverse=True, key=lambda x: x[0])
        return x[0][1]

    Centers = [Data[0]]
    while (len(Centers) < k):
        x = maximizing_d(Data, Centers)
        Centers.append(x)
    return Centers


if __name__ == '__main__':
    start_time = time.time()
    INPUTFILENAME = "rosalind_ba8a.txt"
    OUTPUTFILENAME = "ba8a.txt"
    file = open(INPUTFILENAME, "r")
    k, m = map(int, file.readline().split())
    datapoints = []
    for line in file:
        ar = list(map(float, line.split()))
        datapoints.append(ar)
    file.close()
    centers = FarthestFirstTraversal(datapoints, k)
    file = open(OUTPUTFILENAME, "w+")
    for center in centers:
        for i in range(0, len(center)):
            if i == len(center) - 1:
                print(center[i])
                file.write(str(center[i]))
                file.write("\n")
            else:
                print(center[i], end=' ')
                file.write(str(center[i]) + " ")
    print("time:", time.time() - start_time)
