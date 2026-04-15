def greet(name):
    print(f"Hello, {name}!")

greet("Syeda")
greet("Aaira")
greet("Fatima")

print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX")

def call_greet():
    print(f"Hi")

call_greet()

print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX")

def run_test(testName, expected, actual):

    if(expected == actual):
        print(f"{testName} PASSED")
    else:
        print(f"{testName} FAILED")

run_test("Test 1", "pass", "pass")
run_test("Test 2", 20, 20)
run_test("Test 3", 30, 40)
run_test("Test 4", "fail", "fail")
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX")

def call_llm(prompt, model="gpt4", temperature=0.7, max_token=10):
    print(f"Calling {model} with prompt: {prompt}")
    print(f"Temperature: {temperature}")
    print(f"Max Token: {max_token}")
    return "Response from {model}"
print("---------------------------")
response = call_llm("Hello, how are you?")
print("this is response "+response)
print("---------------------------")
print(call_llm("Hello, how are you?"))
print(call_llm("Hello, how are you?", model="gpt-4.1"))
print(call_llm("Hello, how are you?", model="gpt-4.1", temperature=0.5))
print(call_llm("Hello, how are you?", model="gpt-4.1", temperature=0.5, max_token=100))
    