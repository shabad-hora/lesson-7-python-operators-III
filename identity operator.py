x = 6
if (type(x) is int):
    print("true")
else:
    print("false")

x = 6.0
if (type(x) is not float):
    print("true")
else:
    print("false")

x = 32
y = 32
if ( x is y ):
    print("x and y  SAME identity")
y = 31
if ( x is not y ):
    print("x and y have DIFFERENT identity")