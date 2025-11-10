import os


def copy_file(command: str) -> None:
    copy_list = command.strip().split()
    if len(copy_list) != 3 or copy_list[0] != "cp":
        return None
    source = copy_list[1]
    if not os.path.exists(source):
        return None
    dest = copy_list[-1]
    if source == dest:
        return None
    with open(source, "r") as r:
        content = r.read()
    with open(dest, "w") as w:
        w.write(content)


with open("file.txt", "w") as f:
    f.write("Hello")
try:
    copy_file("cp file.txt new_file.txt")
except FileNotFoundError as e:
    print(e)

print(open("file.txt").read() == open("new_file.txt").read())
