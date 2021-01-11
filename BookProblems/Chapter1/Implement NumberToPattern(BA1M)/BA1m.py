def numberToPattern(index, k):
    pattern = ''
    while k > 0:
        reminder = index % 4
        index = index // 4
        k -= 1
        pattern = nucleotides[reminder] + pattern
    return pattern


if __name__ == '__main__':
    INPUT_FILE_NAME = 'rosalind_ba1m.txt'
    OUTPUT_FILE_NAME = 'rosalind.txt'
    file = open(INPUT_FILE_NAME, 'r')
    nucleotides = ['A', 'C', 'G', 'T']
    index = int(file.readline())
    k = int(file.readline())
    file.close()
    file = open(OUTPUT_FILE_NAME, 'w')
    file.write(numberToPattern(index, k))
