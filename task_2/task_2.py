"""Написать программу, которая будет вычислять сумму 3 способами
(while, for, рекурсия) следующего массива чисел – [3, 1, 5, 7, 9]."""


def calculate_the_sum(list_numbers):

    # First method - 'for'
    sum = 0
    for number in list_numbers:
        sum += number
    print('First method \'for\': Sum == {}'.format(sum))

    # Second method - 'while'
    sum = 0
    current = 0
    while current < len(list_numbers):
        sum += list_numbers[current]
        current += 1

    print('Second method \'while\': Sum == {}'.format(sum))

    # Second method - 'recursion'
    def recursion(list_numbers, current=0):

        if current is len(list_numbers):
            return 0
        else:
            return list_numbers[current] + recursion(list_numbers, current + 1)

    sum = recursion(list_numbers)
    print('Third method \'recursion\': Sum == {}'.format(sum))


if __name__ == "__main__":

    list_numbers = [3, 1, 5, 7, 9]
    calculate_the_sum(list_numbers)
