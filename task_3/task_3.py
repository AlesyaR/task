"""Написать скрипт/программу которая должна
1) осуществлять поиск в iplir.conf и определять содержатся ли в указанной секции id, указанные записи (записей не меньше 1го).

2) В случае положительного результата просто выводить сообщение о успешном завершении.

3) В случае отрицательного результата выводить что именно пошло не так, какую из записей или id не удалось найти.

4) Аргументы содержатся в конфигурационном файле:

    a. path – путь к iplir.conf;

    b. id – id секция которую будем анализировать

    c. 1 или несколько записей –  которые нужно искать в данной секции(указывается регуляркой)


Пример конфига (conf.txt), для положительного результата
path = /tmp/iplir.conf
id = 0x1620001f
string = “tunnel.*19.0.0.100-19.0.0.110.*19.0.0.100-19.0.0.110”
string1 = “tunnel.*19.0.0.1-19.0.0.1.*19.0.0.1-19.0.0.1”
string2 = “ip.*173.18.0.1”

Пример запуска
<script_name> /tmp/conf.txt"""

import os
import re
import sys


def search_in_conf(path):

    def search_line(id_section, list_string):

        # searching lines in need id_section
        for string in list_string:
            is_found = False

            for line in id_section:
                if re.search(string, line):
                    is_found = True
                    break

            if not is_found:
                print('\tThe string {} wasn\'t found in section!'.format(string))
                return False

        return True

    assert os.path.exists(path), "File {} wasn't found".format(path)

    list_search = dict()
    path_config_file = ''
    id = None

    # parsing conf.txt
    with open(path) as file:
        for line in file:
            param = line.split('=')

            if line.startswith('path'):
                path_config_file = param[1].strip()

            elif line.startswith('id'):
                id = param[1].strip().lower()
                search = dict(is_found=False, search=list())
                list_search[id] = search

            elif line.strip():
                param[1] = param[1].strip()
                list_search[id]['search'].append(param[1][1:-1])

    assert os.path.exists(path_config_file), "File {} wasn't found".format(path_config_file)

    with open(path_config_file) as file:
        for line in file:

            if not line.startswith('id'):
                continue

            id = line.split('=')[1].strip()
            if id.lower() in list_search.keys():

                print('Search strings in section with id = {}:'.format(id.lower()))
                list_search[id.lower()]['is_found'] = True

                read_line = file.readline()
                id_section = list()
                while read_line.strip():   #the string is not empty
                    id_section.append(read_line.strip())
                    read_line = file.readline()

                if search_line(id_section, list_search[id.lower()]['search']):
                    print('\tSearching was finished successfully!\n')
                else:
                    print('\tSearching was failed!\n')

    #check is_found all needed id_section
    for key, value in list_search.items():
        if not value['is_found']:
            print('ID_section {} wasn\'t found!Failed!'.format(key))


if __name__ == '__main__':
    assert len(sys.argv) is 2, "Insufficient number of arguments"
    search_in_conf(sys.argv[1])


