class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s)<10:
            return []
        else:
            visited = set()
            string1 = s[:10]
            visited.add(string1)
            answer = set()
            i=1
            while(i <= len(s)):
                if s[i:i+10] in visited:
                    answer.add(s[i:i+10])
                else:
                    visited.add(s[i:i+10])
                i=i+1
            return answer
