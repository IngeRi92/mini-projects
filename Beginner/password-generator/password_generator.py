import secrets
import string

def generate_password(length=12, use_numbers=True, use_special_chars=True):
    """Genereerib tugeva juhusliku parooli."""
    characters = string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    
    return ''.join(secrets.choice(characters) for _ in range(length))

if __name__ == "__main__":
    print("Turvaline parool:", generate_password())
    print("Lihtsam parool (ilma erimärkideta):", generate_password(use_special_chars=False))