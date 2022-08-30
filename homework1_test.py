from string import digits
from homework1_cmpsc442 import extract_and_apply
from homework1_cmpsc442 import concatenate
from homework1_cmpsc442 import transpose
from homework1_cmpsc442 import copy
from homework1_cmpsc442 import all_but_last
from homework1_cmpsc442 import every_other
from homework1_cmpsc442 import prefixes
from homework1_cmpsc442 import suffixes
from homework1_cmpsc442 import slices
from homework1_cmpsc442 import normalize
from homework1_cmpsc442 import no_vowels
from homework1_cmpsc442 import digits_to_words
from homework1_cmpsc442 import to_mixed_case
from homework1_cmpsc442 import Polynomial

def test_section1():
    # Test extract_and_apply
    l = [1, 2, 3, 4, 5, 6]

    out = extract_and_apply(l, lambda x : x % 2 == 0, lambda x : x / 2)
    assert out == [1, 2, 3]

    out = extract_and_apply(l, lambda x : x % 2 == 1, lambda x : x * 2)
    assert out == [2, 6, 10]

    out = extract_and_apply(l, lambda x : x > 10, lambda x : x)
    assert out == []

    out = extract_and_apply(l, lambda x : True, lambda x : 3 * x)
    assert out == [3, 6, 9, 12, 15, 18]

    # Test concatenate
    out = concatenate([[1, 2, 3, 4], [5, 6, 7]])
    assert out == [1, 2, 3, 4, 5, 6, 7]

    out = concatenate([[], [5, 6, 7]])
    assert out == [5, 6, 7]

    out = concatenate([[8, 9, 10, 11], [5, 6, 7]])
    assert out == [8, 9, 10, 11, 5, 6, 7]

    out = concatenate(["abc", (0, [0])])
    assert out == ['a', 'b', 'c', 0, [0]]

    # Test transpose 
    out = transpose([[1, 2, 3]])
    assert out == [[1], [2], [3]]

    out = transpose([[1], [2], [3]])
    assert out == [[1, 2, 3]]

    out = transpose([[1, 2], [3 ,4], [5, 6]])
    assert out == [[1, 3, 5], [2, 4, 6]]

    out = transpose([[1, 3, 5], [2, 4, 6]])
    assert out == [[1, 2], [3 ,4], [5, 6]]
    
    print("Passed Section 1") 

def test_section2():
    # Test copy
    assert copy("abc") == "abc"
    assert copy((1, 2, 3)) == (1, 2, 3)
    assert copy([4, 5, 6, 7, 8]) == [4, 5, 6, 7, 8]

    # Test all_but_last
    assert all_but_last("abc") == "ab"
    assert all_but_last((1, 2, 3)) == (1, 2)
    assert all_but_last([4, 5, 6, 7, 8]) == [4, 5, 6, 7]
    assert all_but_last("") == ''
    assert all_but_last([]) == []

    # Test every_other 
    assert every_other([1, 2, 3, 4, 5]) == [1, 3, 5]
    assert every_other("abcde") == "ace"
    assert every_other([1, 2, 3, 4, 5, 6]) == [1, 3, 5]
    assert every_other("abcdef") == "ace"

    print("Passed Section 2")  

def test_section3():
    # Test prefixes 
    assert prefixes([1, 2, 3]) != [[], [1], [1, 2], [1, 2, 3]]
    assert prefixes("abc") != ["", "a", "ab", "abc"]
    assert list(prefixes([1, 2, 3])) == [[], [1], [1, 2], [1, 2, 3]]
    assert list(prefixes("abc")) == ["", "a", "ab", "abc"]

    # Test suffixes 
    assert suffixes([1, 2, 3]) != [[1, 2, 3], [2, 3], [3], []]
    assert suffixes("abc") != ["abc", "bc", "c", ""]
    assert list(suffixes([1, 2, 3])) == [[1, 2, 3], [2, 3], [3], []]
    assert list(suffixes("abc")) == ["abc", "bc", "c", ""]

    # Test slices 
    assert slices([1, 2, 3]) != [[1], [1, 2], [1, 2, 3], [2], [2, 3], [3]]
    assert slices("abc") != ['a', 'ab', 'abc', 'b', 'bc', 'c']
    assert list(slices([1, 2, 3])) == [[1], [1, 2], [1, 2, 3], [2], [2, 3], [3]]
    assert list(slices("abc")) == ['a', 'ab', 'abc', 'b', 'bc', 'c']

    print("Passed Section 3")  

