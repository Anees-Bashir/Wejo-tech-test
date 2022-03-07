def read_row(file):
    next_line = file.readline()

    if len(next_line) > 0:
        return parse_row(next_line)

    return None

def parse_row(next_line):
    replace_next_line = next_line.replace('"','')
    new_next_line = replace_next_line.replace(',',' - ')
    print(new_next_line)
    
    return new_next_line
