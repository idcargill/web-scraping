from scraper.scraper import get_citations_needed_count
from scraper.scraper import get_citations_needed_report


def test_citations_needed():
    actual = get_citations_needed_count('https://en.wikipedia.org/wiki/Lisp_(programming_language)')
    expected = 5
    assert actual == expected


def test_report():
    text = get_citations_needed_report('https://en.wikipedia.org/wiki/Lisp_(programming_language)')
    expected = 'Garbage collection routines were developed by MIT graduate student[citation needed] Daniel Edwards, prior to 1962.[17]' in text
    assert expected == True
    

def test_report_2():
    text = get_citations_needed_report('https://en.wikipedia.org/wiki/Lisp_(programming_language)')
    expected = 'The essential difference between atoms and lists was that atoms were immutable and unique. Two atoms that appeared in different places in source code but were written in exactly the same way represented the same object,[citation needed] whereas each list was a separate object that could be altered independently of other lists and could be distinguished from other lists by comparison operators.' in text
    assert expected == True
    

def test_report_3():
    text = get_citations_needed_report('https://en.wikipedia.org/wiki/Ayodhya#Etymology_and_names')
    expected = 'The word "Ayodhya" is a regularly formed derivation of the Sanskrit verb yudh' in text
    assert expected == True


def test_count_no_citations():
    count = get_citations_needed_count('https://en.wikipedia.org/wiki/JavaScript')
    expected = 0
    assert expected == count

def test_report_no_citations():
    text = get_citations_needed_report('https://en.wikipedia.org/wiki/JavaScript')
    expected = 'No citations needed here'
    assert text == expected