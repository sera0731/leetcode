class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        output = []
        
        for i in range(1, n+1) :
            
            three = i % 3 == 0
            five = i % 5 == 0
            
            if three and five :
                output.append("FizzBuzz")
            elif five :
                output.append("Buzz")
            elif three :
                output.append("Fizz")
            else :
                output.append(str(i))
                
        return output
            
