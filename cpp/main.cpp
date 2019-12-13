#include <bits/stdc++.h>

auto minimumSwaps(std::vector<int> x){
	auto right_pos = std::unordered_map<int, int>{};
	auto sorted = x;
	std::sort(sorted.begin(), sorted.end());
	for (int i=0; i<sorted.size(); ++i)
		right_pos.insert({sorted[i], i});
	
	int swaps = 0;
	while (sorted != x){
		std::vector<int> entropy = {};
		for (auto i=0; i<x.size(); i++)
			entropy.push_back(i - right_pos[x[i]]);
		auto minima = std::min_element(entropy.begin(), entropy.end());
		auto maxima = std::max_element(minima, entropy.end());
		auto i_min = std::distance(entropy.begin(), minima);
		auto i_max = std::distance(entropy.begin(), maxima);
		std::swap(x[i_min], x[i_max]);
		swaps++;
	}

	return swaps;
}

int main()
{
	//init vectors
	auto x = std::vector<int>{7, 1, 3, 2, 4, 5, 6};
	int res = minimumSwaps(x);
	std::cout << res << std::endl;

	return 0;
}
