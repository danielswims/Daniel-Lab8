def encode(password):
    encoded = ''
    for index, num in enumerate(password):
        if int(num) + 3 >= 10:
            encoded += str(int(password[index]) + 3 - 10)
            # list.append(int(password[index]) + 3 - 10)
        else:
            encoded += str(int(password[index]) + 3)
            # list.append(int(password[index]) + 3)
    return encoded


