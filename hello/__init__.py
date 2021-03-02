import check50
import check50.c

@check50.check()
def exists():
    """hello.c exists"""
    check50.exists("hello.c")

@check50.check(exists)
def prints_hello():
    """prints "hello, world\\n" """
    # regex=True by default :)
    check50.run("python3 hello.py").stdout("[Hh]ello, world!?\n").exit(0)
