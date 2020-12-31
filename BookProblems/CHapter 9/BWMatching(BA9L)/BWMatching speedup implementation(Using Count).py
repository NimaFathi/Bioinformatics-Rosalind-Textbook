import time
def generate_firstOccurrence(lastcolumn):
    lastcolumn.sort()
    first_occurrence = [0]
    last = 0
    for i in range(1, len(lastcolumn) - 1):
        if lastcolumn[i] != lastcolumn[last]:
            first_occurrence.append(i)
        last = i
    return first_occurrence

def charIndex(char):
    alphabetic_order = ['$', 'A', 'C', 'G', 'T']
    for i in range(len(alphabetic_order)):
        if char == alphabetic_order[i]:
            return i

def count(bwt):
    CountArray = list()
    dollar_count = 0
    A_count = 0
    C_count = 0
    G_count = 0
    T_count = 0
    for ch in bwt:
        count = [dollar_count, A_count, C_count, G_count, T_count ]
        CountArray.append(count)
        if ch == '$':
            dollar_count += 1
        elif ch == 'A':
            A_count += 1
        elif ch == 'C':
            C_count += 1
        elif ch == 'G':
            G_count +=1
        else:
            T_count += 1

    CountArray.append([dollar_count,A_count,C_count,G_count,T_count])
    return CountArray

def checker(char, bwt, top, bottom):
    container = []
    for i in range(top, bottom + 1):
        if bwt[i] == char:
            container.append(i)
    if not container:
        return -1, -1
    return container[0], container[-1]

def BetterBWMatching(firstOccurrence, count, lastColumn, pattern):
    top = 0
    bottom = len(lastColumn) - 1
    while top <= bottom:
        if pattern:
            ch = pattern[len(pattern) - 1]
            pattern = pattern[:-1]
            returned = checker(ch, lastColumn, top, bottom)
            if returned[0] > -1:
                chIndex = charIndex(ch)
                #print(ch)
                #print(chIndex)
                top = firstOccurrence[chIndex] + count[top][chIndex]
                #print(top)
                bottom = firstOccurrence[chIndex] + count[bottom + 1][chIndex] - 1
            else:
                return 0
        else:
            return bottom - top + 1




if __name__ == '__main__':
    start = time.time()
    INPUTFILETEXT = "rosalind_ba9m.txt"
    input_file = open(INPUTFILETEXT, "r")
    text = input_file.readline()
    text = text[:-1] #ignore \n
    bwt = list(text)
    patterns = list(map(str, input_file.readline().split()))
    input_file.close()
    first_occurrence = generate_firstOccurrence(bwt.copy())
    count_array = count(bwt)
    file = open("ba9m.txt", "w+")
    for pattern in patterns:
        file.write(str(BetterBWMatching(first_occurrence, count_array, bwt, pattern)))
        file.write(' ')
    file.close()
    end = time.time()
    print(end - start)