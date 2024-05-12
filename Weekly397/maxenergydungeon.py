# In a mystic dungeon, n magicians are standing in a line. 
# Each magician has an attribute that gives you energy. 
# Some magicians can give you negative energy, which means taking energy from you.
# You have been cursed in such a way that after absorbing energy from magician i, 
# you will be instantly transported to magician (i + k). 
# This process will be repeated until you reach the magician where (i + k) does not exist.
# In other words, you will choose a starting point and then teleport with 
# k jumps until you reach the end of the magicians' sequence, absorbing all the energy during the journey.
# You are given an array energy and an integer k. Return the maximum possible energy you can gain.

def maxenergy(energy, k):
    if len(energy) == 1:
        return energy[0]
    else:
        res = 0
        i = 0
        while (energy[i] + energy[k]) in energy:
            newvalue = energy[i] + energy[i + k]
            res = max(res, newvalue)
            i += 1
    return res

# my solution fails to work with the fact that i + k in energy means that 
# in examples like [-2,-3,-1], k = 2, -2 + -1 actually is in energy;
# magician with value -3 is literally in energy