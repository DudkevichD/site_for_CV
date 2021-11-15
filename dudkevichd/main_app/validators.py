from django.core.exceptions import ValidationError


def my_validator(self):
    limit = 1024 * 1024 * 10
    if self.size > limit:
        raise ValidationError('Файл свыше 10MB недопустим')
    self = str(self)
    if self.split('.')[-1] not in ['pdf', 'jpg']:
        raise ValidationError(r'Файл не формата "pdf" или "jpg"')
