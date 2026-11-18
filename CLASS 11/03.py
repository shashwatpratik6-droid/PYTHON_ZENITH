n = int(input())
steps = 0

while n >= 10:
  old_n = n
  digit_sum = 0
  i = n

  while i > 0:
    digit_sum += i % 10
    i //= 10

  print(f"{old_n} -> {digit_sum}")
  n = digit_sum
  steps += 1

print(f"Single digit: {n}")
print(f"Steps: {steps}")