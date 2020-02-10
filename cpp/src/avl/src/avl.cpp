#include "avl/avl.h"

namespace avl
{

template<typename T>
Node<T>::Node(T _value): value(_value) {}

template<typename T>
AVL<T>::AVL() {}

template<typename T>
AVL<T>::AVL(const std::vector<T>& data) {
	for(T e: data)
		this->insert(e);
}

template<typename T>
void AVL<T>::insert(const T& key) {
	if(!this->root) {
		this->root = std::shared_ptr<Node<T>>(new Node<T>(key));
		return;
	}
	return this->insert(key, this->root);
}

template<typename T>
int AVL<T>::height(std::shared_ptr<Node<T>> node){
	if(!node)
		return 0;
	int h_left = 0, h_right = 0;
	if(node->left)
		h_left += node->left->height;
	if(node->right)
		h_right += node->right->height;
	return std::max(h_left, h_right) + 1;
}

template<typename T>
void AVL<T>::insert(const T& key, std::shared_ptr<Node<T>> node) {
	if(!node)
		return;
	//standard insertion
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
	//update height
	node->height = this->height(node);
	//repair violations
	auto balance_factor = this->height(node->right) - this->height(node->left);
	//right rotation
	if(balance_factor < -1) {
		//compound left rotation
		if(key > node->left->value)
			this->rotate_left(node->left);
		this->rotate_right(node);
	}
	//left rotation
	else if(balance_factor > 1){
		//compound right rotation
		if(key < node->right->value)
			this->rotate_right(node->right);
		this->rotate_left(node);
	}
}

template<typename T>
std::shared_ptr<Node<T>> AVL<T>::max() {
	if(!this->root)
		return nullptr;
	auto node = this->root;
	while(node->right)
		node = node->right;
	return node;
}

template<typename T>
std::shared_ptr<Node<T>> AVL<T>::min() {
	if(!this->root)
		return nullptr;
	auto node = this->root;
	while(node->left)
		node = node->left;
	return node;
}

template<typename T>
std::shared_ptr<Node<T>> AVL<T>::successor(const T& key) {
	if(!this->root)
		return nullptr;
	return this->successor(key, this->root);
}

template<typename T>
std::shared_ptr<Node<T>> AVL<T>::successor(const T& key, 
										   std::shared_ptr<Node<T>> node,
										   std::shared_ptr<Node<T>> ancestor) {
	if(!node)
		return ancestor;
	if(node->value == key) {
		//no right child to explore, return the next biggest ancestor
		if(!node->right)
			return ancestor;
		//explore and return the min of the left subtree
		else {
			auto tmp = node->right;
			while(tmp->left)
				tmp = tmp->left;
			return tmp;
		}
	}
	if(key < node->value)
		return this->successor(key, node->left, node);
	else
		return this->successor(key, node->right, ancestor);
}

/// standard binary search
template<typename T>
std::shared_ptr<Node<T>> AVL<T>::search(const T& key) {
	if(!this->root)
		return nullptr;
	return this->search(key, this->root);
}

template<typename T>
std::shared_ptr<Node<T>> AVL<T>::search(const T& key,
										std::shared_ptr<Node<T>> node) {
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
void AVL<T>::rotate_right(std::shared_ptr<Node<T>> node) {
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
	//update height...
	node->right->height = this->height(node->right);
	node->height = this->height(node);
}

/// standard left rotation: https://en.wikipedia.org/wiki/AVL_tree#Simple_rotation
template<typename T>
void AVL<T>::rotate_left(std::shared_ptr<Node<T>> node) {
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
	//update height...
	node->left->height = this->height(node->left);
	node->height = this->height(node);
}

/// initializer for the recursive erase function
template<typename T>
void AVL<T>::erase(const T& key) {
	if(!this->root)
		return;
	std::shared_ptr<Node<T>> father = nullptr;
	return erase(key, this->root, father);
}

/// rotate the node to be erased until it becomes a leaf and then delete is trivial
template<typename T>
void AVL<T>::erase(const T& key,
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
			this->erase(key, node->left, node);
		else
			this->erase(key, node->right, node);
	}
	//update height
	node->height = this->height(node);
	//repair violations
	auto balance_factor = this->height(node->right) - this->height(node->left);
	//right rotation
	if(balance_factor < -1) {
		//compound left rotation
		if(this->height(node->left->right) > this->height(node->left->left))
			this->rotate_left(node->left);
		this->rotate_right(node);
	}
	//left rotation
	else if(balance_factor > 1){
		//compound right rotation
		if(this->height(node->right->left) > this->height(node->right->right))
			this->rotate_right(node->right);
		this->rotate_left(node);
	}
}

template<typename T>
void AVL<T>::traverse() {
	if(!this->root)
		return;
	return traverse(this->root);
}

template<typename T>
void AVL<T>::traverse(std::shared_ptr<Node<T>> node, int level) {
	if(!node)
		return;
	this->traverse(node->left, level+1);
	for(auto i = 0; i < level; i++)
		std::cout << "\t";
	std::cout << "-->(" << std::to_string(node->value) << ")"
				<< "h" << node->height << std::endl;
	this->traverse(node->right, level+1);
}

} // namespace avl

// only here for testing while we implement the gtest module
int main()
{
	std::vector<int> test = {5,7,0,9,3,2,8};
	auto tree = avl::AVL<int>(test);
	tree.traverse();
	auto to_erase = 5;
	std::cout << "----- erasing: " << to_erase << " -----" << std::endl;
	//tree.erase(to_erase);
	//tree.traverse();
	auto node = tree.search(9);
	if(node)
		std::cout << "node found: " << std::to_string(node->value) << std::endl;
	node = tree.max();
	if(node)
		std::cout << "max node found: " << std::to_string(node->value) << std::endl;
	node = tree.min();
	if(node)
		std::cout << "min node found: " << std::to_string(node->value) << std::endl;
	node = tree.successor(8);
	if(node)
		std::cout << "successor node found: " << std::to_string(node->value) << std::endl;
	return 0;
}
