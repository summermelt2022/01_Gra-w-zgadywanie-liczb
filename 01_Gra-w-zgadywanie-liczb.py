from random import randint


def guess(n, k):
    """
    Comparison between computer random chosen number and user chosen number.
    :param n: User chosen number.
    :param k: Computer random chosen number.
    :return: String sentence.
    """
    if not n.isnumeric():
        return "It's not a number!"
    else:
        n_int = int(n)
        if n_int == k:
            return "You win!"
        elif n_int < k:
            return "To small!"
        elif n_int > k:
            return "To big!"


computer_number = randint(1, 100)

while True:
    user_number = input('Guess the number: ')
    if guess(user_number, computer_number) == "You win!":
        print(guess(user_number, computer_number))
        break
    print(guess(user_number, computer_number))
