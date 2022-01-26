# Phase I

## Write the tree node class

Create a file named `tree.py`. In there, declare a class named `Node`. Create an initializer for `Node` that does the following things.

* Accepts a parameter named `value` and sets an instance variable named `_value` to that value

* Sets the `_parent` instance variable to `None`

* Sets the `_children` instance variable to a new empty list

Then, add the following to the class:

* A getter property method named `value` that returns the value in `_value`

* A getter property method named `children` that returns the value of `_children`

* A method named `add_child` that takes a node to append it to the list in `_children` and update the node's `_parent`, if the node is not already in `_children`

* A method named `remove_child` that takes a node to remove it from the list in `_children` and resets its `_parent` to `None`

* A getter property method named `parent` that returns the value of `_parent`

* A setter property method named `parent` that sets the parent property *and* calls the `add_child` method of the parent node passing itself as the node to add to the list of children

Once you do that, you should be able to run the tests and see that all of the tests for `__init__()` works and most of the ones for `parent()` should pass. You'll finish the other tests for that method soon

## Reassign parents

Currently, the `parent()` setter does not update a node's children when it is reassigned or removed as a parent. Add the following code to the bottom of your `tree.py` file and run `python3 tree.py` to manually test and examine the children:

```zsh
node1 = Node("root1")
node2 = Node("root2")
node3 = Node("root3")

node3.parent = node1
node3.parent = node2

print(node1.children)
print(node2.children)
```

You should see two lists containing `node3` w/ the same identifier:

```zsh
[<__main__.Node object at 0x10ee02640>]
[<__main__.Node object at 0x10ee02640>]
```

When you assign `node1` as the parent of `node3`, `node3` adds itself to the children of `node1`. When you then assign the parent of `node3` to `node2`, `node3` adds itself to the children of `node2`, but *is still in the children of `node1`*. That doesn't make sense.

Modify the `parent()` setter to *remove* the child from the existing parent (if one exists) *before* adding itself to the new parent's children list. You should have already implemented the `remove_child` method. Use it.

After adding the condition to remove the child node from the parent if the child has a parent, you'll receive a new error:

```zsh
AttributeError: 'NoneType' object has no attribute 'add_child'
```

Add a condition to make sure that the input parent `node` is not `None` before adding the child node to the parent. Now if you run `python3 tree.py` again, you'll notice that your script is running in an endless recursive loop w/ the following error:

```py
RecursionError: maximum recursion depth exceeded
```

Think of how the `add_child` and `remove_child` methods are both invoking the `parent()` setter. What would be the base case to prevent an endless recursive call of the `parent()` setter?

Add the base case. Manually test your `parent()` setter. Once you are no longer receiving errors, comment out the test cases and run the test suite w/ `python -m unittest`. Now all of the `parent()` setter tests should pass. You should have four remaining tests to pass

## Searching

Write a method named `depth_search(value)` that takes a value to search for, performs a depth-first search, and returns the node that contains the value, if it exists. Otherwise, it should return `None`.

Write a method named `breadth_search(value)` that takes a value to search for, performs a breadth-first search, and returns the node that contains the value, if it exists. Otherwise, it should return `None`.

All of the tests should now pass.
