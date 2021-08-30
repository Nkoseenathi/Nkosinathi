def countpairs(s):

    if len(s)<2:
        return 0
    
    else:
        if s[0]==s[1] :
            return countpairs(s[2:])+1

        else:
            return countpairs(s[2:])
                        
