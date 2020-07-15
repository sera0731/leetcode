class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        processed_str = ''.join([ch.lower() if ch.isalnum() else ' ' for ch in paragraph])
        words = processed_str.split()
        
        banned_words = set(banned)
        count = {}
        
        most_common = [0, ""]
        
        for word in words :
            if word not in banned_words :
                count[word] = count.get(word, 0) + 1
                if count[word] > most_common[0] :
                    most_common = count[word], word

        return most_common[1]
        
