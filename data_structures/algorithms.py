"""
Tập hợp các thuật toán sắp xếp, tìm kiếm và các thuật toán bổ trợ.
Mỗi thuật toán đều có phân tích độ phức tạp và use cases phù hợp.
"""

class SortingAlgorithms:
    @staticmethod
    def bubble_sort(arr):
        """
        Bubble Sort - Sắp xếp nổi bọt
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        Stable: Yes
        Best for: Small arrays and nearly sorted arrays
        """
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr

    @staticmethod
    def selection_sort(arr):
        """
        Selection Sort - Sắp xếp chọn
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        Stable: No
        Best for: Small arrays where memory is limited
        """
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

    @staticmethod
    def insertion_sort(arr):
        """
        Insertion Sort - Sắp xếp chèn
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        Stable: Yes
        Best for: Small arrays and nearly sorted arrays
        """
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    @staticmethod
    def merge_sort(arr):
        """
        Merge Sort - Sắp xếp trộn
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        Stable: Yes
        Best for: Large datasets where stable sort is needed
        """
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = SortingAlgorithms.merge_sort(arr[:mid])
        right = SortingAlgorithms.merge_sort(arr[mid:])

        return SortingAlgorithms._merge(left, right)

    @staticmethod
    def _merge(left, right):
        """Helper function for merge sort"""
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    @staticmethod
    def quick_sort(arr):
        """
        Quick Sort - Sắp xếp nhanh
        Time Complexity: O(n log n) average, O(n^2) worst
        Space Complexity: O(log n)
        Stable: No
        Best for: Large datasets where average case performance is important
        """
        if len(arr) <= 1:
            return arr

        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        return SortingAlgorithms.quick_sort(left) + middle + SortingAlgorithms.quick_sort(right)

    @staticmethod
    def heap_sort(arr):
        """
        Heap Sort - Sắp xếp vun đống
        Time Complexity: O(n log n)
        Space Complexity: O(1)
        Stable: No
        Best for: Large datasets where memory is limited
        """
        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and arr[left] > arr[largest]:
                largest = left

            if right < n and arr[right] > arr[largest]:
                largest = right

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        n = len(arr)
        # Build max heap
        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)

        # Extract elements from heap one by one
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            heapify(arr, i, 0)

        return arr

class SearchingAlgorithms:
    @staticmethod
    def linear_search(arr, target):
        """
        Linear Search - Tìm kiếm tuần tự
        Time Complexity: O(n)
        Space Complexity: O(1)
        Best for: Small arrays or unsorted arrays
        """
        for i, item in enumerate(arr):
            if item == target:
                return i
        return -1

    @staticmethod
    def binary_search(arr, target):
        """
        Binary Search - Tìm kiếm nhị phân
        Time Complexity: O(log n)
        Space Complexity: O(1)
        Best for: Sorted arrays
        """
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    @staticmethod
    def jump_search(arr, target):
        """
        Jump Search - Tìm kiếm nhảy
        Time Complexity: O(√n)
        Space Complexity: O(1)
        Best for: Sorted arrays where jumping ahead is beneficial
        """
        n = len(arr)
        step = int(n ** 0.5)
        
        prev = 0
        while arr[min(step, n) - 1] < target:
            prev = step
            step += int(n ** 0.5)
            if prev >= n:
                return -1

        while arr[prev] < target:
            prev += 1
            if prev == min(step, n):
                return -1

        if arr[prev] == target:
            return prev

        return -1

class UtilityAlgorithms:
    @staticmethod
    def find_max_min(arr):
        """
        Tìm giá trị lớn nhất và nhỏ nhất
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not arr:
            return None, None

        max_val = min_val = arr[0]
        for num in arr[1:]:
            if num > max_val:
                max_val = num
            if num < min_val:
                min_val = num

        return max_val, min_val

    @staticmethod
    def find_kth_largest(arr, k):
        """
        Tìm phần tử lớn thứ k
        Time Complexity: O(n) average case
        Space Complexity: O(1)
        """
        def quickselect(arr, k):
            if not arr:
                return None

            pivot = arr[len(arr) // 2]
            left = [x for x in arr if x < pivot]
            equal = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]

            if k <= len(right):
                return quickselect(right, k)
            elif k <= len(right) + len(equal):
                return pivot
            else:
                return quickselect(left, k - len(right) - len(equal))

        if k < 1 or k > len(arr):
            return None
        return quickselect(arr, k)

    @staticmethod
    def count_frequency(arr):
        """
        Đếm tần suất xuất hiện của các phần tử
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        frequency = {}
        for item in arr:
            frequency[item] = frequency.get(item, 0) + 1
        return frequency

    @staticmethod
    def find_duplicates(arr):
        """
        Tìm các phần tử trùng lặp
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        seen = set()
        duplicates = set()
        for item in arr:
            if item in seen:
                duplicates.add(item)
            seen.add(item)
        return list(duplicates)

    @staticmethod
    def rotate_array(arr, k):
        """
        Xoay mảng k vị trí
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        def reverse(arr, start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        n = len(arr)
        k = k % n  # Normalize k
        
        reverse(arr, 0, n - 1)
        reverse(arr, 0, k - 1)
        reverse(arr, k, n - 1)
        return arr

    @staticmethod
    def find_missing_number(arr):
        """
        Tìm số còn thiếu trong dãy từ 0 đến n
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        n = len(arr)
        expected_sum = (n * (n + 1)) // 2
        actual_sum = sum(arr)
        return expected_sum - actual_sum

# Ví dụ sử dụng
if __name__ == "__main__":
    # Test sorting algorithms
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", test_array)
    
    print("\nTesting Sorting Algorithms:")
    print("Bubble Sort:", SortingAlgorithms.bubble_sort(test_array.copy()))
    print("Selection Sort:", SortingAlgorithms.selection_sort(test_array.copy()))
    print("Insertion Sort:", SortingAlgorithms.insertion_sort(test_array.copy()))
    print("Merge Sort:", SortingAlgorithms.merge_sort(test_array.copy()))
    print("Quick Sort:", SortingAlgorithms.quick_sort(test_array.copy()))
    print("Heap Sort:", SortingAlgorithms.heap_sort(test_array.copy()))
    
    # Test searching algorithms
    sorted_array = sorted(test_array)
    target = 22
    print("\nTesting Searching Algorithms:")
    print(f"Linear Search for {target}:", SearchingAlgorithms.linear_search(sorted_array, target))
    print(f"Binary Search for {target}:", SearchingAlgorithms.binary_search(sorted_array, target))
    print(f"Jump Search for {target}:", SearchingAlgorithms.jump_search(sorted_array, target))
    
    # Test utility algorithms
    print("\nTesting Utility Algorithms:")
    max_val, min_val = UtilityAlgorithms.find_max_min(test_array)
    print("Max and Min values:", max_val, min_val)
    print("3rd largest element:", UtilityAlgorithms.find_kth_largest(test_array, 3))
    
    test_array_with_duplicates = [1, 3, 1, 4, 5, 3, 2, 4]
    print("Frequency count:", UtilityAlgorithms.count_frequency(test_array_with_duplicates))
    print("Duplicates:", UtilityAlgorithms.find_duplicates(test_array_with_duplicates))
    
    rotated = test_array.copy()
    print("Rotated array by 3 positions:", UtilityAlgorithms.rotate_array(rotated, 3))
    
    missing_array = [0, 1, 3, 4, 5]
    print("Missing number in sequence:", UtilityAlgorithms.find_missing_number(missing_array))
