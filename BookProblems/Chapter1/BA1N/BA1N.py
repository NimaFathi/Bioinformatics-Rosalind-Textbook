def neighbors(pattern, d):
    pattern_length = len(pattern)
    alphabet = ["A", "C", "G", "T"]

    if d == 0:
        return pattern

    if pattern_length == 1:
        return ["A", "C", "G", "T"]

    neighborhood = []
    suffixNeighbors = []
    suffixNeighbors = neighbors(suffix(pattern), d)

    for i in range(len(suffixNeighbors)):

        if hammingDistance(suffix(pattern), suffixNeighbors[i]) < d:
            for j in range(4):
                tempstr = alphabet[j] + suffixNeighbors[i]
                neighborhood.append(tempstr)
        else:
            tempstr = pattern[0] + suffixNeighbors[i]
            neighborhood.append(tempstr)

    return neighborhood


def suffix(str1):
    return str1[1:]


def hammingDistance(str1, str2):
    if len(str1) != len(str2):
        return None

    haming_dist = 0

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            haming_dist += 1

    return haming_dist


if __name__ == '__main__':

    input_str = input()
    d = int(input())

    ans = neighbors(input_str, d)

    for i in ans:
        print(i)
