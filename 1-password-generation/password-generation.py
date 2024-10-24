from argparse import ArgumentParser
import secrets
import random
import string

parser = ArgumentParser(
    prog="Password Generator",
    description="Tool to generate a random password",
)

parser.add_argument("-n", "--numbers", default=0, help="Include numbers", type=int)
parser.add_argument("-l", "--lowercase", default=0, help="Include lowercase letters", type=int)
parser.add_argument("-u", "--uppercase", default=0, help="Include uppercase letters", type=int)
parser.add_argument("-s", "--special-chars", default=0, help="Include special characters", type=int)
parser.add_argument("-t", "--total-length", type=int, help="Total length of the password")
parser.add_argument("-a", "--amount", default=1, type=int)
parser.add_argument("-o", "--output-file")

args = parser.parse_args()

passwords = []

for _ in range(args.amount):
    if args.total_length:
        passwords.append("".join([secrets.choice(string.digits + string.ascii_letters + string.punctuation) for _ in range(args.total_length)]))
    else:
        passwords = []

# Nếu / bao nhiêu số mà password cần chứa
for _ in range(args.numbers):
    passwords.append(secrets.choice(string.digits))

# Nếu / bao nhiêu chữ cái hoa mà password cần chứa
for _ in range(args.uppercase):
    passwords.append(secrets.choice(string.ascii_uppercase))

# Nếu / bao nhiêu chữ cái thường mà password cần chứa
for _ in range(args.lowercase):
    passwords.append(secrets.choice(string.ascii_lowercase))

# Nếu / bao nhiêu ký tự đặc biệt mà password cần chứa
for _ in range(args.special_chars):
    passwords.append(secrets.choice(string.punctuation))

# Dùng random.shuffle để [trộn] các ký tự trong mảng password
random.shuffle(passwords)

# Lưu passwords[] vào file .txt
if args.output_file:
    with open(args.output_file, "w") as f:
        for password in passwords:
            f.write(password + "\n")

# In ra các password
print("\n".join(passwords))