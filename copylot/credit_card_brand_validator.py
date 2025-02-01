import re

def luhn_algorithm(card_number):
    total = 0
    reverse_digits = list(map(int, str(card_number)))[::-1]
    for i, digit in enumerate(reverse_digits):
        if i % 2 == 1:
            doubled = digit * 2
            if doubled > 9:
                total += doubled - 9
            else:
                total += doubled
        else:
            total += digit
    return total % 10 == 0

def validate_credit_card(card_number):
    card_number = str(card_number)
    
    if not luhn_algorithm(card_number):
        return {"valid": False, "brand": "Invalid"}
    
    card_patterns = {
        "Visa": r"^4\d{15}$",
        "Mastercard": r"^5[1-5]\d{14}$|^2(2[2-9]|[3-9][0-9])\d{12}$",
        "American Express": r"^3[47]\d{13}$",
        "Diners Club": r"^3[689]\d{12}$|^30[0-5]\d{11}$",
        "Discover": r"^6011\d{12}$|^6221[2-9]\d{10}$|^64[4-9]\d{13}$|^65\d{14}$",
        "EnRoute": r"^2014\d{11}$|^2149\d{11}$",
        "JCB": r"^352[8-9]\d{12}$|^35[3-8]\d{13}$",
        "Voyager": r"^8699\d{11}$",
        "HiperCard": r"^6062\d{12}$",
        "Aura": r"^50\d{14}$"
    }
    
    for brand, pattern in card_patterns.items():
        if re.match(pattern, card_number):
            return {"valid": True, "brand": brand}
    
    return {"valid": False, "brand": "Invalid"}


if __name__ == "__main__":

    list_of_examples = [
        {"mastercard": ["5581739554366756", "5104429416265358"]},
        {"visa": ["4716248461287346", "4716867643733446"]},
        {"american_express": ["348994365361125", "376773509352256"]},
        {"diners_club": ["36532945750990", "30288849848788"]},
        {"discover": ["6011763308136263", "6011328021935910"]},
        {"enroute": ["214926869286318", "201455367253914"]},
        {"jcb": ["3587378108470654", "3566448702546715"]},
        {"voyager": ["869948918402132", "869904758850419"]},
        {"hipercard": ["6062823562475589", "6062825074951338"]},
        {"aura":  ["5063934673404912", "5034953742755159"]},
        {"invalid": ["1111111111111111", "1063934673404912"]},
    ]

    for example in list_of_examples:
        for brand, cards in example.items():
            for card in cards:
                result = validate_credit_card(card)
                print(f"Brand: {result['brand']:<16} | Valid: {result['valid']:1} | Card: {card}")
