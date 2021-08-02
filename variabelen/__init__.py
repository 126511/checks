import check50


@check50.check()
def exists():
    """variabelen.txt bestaat"""
    check50.exists("variabelen.txt")
    
@check50.check(exists)
def integer():
    """variabele geheel getal goed gedeclareerd"""

    text = open("variabelen.txt").read()
    if "int aantal_ijsjes = 6;" not in text:
        raise check50.Failure(f"Variabele geheel getal niet goed gedeclareerd.")

@check50.check(exists)
def character():
    """variabele karakter goed gedeclareerd"""

    text = open("variabelen.txt").read()
    if "char schreeuw = '!';" not in text:
        raise check50.Failure(f"Variabele karakter niet goed gedeclareerd.")

@check50.check(exists)
def string():
    """variabele stuk tekst goed gedeclareerd"""

    text = open("variabelen.txt").read()
    if 'string test = "Dit is een test";' not in text:
        raise check50.Failure(f"Variabele stuk tekst niet goed gedeclareerd.")

        
        
