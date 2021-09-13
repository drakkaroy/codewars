class Automaton(object):

    def __init__(self):
        self.states = []
        self.state = 'q1'

    def transition(self, item):
        if self.state == 'q1':
            if item == '1':
                self.state = 'q2'
            elif item == '0':
                self.state = 'q1'
        elif self.state == 'q2':
            if item == '1':
                self.state = 'q2'
            elif item == '0':
                self.state = 'q3'
        elif self.state == 'q3':
            if item == '1' or item == '0':
                self.state = 'q2'

    def read_commands(self, commands):
        for item in commands:
            self.transition(item)
        return True if self.state == 'q2' else False

my_automaton = Automaton()

my_automaton.read_commands(["1", "0", "0", "1"])

# Best solution 
# class Automaton(object):

#     def __init__(self):
#         self.automata = {('q1', '1'): 'q2', ('q1', '0'): 'q1', 
#                          ('q2', '0'): 'q3', ('q2', '1'): 'q2',
#                          ('q3', '0'): 'q2', ('q3', '1'): 'q2'}
#         self.state = "q1"

#     def read_commands(self, commands):
#         for c in commands:
#             self.state = self.automata[(self.state, c)]
#         return self.state=="q2"

# my_automaton = Automaton()

# Interesting solution

# class Automaton(object):

#     def __init__(self):
#         self.states = {'q1':['q1', 'q2'], 'q2':['q3', 'q2'], 'q3':['q2', 'q2']}
#         self.ini_state = 'q1'
#         self.final_state = 'q2'

#     def read_commands(self, commands):
#         current_state = self.ini_state
#         for alp in commands :
#             current_state = self.states[current_state][int(alp)]
#         return current_state == self.final_state

# my_automaton = Automaton()