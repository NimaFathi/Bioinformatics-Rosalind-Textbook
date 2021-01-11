from collections import defaultdict, Counter

if __name__ == '__main__':
    INPUTFILE = 'rosalind_ba10e.txt'
    OUTPUTFILE = 'ba10e.txt'
    file = open(INPUTFILE, 'r')
    threshhold = float(file.readline())
    file.readline()
    alpahbet = list(map(str, file.readline().split()))
    file.readline()
    alignments = []
    counter = 0
    for line in file:
        alignments.append(line.replace("\n", ""))
    file.close()
    ligality = [0 for i in range(len(alignments[0]))]
    count_mutation = 0
    for i in range(len(alignments[0])):
        count_mutation = 0
        for j in range(len(alignments)):
            if alignments[j][i] == '-':
                count_mutation += 1
        if count_mutation / len(alignments) >= threshhold:
            ligality[i] = 0
        else:
            ligality[i] = 1
            counter += 1
    transition_table = [[0 for i in range(3 * counter + 3)] for j in range(3 * counter + 3)]
    v = 2
    rows = {'S': 0, 'I0': 1}
    for i in range(1, counter + 1):
        rows['M' + str(i)] = v
        v += 1
        rows['D' + str(i)] = v
        v += 1
        rows['I' + str(i)] = v
        v += 1
    rows['E'] = v
    emission = defaultdict(list)
    for i in range(len(alignments)):
        count_mutation = 0
        for j in range(len(alignments[0])):
            if ligality[j] == 1:
                count_mutation += 1
                if alignments[i][j] == '-':
                    continue
                else:
                    emission['M' + str(count_mutation)].append(alignments[i][j])
            else:
                if alignments[i][j] == '-':
                    continue
                else:
                    emission['I' + str(count_mutation)].append(alignments[i][j])
    # print(emission)
    states = defaultdict(dict)
    for i in range(len(alignments)):
        count_mutation = 0
        states[i][-1] = 'S'
        for j in range(len(alignments[0])):
            if ligality[j] == 1:
                count_mutation += 1
                if alignments[i][j] == '-':
                    states[i][j] = 'D' + str(count_mutation)
                else:
                    states[i][j] = 'M' + str(count_mutation)
            else:
                if alignments[i][j] == '-':
                    if j == len(alignments[0]) - 1:
                        states[i][j] = 'E'
                    continue
                else:
                    states[i][j] = 'I' + str(count_mutation)
                    if j == len(alignments[0]) - 1:
                        states[i][j + 1] = 'E'
    mydict = defaultdict(list)
    for i in states:
        mystr = ",".join(states[i].values())
        x = mystr.split(",")
        for i in range(len(x)):
            if i < len(x) - 1:
                mydict[x[i]].append(x[i + 1])

    file = open(OUTPUTFILE, 'w')
    for i in rows.keys():
        print("\t" + i, end="")
    print()
    for key, val in rows.items():
        print(key, end=" ")
        x = Counter(mydict[key])
        for j in rows.keys():
            if len(mydict[key]) != 0:
                if x[j] == 0:
                    print(0, end="\t")
                elif x[j] == emission[key]:
                    print(1, end="\t")
                else:
                    print(round(x[j] / len(mydict[key]), 3), end="\t")
            else:
                print(0, end="\t")
        print()
    print('--------')
    for i in alpahbet:
        print("\t" + i, end="")
    print()
    for key, val in rows.items():
        print(key, end="\t")
        x = Counter(emission[key])
        for j in alpahbet:
            if len(emission[key]) != 0:
                if x[j] == 0:
                    print(0, end="\t")
                elif x[j] == len(emission[key]):
                    print(1, end="\t")
                else:
                    print(round(x[j] / len(emission[key]), 3), end="\t")
            else:
                print(0, end="\t")
        print()
