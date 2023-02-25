def skillCombo(dailySkillSet):
    # Write your code here
    def isprime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    dailySkillSet.pop(0)

    ans = []
    for i in dailySkillSet:  # for each day
        set1 = set()
        for j in range(1, i + 1):  # for each number
            if isprime(j):
                set1.add(j)
        if len(set1) < 2:
            ans.append(0)
        else:
            count = 0
            for k in set1:
                for l in set1:
                    if isprime(k + l) and k + l <= i:
                        count += 1
            ans.append(int(count / 2))
    print(ans)

skillCombo([4,2,5,6,15])