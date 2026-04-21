# Mini Project: Password Strength Checker

passwords = ["Data123", "hello", "Admin@2023", "pass#", "PyTh0n !", "12345678"]

def is_strong(pwd):
    special = "!@#$%^&*"
    return (
        len(pwd) >= 8
        and any(c.isupper() for c in pwd)
        and any(c.isdigit() for c in pwd)
        and any(c in special for c in pwd)
    )

for pwd in passwords:
    if is_strong(pwd):
        print(f"{pwd}: ✅ Strong")
    else:
        print(f"{pwd}: ❌ Weak")
