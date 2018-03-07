"""

John and his friend Jack both like to swim, but rarely at the same time. Every 
third day, Jack will swim in the pool alone. When Jack isn’t swimming, John 
will swim in the pool alone. However, every 50th day, both boys will swim in 
the same pool. Write some pseudocode that loops through 365 days, and outputs 
who is swimming on each day starting at day 1.



"""

def who_is_swimming(n):
    """function returns who is swimming on the nth day, given these rules:
           * Jacks swims every third day
           * John swims on days when Jack does not
           * Every 50th day, both John and Jack swim"""
    answer = []
    if n % 3 == 0 or n % 50 == 0:
        answer.append("jack")
    if n % 3 != 0:
        answer.append("john")
    return answer

def swimming_report():
    print("Day", "Who is Swimming?")
    for day in range(1, 365+1):
        print(day, ": ", who_is_swimming(day)) 

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    swimming_report()

