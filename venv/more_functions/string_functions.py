
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
