# def fibo(n):
#     fibo_list = [0, 1]
#
#     if n <= 2:
#         return fibo_list[:n]
#
#     for i in range(2, n):
#         next_number = fibo_list[i - 1] + fibo_list[i - 2]
#         fibo_list.append(next_number)
#
#     return fibo_list
#
# fib_sequence = fibo(3)
# print(fib_sequence)
#
#
# def divide_array(nums, divider):
#     divide_nums = []
#     for i in range(divider,len(nums)):
#         if nums[i] % divider == 0:
#             divide_nums.append(nums[i-divider+1:i+1])
#     return divide_nums
#
# print(divide_array([0,1,2,3,4,5,6,7,8,9,10,11,12], 4))


# def maxProfit(prices):
#     if len(prices) <= 1:
#         return 0
#
#     good_to_buy = []
#     good_to_sell = []
#
#     for i in range(len(prices)-1):
#
#         if prices[i] < prices[i + 1]:
#             good_to_buy.append(prices[i])
#         elif prices[i] > prices[i + 1]:
#             if prices[i] != prices[0]:
#                 good_to_sell.append(prices[i])
#
#     if len(good_to_buy) == 0 or len(good_to_sell) == 0:
#         return 0
#     return max(good_to_sell) - min(good_to_buy)
#
# print(maxProfit([7,6,4,3,1]))


# def factorial(num):
#     if num == 1 or num == 0:
#         return 1
#     else:
#         result = num * factorial(num-1)
#         return result
#
# print(factorial(3))

# def factorial(n):
#     calc = 1
#     for number in range(1,n+1):
#         calc *= number
#     return calc
# print(factorial(3))
#
# def fibo(n):
#     fibo_list = [0,1]
#     if n<=2:
#         return fibo_list[:n]
#
#     for i in range(2,n+1):
#         next =  fibo_list[i-1] + fibo_list[i-2]
#         fibo_list.append(next)
#     return fibo_list
#
# print(fibo(6))
#
def fibo_rec(n):
    if n<=1:
        return n

    return fibo_rec(n-1) + fibo_rec(n-2)


for i in range(1,6):
    print(fibo_rec(i))






# def reverse_list(l):
#     revers_l = []
#     i = len(l)-1
#     for somthing in l:
#         revers_l.append(l[i])
#         i -= 1
#     return revers_l
# print(reverse_list([1,2,3,4]))

def ret_max_val(l):
    max = 0
    for num in l:
        if num > max:
            max = num
    return max

print(ret_max_val([1,16,35,10]))