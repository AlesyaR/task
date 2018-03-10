"""Написать программу, которая генерирует непустой файла (содержащий произвольные данные) произвольного размера в произвольной директории.

На вход программа должна принимать следующие аргументы:
имя файла,
размер файла как в обычном виде (в виде количества байт) так и в « human readable» виде (например, 10MB),
полный путь до каталога, где этот файл должен быть создан.

Программа будет запускаться под ОС Windows.
Примеры запуска программы:
create_custom_file my_test_file 100MB C:\test_folder
create_custom_file my_test_file 1024 C:\test_folder
create_custom_file my_test_file 1KB C:\test_folder"""


import os
import sys


def create_custom_file(size, path, name):
    assert size, 'Size is zero'

    path_file = os.path.join(path, name)
    get_size = dict(KB=lambda size: int(size) * 1024 ** 1,
                    MB=lambda size: int(size) * 1024 ** 2,
                    GB=lambda size: int(size) * 1024 ** 3,
                    TB=lambda size: int(size) * 1024 ** 4)

    if size.isdigit():
        size_in_byte = int(size)
    else:
        unit = size[len(size) - 2:len(size)]
        size_in_byte = get_size[unit.upper()](size[:-2])

    string = 'Hello, i am custom file!\n'
    print('Creating file with param:\n  name = {}\n  path = {}\n  size = {}'.format(name, path_file, size_in_byte))

    with open(path_file, 'w') as file:

        count_of_retry = size_in_byte // len(string)
        file.write(string * count_of_retry)

    # check size of file:
    print('check size of file:\n  size of file = {} byte'.format(os.path.getsize(path_file)))


if __name__ == '__main__':

    assert len(sys.argv) is 4, "Insufficient number of arguments"
    create_custom_file(sys.argv[1], sys.argv[2], sys.argv[3])
