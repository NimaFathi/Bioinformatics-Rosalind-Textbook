def markov_hidden_path(hidden_path, outcome_path, transition_matrix, hmapper, omapper):
    p = 1
    for i, sign in enumerate(hidden_path):
        p *= transition_matrix[osign_mapper[outcome_path[i]]][hsign_mapper[hidden_path[i]]]
    return p


if __name__ == '__main__':
    INPUT_FILE_NAME = 'rosalind_ba10b.txt'
    OUTPUT_FILE_NAME = 'ba10b'
    file = open(INPUT_FILE_NAME, 'r')
    hidden_str = file.readline().replace("\n", "")
    file.readline()
    hidden_signs = list(map(str, file.readline().split()))
    file.readline()
    outcome_str = file.readline().replace("\n", "")
    file.readline()
    outcome_signs = list(map(str, file.readline().split()))
    file.readline()
    file.readline()
    transition_matrix = []
    for i in range(len(outcome_signs)):
        f = list(map(str, file.readline().split()))
        transition_matrix.append([float(x) for i, x in enumerate(f) if i > 0])
    file.close()
    hsign_mapper = {}
    osign_mapper = {}
    for i, sign in enumerate(hidden_signs):
        hsign_mapper[sign] = i
    for i, sign in enumerate(outcome_signs):
        osign_mapper[sign] = i
    file = open(OUTPUT_FILE_NAME, "w")
    file.write(str(markov_hidden_path(hidden_str, outcome_str, transition_matrix, hsign_mapper, osign_mapper)))
