from LastColumn import cyclicForm

if __name__ == '__main__':
    text = input()
    form = cyclicForm(text)
    form.sort()
    first_column = ""
    for pattern in form:
        first_column += pattern[0]
    print(first_column)