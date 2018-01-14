def is_isogram(string):
    check_string = ""
    for i in string.lower():
        if i in check_string and i.isalpha():
            return False
        else:
            check_string = check_string + i

    return True
