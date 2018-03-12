"""Генерация произвольного файла.
На вход программа принимает следующие аргументы:
    * имя файла,
    * размер файла как в обычном виде (в виде количества байт) так и в « human readable» виде (например, 10MB),
    * полный путь до каталога, где этот файл должен быть создан.

Примеры запуска программы:
create_custom_file my_test_file 100MB C:\test_folder
create_custom_file my_test_file 1024 C:\test_folder
create_custom_file my_test_file 1KB C:\test_folder"""

from random import choice
import os
from string import ascii_letters
import sys


def create_custom_file(name, size, path):
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

    print('Creating file with param:\n  name = {}\n  path = {}\n  size = {}'.format(name, path_file, size_in_byte))

    with open(path_file, 'w') as file:
        file.write(size_in_byte*choice(ascii_letters))

    # check size of file:
    print('check size of file:\n  size of file = {} byte'.format(os.path.getsize(path_file)))


if __name__ == '__main__':

    assert len(sys.argv) is 4, "Insufficient number of arguments"
    create_custom_file(sys.argv[1], sys.argv[2], sys.argv[3])
