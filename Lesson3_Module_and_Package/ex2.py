
import time
import datetime
def fun_print_next_day():
    tomorrow = datetime.datetime.now() + datetime.timedelta(days = 1)
    print(tomorrow)
    
print(fun_print_next_day())