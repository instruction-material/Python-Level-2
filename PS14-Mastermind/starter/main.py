sample_signal = "2032"
sample_trial = "2230"
exact = 0

for signal_digit, trial_digit in zip(sample_signal, sample_trial):
    if signal_digit == trial_digit:
        exact += 1
print(f"Exact: {exact}")

# Count misplaced digits after removing the already-matched positions.
