#include "stack/stack.h"

namespace stack
{

template<typename T>
Node<T>::Node(T _value): value(_value) {}

template<typename T>
Stack<T>::Stack() {}

template<typename T>
Stack<T>::Stack(const std::vector<T>& data) {
	for(auto e: data)
		this->push(e);
}

template<typename T>
void Stack<T>::push(const T& key) {
	//special case: empty list
	if(!this->head){
		this->head = std::shared_ptr<Node<T>>(new Node<T>(key));
		return;
	}
	//general case
	auto tmp = this->head;
	this->head = std::shared_ptr<Node<T>>(new Node<T>(key));
	this->head->next = tmp;
}

template<typename T>
std::shared_ptr<Node<T>> Stack<T>::pop() {
	//special case: empty list
	if(!this->head)
		return nullptr;
	auto tmp = this->head;
	this->head = this->head->next;
	return tmp;
}

template<typename T>
std::shared_ptr<Node<T>> Stack<T>::peek() {
	//special case: empty list
	if(!this->head)
		return nullptr;
	return this->head;
}

} // namespace stack

// only here for testing while we implement the gtest module
int main()
{
	std::vector<int> test = {1, 2, 3, 4, 5, 6, 7, 8};
	auto linked = stack::Stack<int>(test);
	auto node = linked.pop();
	node = linked.peek();
	return 0;
}
