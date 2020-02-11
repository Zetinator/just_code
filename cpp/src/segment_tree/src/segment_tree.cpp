#include <bits/stdc++.h>

const u_int64_t N = std::numeric_limits<u_int64_t>::max()/2;  // limit for array size
std::unordered_map<int, int> tree;

void modify(int n_element, int new_value) {
    for (tree[n_element += N] = new_value; n_element > 0; n_element >>= 1)
        tree[n_element >> 1] = tree[n_element] + tree[n_element ^ 1];
}

int query(int l, int r) {
    int res = 0;
    for (l += N, r += N; l < r; l >>= 1, r >>= 1) {
        if (l & 1)
            res += tree[l++];
        if (r & 1)
            res += tree[--r];
    }
    return res;
}

int main() {
    modify(1, 69);
    modify(2, 1);
    printf("%d\n", query(0, 10));
	std::cout << "print the tree:\n";
    for(auto e:tree)
	    std::cout << std::to_string(e.first) << " " << e.second << "\n";
    return 0;
}