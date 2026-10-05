import pytest

from estacionamiento import Estacionamiento


@pytest.fixture
def sistema():
    """Preparación reutilizable para las pruebas."""
    return Estacionamiento()

#Casos normales:

def test_1(sistema):
    # Arrange
    minutos = 7
    # Act
    resultado = sistema.calcular_total(minutos, "normal", False)
    # Assert
    assert resultado == 0.0

def test_2(sistema):
    # Arrange
    minutos = 71
    # Act
    resultado = sistema.calcular_total(minutos, "normal", False)
    # Assert
    assert resultado == 35.0

def test_3(sistema):
    # Arrange
    minutos = 23
    # Act
    resultado = sistema.calcular_total(minutos, "normal", False)
    # Assert
    assert resultado == 20.0


#Casos frontera:

def test_4(sistema):
    # Arrange
    minutos = 0
    # Act
    resultado = sistema.calcular_total(minutos, "normal", False)
    # Assert
    assert resultado == 0.0

def test_5(sistema):
    # Arrange
    minutos = 15
    # Act
    resultado = sistema.calcular_total(minutos, "normal", False)
    # Assert
    assert resultado == 0.0

def test_6(sistema):
    # Arrange
    minutos = 16
    # Act
    resultado = sistema.calcular_total(minutos, "normal", False)
    # Assert
    assert resultado == 20.0

def test_7(sistema):
    # Arrange
    minutos = 60
    # Act
    resultado = sistema.calcular_total(minutos, "normal", False)
    # Assert
    assert resultado == 20.0

def test_8(sistema):
    # Arrange
    minutos = 61
    # Act
    resultado = sistema.calcular_total(minutos, "normal", False)
    # Assert
    assert resultado == 35.0

def test_9(sistema):
    # Arrange
    minutos = 121
    # Act
    resultado = sistema.calcular_total(minutos, "normal", False)
    # Assert
    assert resultado == 50.0


# Entradas inválidas:

def test_10(sistema):
    # Arrange
    minutos = -3
    # Act y assert
    with pytest.raises(ValueError):
        sistema.calcular_total(minutos, "normal", False)

def test_11(sistema):
    # Arrange
    minutos = 47
    # Act y assert
    with pytest.raises(ValueError):
        sistema.calcular_total(minutos, "Batman", False)


#Interacción entre reglas:

def test_12(sistema):
    # Arrange
    minutos = 43
    # Act
    resultado = sistema.calcular_total(minutos, "frecuente", False)
    # Assert
    assert resultado == 18.0

def test_13(sistema):
    # Arrange
    minutos = 79
    # Act
    resultado = sistema.calcular_total(minutos, "frecuente", True)
    # Assert
    assert resultado == 300.0


#Decimales:

def test_14(sistema):
    # Arrange
    minutos = 97
    # Act
    resultado = sistema.calcular_total(minutos, "frecuente", False)
    # Assert
    assert resultado == 31.5

#Caso adicional:

def test_15(sistema):
    # Arrange
    minutos = 0
    # Act
    resultado = sistema.calcular_total(minutos, "normal", True)
    # Assert
    assert resultado == 300.0

# TODO:
# 1. Agregue casos normales.
# 2. Agregue casos frontera.
# 3. Agregue entradas inválidas con pytest.raises.
# 4. Agregue casos parametrizados con @pytest.mark.parametrize.
# 5. Use pytest.approx cuando el resultado esperado tenga decimales.
# 6. Pruebe interacciones entre reglas.
