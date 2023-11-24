#include <iostream>
#include <vector>
#include <set>
using AdjusmentList = std::vector<std::set<std::pair<int, char>>>;
void Print(const AdjusmentList &NFA, const std::vector<int> &EndStates, const std::string &type);