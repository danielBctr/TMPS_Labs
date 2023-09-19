# Laboratory work Nr.1

### Course: TMPS
### Author: Bucătaru Daniel, FAF-211


----

## Theory
The SOLID principles are a set of guidelines for writing clean and maintainable code:

1. Single Responsibility Principle (SRP): Each class should have one responsibility, making code easier to understand and maintain.

2. Open-Closed Principle (OCP): Software entities should be open for extension but closed for modification, allowing for easy updates without altering existing code.

3. Liskov Substitution Principle (LSP): Derived classes should seamlessly replace base classes without changing program behavior, ensuring consistent behavior.

4. Interface Segregation Principle (ISP): Create specific interfaces for classes, avoiding unnecessary method implementations and reducing coupling.

5. Dependency Inversion Principle (DIP): Depend on abstractions, not concrete implementations, for flexibility and easy component substitution.

6. These principles promote modular, flexible, and robust software design.

----
## Objectives:




----
## Implementation description

 This function "generate_word" that takes a string parameter character and returns a string.
 The method first checks if the input character is a terminal symbol, which are the basic building blocks of the grammar. 
 If the character is a terminal, the method simply returns the character.
````
   def word_generator(self, character: str = None) -> str:
        if character is None:
            character = self.start_symbol
        if character in self.terminals:
            return character
        right_sides = self.productions[character]
        random_right_side = random.choice(right_sides)
        word = ''
        for right_char in random_right_side:
            word += self.word_generator(right_char)
        return word
````
 This code represents the method "to_finite_automaton" that converts a context-free grammar into a finite automaton, 
 represented by an instance of the FiniteAutomaton class. The method returns the created automaton.
````
        def to_finite_automaton(self):
        states = set(self.non_terminals) | {''}
        final_states = {''}
        transitions = [Transitions(non_terminal, right_side[1] if len(right_side) > 1 else '', right_side[0]) for
                       non_terminal in self.non_terminals for right_side in self.productions[non_terminal]]
        automaton = FiniteAutomaton(transitions)
        automaton.put_states(states)
        automaton.put_first_state(str(self.start_symbol))
        automaton.put_accept_states(final_states)
        automaton.put_alphabet(self.terminals)
        return automaton
````

 This code represents the method "check_word" that takes a single argument word. 
 The method uses a finite automaton to determine whether the input word is valid
````
    def check_word(self, word):
        state = self.first_state[0]
        for i in word:
            state = next((t.get_next_state() for t in self.transitions if
                          t.get_current_state() == state and t.get_transition_label() == i), None)
            if state is None:
                return False
        return str(state) in self.true_state
````
----
## Conclusions / Screenshots / Results
### Screenshots/Results:

----
### Conclusion:
   In this laboratory work on formal languages, finite automaton, and grammar, 
I have implemented a Python program that provides a suite of functionalities for constructing, 
manipulating, and working with finite automata and grammars.
The program includes a class for FiniteAutomaton, 
which has methods for adding and retrieving states, transitions, and alphabet, 
as well as for checking whether a given input string is accepted by the automaton. 
In addition, there is a Grammar class that can generate random words based on its production rules.
Throughout the laboratory work, I was able to learn about the fundamental concepts of formal languages, finite automata, and grammars. 
I was also able to understand the relationships between these concepts and how they are used in computer science to model and describe various types of languages.
The code that I have implemented during the laboratory work has been tested thoroughly and has proven to work as intended, which has provided me with a better understanding of how these formal systems work.

----
## References

https://github.com/DrVasile/FLFA-Labs/blob/master/1_RegularGrammars/task.md 
