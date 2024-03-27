from multiprocessing import Process, Value
from threading import Thread


def multithreading_factorial(num, factorial_result):
    result = 1

    for i in range(2, num + 1):
        result *= i

    factorial_result.append(result)


def multiprocessing_sum_of_squares(numbers, result):

    for i in numbers:
        result.value += i**2


if __name__ == "__main__":
    fact_num = 10
    fact_result = []

    square_result = Value("i", 0)
    square_list = [1, 2]

    thread = Thread(
        target=multithreading_factorial,
        args=(
            fact_num,
            fact_result,
        ),
    )

    process = Process(
        target=multiprocessing_sum_of_squares,
        args=(
            square_list,
            square_result,
        ),
    )

    thread.start()
    process.start()

    thread.join()
    process.join()

    print(fact_result)
    print(square_result.value)
