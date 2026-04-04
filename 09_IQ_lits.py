test_result2 = ["pass", "fail", "pass", "fail", "pass"]

fail_count = 0

for test in test_result2:
    if test == "fail":
        fail_count += 1

print(fail_count)

print(f"fail_count: {fail_count} out of {len(test_result2)}")


print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX")

models = ["gpt-4.1", "gpt-4o", "gpt-4.1-mini", "gpt-4o-mini"]

for index , model in enumerate (models):
    print(f" Model {index + 1}: {model}")