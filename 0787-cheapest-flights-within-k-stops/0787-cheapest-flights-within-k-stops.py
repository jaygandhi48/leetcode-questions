import heapq
from typing import List

class Solution:
    def findCheapestPrice(
        self,
        n: int,
        flights: List[List[int]],
        src: int,
        dst: int,
        k: int
    ) -> int:
        graph = [[] for _ in range(n)]
        for from_city, to_city, price in flights:
            graph[from_city].append((to_city, price))
        heap = []
        heapq.heappush(heap, (0, src, 0))
        min_flights = [float("inf")] * n
        while heap:
            cost, city, flights_taken = heapq.heappop(heap)
            if city == dst:
                return cost
            if flights_taken >= min_flights[city]:
                continue #Skip if this has taken more flights than minimum
            min_flights[city] = flights_taken
            if flights_taken > k:
                continue
            for next_city, price in graph[city]:
                heapq.heappush(heap,(cost + price, next_city, flights_taken + 1))
        return -1