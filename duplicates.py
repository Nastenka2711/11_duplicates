import sys
import os
import filecmp

list_files = []


def are_files_duplicates(file_path1, file_path2):
    if filecmp.cmp(file_path1, file_path2):
        print("Файлы  " + str(file_path1) + "  и  " + str(file_path2) +
              "  совпадают")
        rez = int(input("Какой удалить? 1 или 2? "))
        if rez == 1:
            os.remove(file_path1)
            list_files.pop(list_files.index(file_path1))
            print("Файл  " + str(file_path1) + "  удалён")
        elif rez == 2:
            os.remove(file_path2)
            list_files.pop(list_files.index(file_path2))
            print("Файл  " + str(file_path2) + "  удалён")
        else:
            print("Файл не удалён, продолжаем")


def search_in_dir(name_dir):
    for rootdir, dirs, files in os.walk(name_dir):
        for f in files:
            list_files.append(os.path.join(rootdir, f))
    return 0


if __name__ == "__main__":
    if len(sys.argv) == 1:
        name_dir = input("Введите название директории:")
    else:
        name_dir = sys.argv[1]
    if os.path.exists(name_dir) and os.path.isdir(name_dir):
        search_in_dir(name_dir)
        for file_path1 in list_files:
            for file_path2 in list_files:
                if file_path2 > file_path1:
                    are_files_duplicates(file_path1, file_path2)
        print("Порядок в файлах")
    else:
        print("Не найдено такого каталога")
