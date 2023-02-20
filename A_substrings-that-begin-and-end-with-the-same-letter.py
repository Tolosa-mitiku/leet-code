def take_input():
    given_string = input()
    return  given_string

def count_substrings( input_string ):
    # Interviewee’s code
    count = {}
    ans = len(s)
    for char in s:
        if char not in count:
            count[char] = 1   
        else:
            ans += count[char]
            count[char] = count[char] + 1
        
    return ans

if __name__ == "__main__":
    tests = int(input())
    for _ in range(tests):
        input_string = take_input()
        answer = count_substrings(input_string)
        print(answer)    