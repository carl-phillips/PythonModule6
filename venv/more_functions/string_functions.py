"""
Carl Phillips, this function takes a message and multiplies it
:param : message, the message you choose
:param : n, the number of times to see the message
:returns : the message multiplied
"""
def multiply_string(message, n):
    multiplied_message = ""

    for i in range(n):
        multiplied_message += str(message)

    return multiplied_message


if __name__ == '__main__':
    try:
        message = "Hello "
        print(multiply_string(message, 7))
    except Exception as err:
        print("Error " + str(err))
