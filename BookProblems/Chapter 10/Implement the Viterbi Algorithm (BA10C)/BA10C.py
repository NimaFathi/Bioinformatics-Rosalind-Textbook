def viterbi(hidden_path, out_signs, transition_matrix, hidden_transition_matrix, osign_mapper,
            hsign_mapper):
    def calculate_s(s, k, i):
        s_i_k = []
        for j in range(len(out_signs)):
            s_i_k.append(s[-1][j] * transition_matrix[j][osign_mapper[k]] * hidden_transition_matrix[osign_mapper[k]][
                hsign_mapper[i]]
                         )
        return max(s_i_k)

    def backtrack():
        s = []
        for i, hidenChar in enumerate(hidden_path):
            if i == 0:
                s_source = []
                for j in out_signs:
                    s_source.append(1 *
                                    (1 / len(out_signs)) * hidden_transition_matrix[osign_mapper[j]][
                                        hsign_mapper[hidden_path[i]]]
                                    )
                s.append(s_source)
            else:
                s.append([calculate_s(s, k, hidenChar) for k in out_signs])
        n = len(s) - 1
        max_state = s[n].index(max(s[n]))
        path = [out_signs[max_state]]
        while True:
            eval_p = []
            for j in range(len(out_signs)):
                eval_p.append(
                    s[n - 1][j] * transition_matrix[osign_mapper[out_signs[j]]][osign_mapper[out_signs[max_state]]])
            max_state = eval_p.index(max(eval_p))
            path.append(out_signs[max_state])
            n -= 1
            if n <= 0:
                return path[::-1]

    return ''.join(backtrack())


if __name__ == '__main__':
    INPUTFILE = 'rosalind_ba10c.txt'
    OUTPUTFILE = 'rosalind.txt'
    file = open(INPUTFILE, 'r')
    hidden_str = file.readline().replace("\n", "")
    file.readline()
    hidden_signs = list(map(str, file.readline().split()))
    file.readline()
    outcome_signs = list(map(str, file.readline().split()))
    file.readline()
    file.readline()
    transition_matrix = []
    hidden_transition_matrix = []
    for i in range(len(outcome_signs)):
        f = list(map(str, file.readline().split()))
        transition_matrix.append([float(x) for i, x in enumerate(f) if i > 0])
    file.readline()
    file.readline()
    for i in range(len(outcome_signs)):
        f = list(map(str, file.readline().split()))
        hidden_transition_matrix.append([float(x) for i, x in enumerate(f) if i > 0])

    file.close()
    hsign_mapper = {}
    osign_mapper = {}
    for i, sign in enumerate(hidden_signs):
        hsign_mapper[sign] = i
    for i, sign in enumerate(outcome_signs):
        osign_mapper[sign] = i
    file = open(OUTPUTFILE, "w")
    file.write(str(viterbi(hidden_str, outcome_signs, transition_matrix, hidden_transition_matrix, osign_mapper,
                  hsign_mapper)))
