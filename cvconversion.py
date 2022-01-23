import random 
cvrs = []
# Run the test 10,000 times.
for i in range(100):
    # Simulate 1,000 sessions.
    conversions = 0
    nonconversions = 0
    for j in range(1000):
         # Get a random number between 0 and 1 
         # and check if it's above 5% (0.05).
        if random.random() > 0.05:
             # Count the conversion.
             conversions += 1
            # print("Converted:",conversions)
        else:
            nonconversions += 1
           # print("Not converted",nonconversions)

    # Calculate our CVR.
    cvr = conversions / 1000
    # Store the CVR for later.
    cvrs += [cvr]
print(cvrs)