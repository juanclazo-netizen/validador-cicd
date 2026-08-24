import re


def validar_email(email: str) -> bool:
    patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(patron, email))


def validar_password(password: str) -> bool:
    if len(password) < 8:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    return True


def validar_formulario(datos: dict) -> dict:
    errores = []

    email = datos.get("email", "")
    if not validar_email(email):
        errores.append("Email inválido")

    password = datos.get("password", "")
    if not validar_password(password):
        errores.append("Password no cumple los requisitos mínimos")

    dni = datos.get("dni", "")
    if not (isinstance(dni, str) and len(dni) == 8 and dni.isdigit()):
        errores.append("DNI debe tener exactamente 8 dígitos numéricos")

    return {"valido": len(errores) == 0, "errores": errores}