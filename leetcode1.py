def substring(candidates,target):
    def backtrack(start, target, path):
        for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, target - candidates[i], path)
                path.pop()
    result = []
    backtrack(0, target, [])
    return result
candidates=[10,1,2,7,6,1,5]
target=8
print(substring(candidates,target))

