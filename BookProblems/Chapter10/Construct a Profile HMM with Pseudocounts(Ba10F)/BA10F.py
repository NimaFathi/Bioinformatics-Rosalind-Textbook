from collections import defaultdict


def profileHMMPseudocounts(threshhold, pseudocount, alphabet, alignments):
    threshhold = threshhold * len(alignments)
    states = []
    insert_index = []
    for i in range(len(alignments[0])):
        total = 0
        for j in range(len(alignments)):
            if alignments[j][i] == '-':
                total += 1
        if total >= threshhold:
            insert_index.append(i)

    emission = {}
    emission['S'] = defaultdict(int)
    emission['E'] = defaultdict(int)
    emission['I0'] = defaultdict(int)
    for i in range(1, len(alignments[0]) - len(insert_index) + 1):
        emission['I' + str(i)] = dict((x, 0) for x in alphabet)
        emission['M' + str(i)] = dict((x, 0) for x in alphabet)
        emission['D' + str(i)] = dict((x, 0) for x in alphabet)

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
    states_dict = defaultdict(dict)
    for i in range(len(alignments)):
        count_mutation = 0
        for j in range(len(alignments[0])):
            if ligality[j] == 1:
                count_mutation += 1
                if alignments[i][j] == '-':
                    states_dict[i][j] = 'D' + str(count_mutation)
                else:
                    states_dict[i][j] = 'M' + str(count_mutation)
            else:
                if alignments[i][j] == '-':
                    if j == len(alignments[0]) - 1:
                        states_dict[i][j] = 'E'
                    continue
                else:
                    states_dict[i][j] = 'I' + str(count_mutation)
                    if j == len(alignments[0]) - 1:
                        states_dict[i][j + 1] = 'E'
    for key, value in states_dict.items():
        states.append(list(states_dict[key].values()))

    for i in range(len(alignments)):
        current_index = 1
        for j in range(len(alignments[i])):
            if j in insert_index:
                if alignments[i][j] != '-':
                    emission['I' + str(current_index - 1)][alignments[i][j]] += 1
            else:
                if alignments[i][j] != '-':
                    emission['M' + str(current_index)][alignments[i][j]] += 1
                current_index += 1

    for key in emission:
        if key != 'S' and key != 'E' and not key.startswith('D'):
            total = 0
            for subk in emission[key]:
                total += emission[key][subk]
            if total > 0:
                sub_total = 0
                for subk in emission[key]:
                    emission[key][subk] = (1.0 * emission[key][subk]) / total + pseudocount
                    sub_total += 1.0 * emission[key][subk]
                for subk in emission[key]:
                    emission[key][subk] = emission[key][subk] / sub_total
            else:
                for subk in emission[key]:
                    emission[key][subk] = 1.0 / len(alphabet)
    transition = defaultdict()
    transition['S'] = defaultdict(int)
    transition['S']['I0'] = 0
    transition['S']['M1'] = 0
    transition['S']['D1'] = 0
    for i in states:
        transition['S'][i[0]] += 1
    transition['I0'] = defaultdict(int)
    transition['I0']['I0'] = 0
    transition['I0']['M1'] = 0
    transition['I0']['D1'] = 0

    for i in range(len(states)):
        for j in range(len(states[i]) - 1):
            if states[i][j] not in transition:
                transition[states[i][j]] = {}
            if states[i][j + 1] not in transition[states[i][j]]:
                transition[states[i][j]][states[i][j + 1]] = 0
            transition[states[i][j]][states[i][j + 1]] += 1
        if not states[i][len(states[i]) - 1] in transition:
            transition[states[i][len(states[i]) - 1]] = {}
        if not 'E' in transition[states[i][len(states[i]) - 1]]:
            transition[states[i][len(states[i]) - 1]]['E'] = 0
        transition[states[i][len(states[i]) - 1]]['E'] += 1

    if 'I' + str(len(alignments[0]) - len(insert_index)) not in transition:
        transition['I' + str(len(alignments[0]) - len(insert_index))] = {}
        if not 'E' in transition['I' + str(len(alignments[0]) - len(insert_index))]:
            transition['I' + str(len(alignments[0]) - len(insert_index))]['E'] = 0

    if 'D' + str(len(alignments[0]) - len(insert_index)) not in transition:
        transition['D' + str(len(alignments[0]) - len(insert_index))] = {}
        if not 'E' in transition['D' + str(len(alignments[0]) - len(insert_index))]:
            transition['D' + str(len(alignments[0]) - len(insert_index))]['E'] = 0

    if 'M' + str(len(alignments[0]) - len(insert_index)) not in transition:
        transition['M' + str(len(alignments[0]) - len(insert_index))] = {}
        if not 'E' in transition['M' + str(len(alignments[0]) - len(insert_index))]:
            transition['M' + str(len(alignments[0]) - len(insert_index))]['E'] = 0

    for i in range(1, len(alignments[0]) - len(insert_index) + 1):
        if not 'I' + str(i) in transition:
            transition['I' + str(i)] = {}
        if not 'M' + str(i) in transition:
            transition['M' + str(i)] = {}
        if not 'D' + str(i) in transition:
            transition['D' + str(i)] = {}

    for key in transition:
        if key != 'E':
            total = 0
            for subk in transition[key]:
                total += transition[key][subk]
            if key != 'S' and key != 'I0':
                if key[1:] != str(len(alignments[0]) - len(insert_index)):
                    if not 'I' + key[1:] in transition[key]:
                        transition[key]['I' + key[1:]] = 0
                    if not 'D' + str(int(key[1:]) + 1) in transition[key]:
                        transition[key]['D' + str(int(key[1:]) + 1)] = 0
                    if not 'M' + str(int(key[1:]) + 1) in transition[key]:
                        transition[key]['M' + str(int(key[1:]) + 1)] = 0
                else:
                    if not 'I' + key[1:] in transition[key]:
                        transition[key]['I' + key[1:]] = 0
                    if not 'E' in transition[key]:
                        transition[key]['E'] = 0

            for subk in transition[key]:
                if total > 0:
                    transition[key][subk] = 1.0 * transition[key][subk] / total
                    transition[key][subk] = (transition[key][subk] + pseudocount) / (
                                1 + pseudocount * len(transition[key]))
                else:
                    if len(transition[key]) == 3:
                        transition[key][subk] = 1.0 / 3
                    if len(transition[key]) == 2:
                        transition[key][subk] = 1.0 / 2

    return transition, emission


if __name__ == '__main__':
    INPUTFILE = 'rosalind_ba10f.txt'
    file = open(INPUTFILE, 'r')
    ll = list(map(str, file.readline().split("\t")))
    threshhold = float(ll[0])
    pseudocount = float(ll[1].replace("\n", ""))
    file.readline()
    alpahbet = list(map(str, file.readline().split()))
    file.readline()
    alignments = []
    counter = 0
    for line in file:
        alignments.append(line.replace("\n", ""))
    file.close()
    transition, emission = profileHMMPseudocounts(threshhold, pseudocount, alpahbet, alignments)
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

    for i in rows.keys():
        print("\t" + i, end="")
    print()
    for key, value in rows.items():
        print(key, end="\t")
        if key == 'E':
            for j in rows.keys():
                print(0, end="\t")
            print()
            continue

        for j in rows.keys():
            if j in transition[key].keys():
                print(round(transition[key][j], 3), end="\t")
            else:
                print(0, end="\t")
        print()
    print("--------")
    for key in rows.keys():
        print(key, end="\t")
        if key == 'E':
            for j in alpahbet:
                print('0', end="\t")
            continue
        for j in alpahbet:
            print(round(emission[key][j], 3), end="\t")
        print()
