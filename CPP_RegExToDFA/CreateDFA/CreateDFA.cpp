#include "CreateDFA.h"

// Не будет комментариев, я устал
int currentDFAState = 0;

void NextDFAState() {
	currentDFAState++;
}

// Making Epsilon closure real
void EClosure (SETInt &Q, AdjusmentList NFA) {

	std::stack<int> T;
	for (auto q : Q) {
		T.push(q);
	}

	while (!T.empty()) {
		int t = T.top();
		T.pop();

		for (auto edge : NFA[t]) {
			if (edge.second == '_') {
				int u = edge.first;

				if (!Q.contains(u)) {
					Q.insert(u);
					T.push(u);
				}
			}
		}
	}
}

// Collecting some stuff
std::map<char, std::set<int>> collect (std::set<int> &key, const AdjusmentList &g) {
	std::map<char, std::set<int>> mp;
	for (auto& v : key) {
		for (auto&& [u, b] : g[v]) {
			mp[b].insert(u);
		}
	}

	mp.erase('_');

	for (auto&& [_, encl] : mp) {
		EClosure(encl, g);
	}

	return mp;
}

// Change current StateSet
std::set<int> move (const std::set<int> &Q, char& el, const AdjusmentList &NFA) {
	std::set<int> result;

	for (auto vertex : Q) {
		for (auto edge : NFA[vertex]) {
			if (edge.second == el && !result.contains(el)) result.insert(edge.first);
		}
	}

	return result;
}

// DFA Creation function
std::tuple<AdjusmentList, std::vector<int>> CreateDFA(AdjusmentList NFA, const std::vector<int> &NFAEndStates) {
	AdjusmentList DFA;
	DFAContainer EClosureMap;
	std::vector<int> EndStates;

	std::queue<SETInt> MapQueue;

	SETInt CurrentStateSet = { 0 };
	EClosure(CurrentStateSet, NFA);

	MapQueue.push(CurrentStateSet);
	while (!MapQueue.empty()) {
		auto vertexSet = MapQueue.front();
		MapQueue.pop();

		if (EClosureMap.contains(vertexSet)) {
			continue;
		}

		EClosureMap[vertexSet] = {};

		auto mp = collect(vertexSet, NFA);

		for (auto &&[elem, closure] : mp) {
			EClosureMap[vertexSet].insert({ closure, elem });
			MapQueue.push(closure);
		}
	}

	std::map<SETInt, int> number;
	for (auto x : EClosureMap) {
		DFA.emplace_back();
		number[x.first] = currentDFAState;
		NextDFAState();
	}

	currentDFAState = 0;

	for (auto &&[key, edges] : EClosureMap) {
		for (const auto &edge : edges) {
			DFA[currentDFAState].insert({number[edge.first], edge.second});
		}
		for (const auto &v : key) {
			if (*NFAEndStates.rbegin() == v) {
				EndStates.push_back(currentDFAState);
			}
		}
		NextDFAState();
	}

	return {DFA, EndStates};
}