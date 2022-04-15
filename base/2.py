def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i, n):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


def bubble_sort(nums):
    n = len(nums)
    for c in range(n):
        for i in range(1, n-c):
            if nums[i-1] > nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
    return nums


def insertion_sort(nums):
    n = len(nums)
    for i in range(n):
        while i > 0 and nums[i-1] > nums[i]:
            nums[i - 1], nums[i] = nums[i], nums[i - 1]
            i-=1
    return nums


def quick_sort(nums):
    n = len(nums)

    def quick(left, right):
        if left > right:
            return nums
        pivot = left
        i = left
        j = right
        while i < j:
            while i <j  and nums[j] > nums[pivot]:
                j -= 1
            while i <j  and nums[i] < nums[pivot]:
                i += 1

            nums[i], nums[j] = nums[j], nums[i]

        nums[j], nums[pivot] = nums[pivot], nums[j]
        quick(left, j-1)
        quick(j+1, right)
        return nums

    quick(0, n-1)





if __name__ == '__main__':
    nums = [1,4,3,2,6,9,7,1,4,10,101,32,2,3,6]
    selection_sort(nums)
    print(nums)