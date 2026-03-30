class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix[0])-1
        t, b = 0, len(matrix)-1

        while l < r:
            for i in range(r-l):
                topL = matrix[t][l+i]
                topR = matrix[t+i][r]
                bottomR = matrix[b][r-i]
                bottomL = matrix[b-i][l]
                
                matrix[t][l+i] = bottomL
                matrix[t+i][r] = topL
                matrix[b][r-i] = topR
                matrix[b-i][l] = bottomR
            l += 1
            t += 1
            r -= 1
            b -= 1
        