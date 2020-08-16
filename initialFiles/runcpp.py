import subprocess

print("Enter your number: ")
number = input()
print(" ")

string = "./printhello.exe " + number + " hello"

subprocess.Popen(string)