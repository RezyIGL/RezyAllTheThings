#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <queue>
using SETInt = std::set<int>;
using AdjusmentList = std::vector<std::set<std::pair<int, char>>>;
using DFAContainer = std::map<SETInt, std::set<std::pair<SETInt, char>>>;
std::tuple<AdjusmentList, std::vector<int>> CreateDFA(AdjusmentList NFA, const std::vector<int> &NFAEndStates);