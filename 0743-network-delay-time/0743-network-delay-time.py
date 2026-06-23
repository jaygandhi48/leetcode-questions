import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #make distance array
        timeMin = [float('inf')] * (n)
        minHeap = []
        timeMin[k-1] = 0
        #make visited array
        visited = set()
        #make a graph
        graph = [[] for i in range(n)] #Store the neighbour for each graph
        for fromPlace,toPlace,time in times:
            graph[fromPlace-1].append((toPlace - 1, time))
        
        heapq.heappush(minHeap, (0, k-1))
        while minHeap:
            time,location = heapq.heappop(minHeap)
            if location in visited: 
                continue 
            visited.add(location)
            #Mark the location as visited
            visited.add(location)
            #Check its neighbours
            for toPlace, edgeW in graph[location]:
                #check if toPlace is not in  visited:
                if timeMin[toPlace] > time + edgeW:
                    timeMin[toPlace] = time + edgeW
                    heapq.heappush(minHeap, (time + edgeW, toPlace))

        if float('inf') in timeMin:
            return -1
        return max(timeMin)
            
      