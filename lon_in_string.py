# Compare two numeric strings
def isGreater(a, b):

    if len(a) > len(b):
        return True
    if len(a) < len(b):
        return False

    return a > b


def maxOdd(s):

    ans = ""
    n = len(s)

    for i in range(n):
        for j in range(i, n):

            sub = s[i:j+1]

            # check if last digit is odd
            last = sub[-1]

            if int(last) % 2 != 0:

                # update answer if current substring is larger
                if ans == "" or isGreater(sub, ans):
                    ans = sub

    return ans


if __name__ == "__main__":

    s = "504"

    print(maxOdd(s))