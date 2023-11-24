public class Solution {
    public bool IsValid(string s) {
        Stack<char> stack = new Stack<char>();

        foreach (var c in s)
        {
            if (c == '(' || c == '[' || c == '{')
            {
                stack.Push(c);
            }

            else
            {
                if (!stack.Any() ||
                    c == ')' && stack.Peek() != '(' ||
                    c == ']' && stack.Peek() != '[' ||
                    c == '}' && stack.Peek() != '{')
                {
                    return false;
                }

                stack.Pop();
            }
        }
        
        return !stack.Any();
    }
}