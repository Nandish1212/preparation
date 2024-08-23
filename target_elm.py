#Find the targeted element in an array!
def targeted_num(arr,target):
    if target in arr:
        return f'The targeted element {target} found at {arr.index(target)}!'
    return f'The targeted element {target} not found!'
    
arr=[2,3,4,10,40]
target=40
print(targeted_num(arr,target))