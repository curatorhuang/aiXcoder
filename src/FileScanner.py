import os


def scan_folder(folder_path, file_extension):
    if not os.path.isdir(folder_path):
        print("指定的路径不是一个文件夹")
        return

    files = [f for f in os.listdir(folder_path) if f.endswith(file_extension)]
    if files:
        for file in files:
            print(f"找到文件: {os.path.join(folder_path, file)}")
    else:
        print("没有找到符合条件的文件")


def count_files_with_extension(folder_path, file_extension):
    if not os.path.isdir(folder_path):
        print("指定的路径不是一个文件夹")
        return 0

    files = [f for f in os.listdir(folder_path) if f.endswith(file_extension)]
    return len(files)


def get_file_size(folder_path, file_name):
    file_path = os.path.join(folder_path, file_name)
    if os.path.isfile(file_path):
        return os.path.getsize(file_path)
    else:
        return -1


if __name__ == "__main__":
    folder_path = input("请输入文件夹路径: ")
    file_extension = input("请输入文件后缀名: ")

    # 扫描文件夹并打印符合条件的文件
    scan_folder(folder_path, file_extension)

    # 计算特定后缀名文件的数量
    count = count_files_with_extension(folder_path, file_extension)
    print(f"文件夹中共有 {count} 个 {file_extension} 文件")

    # 获取文件大小
    file_name = input("请输入文件名: ")
    size = get_file_size(folder_path, file_name)
    if size >= 0:
        print(f"文件 {file_name} 的大小为 {size} 字节")
    else:
        print(f"文件 {file_name} 不存在")
