def generateParenthesis(n):
    result = []
    def generate(s, open_count, close_count):
        if len(s) == 2 * n:
            result.append(s)
            return
        if open_count < n:
            generate(s + '(', open_count + 1, close_count)
        if close_count < open_count:
            generate(s + ')', open_count, close_count + 1)
    generate('', 0, 0)
    return result
n = int(input("Enter a number: "))
print("Output for Test Case 1:", generateParenthesis(n))