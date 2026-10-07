
import heapq
from Collection import Counter 
from Typing import List

class Solution:
  def topKFrequentElements(Self,nums:List[int], K:[int]) ->List[int]:
    count = Counter(nums)
    min_heap[]
    for nums,freq in count.items():
      heapq.heappush(min_heap, (nums, freq))
      if len(min_heap) > K:
        heapq.heappop(min_heap)

Return [nums for freq, nums in min_heap]
