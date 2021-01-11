def suffixArray(s):
    suffixes = [(s[i:], i) for i in range(len(s))]
    suffixes.sort()
    return [s[1] for s in suffixes]


# didnt used
def binary_search(list, pattern, first, last):
    middle = (first + last) // 2
    if last >= first:
        if (pattern == text[list[middle]:]):
            return middle
        elif (pattern < text[list[middle]:]):
            return binary_search(list, pattern, first, middle - 1)
        else:
            return binary_search(list, pattern, middle + 1, last)
    else:
        return -1


if __name__ == '__main__':
    text = input()
    output = []
    patterns = []
    suffix_array = suffixArray(text)
    while True:
        try:
            x = input()
            patterns.append(x)
        except:
            break

    for pattern in patterns:
        for i in suffix_array:

            if (text[i:i + len(pattern)] == pattern):
                output.append(i)
                continue
            if (len(text[i:]) > len(pattern) and text[i:] > pattern):
                break
    output.sort()
    for out in output:
        print(out, end=" ")
