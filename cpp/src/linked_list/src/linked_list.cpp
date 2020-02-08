#include "linked_list/linked_list.h"

namespace linked_list
{

template<typename T>
Node<T>::Node(T _value): value(_value) {}

template<typename T>
LinkedList<T>::LinkedList() {}

//template<typename T>
//LinkedList<T>::LinkedList(std::vector<T> data) {
	//for(auto e: data)
		//this->insert(e);
//}


template<typename T>
void LinkedList<T>::append(T& key) {
	if(!head){
		head = new Node<T>(key);
		return;
	}
	auto node = head;
	while(node->next)
		node = node->next;
	node->next = new Node<T>(key);
}

template<typename T>
Node<T>* LinkedList<T>::search(T& key) {
	if(!head)
		return nullptr;
	auto node = head;
	while(node){
		if(node->value == key)
			return node;
		node = node->next;
	}
	return nullptr;
}

template<typename T>
void LinkedList<T>::traverse() {
	if(!head)
		return;
	auto node = head;
	while(node){
		std::cout << "->(" + std::to_string(node->value) << ")";
		node = node->next;
	}
	std::cout << std::endl;
}

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
	auto linked = linked_list::LinkedList<int>();
	linked.append(test);
	test = 117;
	linked.append(test);
	test = 72;
	linked.append(test);
	linked.traverse();
	auto node = linked.search(test);
	if(node)
		std::cout << "found: " << std::to_string(node->value) << std::endl;
	//std::vector<int> test = {1, 2, 3, 4, 5};
	//auto list = linked_list::LinkedList<int>(test);
	//auto node = linked_list::Node<int>(69);
	//std::cout << argv[1] << " quiere mucho a su marion :(" << std::endl;
	//std::cout << "print node: " << std::to_string(node.value) << std::endl;
	return 0;
}
