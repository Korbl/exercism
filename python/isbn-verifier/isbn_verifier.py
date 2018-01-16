def verify(isbn):
    isbn = isbn.replace("-", "")
    if len(isbn) != 10:
        return False
    product = 0
    for a, b in zip(isbn, range(10, 0, -1)):
        if a == 'X' and b == 1:
            a = 10
        try:
            product += int(a) * b
        except:
            return False

    return product % 11 == 0
