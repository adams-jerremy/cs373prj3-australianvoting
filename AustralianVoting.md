# Introduction #

Australian ballots require that the voter rank the candidates in order of choice. Initially only the first choices are counted and if one candidate receives more than 50% of the vote, that candidate is elected. If no candidate receives more than 50%, all candidates tied for the lowest number of votes are eliminated. Ballots ranking these candidates first are recounted in favour of their highest ranked candidate who has not been eliminated. This process continues [is, the lowest candidate is eliminated and each ballot is counted in favour of its ranked non-eliminated candidate](that.md) until one candidate receives more than 50% of the vote or until all candidates are tied.


# Details #

Read in each Candidate, store them while maintaining position in a list.

Read in each line of votes and create a ballot for each.  The ballot holds a pointer to the current winner, and holds the list of votes.  Ballot also has a static boolean list that keeps track of who has already lost.

Find the max and the min number of votes.  If max and min are equal, we have a tie.  All remaining candidates are equally good. If the max is greater than half of the total votes, we have a winner.  Otherwise, redistribute votes for candidates tied for last.

Repeat.