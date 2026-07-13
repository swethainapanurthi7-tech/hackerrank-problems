import re

def fun(s):
    pattern = r'^[A-Za-z0-9_-]+@[A-Za-z0-9]+\.[A-Za-z]{1,3}$'
    return bool(re.match(pattern, s))

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = [input().strip() for _ in range(n)]

    filtered_emails = filter_mail(emails)
    print(sorted(filtered_emails))
