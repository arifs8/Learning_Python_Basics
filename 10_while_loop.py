#while loop

from email import charset
retries = 0;
max_retries =3;

while retries < max_retries:
    print(f"Retry {retries + 1}...")
    retries += 1

print("Done")

print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX")


score = [80, 90, 70, 60, 50]

new_score = []

while score:
    current_score = score.pop()
    if current_score >= 70:
        new_score.append(current_score)

print(new_score)
