#include <bits/stdc++.h>

namespace {
	//variadic function
	template<typename T>
		T adder(T v) {
			return v;
		}
	template<typename T, typename... Args>
		T adder(T first, Args... args) {
			std::cout << __PRETTY_FUNCTION__ << "\n";
			return first + adder(args...);
		}

	//tuple maker
	template <typename... T> auto foo(T&&... args) {
		return std::make_tuple(args...);
	}
}

int main()
{
	//init vectors
	auto myList = std::vector<int>{ 6, 3, 7, 8 };

	//init dicts
	auto myDict = std::unordered_map<int, std::string>{ { 5, "foo" }, { 6, "bar" } };

	//init arrays
	std::array<int, 3> erick = {1,2,3};

	std::string marion = "erick quiere mucho a marion";
	std::string r_marion = marion;
	std::reverse_copy(marion.begin(), marion.end(), r_marion.begin());
	std::cout << r_marion << std::endl;
	std::cout << marion << std::endl;

	for (auto e : erick)
		std::cout << e << std::endl;

	return 0;
}
