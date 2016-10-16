import sys
import os
import filecmp


def input_dir_name():
    if len(sys.argv) == 1:
        dir_name = input("Введите название директории  ")
    else:
        dir_name = sys.argv[1]
    return dir_name


def dir_exists(dir_name):
    return os.path.exists(dir_name) and os.path.isdir(dir_name)


def create_list_files(dir_name):
    list_files = []
    for rootdir, dirs, files in os.walk(dir_name):
        for f in files:
            list_files.append(os.path.join(rootdir, f))
    return list_files


def search_duplicate(list_files):
    for file_path1 in list_files:
        for file_path2 in list_files:
            if file_path2 > file_path1:
                result_remove = are_files_duplicates(file_path1,
                                                     file_path2,
                                                     list_files)
                if result_remove:
                    break


def are_files_duplicates(file_path1, file_path2, list_files):
    if filecmp.cmp(file_path1, file_path2):
        return select_one_file(file_path1, file_path2, list_files)


def select_one_file(file_path1, file_path2, list_files):
    result_input = input("Файлы:\n'%(file1)s'\n'%(file2)s'\nсовпали.\n \
                          Какой удалить? 1 или 2?\n" % {"file1": file_path1,
                                                        "file2": file_path2})
    if result_input == '1':
        remove_file(file_path1, list_files)
        return True
    elif result_input == '2':
        remove_file(file_path2, list_files)
    else:
        print("Файл не удалён, продолжаем")


def remove_file(file_path, list_files):
    list_files.pop(list_files.index(file_path))
    os.remove(file_path)
    if os.path.exists(file_path):
        print("Ошибка при удалении файла")
    else:
        print("Файл %(file)s удалён." % {"file": file_path})


if __name__ == "__main__":
    dir_name = input_dir_name()
    if not dir_exists(dir_name):
        print("Не найденно данного каталога")
    else:
        search_duplicate(create_list_files(dir_name))
        print("Порядок в файлах")
