from story import DataBundle

#TEST 1 SHARING 200MBS

bundle = DataBundle(500)
result = bundle.add_data(200)
print("Expected result: True")
print("Actual result:", result)
print("Expected remaining data: 700 MB")
print("Actual remaining data:", bundle.remaining, "MB")

#TEST 2: sharing 0 MB

bundle = DataBundle(500)
result = bundle.add_data(0)
print("Expected result: False")
print("Actual result:", result)
print("Expected remaining data: 500 MB")
print("Actual remaining data:", bundle.remaining, "MB")

#TEST 3: sharing negative data

bundle = DataBundle(500)
result = bundle.add_data(-100)
print("Expected result: False")
print("Actual result:", result)
print("Expected remaining data: 500 MB")
print("Actual remaining data:", bundle.remaining, "MB")