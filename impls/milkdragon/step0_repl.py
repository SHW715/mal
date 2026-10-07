def READ(text):
    return text


def EVAL(text):
    return text


def PRINT(text):
    return text

def rep(text):
    read_result = READ(text)
    eval_result = EVAL(read_result)
    print_result = PRINT(eval_result)
    return print_result

while True:
    try:
        text = input("user> ")
        result = rep(text)
        print(result)
    except EOFError:
        break