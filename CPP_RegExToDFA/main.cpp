#include "CreateNFA.h"
#include "CreateDFA.h"
#include "Print.h"

int main() {
	// Just text.
	std::cout << "You can use: 'A-Z', 'a-z', '*', '+', '(', ')'" << std::endl;
	std::cout << "Enter your Regular Expression:";

	// RegExp.
	std::string expr;
	std::getline(std::cin, expr);

	// Creating Non-Determined Finite Automaton
	auto &&[NFA, EndStates] = CreateNFA(expr);
	Print(NFA, EndStates, "NFA"); // Print it in console

	// Creating Determined Finite Automaton
	auto &&[DFA, EndStatesDFA] = CreateDFA(NFA, EndStates);
	Print(DFA, EndStatesDFA, "DFA"); // Print it in console

	// We're done
	return 0;
}
