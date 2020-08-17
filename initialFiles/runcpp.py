import subprocess

print("Enter your number: ")
number = input()
print(" ")

print("Enter your word: ")
word = input()
print(" ")

string = "./printhello.exe " + number + " " + word

subprocess.Popen(string)