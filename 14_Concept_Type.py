def calculator(passed, total):
    return (passed / total) * 100

result = calculator(80, 100)
print(f"The result is {result}")
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX")

#strict type

def calculator(passed: int, total: int) -> float:
    return(passed/total)*100

result2 = calculator(77.5,100)
print(f"The result is {result2}")
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX")

def evaluate_test(
    test_name: str, 
    score: float, 
    threshold: float, 
    passed: bool) -> dict:
    return {
        "test_name": test_name,
        "score": score,
        "threshold": threshold,
        "passed": passed
    }

result3 = evaluate_test("Test 1", 80, 70, True)
print(result3)