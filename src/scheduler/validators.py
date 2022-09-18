from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_no_space(value):
    if ' ' in value.strip():
        raise ValidationError(
            _('%(value)s contains a space.'),
            params={'value': value},
        )
