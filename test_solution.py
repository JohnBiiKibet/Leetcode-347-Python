from solution import Solution

def test_top_k_frequent_standard():
    sol = Solution()
    # Example 1 from LeetCode
    assert sorted(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]

def test_top_k_frequent_single_element():
    sol = Solution()
    # Example 2 from LeetCode
    assert sol.topKFrequent([1], 1) == [1]

def test_top_k_frequent_all_unique():
    sol = Solution()
    # All elements have a frequency of 1, return any k elements
    result = sol.topKFrequent([1, 2, 3, 4], 2)
    assert len(result) == 2
    assert set(result).issubset({1, 2, 3, 4})

def test_top_k_frequent_negative_numbers():
    sol = Solution()
    # Testing negative numbers and varying frequencies
    assert sorted(sol.topKFrequent([-1, -1, 2, 2, 2, 3], 2)) == [-1, 2]
