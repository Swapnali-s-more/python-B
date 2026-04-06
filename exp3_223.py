import itertools
def is_tautology(expression):
    variables = sorted(list(set(c for c in expression if 'a' <= c <= 'z')))

    if not variables:
        return bool(eval(expression))

    results = []

    for assignment in [(True, False)]:
        try:
            result = True
            results.append(result)
        except Exception as e:
            print(e)
            return False   # ✅ inside function

    return all(results)   # ✅ inside function

if __name__ == "__main__":

    expr1 = "(p or not p)"
    print(f"Is '{expr1}' a tautology? {is_tautology(expr1)}")
 
    expr2 = "(p and not p)"
    print(f"Is '{expr2}' a tautology? {is_tautology(expr2)}")
 
    expr3 = "((p or q) and not p) <= q" # (P or Q) and not P implies Q
    print(f"Is '{expr3}' a tautology? {is_tautology(expr3)}")
       
    expr4 = "(not p or q) or (not q or p)"
    print(f"Is '{expr4}' a tautology? {is_tautology(expr4)}")