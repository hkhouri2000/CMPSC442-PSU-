############################################################
# CMPSC 442: Homework 1
############################################################

student_name = "Hamdan Alkhoori"

############################################################
# Section 1: Working with Lists
############################################################

def extract_and_apply(l, p, f):
    return[f(i) for i in l if p(i)]

def concatenate(seqs):
    return [x for i in seqs for x in i]

def transpose(matrix):
    return [[matrix[k][i] for k in range(len(matrix))] for i in range(len(matrix[0]))]

############################################################
# Section 2: Sequence Slicing
############################################################

def copy(seq):
    return seq[:]

def all_but_last(seq):
    return(seq[:-1])

def every_other(seq):
    return seq[::2]

############################################################
# Section 3: Combinatorial Algorithms
############################################################

def prefixes(seq):
    for i in range(len(seq) + 1):
        yield seq[:i]

def suffixes(seq):
    for j in range(len(seq) + 1):
        yield seq[j:]

def slices(seq):
    for i in range(len(seq)):
        for j in range(i + 1, len(seq) + 1):
            yield seq[i:j]

############################################################
# Section 4: Text Processing
############################################################

def normalize(text):
    return ' '.join(text.strip().lower().split())

def no_vowels(text):
    return ''.join([c for c in text if c.lower() not in ['a', 'e', 'i', 'o', 'u']])

def digits_to_words(text):
    num_in_word = "zero one two three four five six seven eight nine".split() 
    return ' '.join([num_in_word[int(c)] for c in text if c.isdigit()])

def to_mixed_case(name):
    casedName = ''.join(w[0].upper() + w[1:] for w in name.lower().split('_') if len(w) > 0)
    return casedName[0].lower() + casedName[1:] if len(casedName) > 0 else ""

############################################################
# Section 5: Polynomials
############################################################

class Polynomial(object):

    def __init__(self, polynomial):
        self.polynomial = tuple(polynomial)

    def get_polynomial(self):
        return self.polynomial

    def __neg__(self):
        return Polynomial([(-coeff, power) for coeff, power in self.polynomial])

    def __add__(self, other):
        return Polynomial(self.polynomial + other.polynomial)

    def __sub__(self, other):
        return Polynomial(self.polynomial + (-other).polynomial)

    def __mul__(self, other):
        return Polynomial([(coeff1 * coeff2, pw1 + pw2) for coeff1, pw1 in self.polynomial for coeff2, pw2 in other.polynomial])

    def __call__(self, x):
        return sum((coeff * x ** pw for coeff, pw in self.polynomial))

    def simplify(self):
        temp = list(self.polynomial[:])     # Make a copy of the polynomial 
        temp.sort(key = lambda x : x[1])    # Sort by power 

        pol = []                            # Combine terms with similar powers
        for p in temp:
            if p[0] == 0:                   # Skip terms with zero coefficients
                continue 

            if len(pol) == 0:
                pol.insert(0, p)            # Prepend term if pol is empty 
            elif pol[0][1] != p[1]:
                pol.insert(0, p)            # Append term if pol power is 
                                            # different than the first term 
            else:
                pol[0] = (pol[0][0] + p[0], p[1])   # Add coefficients of 
                                                    # similar terms 

        pol = [p for p in pol if p[0] != 0]       # Trim zero coefficents

        if len(pol) > 0:                            # Save the new polynomial
            self.polynomial = tuple(pol)
        else:
            self.polynomial = ((0, 0))              # Place holder
                
        return 


        temp_polynomial = []
        for i in self.polynomial:
            temp_polynomial.append(i)
        temp_polynomial.sort(key=lambda x: x[1])
        new_polynomial = []
        for i in range(len(temp_polynomial)):
            if temp_polynomial[i][0] == 0:
                continue
            for j in range(i + 1, len(temp_polynomial)):
                if temp_polynomial[j][0] == 0:
                    continue
                if temp_polynomial[i][1] == temp_polynomial[j][1]:
                    temp_polynomial[i] = (temp_polynomial[i][0] + temp_polynomial[j][0], temp_polynomial[i][1])
                    temp_polynomial[j] = (0, temp_polynomial[j][1])
        temp_polynomial.sort(key=lambda x: x[1], reverse=True)
        if len(temp_polynomial) == 0:
            temp_polynomial.append((0, 0))
        self.polynomial = temp_polynomial

    def __str__(self):
        polynomial = ""
        for i in range(len(self.polynomial)):
            term = self.polynomial[i]
            sign = " - " if term[0] < 0 else " + "
            coefficient = abs(term[0])

            if coefficient == 0:
                continue 

            if term[1] == 0:
                polynomial += sign + str(coefficient) 
            elif term[1] == 1:
                polynomial += sign + str(coefficient) + "x"
            else:
                polynomial += sign + str(coefficient) + "x^" + str(term[1]) 
        return polynomial.strip(" + ")
               
############################################################
# Section 6: Feedback
############################################################

feedback_question_1 = """
It took me approximately 14 hours to complete HW1
"""

feedback_question_2 = """
The challenging task was working with the last task, that is task 5.
Implementing the class functions major the __str__ and simplify was very challenging.
To implement this function I included functions which I have not attached here since those functions were
not included in this template and I am doubting if the two functions will run well.
"""

feedback_question_3 = """
The fact that functions could be implemented through just a single line of code made the assigment interesting.
The only thing I would change is the last task "Polynomial Class". I would include more functions that will help
simplify the simplify() function.
"""