def test_section4():
    # Test normalize
    assert normalize("This is an example.") == "this is an example."
    assert normalize("    EXTRA   SPACE    ") == "extra space"

    # Test no_vowels
    assert no_vowels("This Is An Example.") == "Ths s n xmpl."
    assert no_vowels("We love Python!") == "W lv Pythn!"

    # Test digits_to_words 
    assert digits_to_words("Zip code: 19104") == "one nine one zero four"
    assert digits_to_words("Pi is 3.1415...") == "three one four one five"
    assert digits_to_words("no digits here") == ""

    # Test to_mixed_case
    assert to_mixed_case("to_mixed_case") == "toMixedCase"
    assert to_mixed_case("__EXAMPLE__NAME__") == "exampleName"
    assert to_mixed_case("___") == ""
    assert to_mixed_case("") == ""

    print("Passed Section 4")  

def test_section5():
    # Test Polynomial 
    p, q = Polynomial([(2, 1), (1, 0)]), Polynomial([(2, 1), (-1, 0)])

    assert str(p) == "2x + 1"
    assert str(q) == "2x - 1"

    r = (p * p) + (q * q) - (p * q)
    assert str(r) == "4x^2 + 2x + 2x + 1 + 4x^2 - 2x - 2x + 1 - 4x^2 + 2x - 2x + 1"

    r.simplify()
    assert str(r) == "4x^2 + 3"

    comp = [(x, r(x)) for x in range(-4, 5)]
    assert [(-4, 67), (-3, 39), (-2, 19), (-1, 7), (0, 3), (1, 7), (2, 19), (3, 39), (4, 67)]

    # Test Polynomial.get_polynomial()
    assert Polynomial([(2, 1), (1, 0)]).get_polynomial() == ((2, 1), (1, 0))
    assert Polynomial(((2, 1), (1, 0))).get_polynomial() == ((2, 1), (1, 0))

    # Test Polynomial.__neg__()
    p = Polynomial([(2, 1), (1, 0)])
    q = -p
    assert q.get_polynomial() == ((-2, 1), (-1, 0))

    q = -(-p)
    assert q.get_polynomial() == ((2, 1), (1, 0))

    # Test Polynomial.__add__()
    q = p + p
    assert q.get_polynomial() == ((2, 1), (1, 0), (2, 1), (1, 0))

    q = Polynomial([(4, 3), (3, 2)])
    r = p + q
    assert r.get_polynomial() == ((2, 1), (1, 0), (4, 3), (3, 2))

    # Test Polynomial.__sub__()
    q = p - p 
    assert q.get_polynomial() == ((2, 1), (1, 0), (-2, 1), (-1, 0))

    q = Polynomial([(4, 3), (3, 2)])
    r = p - q
    assert r.get_polynomial() == ((2, 1), (1, 0), (-4, 3), (-3, 2))

    # Test Polynomial.__mul__() 
    q = p * p
    assert q.get_polynomial() == ((4, 2), (2, 1), (2, 1), (1, 0))

    q = Polynomial([(4, 3), (3, 2)])
    r = p * q 
    assert r.get_polynomial() == ((8, 4), (6, 3), (4, 3), (3, 2))

    # Test Polynomial.__call__()
    assert [p(x) for x in range(5)] == [1, 3, 5, 7, 9]

    q = -(p * p) + p
    assert [q(x) for x in range(5)] == [0, -6, -20, -42, -72]

    # Test Polynomial.simplify()
    q = -p + (p * p)
    q.simplify() 
    assert q.get_polynomial() == ((4, 2), (2, 1))

    q = p - p
    q.simplify()
    assert q.get_polynomial() == ((0, 0))

    print("Passed Section 5")  

if __name__ == '__main__':
    test_section1()
    test_section2()
    test_section3()
    test_section4()
    test_section5()