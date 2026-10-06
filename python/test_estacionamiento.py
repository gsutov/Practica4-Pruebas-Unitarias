import pytest

from estacionamiento import Estacionamiento


@pytest.fixture
def sistema():
    """Preparación reutilizable para las pruebas."""
    return Estacionamiento()


#Casos normales:

def test_7_minutos_gratis(sistema):
    #Caso 1
    #R5: de 1 a 15 minutos es gratis
    # Arrange
    minutos = 7
    # Act
    resultado = sistema.calcular_total(minutos, "normal", False)
    # Assert
    assert resultado == 0.0

def test_71_minutos_35(sistema):
    #Caso 2
    #R7: $20 por la primera hora y $15 por cada hora adicional iniciadas
    # Arrange
    minutos = 71
    # Act
    resultado = sistema.calcular_total(minutos, "normal", False)
    # Assert
    assert resultado == 35.0

def test_23_minutos_20(sistema):
    #Caso 3
    #R6: de 16 a 60 minutos son $20
    # Arrange
    minutos = 23
    # Act
    resultado = sistema.calcular_total(minutos, "normal", False)
    # Assert
    assert resultado == 20.0


#Casos frontera:

def test_0_minutos_gratis(sistema):
    #Caso 4
    #R4: 0 minutos es gratis
    # Arrange
    minutos = 0
    # Act
    resultado = sistema.calcular_total(minutos, "normal", False)
    # Assert
    assert resultado == 0.0

def test_15_minutos_gratis(sistema):
    #Caso 5
    #R5: de 1 a 15 minutos es gratis
    # Arrange
    minutos = 15
    # Act
    resultado = sistema.calcular_total(minutos, "normal", False)
    # Assert
    assert resultado == 0.0

def test_16_minutos_costo_20(sistema):
    #Caso 6
    #R6: de 16 a 60 minutos son $20
    # Arrange
    minutos = 16
    # Act
    resultado = sistema.calcular_total(minutos, "normal", False)
    # Assert
    assert resultado == 20.0

def test_60_minutos_costo_20(sistema):
    #Caso 7
    #R6: de 16 a 60 minutos son $20
    # Arrange
    minutos = 60
    # Act
    resultado = sistema.calcular_total(minutos, "normal", False)
    # Assert
    assert resultado == 20.0

def test_61_minutos_costo_35(sistema):
    #Caso 8
    #R7: $20 por la primera hora y $15 por cada hora adicional iniciadas
    # Arrange
    minutos = 61
    # Act
    resultado = sistema.calcular_total(minutos, "normal", False)
    # Assert
    assert resultado == 35.0

def test_121_minutos_costo_50(sistema):
    #Caso 9
    #R7: $20 por la primera hora y $15 por cada hora adicional iniciadas
    # Arrange
    minutos = 121
    # Act
    resultado = sistema.calcular_total(minutos, "normal", False)
    # Assert
    assert resultado == 50.0


# Entradas inválidas:

def test_minutos_negativos(sistema):
    #Caso 10
    #R1 y R10: Los minutos deben serun entero mayor o igual a 0, si son negativos lanza un error
    # Arrange
    minutos = -3
    # Act y assert
    with pytest.raises(ValueError):
        sistema.calcular_total(minutos, "normal", False)

def test_tipo_usuario_invalido(sistema):
    #Caso 11
    #R11 y R2: El tipo de cliente debe ser "normal" o "frecuente", si es otro lanza un error
    # Arrange
    minutos = 47
    # Act y assert
    with pytest.raises(ValueError):
        sistema.calcular_total(minutos, "Batman", False)


#Interacción entre reglas:

def test_cliente_frecuente_costo_18(sistema):
    #Caso 12
    #R8: Los clientes frecuentes tienen un 10% de descuento sobre el total a pagar
    #R7: $20 por la primera hora y $15 por cada hora adicional
    # Arrange
    minutos = 43
    # Act
    resultado = sistema.calcular_total(minutos, "frecuente", False)
    # Assert
    assert resultado == 18.0

def test_cliente_frecuente_boleto_perdido(sistema):
    #Caso 13
    #R3 y R8: Boleto perdido sin importar el tipo de cliente
    # Arrange
    minutos = 79
    # Act
    resultado = sistema.calcular_total(minutos, "frecuente", True)
    # Assert
    assert resultado == 300.0


#Decimales:

def test_costo_con_decimales(sistema):
    #Caso 14
    #R7 y R8: $20 de la primer hora más $15 del inicio de la segunda menos 10% por cliente frecuente
    # Arrange
    minutos = 97
    # Act
    resultado = sistema.calcular_total(minutos, "frecuente", False)
    # Assert
    assert resultado == 31.5


#Caso adicional:

def test_0_minutos_boleto_perdido(sistema):
    #Caso 15
    #R3 y R8: Boleto perdido, entonces aunque sean $0 por estar 0 minutos, los $300 siguen teniendo prioridad
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