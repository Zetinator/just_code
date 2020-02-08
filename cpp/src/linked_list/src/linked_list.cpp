#include "linked_list/linked_list.h"

namespace linked_list
{

template<typename T>
class LinkedList<T>::Node {
	//basic chainable unit
	private:
		T value;
		Node* next;
	public:
		Node(const T& _value): value(_value), next(nullptr_t){};
		~Node();
		// print operator
		operator std::string(){return std::string(value);};
};

template<typename T>
//LinkedList<T>::LinkedList(std::vector<T> data) {
LinkedList<T>::LinkedList(uint32_t _value) {
	Node* head(_value);
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

	//std::vector<uint32_t> test = {1, 2, 3, 4, 5};
	auto node = linked_list::LinkedList<uint32_t>(69);
	std::cout << argv[1] << " quiere mucho a su marion :(" << std::endl;
	return 0;
}
