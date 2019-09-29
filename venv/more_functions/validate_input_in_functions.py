def score_input(test_name, test_score, invalid_message):
    """
    this function takes the users name and score, if the score is invalid, it will print the message defined
    :param test_name: name user has, is mandatory
    :param test_score: score user has, is not mandatory
    :param invalid_message: optional, default value Invalid test score, try again!
    :return: returns the message of user information
    """
    if invalid_message == "":
        invalid_message = "Invalid test score, try again!"

    while test_name == "":
        test_name = input("Enter your name: ")
        if test_name == "":
            return(invalid_message)

    return "Test name: " + str(test_score)



if __name__ == '__main__':
    test_name = input("Enter your name: ")
    test_score = input("Enter your score: ")
    invalid_message = input("Enter invalid message: ")

    print(score_input(test_name, test_score, invalid_message))
