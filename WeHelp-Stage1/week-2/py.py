from unittest import result


class Q1:
    print("\nQ1.")
    def calculate(min, max, step):
    # 請用你的程式補完這個函式的區塊
        total=0
        for i in range(min, max+1, step): #第三格表示每次迴圈遞加的值
            if i<=max+1:
                total=total+i
        print("印出 "+str(total))
    calculate(1, 3, 1) # 你的程式要能夠計算 1+2+3，最後印出 6 
    calculate(4, 8, 2) # 你的程式要能夠計算 4+6+8，最後印出 18 
    calculate(-1, 2, 2) # 你的程式要能夠計算 -1+1，最後印出 0

class Q2:
    print("\nQ2.")
    def avg(data):
        # 請用你的程式補完這個函式的區塊
        nums=0
        sum=0
        length=len(data["employees"])
        for i in range(0, length, 1) :
            employees = data["employees"][i]
            if employees["manager"] == False:
                nums=nums+1
                sum = sum + (employees["salary"])
        print("非 manager 的員工平均薪資"+str(sum / nums))
        # print(sum / nums)
    avg({
        "employees":[ 
            {
                "name":"John", 
                "salary":30000, 
                "manager":False
            }, 
            {
                 "name":"Bob", 
                 "salary":60000, 
                 "manager":True
            }, 
            {
                 "name":"Jenny", 
                 "salary":50000, 
                 "manager":False
            }, 
            {
                "name":"Tony", 
                "salary":40000, 
                "manager":False
            } 
        ]
    }) # 呼叫 avg 函式

class Q3:
    print("\nQ3.")
    def func(a):
        # 請用你的程式補完這個函式的區塊
        def func(b,c):
            result=a+b*c
            print("印出"+str(a)+"+("+str(b)+"*"+str(c)+")的結果 "+str(result))
        return func    
    func(2)(3, 4) # 你補完的函式能印出 2+(3*4) 的結果 14 
    func(5)(1, -5) # 你補完的函式能印出 5+(1*-5) 的結果 0 
    func(-3)(2, 9) # 你補完的函式能印出 -3+(2*9) 的結果 15 
    # 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果       
       
class Q4:
    print("\nQ4.")
    def maxProduct(nums):
        # 請用你的程式補完這個函式的區塊 
        Array = []
        length = len(nums)
        for i in range(0, length):
            for j in range(i+1, length):
                result = nums[i]*nums[j]
                Array.append(result) #將相乘結果丟進Array       
        max_value = max(Array)
        print(max_value)         
    maxProduct([5, 20, 2, 6]) # 得到 120 
    maxProduct([10, -20, 0, 3]) # 得到 30 
    maxProduct([10, -20, 0, -3]) # 得到 60 
    maxProduct([-1, 2]) # 得到 -2 
    maxProduct([-1, 0, 2]) # 得到 0 
    maxProduct([5,-1, -2, 0]) # 得到 2 
    maxProduct([-5, -2]) # 得到 10        

class Q5:
    print("\nQ5.")    
    def twoSum(nums, target):
        # your code here
        length = len(nums)
        for i in range(0, length):
            for j in range(i+1, length):
                sum = nums[i]+nums[j]
                if sum == target:
                    print("because nums[" + str(i) + "]+nums[" + str(j) + "] is " + str(target) + ".")
                    return [i, j]
    result=twoSum([2, 11, 7, 15], 9)
    print(result) # show [0, 2] because nums[0]+nums[2] is 9

class Q6:
    print("\nQ6.")
    def maxZeros(nums):
        # 請用你的程式補完這個函式的區塊 
        max_value = 0
        Array = [0]
        length = len(nums)
        for i in range(0, length):
            if nums[i] == 0:
                max_value = max_value+1
                Array.append(max_value) #將連續長度丟進Array
            else:
                max_value = 0
                continue
        result = max(Array)
        print(result)     
    maxZeros([0, 1, 0, 0]) # 得到 2
    maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4 
    maxZeros([1, 1, 1, 1, 1]) # 得到 0 
    maxZeros([0, 0, 0, 1, 1]) # 得到 3    