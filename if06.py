def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    n1 = n%10
    a = n//10
    n2 = a%10
    b=a//10
    n3=b%10
    c=b//10
    n4=c%10
    n5 = c//10
    
    if n1>n2 and n1>n3 and n1>n4 and n1>n5:
        return 1
    if n2>n1 and n2>n3 and n2>n4 and n2>n5:
        return 2
    if n3>n1 and n3>n2 and n3>n4 and n3>n5:
        return 3
    if n4>n1 and n4>n2 and n4>n3 and n4>n5:
        return 4
    if n5>n1 and n5>n2 and n5>n3 and n5>n4:
        return 5
print(main(14289))
    