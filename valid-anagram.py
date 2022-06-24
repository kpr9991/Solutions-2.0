class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        #Solution 1
        return sorted(s)==sorted(t)
    
        #Solution 2
        # Take the values of t into dict with counts
        # Match with counts in S if yesreturn true else false
        # For matching u can either make a new dict or use the same
        dict={}
        for char in s:
            dict[char]+=dict.get(char,0)+1
        c=0
        for char in t:
            if dict.get(char):
                dict[char]-=1
                if dict[char]==0:
                    c+=1
                if dict[char]<0:
                    return False
            else:
                return False
        
        return c==len(dict)


    
        
        
        
