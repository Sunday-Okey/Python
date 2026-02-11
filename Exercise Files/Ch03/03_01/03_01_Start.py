# Command Line Arguments
import sys
import tempfile
# Print Arguments
# print("Number of arguments:", len(sys.argv), 'arguments')
# print("Arguments ", sys.argv)
# # Remove Arguments
# sys.argv.remove(sys.argv[0])
# print("Arguments ", sys.argv)
# # Sum up the Arguments
# arguments = sys.argv
# sum_ = 0
# for arg in arguments:
#     try:
#         num = int(arg)
#     except Exception:
#         print("Bad input")
#     sum_ += num
# print(sum_)

# myfile = open("scores.txt", "w")
# print(myfile.name)
# print(myfile.mode)
# myfile.write("GBJ: 100\nKHD : 99\nBBB : 89")

# myfile = open("scores.txt")
# for line in myfile:
#     print(line.strip())

tempfile = tempfile.TemporaryFile()
tempfile.write(b"Save this special number for me: 6787866")
tempfile.seek(0)

print(tempfile.read())
tempfile.close()