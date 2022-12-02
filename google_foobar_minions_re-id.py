# Re-ID
# =====

# There's some unrest in the minion ranks: minions with ID numbers like "1", "42", and other "good" numbers have been lording it over the poor minions who are stuck with more boring IDs. To quell the unrest, Commander Lambda has tasked you with reassigning everyone new, random IDs based on her Completely Foolproof Scheme.

# She's concatenated the prime numbers in a single long string: "2357111317192329...". Now every minion must draw a number from a hat. That number is the starting index in that string of primes, and the minion's new ID number will be the next five digits in the string. So if a minion draws "3", their ID number will be "71113".

# Help the Commander assign these IDs by writing a function solution(n) which takes in the starting index n of Lambda's string of all primes, and returns the next five digits in the string. Commander Lambda has a lot of minions, so the value of n will always be between 0 and 10000.

def solution(n):
    new_id = ''
    for i in range(1, 20200):
        if i > 1:
            x = 0
            primes = 2
            while primes < i and x == 0:
                if i % primes == 0:
                    x += 1
                primes += 1
            if x == 0:
                new_id += str(i)
    return new_id[n:n+5]


print(solution(10000))