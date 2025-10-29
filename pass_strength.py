import zxcvbn

def analyze_password_strength(password):
    """Analyze password strength using zxcvbn"""
    strength = zxcvbn.zxcvbn(password)  # Get the strength score from zxcvbn
    score = strength['score']  # Score is from 0 to 4, where 4 is the strongest

    if score == 0:
        return "Very Weak"
    elif score == 1:
        return "Weak"
    elif score == 2:
        return "Fair"
    elif score == 3:
        return "Strong"
    else:
        return "Very Strong"

def generate_wordlist(name, date, pet):
    """Generate a list of password variations based on user input"""
    wordlist = []
    wordlist.append(name)
    wordlist.append(date)
    wordlist.append(pet)

    # Add common variations and patterns
    wordlist.append(name + '123')
    wordlist.append(name + date)
    wordlist.append(name + pet)
    wordlist.append(date + '2023')
    
    return wordlist
