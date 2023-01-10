# Prefix and Postfix

The problem [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/description/) in leetcode asked for an algorithm that is O(n) and would return a list with the product of all values except the one in the i'th position. The problem explains it better than me. The thing is that, I was banging my head into the wall trying to figure out how can you achieve this.

Two things ariesed from solving this issue, first, think about O(2n) or O(3n) or O(100n), that would still be O(n), so whenever you see this into play think about possible solutions for this outcome. 

But the real problem was solved with the second thing I learned. I was not able to see how this could be achieved without O(n^2) algorithms, but then came the prefix and postfix solution. Neetcode made an incredible [video](https://www.youtube.com/watch?v=bNvIQI2wAjk) about this.

Essentially if I multiply the prefix value and postfix values, I can get the result.
All I needed to do is get the prefix and postfix, and store their products.
You can do this by having a variable keep value of the current multiplication and save it in a list while doing it.

Remember this, think about prefixes and postfixes when you need the product of values of a list. You can find an implementation [here](./array/product_of_array_self.py).