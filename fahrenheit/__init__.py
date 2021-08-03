import check50
import check50.c

@check50.check()
def exists():
    """hello.c exists"""
    check50.exists("main.c")

@check50.check(exists)
def compiles():
    """hello.c compiles"""
    check50.c.compile("main.c", lcs50=True)

@check50.check(compiles)
def hundred():
    """correctly handles 100"""
    check50.run("./main").stdin("100").stdout("37").exit()

@check50.check(compiles)
def eighty():
    """correctly handles 80"""
    check50.run("./main").stdin("80").stdout("26").exit()
    
@check50.check(compiles)
def sixty():
  """correctly handles 60"""
  check50.run("./main").stdin("60").stdout("15").exit()
