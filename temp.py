from datetime import datetime

def intobit(inti):
    return format(inti,"4b")
digit1hour = list(map(intobit,map(int,str(datetime.now().hour))))

print(digit1hour)