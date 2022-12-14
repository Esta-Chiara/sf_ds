"""Game guess a number
The computer itself invents and guesses the number itself.
"""

from operator import le
import numpy as np

def random_predict(number:int=42) -> int:
    """Randomly guess a number
    Args:
        number (int, optional): hidden number. Defaults to 42.
    Returns:
        int: count of attempts
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 500) # estimated number
        if number == predict_number:
            break # exit from the loop if guessed right
    return(count)

def binary_search(number:int=42) -> int:
    """Search a number using binary search

    Args:
        number (int, optional): hidden number. Defaults to 42.

    Returns:
        int: count of attempts
    """
    count = 0
    left = 0
    right = 100
    
    while True:
        count += 1
        predict_number = (left + right)//2 + (left + right)%2  # estimated number
        if number == predict_number:
            break  # exit from the loop if guessed right  
        elif number > predict_number:  # if the estimated number is greater than the hidden one
            left = predict_number  # shift the left border of the search
        else:  # if the estimated number is less than the hidden one
            right = predict_number  # shift the right border of the search
    
    return count

def score_game(predictor) -> int:
    """Calculation of the number of guessing attempts on average from 1000 approaches
    Args:
        predictor ([type]): guess function
    Returns:
        int: average number of attempts
    """

    count_ls = [] # list of the attempts number
    np.random.seed(1) 
    random_array = np.random.randint(1, 101, size=(1000)) # list of hidden numbers

    for number in random_array:
        count_ls.append(predictor(number))

    score = int(np.mean(count_ls)) # average number of attempts

    print(f'Ваш алгоритм угадывает число в среднем за {score} попыток')
    return(score)


if __name__ == "__main__":
    # RUN
    score_game(binary_search)
