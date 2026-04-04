model = "claude-sonnet-4-20250514"
model2 ="gpt-6"
model3= "gemini-2.5-flash"

print(model.upper())
print(model2.upper())   
print(model3.upper())

print("-----------------")
print(model.lower())
print(model2.lower())
print(model3.lower())

print("-----------------")
print(type(model))
print(type(model2))
print(type(model3))
print("-----------------")

task= "Summarize bug report"


prompt1 = f"Tou are {model2}. your task is to {task}"
print(prompt1)

