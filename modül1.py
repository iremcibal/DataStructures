def func(input_file, output_file):
    startindex = "{"
    finishindex = "}"
    with open(input_file,"r") as i_file, open(output_file, "w") as o_file:
        tab_count = 0
        for line in i_file:
            for letter in line:
                if(letter == startindex):
                    tab_count += 1
                if(letter == finishindex):
                    tab_count -= 1
                    o_file.seek(o_file.tell() - 1, 0)
                if(letter == "\n"):
                    o_file.write(letter + tab_count * "\t")
                else:
                    o_file.write(letter)

func("source.txt","output.txt")