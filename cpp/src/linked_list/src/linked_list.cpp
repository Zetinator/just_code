#include "linked_list/linked_list.h"

namespace linked_list
{

template<typename T>
LinkedList<T>::LinkedList(std::vector<T> data) {
	for(auto e: data)
		std::cout << std::to_string(e) << std::endl;
	//Node* head();
}

} // namespace Node

// only here for testing
int main(int argc, char const *argv[])
{
	if (argc < 2) {
		// report version
		std::cout << argv[0] << " Version " << "1.0.0" << ".\n";
		std::cout << "Usage: " << argv[0] << " <your name>" << std::endl;
		return 1;
	}

	std::vector<int> test = {1, 2, 3, 4, 5};
	auto node = linked_list::LinkedList<int>(test);
	std::cout << argv[1] << " quiere mucho a su marion :(" << std::endl;
	return 0;
}
