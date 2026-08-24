import pytest
from main import validar_email, validar_formulario, validar_password


def test_validar_email():
    assert validar_email("usuario@test.com") is True
    assert validar_email("correo_invalido") is False


def test_validar_password():
    assert validar_password("ClaveSegura123") is True
    assert validar_password("corta") is False
    assert validar_password("sinnumeroABC") is False
    assert validar_password("sinmayuscula123") is False


def test_validar_formulario_exitoso():
    res = validar_formulario(
        {
            "email": "test@test.com",
            "password": "Password123",
            "dni": "12345678",
        }
    )
    assert res["valido"] is True


def test_validar_formulario_con_errores():
    res = validar_formulario({"password": "123", "dni": "abc"})
    assert res["valido"] is False
    assert len(res["errores"]) == 3