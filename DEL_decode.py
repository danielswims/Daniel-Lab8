
def decode(password):
    decoded = ''
    for index, num in enumerate(password):
        if int(num) - 3 < 0:
            decoded += str(int(password[index]) - 3 + 10)
            # list.append(int(password[index]) + 3 - 10)
        else:
            decoded += str(int(password[index]) - 3)
            # list.append(int(password[index]) + 3)
    return decoded