import csvparser

def read_row(file):
    next_line = file.readline()

    if len(next_line) > 0:
        return parse_row(next_line)

    return None


def test_read_row():
    #assemble 
    expected = 'test'
    #act
    with open('C:/Data Engineering Bootcamp/Tech/test.csv') as file:
        row = read_row(file)
        actual = row
    #assert 

    assert expected == actual
    
#--------------------------------------------------

def parse_row(next_line):
    replace_next_line = next_line.replace('"','')
    new_next_line = replace_next_line.replace(',',' - ')
    print(new_next_line)
    
    return new_next_line

def test_parse_row():
    #assemble 
    next_line = 'test'
    expected = 'test'
    #act 
    actual = parse_row(next_line)
    #assert 
    assert expected == actual