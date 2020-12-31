def cyclicForm(pattern):
    length = len(pattern)
    form = [pattern]

    def cyclicFormed(pattern , k ):
        old = pattern
        new = [0] * len(pattern)
        for i in range(k):
            new[0] = old[-1]
            new[1:] = old[:-1]
            old = new.copy()
        return ''.join(new)

    for i in range(1, length):
        x = cyclicFormed(pattern,i)
        form.append(x)
    return form

if __name__ == '__main__':
    text = input()
    form = cyclicForm(text)
    form.sort()
    BWT = ''
    for pattern in form:
        BWT += pattern[len(pattern) - 1]
    print(BWT)