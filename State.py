# this class only for the first time setup init state for problem and is given to every search
class State:
    def __init__(self, pipes: list, parent, g_n: int, h_n: int, prev_action: tuple):
        self.pipes = pipes
        self.parent = parent
        self.g_n = g_n
        self.prev_action = prev_action

        self.h_n = h_n
        # self.color = ''

    def change_between_two_pipe(self, pipe_src_ind: int, pipe_dest_ind: int):
        self.pipes[pipe_dest_ind].add_ball(self.pipes[pipe_src_ind].remove_ball())

    def h(self):
        for pipe in pipes:
            blue, red = pipe.same_color()
            if blue > red:
                self.h_n = blue
                return self.h_n
            else:
                self.h_n = red
                return self.h_n


    def __hash__(self):
        hash_strings = []
        for i in self.pipes:
            hash_strings.append(i.__hash__())
        hash_strings = sorted(hash_strings)
        hash_string = ''
        for i in hash_strings:
            hash_string += i + '###'
        return hash_string
