# You are given a node that is the beginning of a linked list. This list always
# contains a tail and a loop.
#
# Your objective is to determine the length of the loop.
#
# For example in the following picture the tail's size is 3 and the loop size is
# 11.
#
# Use the `next' attribute to get the following node
#
# node.next
#
# Note: do NOT mutate the nodes!

def loop_size(node):
    pass

# Make a short chain with a loop of 3
node1 = Node()
node2 = Node()
node3 = Node()
node4 = Node()
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2
print(loop_size(node1))                      # 3, Loop size of 3 expected

# Make a longer chain with a loop of 29
nodes = [Node() for _ in xrange(50)]
for node, next_node in zip(nodes, nodes[1:]):
    node.next = next_node
nodes[49].next = nodes[21]
print(loop_size(nodes[0]))                   # 29, Loop size of 29 expected

# Make a very long chain with a loop of 1087
chain = create_chain(3904, 1087)
print(loop_size(chain))                      # 1087, Loop size of 1087 expected
