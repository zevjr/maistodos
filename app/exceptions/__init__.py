"""
# Modulo de Excessões
Item usado para disponibilizar as excessões personalizadas da aplicação.
"""

from .crud_error import (  # isort:skip
    CRUDCreateError,  # isort:skip
    CRUDDeleteError,  # isort:skip
    CRUDSelectError,  # isort:skip
    CRUDUpdateError,  # isort:skip
)  # isort:skip
from .http_error_schema import HTTPError

__all__ = [
    "CRUDCreateError",
    "CRUDUpdateError",
    "CRUDDeleteError",
    "CRUDSelectError",
    "HTTPError",
]
