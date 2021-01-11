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


def generateAllGen(d):
    base_str = ""
    alphabet = ["A", "C", "G", "T"]
    for i in range(d):
        base_str += "A"
    mylist = neighbors(base_str, d)
    return mylist


def frequentMismatch(test_string, pattern, d):
    ans = 0
    length = len(pattern)
    for i in range(len(test_string) - length + 1):
        mystr = test_string[i:i + length]
        if hammingDistance(mystr, pattern) <= d:
            ans += 1
    return ans


if __name__ == '__main__':

    input_str = input()
    k, d = map(int, input().split())
    gen_list = generateAllGen(k)
    temp_max = []
    max_num = 0
    for i in gen_list:
        x = frequentMismatch(input_str, i, d)
        if x > max_num:
            max_num = x
            temp_max.clear()
            temp_max.append(i)
        if x == max_num and i not in temp_max:
            temp_max.append(i)

    for i in temp_max:
        print(i, end=" ")
