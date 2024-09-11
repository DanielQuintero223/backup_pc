def sum_subconjuntos(nums, objetive):
    find_subconjuntos_sum([],nums,objetive,0)

def find_subconjuntos_sum(subconjunto,nums,objetive, indice):
    # caso base
    if objetive == 0:
        print(subconjunto)
        return
    if indice >= len(nums) or objetive < 0:
        return
    
    find_subconjuntos_sum(subconjunto+[nums[indice]],nums,objetive - nums[indice], indice + 1)
    find_subconjuntos_sum(subconjunto,nums,objetive, indice + 1)

nums = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

sum_subconjuntos(nums, 7)