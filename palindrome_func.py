def find_biggest_palindromes(pal):
    # the return array
    ret = []
    # an alternate index that will be incremented backwards along the string
    rev_index = -1  # -1 means not tracking a palindrome
    
    # there can't be any palindromes in a string smaller than three characters.
    if len(pal)<2:
        return []
    
    # a palindrome will be detected if the index is at the center of the palindrome.
    # since palindromes can't be shorter than three letters, there's no point starting
    # with i<2.
    i=2
    while i<len(pal):
        if rev_index is -1:          # If I'm not currently tracking a palindrome:
            if pal[i] == pal[i-1]:   #     if the previous character is the same as me:
                rev_index = i-1      #         set the reverse_index; i'm now tracking a palindrome.
            elif pal[i] == pal[i-2]:
                rev_index = i-2
            i += 1
        elif pal[i] == pal[rev_index-1]:    # go through the palindrome in the reverse direction,
            if rev_index == 0:              # continuing until the characters are no longer the same.
                ret.append( (0,i) )
                rev_index = -1
                continue
            if i == len(pal)-1:
                ret.append( (rev_index-1,len(pal)-1) )
                break
            rev_index -= 1
            i += 1
            continue
        else:
                                            # if tracking a palindrome and the current letter doesn't
            ret.append( (rev_index,i) )     # correspond to the letter on the other side of the palindrome,
            rev_index = -1                  # append the palindrome to the ret array and set rev_index to
                                            # the not tracking a palindrome state.
    
    if len(ret)==0:
        return []
    
    # determines whether two tuples intersect in their ranges
    # ex: (3,7) and (2,5) intersect, but (1,4) and (6,9) do not.
    def intersects(tup1,tup2):
        def between(value,tup):
            if value > tup[0] and value < tup[1]:
                return True
            if value < tup[0] and value > tup[1]:
                return True
            return False
        start1, stop1 = tup1
        start2, stop2 = tup2
        if between(start1,tup2) or between(stop1,tup2):
            return True
        if between(start2,tup1) or between(stop2,tup1):
            return True
        return False
    
    def pal_size(tup):
        dif = tup[1] - tup[0]
        if dif < 0:
            return -dif
        return dif
    
    # check if any of the palindromes intersect, and choose the bigger one.
    i=1
    while i<len(ret):
        if intersects(ret[i-1],ret[i]) and pal_size(ret[i]) > pal_size(ret[i-1]):
            del ret[i-1]
        else:
            i += 1
    
    return ret
