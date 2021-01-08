from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    # seek() 方法用于移动文件读取指针到指定位置。
    # fileObject.seek(offset[, whence])
    # offset -- 开始的偏移量，也就是代表需要移动偏移的字节数
    # whence：可选，默认值为 0。给offset参数一个定义，表示要从哪个位置开始偏移；
    # 0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起
    # 如果操作成功，则返回新的文件位置，如果操作失败，则函数返回 -1
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline(), end = "")

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
