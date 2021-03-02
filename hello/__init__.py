import check50
import check50.c

@check50.check()
def exists():
    """main.c exists"""
    check50.exists("main.c")

@check50.check(exists)
def compiles():
    """main.c compiles"""
    check50.c.compile("main.c", lcs50=True)

@check50.check(compiles)
def prints_hello():
    """prints "hello, world\\n" """
    # regex=True by default :)
    check50.run("./main").stdout("Hello, world!\n").exit()
