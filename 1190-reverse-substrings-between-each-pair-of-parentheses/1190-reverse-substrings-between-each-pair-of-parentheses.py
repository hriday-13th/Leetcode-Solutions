class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        st = []
        
        for i in s:
            if i == ")":
                temp = []
                while st and st[-1] != "(":
                    temp.append(st.pop())
                if st:
                    st.pop()
                st.extend(temp)
            else:
                st.append(i)
                
        return "".join(st)