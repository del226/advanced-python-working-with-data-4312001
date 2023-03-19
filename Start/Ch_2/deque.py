# deque objects are like double-ended queues

import collections
import string


# TODO: initialize a deque with lowercase letters
a = collections.deque(string.ascii_lowercase)
# TODO: deques support the len() function
print(f"Item count: {len(a)}")
# TODO: deques can be iterated over
for elem in a:
    print(elem.upper())
# TODO: manipulate items from either end
d = collections.deque()
d.append(2)
d.append(3)
print("d: ", d)
d.appendleft(1)
print("d: ", d)
d.pop()
print("d after pop:", d)
# TODO: use an index to get a particular item

