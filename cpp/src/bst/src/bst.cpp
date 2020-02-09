#include "bst/bst.h"

namespace bst
{

template<typename T>
Node<T>::Node(T _value): value(_value) {}

template<typename T>
BST<T>::BST() {}

template<typename T>
BST<T>::BST(const std::vector<T>& data) {
	for(T e: data)
		this->insert(e);
}

template<typename T>
void BST<T>::insert(const T& key) {
	if(!this->root) {
		this->root = std::shared_ptr<Node<T>>(new Node<T>(key));
		return;
	}
	return this->insert(key, this->root);
}

template<typename T>
void BST<T>::insert(const T& key, std::shared_ptr<Node<T>> node) {
	//base case: no node
	if(!node)
		return;
	if(node->value == key)
		throw std::invalid_argument("No, duplicates allowed!");
	if(key < node->value) {
		if(node->left)
			this->insert(key, node->left);
		else
			node->left = std::shared_ptr<Node<T>>(new Node<T>(key));
	}
	else {
		if(node->right)
			this->insert(key, node->right);
		else
			node->right = std::shared_ptr<Node<T>>(new Node<T>(key));
	}
}

template<typename T>
std::shared_ptr<Node<T>> BST<T>::max() {
	if(!this->root)
		return nullptr;
	auto node = this->root;
	while(node->right)
		node = node->right;
	return node;
}

template<typename T>
std::shared_ptr<Node<T>> BST<T>::min() {
	if(!this->root)
		return nullptr;
	auto node = this->root;
	while(node->left)
		node = node->left;
	return node;
}

template<typename T>
std::shared_ptr<Node<T>> BST<T>::search(const T& key) {
	if(!this->root)
		return nullptr;
	return this->search(key, this->root);
}

template<typename T>
std::shared_ptr<Node<T>> BST<T>::search(const T& key, std::shared_ptr<Node<T>> node) {
	if(!node)
		return nullptr;
	if(key == node->value)
		return node;
	if(key < node->value)
		return this->search(key, node->left);
	else
		return this->search(key, node->right);
}

template<typename T>
void BST<T>::traverse() {
	if(!this->root)
		return;
	return traverse(this->root);
}

template<typename T>
void BST<T>::traverse(std::shared_ptr<Node<T>> node, int level) {
	if(!node)
		return;
	this->traverse(node->left, level+1);
	for(auto i = 0; i < level; i++)
		std::cout << "\t";
	std::cout << "-->(" << std::to_string(node->value) << ")" << std::endl;
	this->traverse(node->right, level+1);
}

} // namespace bst

// only here for testing while we implement the gtest module
int main()
{
	std::vector<int> test = {5,7,0,9,3,2,8};
	auto tree = bst::BST<int>(test);
	tree.traverse();
	auto node = tree.search(9);
	if(node)
		std::cout << "node found: " << std::to_string(node->value) << std::endl;
	node = tree.max();
	if(node)
		std::cout << "max node found: " << std::to_string(node->value) << std::endl;
	node = tree.min();
	if(node)
		std::cout << "min node found: " << std::to_string(node->value) << std::endl;
	return 0;
}
