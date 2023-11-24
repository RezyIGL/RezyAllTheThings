public class Solution {
    public int EvalRPN(string[] tokens)
    {
        Stack<int> intTokens = new Stack<int>();

        foreach (var token in tokens)
        {
            if (Int32.TryParse(token, out int intToken))
            {
                intTokens.Push(intToken);
            }
            else
            {
                int temp = 0;
                int rhs = intTokens.Pop();
                int lhs = intTokens.Pop();
                
                if (token == "*") temp = lhs * rhs;
                else if (token == "/") temp = lhs / rhs;
                else if (token == "+") temp = lhs + rhs;
                else if (token == "-") temp = lhs - rhs;
                
                intTokens.Push(temp);
            }
        }
        
        return intTokens.Pop();
    }
}