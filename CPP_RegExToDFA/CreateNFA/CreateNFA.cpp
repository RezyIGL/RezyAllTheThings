#include "CreateNFA.h"
#include "../Print/Print.h"

// Global functions and variable for State counting
int currentNFAState = 0;

void NextNFAState() {
	currentNFAState++;
}

void ResetNFAState() {
	currentNFAState = 0;
}

// NFA Char Handlers
void CreateLetter(AdjusmentList &NFA, const char &let, std::vector<std::pair<int, int>> &hvec) {
	NextNFAState();
	int newState1Id = currentNFAState;

	NextNFAState();
	int newState2Id = currentNFAState;

	int lastId = hvec.rbegin()->second;
	std::pair<int, int> newConnection = {newState1Id, newState2Id};
	hvec.push_back(newConnection);

	std::set<std::pair<int, char>> newState1;
	std::set<std::pair<int, char>> newState2;

	NFA.push_back(newState1);
	NFA.push_back(newState2);

	NFA[newState1Id].insert({newState2Id, let});
	NFA[lastId].insert({newState1Id, '_'});
}

void CreateAsterisk(AdjusmentList &NFA, std::vector<std::pair<int, int>> &hvec) {
	NextNFAState();
	int newStateId = currentNFAState;

	hvec.emplace_back(newStateId, newStateId);
	auto lastId = hvec.rbegin();
	lastId++;

	std::set<std::pair<int, char>> newState;
	NFA.push_back(newState);

	NFA[lastId->second].insert({lastId->first, '_'});
	NFA[lastId->second].insert({newStateId, '_'});
	NFA[lastId->first - 1].insert({newStateId, '_'});
}

void CreatePlus(AdjusmentList &NFA, std::vector<std::pair<int, int>> &hvec) {
	NextNFAState();
	int newStateId = currentNFAState;

	hvec.emplace_back(newStateId, newStateId);
	auto lastId = hvec.rbegin();
	lastId++;

	std::set<std::pair<int, char>> newState;
	NFA.push_back(newState);

	NFA[lastId->second].insert({lastId->first, '_'});
	NFA[lastId->second].insert({newStateId, '_'});
}

void CreateBrackets(AdjusmentList &NFA, const std::string &expr, std::vector<std::pair<int, int>> &helpfulVector) {
	int currState = currentNFAState;

	NFA[currState].insert({currState + 1,'_'});

	auto it = expr.begin();
	while (it != expr.end()) {
		switch (*it) {
			case '*': {
				CreateAsterisk(NFA, helpfulVector);
				it++;
				break;
			}
			case '+': {
				CreatePlus(NFA, helpfulVector);
				it++;
				break;
			}
			case '(': {
				std::string insideExpr;
				std::stack<char> bracketsStack;
				bracketsStack.push('(');

				while (!bracketsStack.empty()) {
					it++;
					if (*it == '(') {
						bracketsStack.push('(');
						insideExpr.push_back(*it);
					} else if (*it == ')') {
						bracketsStack.pop();
						if (bracketsStack.empty()) break;
						else insideExpr.push_back(*it);
					} else {
						insideExpr.push_back(*it);
					}
				}

				CreateBrackets(NFA, insideExpr, helpfulVector);

				it++;
				break;
			}
			default: {
				CreateLetter(NFA, *it, helpfulVector);
				it++;
				break;
			}
		}
	}

	helpfulVector.emplace_back(currState + 1, currentNFAState);
}

// NFA Creation function
std::tuple<AdjusmentList, std::vector<int>> CreateNFA(const std::string &expr) {

	// Non-deterministic Finite Automaton container.
	AdjusmentList NFA;
	NFA.emplace_back();

	std::vector<std::pair<int, int>> helpfulVector;
	helpfulVector.emplace_back(currentNFAState, currentNFAState);

	auto it = expr.begin();
	while (it != expr.end()) {
		switch (*it) {
			case '*': {
				CreateAsterisk(NFA, helpfulVector);
				it++;
				break;
			}
			case '+': {
				CreatePlus(NFA, helpfulVector);
				it++;
				break;
			}
			case '(': {
				std::string insideExpr;
				std::stack<char> bracketsStack;
				bracketsStack.push('(');

				while (!bracketsStack.empty()) {
					it++;
					if (*it == '(') {
						bracketsStack.push('(');
						insideExpr.push_back(*it);
					} else if (*it == ')') {
						bracketsStack.pop();
						if (bracketsStack.empty()) break;
						else insideExpr.push_back(*it);
					} else {
						insideExpr.push_back(*it);
					}
				}

				CreateBrackets(NFA, insideExpr, helpfulVector);

				it++;
				break;
			}
			default: {
				CreateLetter(NFA, *it, helpfulVector);
				it++;
				break;
			}
		}
	}

	std::vector<int> EndStates = {currentNFAState};

	return {NFA, EndStates};
}