def encode(message):
    encoded_message = "" # define the string of the encoded message
    i = 0
    while i <= len(message) - 1: # first loop to run through the string
        count = 1
        ch = message[i]
        j = i
        while j < len(message) - 1: # second loop to check if there's multiples 0
            if message[j] == message[j + 1]:
                count = count + 1
                j = j + 1
            else:
                break
        if ch == "0": # just print those repeated 0's
            encoded_message = encoded_message + str(count) + ch
        else:
            encoded_message = encoded_message + ch
        i = j + 1
    print(encoded_message)


if __name__ == '__main__':
    code = input("Introduce the chain that you want to encode: ")
    encode(code)