class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        adjList = defaultdict(set)
        edgeList = defaultdict(set)

        for seq in sequences:
            for i in range(len(seq)-1):
                for j in range(i+1, len(seq)):
                    adjList[seq[j]].add(seq[i])
                    edgeList[seq[i]].add(seq[j])

        stack = []
        for n in nums:
            if len(adjList[n]) == 0:
                stack.append(n)
        
        for i in range(len(nums)):
            if len(stack) != 1 or stack[0] != nums[i]:
                return False
            
            n = stack.pop()
            for edge in edgeList[n]:
                adjList[edge].remove(n)
                if len(adjList[edge]) == 0:
                    stack.append(edge)
        
        return True