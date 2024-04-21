import fileinput

with fileinput.input(files="0_2_io_file_text_test.txt") as f:
    for line in f:
        print(line)