sieve =[True]*101
for i in range(2,100):
    if sieve[i]:
        print(i)
        for j in range(i*i,100,i):
            sieve[j] = False
            
#Sieve of Eratosthenes
#埃拉托斯特尼筛法,简称埃氏筛或爱氏筛
#是一种由希腊数学家埃拉托斯特尼所提出的一种简单检定素数的算法
#要得到自然数n以内的全部素数,必须把不大于根号n的所有素数的倍数剔除,剩下的就是素数