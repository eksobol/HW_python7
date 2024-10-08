import os

# путь до текущего файла

path = os.path.abspath(__file__)
# путь до текущей папкм

path_dir = os.path.dirname(path)
# слейка текущей папки до tmp

source_dir = os.path.join(path_dir, "tmp")
target_archive = os.path.join(path_dir, "my_test.zip")
