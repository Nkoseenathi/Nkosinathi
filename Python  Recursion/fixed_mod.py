import string

def palindrome (s):

   if len(s) == 1:
      return s.isalpha()

   elif s[0] in string.punctuation or s[0] in string.whitespace:
      return palindrome(s[1:])

   elif s[-1] in string.punctuation or s[-1] in string.whitespace:
      return palindrome(s[:-1])

   elif s[0].lower() == s[-1].lower() and len(s) >2:
      return palindrome (s[1:-1])

   elif len(s)<=2 and s[0]==s[1]: return  palindrome(s[:-1])

   else:
      return False
