from Solution import Solution
from Problem import Problem
from datetime import datetime
from PriorityQueue import PriorityQueue


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

    @staticmethod
    # this method get a first state of Problem and do bfs for find solution if no
    def ucs(prb: Problem) -> Solution:
        # solution is find return None else return the solution
        start_time = datetime.now()
        queue = PriorityQueue()
        dic = {}
        state = prb.initState
        key = state.__hash__()
        dic[key] = state
        queue.add(state, state.g_n)
        while not queue.isEmpty():
            state = queue.pop()

            print(state)

            key = state.__hash__()
            dic[key] = state
            neighbors = prb.newSuccessor(state)
            for c in neighbors:
                if prb.is_goal(c):
                    return Solution(c, prb, start_time)
                if c.__hash__() not in dic:
                    queue.add(c, c.g_n)
        return None

    @staticmethod
    def a_star(prb: Problem) -> Solution:
        start_time = datetime.now()
        queue = PriorityQueue()
        state = prb.initState
        dict = {}
        dict[state.__hash__()] = state
        queue.add(state, state.g_n + state.h_n())

        while queue.isNotEmpty():
            state = queue.pop()
            dict[state.__hash__()] = state
            neighbors = prb.newSuccessor(state)
            for c in neighbors:
                if prb.is_goal(c):
                    return Solution(c, prb, start_time)
                if not c.__hash__() in dict:
                    queue.add(c, c.g_n + c.h_n())
        return None

    @staticmethod
    def ida_star(prb: Problem) -> Solution:
        cut_off = prb.initState.g_n + prb.initState.h_n()
        while True:
            start_time = datetime.now()
            queue = PriorityQueue()
            state = prb.initState
            dict = {}
            dict[state.__hash__()] = state
            queue.add(state, state.g_n + state.h_n())
            cut_off_list = []

            while queue.isNotEmpty():
                state = queue.pop()
                dict[state.__hash__()] = state
                neighbors = prb.newSuccessor(state)
                for c in neighbors:
                    f_n = c.g_n + c.h_n()

                    if prb.is_goal(c):
                        return Solution(c, prb, start_time)

                    cut_off_list.append(f_n)

                    if not c.__hash__() in dict and f_n <= cut_off:
                        queue.add(c, f_n)
            cut_off = min(cut_off_list)

        return None