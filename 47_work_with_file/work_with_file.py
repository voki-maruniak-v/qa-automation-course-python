from pathlib import Path

files_dir_path = Path('files')
files_dir_path.mkdir(exist_ok=True)

print("Do we have dir files?:", files_dir_path.exists(), '\n')

first_file = Path(files_dir_path / 'first.txt')
second_file = Path(files_dir_path / 'second.txt')

with open(first_file, 'w') as f:
    f.write("I'm Vadya\n")
    f.write("I'm from Ukraine\n")

print("Do we have file 'first.txt'?:", first_file.exists(), '\n')

with open(second_file, 'w') as f:
    f.write("I'm Alex\n")
    f.write("I'm from Spain\n")

print("Do we have file 'second.txt'?:", second_file.exists(), '\n')

with open(first_file) as f:
    print(f.read())

with open(second_file) as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line)

if first_file.exists():
    first_file.unlink()

if second_file.exists():
    second_file.unlink()

if files_dir_path.exists():
    files_dir_path.rmdir()

print("Do we have dir files?:", files_dir_path.exists(), '\n')
print("Do we have file 'first.txt'?:", first_file.exists(), '\n')
print("Do we have file 'second.txt'?:", second_file.exists(), '\n')
