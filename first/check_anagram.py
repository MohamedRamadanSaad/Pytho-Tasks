__author__ = 'Mohamed_Ramadan_PC'

def isAnagram(str1,str2):

    if(len(str1)!=len(str2)):
        return False
    else:
        s_str1=sorted(str1.lower())
        s_str2=sorted(str2.lower())

        if s_str1 != s_str2:
            print( "is not anagram")
        else:
            print ("is anagram")

isAnagram("hallo","hAllo")