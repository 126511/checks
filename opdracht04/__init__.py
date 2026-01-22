import check50
import check50.c

@check50.check()
def exists():
    """main.c exists"""
    check50.exists("opdracht04.c")

@check50.check(exists)
def compiles():
    """main.c compiles"""
    check50.c.compile("opdracht04.c", lcs50=True)

@check50.check(compiles)
def prints_hello():
    """prints "Dit is mijn eerste programma\\n" """
    check50.run("./opdracht04").stdout("Dit is mijn eerste programma!\n").exit()
