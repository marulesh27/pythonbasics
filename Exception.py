print("starting line")
try:
    a=10/0
except ZeroDivisionError:
    print("exception raised due to zero division error")
except IndexError:
    print("exception raised due to index out of range")
except NameError:
    print("exception raised due to undefined variable")
except:
    print("some exception raised")
else:
    print("no exception ")
finally:
    print("this is final")
print("outside block")
