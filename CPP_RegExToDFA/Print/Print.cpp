#include "Print.h"

std::string PrintEndStates(const std::vector<int> &EndStates) {
	std::string retString;
	size_t last = EndStates.size() - 1;

	for (size_t i = 0; i < last; i++) {
		retString += std::to_string(EndStates[i]);
		retString += ", ";
	}

	retString += std::to_string(EndStates[last]);

	return retString;
}

// NFA & DFA Output function
void Print(const AdjusmentList &NFA, const std::vector<int> &EndStates, const std::string &type) {
	std::cout << "\nYour " << type << ":" << std::endl;
	int cnt = 0;
	std::cout << "Start: 0; End: " << PrintEndStates(EndStates) << ".";
	std::cout << std::endl;
	for (const auto &vec : NFA) {
		for (const auto &p : vec) {
			std::cout << "\t(" << cnt << " '" << p.second << "' " << p.first << ")" << std::endl;
//			std::cout << cnt << "((" << cnt << "))" << " -->|" << p.second << "| " << p.first << "((" << p.first << "))" << std::endl;
		}
		cnt++;
	}
	std::cout << std::endl;
}