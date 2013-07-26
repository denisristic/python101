# 002-if-else-statement.py

def statement(state):
    if state:
        print("If statement was true!")
    else:
        print("If statement was false!")

if __name__ == '__main__':
    statement(True)
    statement(False)
    statement(None)
    statement(0)
    statement(1)
    statement('a')