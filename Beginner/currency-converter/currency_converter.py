rates = {
    "USD": {"EUR": 0.85, "GBP": 0.73, "JPY": 110.0, "CAD": 1.25, "AUD": 1.35},
    "EUR": {"USD": 1.18, "GBP": 0.86, "JPY": 129.0, "CAD": 1.47, "AUD": 1.59},
    "GBP": {"USD": 1.37, "EUR": 1.16, "JPY": 150.0, "CAD": 1.71, "AUD": 1.85},
    "JPY": {"USD": 0.0091, "EUR": 0.0078, "GBP": 0.0067, "CAD": 0.0114, "AUD": 0.0123},
    "CAD": {"USD": 0.80, "EUR": 0.68, "GBP": 0.58, "JPY": 88.0, "AUD": 1.08},
    "AUD": {"USD": 0.74, "EUR": 0.63, "GBP": 0.54, "JPY": 81.0, "CAD": 0.93},
}
names = {
    "USD": "US Dollar",
    "EUR": "Euro",
    "GBP": "British Pound",
    "JPY": "Japanese Yen",
    "CAD": "Canadian Dollar",
    "AUD": "Australian Dollar",
}


# Näita saadaolevaid valuutasid ja nende nimesid
def show_currencies():
    print("\nAvailable currencies:")
    for code, name in names.items():
        print(f"  {code} - {name}")


# küsi kasutajalt kehtivat valuutakoodi
def get_currency(prompt):
    while True:
        currency_code = input(prompt).upper().strip()
        if currency_code in rates:
            return currency_code
        print("Invalid currency. Try again.")


# Küsi kasutajalt kehtivat summat
def get_amount():
    while True:
        try:
            a = float(input("Enter amount: "))
            if a >= 0:
                return a
            print("Amount cannot be negative.")
        except ValueError:
            print("Invalid number.")


# ühe valuuta teisendamine teise valuutasse
def convert(amount, from_c, to_c):
    if from_c == to_c:
        return amount
    return amount * rates[from_c].get(to_c, 0)


# Põhifunktsioon, mis käivitab valuutavahetuse
def main():
    print("Welcome to Currency Converter!")
    while True:
        show_currencies()
        from_c = get_currency("From currency: ")
        to_c = get_currency("To currency: ")
        amount = get_amount()
        result = convert(amount, from_c, to_c)
        if result:
            print(f"{amount:.2f} {from_c} = {result:.2f} {to_c}")
        else:
            print("Conversion not available.")
        if input("Convert another? (y/n): ").lower() not in ["y", "yes"]:
            break
    print("Thank you for using Currency Converter!")


# Käivita programm otse
if __name__ == "__main__":
    main()
