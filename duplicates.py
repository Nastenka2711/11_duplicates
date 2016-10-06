import sys
import os
import filecmp

list_files = []


def input_name_dir():
    if len(sys.argv) == 1:
        name_dir = input("Введите название директории  ")
    else:
        name_dir = sys.argv[1]
    return name_dir


def existence_dir(name_dir):
    if os.path.exists(name_dir) and os.path.isdir(name_dir):
        return 0
    else:
        return None


def list_files_in_dir(name_dir):
    for rootdir, dirs, files in os.walk(name_dir):
        for f in files:
            list_files.append(os.path.join(rootdir, f))
    return 0


def search_duplicate():
    for file_path1 in list_files:
            for file_path2 in list_files:
                if file_path2 > file_path1:
                    rez_delete = are_files_duplicates(file_path1, file_path2)
                    if rez_delete == 1:
                        break
    return 0


def delete_file(file_path):
    list_files.pop(list_files.index(file_path))
    os.remove(file_path)
    if os.path.exists(file_path):
        print("Ошибка при удалении файла")
    else:
        print("Файл  " + str(file_path) + "  удалён")


def are_files_duplicates(file_path1, file_path2):
    if filecmp.cmp(file_path1, file_path2):
        print("Файлы  " + str(file_path1) + "  и  " + str(file_path2) +
              "  совпадают")
        rez = input("Какой удалить? 1 или 2? ")
        if rez == '1':
            delete_file(file_path1)
            return 1
        elif rez == '2':
            delete_file(file_path2)
            return 2
        else:
            print("Файл не удалён, продолжаем")
    return 0


if __name__ == "__main__":
    name_dir = input_name_dir()
    if existence_dir(name_dir) is None:
        print("Не найденно данного каталога")
    else:
        list_files_in_dir(name_dir)
        search_duplicate()
        print("Порядок в файлах")
