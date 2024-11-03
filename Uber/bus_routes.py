from collections import deque, defaultdict
class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
        clarifying questions:
        - What are the constraints on the routes and bus stops?
        - Are all bus routes guaranteed to have unique bus stops?
        - Are all bus routes guaranteed to have unique bus stops?
        - doess all the buses travel forever
        - can we switch the bus in between or directly take bus two instead of bus one - tescase like that?
        - What is the expected maximum size of the input?
        - Are there any cases to consider for multiple possible paths? (Should we account for ties in the number of buses, or is the first valid path sufficient?)
        - Are there any information that needs to be known when switching buses?
        
        Identifying Edge Cases:
        - 
        """
        #edge case
        if source == target:
            return 0
        
        #mapping of each stop to the list routes that pass thhrough it:
        stop_routes = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                stop_routes[stop].append(i)

        print(stop_routes)

        #BFS initialization - we use data structure queue and set
        queue= deque([(source, 0)])
        visited_stops = set()
        visited_routes = set()

        #implementing bfs
        while queue:
            curr_stop, buses_taken = queue.popleft()
            for bus_route in stop_routes[curr_stop]:
                if bus_route in visited_routes:
                    continue
                visited_routes.add(bus_route)

                for bus_stop in routes[bus_route]:
                    if bus_stop == target:
                        return buses_taken + 1
                    if bus_stop not in visited_stops:
                        visited_stops.add(bus_stop)
                        queue.append((bus_stop, buses_taken+1))

        return -1

                
            



        
        