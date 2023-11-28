#include <iostream>
#include <vector>
#include <map>

using AdjencencyList = std::map<int, std::vector<std::pair<int, char>>>;

AdjencencyList DFA = {
		{0, {
				{0, ' '},
				{1, '('},
				{1, ')'},
				{1, '{'},
				{1, '}'},
				{1, ';'},
				{1, ','},
				{1, '.'},
				{1, '>'},
				{1, '*'},
				{2, '<'},
				{4, '!'},
				{6, '='},
				{8, '+'},
				{10, '|'},
				{12, '&'},
				{14, '\''},
				{18, '"'},
				{24, '^'}
		}},
		 {1, {

		 }},
		{2, {

		}},
		{3, {
			
		}}
};

void NextState() {

}

int main() {

}
