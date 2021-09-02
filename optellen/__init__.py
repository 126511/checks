import check50
import check50.c

@check50.check()
def exists():
    """hello.c bestaat"""
    check50.exists("main.c")

@check50.check(exists)
def compiles():
    """hello.c compileert"""
    check50.include("les2.h")
    check50.c.compile("main.c", lcs50=True)

@check50.check(compiles)
def hundred():
    """4 + 5 = 9"""
    check50.run("./main").stdin("4").stdin("5").stdout("9").exit()

@check50.check(compiles)
def eighty():
    """1 + 2 = 3"""
    check50.run("./main").stdin("1").stdin("2").stdout("3").exit()
    
@check50.check(compiles)
def sixty():
  """100 + 200 = 300"""
  check50.run("./main").stdin("100").stdin("200").stdout("300").exit()
