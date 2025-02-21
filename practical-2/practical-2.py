class FiniteAutomaton:
    def __init__(self, states, input_symbols, transitions, initial_state, accepting_states):
        self.states = states
        self.input_symbols = input_symbols
        self.transitions = transitions
        self.initial_state = initial_state
        self.accepting_states = accepting_states

    def process(self, input_string):
        current_state = self.initial_state
        for symbol in input_string:
            if symbol not in self.input_symbols:
                return False  
            current_state = self.transitions.get((current_state, symbol), None)
            if current_state is None:
                return False  
        return current_state in self.accepting_states

states = {1, 2, 3, 4}
input_symbols = {"a", "b"}
transitions = {
    (1, "a"): 2,
    (1, "b"): 3,
    (2, "a"): 1,
    (2, "b"): 4,
    (3, "a"): 4,
    (3, "b"): 1,
    (4, "a"): 3,
    (4, "b"): 2,
}
initial_state = 1
accepting_states = {2}

automaton = FiniteAutomaton(states, input_symbols, transitions, initial_state, accepting_states)

def test_case_1(string):
    for i in range(len(string)):
        if string[i] == "0":
            if i + 2 >= len(string) or string[i + 1] != "1" or string[i + 2] != "1":
                return False
    return True

def test_case_2(string):
    if len(string) < 2:
        return True  
    return string[-1] == string[-2]

def test_case_3(string):
    if not string:
        return False
    return string[0].isalpha() and all(c.isalnum() for c in string)

print("Finite Automaton Test:")
print(automaton.process("ab"))  
print(automaton.process("aa")) 

print("\nTest Case 1:")
print(test_case_1("011"))  
print(test_case_1("010"))  

print("\nTest Case 2:")
print(test_case_2("abc"))  
print(test_case_2("aba"))  

print("\nTest Case 3:")
print(test_case_3("a123"))  
print(test_case_3("1abc"))