def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        substring = string[i:i + k]
        result = ""
        seen = set()

        for ch in substring:
            if ch not in seen:
                result += ch
                seen.add(ch)

        print(result)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)