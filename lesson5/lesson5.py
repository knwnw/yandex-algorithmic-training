def make_prefix_sum(nums: list) -> list:
    prefix_sum = [0] * (len(nums) + 1)
    for i in range(len(nums) + 1):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
    return prefix_sum


def rsq(prefix_sum, left, right):
    return prefix_sum[right] - prefix_sum[left]


def count_pairs(sorted_list: list, k: int) -> int:  # Why is it O(N)?
    """Find number of pairs of A and B such that (B - A) > k."""
    cnt, j = 0, 0
    for i in range(len(sorted_list)):
        while (j < len(sorted_list) and sorted_list[j] - sorted_list[i] <= k):
            j += 1
        cnt += len(sorted_list) - j
    return cnt


def best_team_sum(players: list) -> int:
    best_sum, now_sum, j = 0, 0, 0
    for i in range(len(players)):
        while (j < len(players)
                and (j == i or players[i] + players[i + 1] >= players[j])):
            now_sum += players[j]
            j += 1
        best_sum = max(best_sum, now_sum)
        now_sum -= players[i]
    return best_sum


def merge_sorted_lists1(nums1: list, nums2: list) -> list:
    """Merge given sorted lists such that the resulted list is also sorted."""
    merged = [0] * (len(nums1) + len(nums2))
    i1, i2 = 0, 0
    inf = max(nums1[-1], nums2[-1]) + 1
    nums1.append(inf)
    nums2.append(inf)
    for k in range(len(nums1) + len(nums2) - 2):
        if nums1[i1] <= nums2[i2]:
            merged[k] = nums1[i1]
            i1 += 1
        else:
            merged[k] = nums2[i2]
            i2 += 1
    nums1.pop()
    nums2.pop()
    return merged


def merge_sorted_lists2(nums1: list, nums2: list) -> list:
    merged = [0] * (len(nums1) + len(nums2))
    i1, i2 = 0, 0
    for k in range(len(nums1) + len(nums2)):
        if i1 != len(nums1) and (i2 == len(nums2) or nums1[i1] <= nums2[i2]):
            merged[k] = nums1[i1]
            i1 += 1
        else:
            merged[k] = nums2[i2]
            i2 += 1
    return merged
