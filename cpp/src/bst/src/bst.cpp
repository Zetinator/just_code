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

/// standard binary search
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

/// standard right rotation: https://en.wikipedia.org/wiki/AVL_tree#Simple_rotation
template<typename T>
void BST<T>::rotate_right(std::shared_ptr<Node<T>> node) {
	if(!node)
		return;
	//set-up
	auto tmp = std::shared_ptr<Node<T>>(new Node<T>(node->value));
	tmp->left = node->left->right;
	tmp->right = node->right;
	//rotate
	node->value = node->left->value;
	node->left = node->left->left;
	node->right = tmp;
}

/// standard left rotation: https://en.wikipedia.org/wiki/AVL_tree#Simple_rotation
template<typename T>
void BST<T>::rotate_left(std::shared_ptr<Node<T>> node) {
	if(!node)
		return;
	//set-up
	auto tmp = std::shared_ptr<Node<T>>(new Node<T>(node->value));
	tmp->left = node->left;
	tmp->right = node->right->left;
	//rotate
	node->value = node->right->value;
	node->left = tmp;
	node->right = node->right->right;
}

/// initializer for the recursive erase function
template<typename T>
void BST<T>::erase(const T& key) {
	if(!this->root)
		return;
	std::shared_ptr<Node<T>> father = nullptr;
	return erase(key, this->root, father);
}

/// rotate the node to be erased until it becomes a leaf and then delete is trivial
template<typename T>
void BST<T>::erase(const T& key,
		std::shared_ptr<Node<T>> node,
		std::shared_ptr<Node<T>> father) {
	if(!node)
		return;
	if(node->value == key) {
		//have children? keep rotating...
		if(node->left || node->right) {
			auto child = (node->left)?node->left:node->right;
			if(node->left == child) {
				this->rotate_right(node);
				this->erase(key, node->right, node);
			}
			else {
				this->rotate_left(node);
				this->erase(key, node->left, node);
			}
		}
		//no children => erase the leaf easily
		else {
			//special case: are you root?
			if(!father){
				this->root = nullptr;
				return;
			}
			//general case:
			if(father->left == node)
				father->left = nullptr;
			else
				father->right = nullptr;
			return;
		}
	}
	//keep looking
	else {
		if(key < node->value)
			return this->erase(key, node->left, node);
		else
			return this->erase(key, node->right, node);
	}

	
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
	auto to_erase = 5;
	std::cout << "----- erasing: " << to_erase << " -----" << std::endl;
	tree.erase(to_erase);
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
