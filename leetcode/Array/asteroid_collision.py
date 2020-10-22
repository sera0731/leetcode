class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        st = []
        
        for i in asteroids :
            
            if i > 0 or not st :
                st.append(i)
            else :
                
                while st :
                    # ->로 가는 같은 크기 행성
                    if st[-1]+i == 0 :
                        st.pop()
                        break
                    # ->로 가는 더 큰 행성
                    if st[-1]+i > 0 :
                        break
                            
                    # ->로 가는 더 작은 행성
                    if st[-1] > 0:
                        st.pop()
                    # <-로 가는 행성
                    else :
                        st.append(i)
                        break
                else :
                    st.append(i)
                        
        return st
        
