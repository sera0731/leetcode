# O(N)
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        stack = []
        ptr = 0
        
        for i in pushed :
            stack.append(i)
            
            while stack and stack[-1] == popped[ptr] :
                stack.pop()
                ptr += 1
        
        return len(stack) == 0

# O(1)
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        push_ptr = 0
        pop_ptr = 0
        
        for x in pushed :
            
            pushed[push_ptr] = x
            
            while push_ptr >= 0 and pushed[push_ptr] == popped[pop_ptr] :
                push_ptr -= 1
                pop_ptr +=1
            
            push_ptr += 1
        
        return push_ptr == 0
    
