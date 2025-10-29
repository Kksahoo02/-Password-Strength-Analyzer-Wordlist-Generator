import argparse
from pass_strength import analyze_password_strength, generate_wordlist

def main():
    # Set up argparse for command-line arguments
    parser = argparse.ArgumentParser(description='Password Strength Analyzer and Wordlist Generator')
    parser.add_argument('password', help='Password to check strength')
    parser.add_argument('name', help='Your name')
    parser.add_argument('date', help='A memorable date')
    parser.add_argument('pet', help='Your pet\'s name')

    args = parser.parse_args()

    # Analyze password strength
    strength = analyze_password_strength(args.password)
    print(f"Password Strength: {strength}")

    # Generate custom wordlist
    wordlist = generate_wordlist(args.name, args.date, args.pet)
    print("\nGenerated Wordlist:")
    for word in wordlist:
        print(word)

if __name__ == '__main__':
    main()
