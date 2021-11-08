class FiniteAutomata:

    def __init__(self, Q, E, q0, F, S):
        self.Q = Q
        self.E = E
        self.q0 = q0
        self.F = F
        self.S = S

    @staticmethod
    def getLine(line):
        return line.strip().split(' ')[2:]

    @staticmethod
    def validate(Q, E, q0, F, S):
        if q0 not in Q:
            return False
        for f in F:
            if f not in Q:
                return False
        for key in S.keys():
            state = key[0]
            symbol = key[1]
            if state not in Q:
                return False
            if symbol not in E:
                return False
            for dest in S[key]:
                if dest not in Q:
                    return False
        return True

    @staticmethod
    def readFromFile(file_name):
        with open(file_name) as file:
            Q = FiniteAutomata.getLine(file.readline())
            E = FiniteAutomata.getLine(file.readline())
            q0 = FiniteAutomata.getLine(file.readline())[0]
            F = FiniteAutomata.getLine(file.readline())
            file.readline()

            S = {}
            for line in file:
                source = line.strip().split('->')[0].strip().replace('(', '').replace(')', '').split(',')[0]
                value = line.strip().split('->')[0].strip().replace('(', '').replace(')', '').split(',')[1]
                destination = line.strip().split('->')[1].strip()

                if (source, value) in S.keys():
                    S[(source, value)].append(destination)
                else:
                    S[(source, value)] = [destination]

            if not FiniteAutomata.validate(Q, E, q0, F, S):
                raise Exception("Wrong input file.")

            return FiniteAutomata(Q, E, q0, F, S)

    """
    DFA refers to Deterministic Finite Automata. A Finite Automata(FA) is said to be deterministic if:
     1.in DFA, given the current state we know what the next state will be
     2.it has only one unique next state
     3.it has no choices or randomness 
    
    """
    def isDfa(self):
        for k in self.S.keys():
            if len(self.S[k]) > 1:
                return False
        return True

    def isAccepted(self, sequence):
        if self.isDfa():
            current = self.q0
            for symbol in sequence:
                if (current, symbol) in self.S.keys():
                    current = self.S[(current, symbol)][0]
                else:
                    return False
            return current in self.F
        return False