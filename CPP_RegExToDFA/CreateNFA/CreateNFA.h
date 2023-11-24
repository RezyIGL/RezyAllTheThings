#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <set>
using AdjusmentList = std::vector<std::set<std::pair<int, char>>>;
std::tuple<AdjusmentList, std::vector<int>> CreateNFA(const std::string &expr);