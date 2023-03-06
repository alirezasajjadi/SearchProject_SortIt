from Solution import Solution
from Problem import Problem
from datetime import datetime

# Kourosh Hassanzadeh 9912762552
# Alireza Sajjadi 9912762596


class Search:
    @staticmethod
    # this method get a first state of Problem and do bfs for find solution if no
    def bfs(prb: Problem) -> Solution:
        # solution is find return None else return the solution
        start_time = datetime.now()
        queue = []
        state = prb.initState
        queue.append(state)
        while len(queue) > 0:
            state = queue.pop(0)
            neighbors = prb.successor(state)
            for c in neighbors:
                if prb.is_goal(c):
                    return Solution(c, prb, start_time)
                queue.append(c)
        return None

    @staticmethod
    # this method get a first state of Problem and do bfs for find solution if no
    def dfs(prb: Problem) -> Solution:
        # solution is find return None else return the solution
        start_time = datetime.now()
        queue = []
        dic = {}
        state = prb.initState
        key = state.__hash__()
        dic[key] = state
        queue.append(state)
        while len(queue) > 0:
            state = queue.pop()
            key = state.__hash__()
            dic[key] = state
            neighbors = prb.successor(state)
            for c in neighbors:
                if prb.is_goal(c):
                    return Solution(c, prb, start_time)
                if c.__hash__() not in dic:
                    queue.append(c)
        return None

    @staticmethod
    # this method get a first state of Problem and do bfs for find solution if no
    def lds(prb: Problem, depth) -> Solution:
        # solution is find return None else return the solution
        start_time = datetime.now()
        queue = []
        dic = {}
        state = prb.initState
        key = state.__hash__()
        dic[key] = state
        queue.append(state)

        while len(queue) > 0:
            state = queue.pop()
            key = state.__hash__()
            dic[key] = state
            neighbors = prb.successor(state)

            for c in neighbors:
                if prb.is_goal(c):
                    return Solution(c, prb, start_time)
                if c.__hash__() not in dic and c.g_n <= depth:
                    queue.append(c)
        return None

    @staticmethod
    def ids(pro: Problem):
        i = 0
        while True:
            result = Search.lds(pro, i)
            i += 1
            if result is not None:
                return result
