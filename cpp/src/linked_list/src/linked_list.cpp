#include "linked_list/linked_list.h"

namespace linked_list
{

template<typename T>
Node<T>::Node(T _value): value(_value) {}

template<typename T>
LinkedList<T>::LinkedList(int data) {
	auto node = Node<int>(data);
	head = &node;
	
	if(!head)
		std::cout << "si, esta bien..." << std::endl;
	if(head)
		std::cout << "head: " << head->value << std::endl;
}
//LinkedList<T>::LinkedList(std::vector<T> data) {
	//for(auto e: data)
		//std::cout << "inserting: " << std::to_string(e) << std::endl;
//}

} // namespace linked_list

// only here for testing
int main(int argc, char const *argv[])
{
	if (argc < 2) {
		// report version
		std::cout << argv[0] << " Version " << "1.0.0" << ".\n";
		std::cout << "Usage: " << argv[0] << " <your name>" << std::endl;
		return 1;
	}

	int test = 69;
	auto list = linked_list::LinkedList<int>(test);
	//std::vector<int> test = {1, 2, 3, 4, 5};
	//auto list = linked_list::LinkedList<int>(test);
	//auto node = linked_list::Node<int>(69);
	//std::cout << argv[1] << " quiere mucho a su marion :(" << std::endl;
	//std::cout << "print node: " << std::to_string(node.value) << std::endl;
	return 0;
}
