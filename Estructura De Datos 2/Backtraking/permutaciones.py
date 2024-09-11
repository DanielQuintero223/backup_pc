nums = [1,2,3,4]
visited = [False]*len(nums)

def permutations(nums, visited, path):
    if len(path) == len(nums):
        print(path)
        return
    for i in range(len(nums)):
        if not visited[i]:
            visited[i] = True
            path.append(nums[i])
            permutations(nums, visited, path)
            path.pop()
            visited[i] = False

permutations(nums, visited, [])
