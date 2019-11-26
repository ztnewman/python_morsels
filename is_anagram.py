from unicodedata import normalize
def is_anagram(a,b):
    alpha_a = normalize('NFC',''.join(filter(str.isalpha, a)))
    alpha_b = normalize('NFC',''.join(filter(str.isalpha, b)))
    sort_a = ''.join(sorted(alpha_a.lower().replace(" ", "")))
    sort_b = ''.join(sorted(alpha_b.lower().replace(" ", "")))
    if sort_a == sort_b:
        return True
    else:
        return False


is_anagram("tea", "eat")
is_anagram("tea", "treat")
is_anagram("sinks", "skin")
print(is_anagram("Listen", "silent"))

print(normalize('NFD',''.join(filter(str.isalpha, "cardiografía"))))
print(normalize('NFD',''.join(filter(str.isalpha, "radiográfica"))))

print(is_anagram("cardiografía", "radiográfica"))
