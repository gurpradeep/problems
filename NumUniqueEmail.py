from typing import List
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        validEmails=set()
        for email in emails:
           validEmails.add(self.extractValidEmail(email))

        return len(validEmails)
    
    def extractValidEmail(self, email)-> str:
        localName, domain = email.split('@')
        idx = localName.find('+')
        if idx!=-1:
            localName = localName[:idx]
        localNameSplit = localName.split('.')
        validLocalName = "".join(localNameSplit)
        validEmail=validLocalName+"@"+domain
        return validEmail


sol = Solution()
print(sol.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
print(sol.numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"]))