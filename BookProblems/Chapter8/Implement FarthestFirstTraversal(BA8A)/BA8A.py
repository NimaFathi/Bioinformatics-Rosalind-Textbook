import math
import sys
import time


def farthest_first_traversal(Data, k):
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

    centers = [Data[0]]
    while (len(centers) < k):
        x = maximizing_d(Data, centers)
        centers.append(x)
    return centers


if __name__ == '__main__':
    start_time = time.time()
    INPUT_FILE_NAME = "rosalind_ba8a.txt"
    OUTPUT_FILE_NAME = "ba8a.txt"
    file = open(INPUT_FILE_NAME, "r")
    k, m = map(int, file.readline().split())
    data_points = []
    for line in file:
        ar = list(map(float, line.split()))
        data_points.append(ar)
    file.close()
    centers = farthest_first_traversal(data_points, k)
    file = open(OUTPUT_FILE_NAME, "w+")
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
