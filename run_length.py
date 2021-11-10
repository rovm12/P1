
def encode(message):
    encoded_message = ""
    i = 0
    while i <= len(message) - 1:
        count = 1
        ch = message[i]
        j = i
        while j < len(message ) -1:
            if message[j] == message[j +1] and message[j] == "0":
                count = count + 1
                encoded_message = encoded_message + str(count) + ch
                j = j+ 1
            else:
                break
        encoded_message = encoded_message  + ch
        i = j + 1
    print(encoded_message)


if __name__ == '__main__':
    encode("0032009")