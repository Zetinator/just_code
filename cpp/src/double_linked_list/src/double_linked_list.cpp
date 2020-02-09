#include "double_linked_list/double_linked_list.h"

namespace double_linked_list
{

template<typename T>
Node<T>::Node(T _value): value(_value) {}

template<typename T>
DoubleLinkedList<T>::DoubleLinkedList() {}

template<typename T>
DoubleLinkedList<T>::DoubleLinkedList(const std::vector<T>& data) {
	for(auto e: data)
		this->append(e);
}

template<typename T>
void DoubleLinkedList<T>::append(const T& key) {
	//special case: empty list
	if(!this->head){
		this->head = std::shared_ptr<Node<T>>(new Node<T>(key));
		this->tail = this->head;
		return;
	}
	//special case: single item
	if(this->head == this->tail) {
		this->head->next = std::shared_ptr<Node<T>>(new Node<T>(key));
		this->tail = this->head->next;
		this->tail->previous = this->head;
		return;
	}
	//general case
	this->tail->next = std::shared_ptr<Node<T>>(new Node<T>(key));
	this->tail->next->previous = this->tail;
	this->tail = this->tail->next;
}

template<typename T>
std::shared_ptr<Node<T>> DoubleLinkedList<T>::pop_back() {
	//special case: empty list
	if(!this->head)
		return nullptr;
	return this->tail;
}

template<typename T>
std::shared_ptr<Node<T>> DoubleLinkedList<T>::pop_front() {
	//special case: empty list
	if(!this->head)
		return nullptr;
	return this->head;
}

template<typename T>
std::shared_ptr<Node<T>> DoubleLinkedList<T>::search(const T& key) {
	if(!this->head)
		return nullptr;
	auto node = this->head;
	while(node){
		if(node->value == key)
			return node;
		node = node->next;
	}
	return nullptr;
}

template<typename T>
void DoubleLinkedList<T>::insert(const T& key, int index) {
	//special case: empty list
	if(!this->head){
		this->head = std::shared_ptr<Node<T>>(new Node<T>(key));
		this->tail = this->head;
		return;
	}
	//special case: insert as head
	if(index == 0){
		auto tmp = this->head;
		this->head = std::shared_ptr<Node<T>>(new Node<T>(key));
		this->head->next = tmp;
		this->head->next->previous = this->head;
		return;
	}
	//general case:
	auto node = this->head;
	while(node->next && (index-1) > 0){
		node = node->next;
		index -= 1;
	}
	auto tmp = node->next;
	node->next = std::shared_ptr<Node<T>>(new Node<T>(key));
	node->next->previous = node;
	node->next->next = tmp;
	node->next->next->previous = node->next;
}

template<typename T>
void DoubleLinkedList<T>::erase(const T& key) {
	//special case: empty list
	if(!this->head)
		return;
	//special case: is tail
	if(this->tail->value == key){
		//single item? take care of the head also...
		if(this->tail == this->head)
			this->head = this->tail->previous;
		this->tail = this->tail->previous;
		if(this->tail)
			this->tail->next = nullptr;
		return;
	}
	//special case: is head
	if(this->head->value == key){
		this->head = this->head->next;
		if(this->head)
			this->head->previous = nullptr;
		return;
	}
	//general case:
	auto node = this->head;
	auto parent = node;
	while(node) {
		if(node->value == key) {
			parent->next = node->next;
			return;
		}
		parent = node;
		node = node->next;
	}
	return;
}

template<typename T>
void DoubleLinkedList<T>::traverse() {
	if(!this->head)
		return;
	auto node = this->head;
	while(node){
		std::cout << "->(" + std::to_string(node->value) << ")";
		node = node->next;
	}
	std::cout << std::endl;
}

} // namespace double_linked_list

// only here for testing while we implement the gtest module
int main()
{
	std::vector<int> test = {1, 2, 3, 4, 5, 6, 7, 8};
	auto linked = double_linked_list::DoubleLinkedList<int>(test);
	auto node = linked.pop_back();
	node = linked.pop_front();
	linked.insert(69, 0);
	linked.erase(69);
	linked.traverse();
	return 0;
}
