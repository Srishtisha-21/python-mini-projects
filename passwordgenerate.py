import random
import string
import argparse
import math

def generate_password(length=12, use_digits=True, use_symbols=True):
    letters = string.ascii_letters
    digits = string.digits if use_digits else ""
    symbols = string.punctuation if use_symbols else ""

    chars = letters + digits + symbols

    if not chars:
        raise ValueError("No character sets selected!")

    return ''.join(random.choice(chars) for _ in range(length))


def calculate_entropy(password: str) -> float:
    """Calculate bits of entropy using character set size."""
    charset_size = 0

    if any(c.islower() for c in password):
        charset_size += 26
    if any(c.isupper() for c in password):
        charset_size += 26
    if any(c.isdigit() for c in password):
        charset_size += 10
    if any(c in string.punctuation for c in password):
        charset_size += len(string.punctuation)

    # Entropy formula: log2(character_set^password_length)
    return len(password) * math.log2(charset_size)


def check_strength(password: str) -> str:
    length = len(password)
    entropy = calculate_entropy(password)

    # Determine strength
    if length < 8 or entropy < 35:
        rating = "Weak"
    elif length < 12 or entropy < 50:
        rating = "Medium"
    elif length < 16 or entropy < 70:
        rating = "Strong"
    else:
        rating = "Very Strong"

    return rating, entropy


def main():
    parser = argparse.ArgumentParser(description="Password Generator with Strength Checker")

    parser.add_argument("-l", "--length", type=int, default=12,
                        help="Length of the password (default: 12)")
    parser.add_argument("--no-digits", action="store_true",
                        help="Exclude digits from password")
    parser.add_argument("--no-symbols", action="store_true",
                        help="Exclude special characters")

    parser.add_argument("--check", type=str,
                        help="Check strength of a custom password")

    args = parser.parse_args()

    if args.check:
        password = args.check
        print(f"\nPassword: {password}")
    else:
        password = generate_password(
            length=args.length,
            use_digits=not args.no_digits,
            use_symbols=not args.no_symbols
        )
        print(f"\nGenerated Password: {password}")

    strength, entropy = check_strength(password)
    print(f"Strength: {strength}")
    print(f"Entropy: {entropy:.2f} bits\n")


if __name__ == "__main__":
    main()
