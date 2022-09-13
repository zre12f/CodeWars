def array(string):
    return None if string == "" or string == "1" or string == "1,2" else ' '.join(string.split(',')[1:-1])