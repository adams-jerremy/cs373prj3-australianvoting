#!/usr/bin/env python


import main
import unittest

# ----------
# TestReader
# ----------

class TestReader (object) :
    def __init__ (self, s) :
        self.i = 0
        self.tokens = s.split('\n')

    def read (self) :
        self.i+=1
        return self.tokens[self.i-1]

# ----------
# TestWriter
# ----------

class TestWriter (object) :
    def __init__(self):
        self.s = ""
    def str (self) :
        return self.s

    def write (self, *a) :
        self.s += str(a[0])
        for w in a[1:] :
            self.s += ' '
            self.s += str(w)
        self.s += '\n'

# -----------
# TestCollatz
# -----------

class TestVoting (unittest.TestCase) :
    
    def test_noCand(self):
        """
        Tests the case where you have zero candidates
        """
        main.candidates = []
        main.election = {}
        main.totalVotes = 0
        reader = TestReader("""0

""")
        main.my_read(reader)
        self.assert_(len(main.candidates) == 0) 
        w = TestWriter()
        main.my_eval()
        main.my_print(w)
        self.assert_(w.str()=="")
    
    def test_oneCand(self):
        """
        Tests the case where you have a single candidate
        and no ballots
        """
        main.candidates = []
        main.election = {}
        main.totalVotes = 0
        reader = TestReader("""1
a

""")
        main.my_read(reader)
        self.assert_("a" in main.candidates) 
        w = TestWriter()
        main.my_eval()
        main.my_print(w)
        self.assert_(w.str()=="a\n")
    
    
    def test_pass1 (self) :
        """
        Tests entire program (read-eval-print cycle)
        """    
        main.candidates = []
        main.election = {}
        main.totalVotes = 0
        reader = TestReader("""3
a
b
c
1 2 3
1 2 3
2 1 3
2 1 3
3 2 1
3 1 2
1 2 3
2 1 3

""")
        main.my_read(reader)
        self.assert_("a" in main.candidates) 
        self.assert_("b" in main.candidates) 
        self.assert_("c" in main.candidates)
        w = TestWriter()
        main.my_eval()
        main.my_print(w)
        self.assert_(w.str()=="a\nb\n")
 
    def test_pass2 (self) :
        """
        Tests entire program (read-eval-print cycle)
        """    
        main.candidates = []
        main.election = {}
        main.totalVotes = 0
        reader = TestReader("""5
John Smith
Jane Doe
Sam Jones
Suzzie SunBeam
Frosty McShivers
1 2 3 4 5
5 4 3 2 1
1 3 4 5 2
2 3 4 1 5
3 1 5 2 4
2 5 3 2 1
2 3 1 4 5
3 1 2 4 5
5 4 2 1 3
3 1 2 4 5
3 2 1 4 5
5 2 4 3 1
1 3 5 2 4
2 1 4 3 5
4 2 1 3 5
3 2 1 4 5
3 2 1 4 5
2 4 1 2 3
5 4 2 1 3
2 5 4 1 3
1 2 4 5 3
1 3 5 4 2
1 3 5 4 2
3 1 2 5 4

""")
        main.my_read(reader)
        self.assert_("Sam Jones" in main.candidates) 
        self.assert_("Suzzie SunBeam" in main.candidates) 
        self.assert_("Frosty McShivers" in main.candidates)
        self.assert_("Jane Doe" in main.candidates) 
        self.assert_("John Smith" in main.candidates)
        w = TestWriter()
        main.my_eval()
        main.my_print(w)
        self.assert_(w.str()=="Jane Doe\nSam Jones\n")
    
         
    def test_pass3 (self) :
        """
        Tests entire program (read-eval-print cycle)
        """    
        main.candidates = []
        main.election = {}
        main.totalVotes = 0
        reader = TestReader("""14
1
2
3
4
5
6
7
8
9
10
11
12
13
14
12 5 11 8 6 13 3 2 10 1 7 9 14 4
8 14 1 13 11 12 5 4 3 10 2 6 7 9
13 12 14 5 7 11 3 10 2 1 9 8 4 6
12 3 7 11 2 10 13 5 9 1 6 14 8 4
11 14 13 1 7 4 2 12 5 3 8 10 9 6
4 3 12 8 5 1 2 7 13 11 10 14 6 9
6 14 3 11 1 5 10 7 13 2 12 4 8 9

""")
        main.my_read(reader)
        self.assert_("1" in main.candidates) 
        self.assert_("2" in main.candidates) 
        self.assert_("3" in main.candidates)
        self.assert_("4" in main.candidates) 
        self.assert_("5" in main.candidates) 
        self.assert_("6" in main.candidates)
        self.assert_("7" in main.candidates) 
        self.assert_("8" in main.candidates) 
        self.assert_("9" in main.candidates)
        self.assert_("10" in main.candidates)
        self.assert_("11" in main.candidates) 
        self.assert_("12" in main.candidates) 
        self.assert_("13" in main.candidates)
        w = TestWriter()
        main.my_eval()
        main.my_print(w)
        self.assert_(w.str()=="12\n")        


if __name__ == "__main__" :
    unittest.main()
