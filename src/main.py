

class Ballot(object):
    hasLost = []

    def __init__(self, votes):
        self.votes = votes
        self.currentIndex = 0;
        
    def winner(self):
        return self.votes[self.currentIndex]
    
    def nextWinner(self):
        while(Ballot.hasLost[self.winner()]):
            self.currentIndex+=1
        return self.winner()
    
def initLost(length):
    Ballot.hasLost = []
    for i in xrange(0,length):
        Ballot.hasLost.append(False)

# -----------
# InputReader
# -----------

class InputReader (object) :
    def read (self) :
        return raw_input()

# ------------
# OutputWriter
# ------------

class OutputWriter (object) :
    def write (self, *a) :
        for w in a :
            print w,
        print

# -------
# my_read
# -------

def my_read (r) :
    global candidates
    global election
    global totalVotes
    try :
        s = raw_input()
        numCand = int(s)
        initLost(numCand)
        for i in xrange(0,numCand):
            candidates.append(raw_input());
            election[i] = [] #.append([]);
        while True:
            r = raw_input().split()
            r = [int(a)-1 for a in r]
            if len(r) == 0: 
                break
            b = Ballot(r)
            election[b.winner()].append(b)
            totalVotes+=1
        
    except EOFError :
        return False
    return True

def my_eval():
    global candidates
    global election
    while(True):
        max = -1
        min = 2000000000
        temp = 0
        minIndex = -1
        maxIndex = -1
        for c in election:
            temp = len(election[c])
            if temp > max:
                max = temp
                maxIndex = c
            if temp<min:
                min = temp
        if maxIndex == -1:
            return
        #print candidates[maxIndex],
        #print "has most votes with: ",
        #print max
        #print "least votes is: ",
        #print min
        if max>totalVotes/2:
            #print "totalVotes/2 is: ",
            #print totalVotes/2,
            #print " so ",
            #print candidates[maxIndex],
            #print "auto wins"
            election = {maxIndex:[]}
            return
        if min == max:
            return
        losers = []
        for c in election:
            if len(election[c]) == min:
                losers.append(c);
                #print candidates[c],
                #print " ",
        #print " tied for losing like a bitch"
        
        for c in losers:
            Ballot.hasLost[c] = True
            for b in election[c]:
                #print "ballot given to",
                election[b.nextWinner()].append(b)
                #print candidates[b.winner()]
            del election[c]

def my_print (w) :
#    i = 0
#    keys = election.keys()
#    for i in xrange(0,len(keys)):
#        print candidates[keys[i]],
#        if(i != len(keys)-1):
#            print
    for c in election:
       print candidates[c]
    

candidates = []
election = {}
totalVotes = 0

def main () :
    """
    runs the program
    """
    
    global candidates
    global election
    
    numCases = int(raw_input())
    raw_input()
    while numCases > 0  :
        b = my_read(InputReader())
        my_eval()
        my_print(OutputWriter())
        candidates = []
        election = {}
        totalVotes = 0
        numCases-=1
        if not b:
            break
        print
 
        

if __name__ == "__main__" :
    main()

