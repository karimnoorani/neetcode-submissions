class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        L, R = 0, len(matrix[0])-1
        T, B = 0, len(matrix)-1

        while L <= R:
            for i in range(R-L):
                topL = matrix[T][L+i]
                topR = matrix[T+i][R]
                bottomR = matrix[B][R-i]
                bottomL = matrix[B-i][L]

                matrix[T+i][R] = topL
                matrix[B][R-i] = topR
                matrix[B-i][L] = bottomR
                matrix[T][L+i] = bottomL
            
            L += 1
            R -= 1
            T += 1
            B -= 1

            