def verify(isbn):
    if not isbn:
        return False
    count = 10
    product = 0
    for i in isbn.replace('-', ''):
        if i == 'X' and count == 1:
            i = 10
        try:
            product += int(i) * count
            count -= 1
        except:
            return False

    return product % 11 == 0
