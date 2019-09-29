def score_input(test_name, test_score, invalid_message):
    """
    this function takes the users name and score, if the score is invalid, it will print the message defined
    :param test_score: score user has, is not mandatory
    :param invalid_message: optional, default value Invalid test score, try again!
    :return: returns true or false to validate input
    """
    if test_name == "":
        print(invalid_message)
        raise ValueError

    while True:
        if test_score == "":
            test_score = 0
            print(test_name + " " + str(test_score))
            return True
        elif int(test_score) < 0 or int(test_score) > 100:
            print(invalid_message)
            return False
        else:
            print(test_name + " " + str(test_score))
            return True




if __name__ == '__main__':
    try:
        invalid_message = input("Enter error message: ")

        if invalid_message == "":
            invalid_message = "Invalid test score, try again!"

        test_name = None
        while test_name == None:
            test_name = input("Please enter name: ")
            if test_name == "":
                print(invalid_message)
                test_name = None
                continue

        test_score = input("Please enter score: ")

        while score_input(test_name, test_score, invalid_message) == False:
            test_score = input("Please enter score: ")
            score_input(test_name, test_score, invalid_message)

    except ValueError:
        print(invalid_message)
