import re

class Email:
    def __init__(self, mask_char="x"):
        self.mask_char = mask_char

    def mask(self, email):
        local, domain = email.split("@")
        masked_local = self.mask_char * len(local)
        return f"{masked_local}@{domain}"

class PhoneNumber:
    def __init__(self, mask_char="x", mask_length=3):
        self.mask_char = mask_char
        self.mask_length = mask_length

    def mask(self, phone_number):
        normalized_phone = " ".join(phone_number.split())
        visible_length = len(normalized_phone.replace(" ", "")) - self.mask_length
        visible_count = 0
        masked_phone = ""

        for ch in normalized_phone:
            if ch == " ":
                masked_phone += " "
            elif visible_count < visible_length:
                masked_phone += ch
                visible_count += 1
            else:
                masked_phone += self.mask_char
        return masked_phone
    
class Skype:
    def __init__(self, mask_char="x"):
        self.mask_char = mask_char

    def mask(self, skype_contact):
            return re.sub(r'(skype:)[^?]+', r'\1' + self.mask_char * 3, skype_contact)