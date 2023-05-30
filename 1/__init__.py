import check50


@check50.check()
def exists():
    """main.py exists"""
    check50.exists("main.py")

@check50.check(exists)
def testNegative():
    """print een 0 voor een negatief getal"""
    check50.run("python3 main.py").stdin("-5").stdout("0").exit()

@check50.check(exists)
def test10():
    """input van 10 geeft 20"""
    check50.run("python3 main.py").stdin("10").stdout("20").exit()

@check50.check(exists)
def test9():
    """input van 9 geeft 20"""
    check50.run("python3 main.py").stdin("9").stdout("20").exit()

