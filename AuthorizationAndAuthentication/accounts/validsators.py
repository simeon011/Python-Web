from django.core.exceptions import ValidationError


class PassValidator:
    def validator(self, password, user=None):
        if len(set(password)) <= 6:
            raise ValidationError("Password must be between 6 and 20 characters")

    def get_help_text(self):
        return "Your password should at least contain 6 unique"
