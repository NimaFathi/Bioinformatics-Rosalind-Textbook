from LinkeedList.LinkedList import LinkedList, Node


def btw_array_generator(forms):
    bwt = ''
    for form in forms:
        bwt += form[len(form) - 1]
    return bwt


def firstColumn_generator(forms):
    first_column = ""
    for form in forms:
        first_column += form[0]
    return first_column


def FirstToLast_array(dsign):
    l_shift = [dsign]
    for i in llist_array:
        for j in i:
            l_shift.append(j.value)
    return l_shift


def orginal_pattern(l_shift, bwt):
    current = l_shift[l_shift[0]]
    orginalP = ''
    for i in range(len(bwt)):
        orginalP += bwt[current]
        current = l_shift[current]
    return orginalP


if __name__ == '__main__':
    bwt = input()
    chars = list(bwt)
    chars.sort()
    first_column = firstColumn_generator(chars)
    A_llist = LinkedList()
    T_llist = LinkedList()
    C_llist = LinkedList()
    G_llist = LinkedList()
    for i in range(len(bwt) - 1, -1, -1):
        ch = bwt[i]
        node = Node(i)
        if ch == 'A':
            A_llist.insert_head(node)
        elif ch == 'T':
            T_llist.insert_head(node)
        elif ch == 'C':
            C_llist.insert_head(node)
        elif ch == 'G':
            G_llist.insert_head(node)
        else:
            dsign = i
    llist_array = [A_llist, C_llist, G_llist, T_llist]
    firstLast = FirstToLast_array(dsign)
    print(firstLast)
    print(orginal_pattern(firstLast, bwt))
