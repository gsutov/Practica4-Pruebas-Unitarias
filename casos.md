### Casos normales
| Casos | Entrada | Resultado Esperado | Regla | Justificación |
|---|---|---|---|---|
| 1 | 7 min, normal, boleto no perdido | $0.00 | R5 | De 1 a 15 minutos es gratis |
| 2 | 71 min, normal, boleto no perdido | $35.00 | R7 | $20 de la primer hora más $15 del inicio de la segunda |
| 3 | 23 min, normal, boleto n operdido | $20.00 | R6 | De 16 a 60 minutos son $20 |


### Casos frontera
| Casos | Entrada | Resultado Esperado | Regla | Justificación |
|---|---|---|---|---|
| 4 | 0 min, normal, boleto no perdido | $0.00 | R4 | 0 minutos es gratis |
| 5 | 15 min, normal, boleto no perdido | $0.00 | R5 | De 1 a 15 minutos es gratis |
| 6 | 16 min, normal, boleto no perdido | $20.00 | R6 | De 16 a 60 minutos son $20 |
| 7 | 60 min, normal, boleto no perdido | $20.00 | R6 | De 16 a 60 minutos son $20 |
| 8 | 61 min, normal, boleto no perdido | $35.00 | R7 | $20 de la primer hora más $15 del inicio de la segunda |
| 9 | 121 min, normal, boleto no perdido | $50.00 | R7 | $20 de la primer hora más $15 de la segunda más 15 del inicio de la tercera |

### Entradas inválidas
| Casos | Entrada | Resultado Esperado | Regla | Justificación |
|---|---|---|---|---|
| 10 | -3 min, normal, boleto no perdido | ERROR | R10 | Minutos negativos |
| 11 | 47 min, Batman, boleto no perdido | ERROR | R11 | Tipo de cliente no válido |

#### Interacción entre reglas
| Casos | Entrada | Resultado Esperado | Reglas | Justificación |
|---|---|---|---|---|
| 12 | 43 min, frecuente, boleto no perdido | $18.00 | R6 y R8 | De 16 a 60 minutos es $20 menos el 10% por cleinte frecuente |
| 13 | 79 min, frecuente, boleto perdido | $300.00 | R3 y R8 | Boleto perdido sin importar el tipo de cliente |

### Números decimales
| Casos | Entrada | Resultado Esperado | Reglas | Justificación |
|---|---|---|---|---|
| 14 | 97 min, frecuente, boleto no perdido | $31.50 | R7 y R8 | $20 de la primer hora más $15 del inicio de la segunda menos 10% por cliente frecuente |

### Caso adicional
| Casos | Entrada | Resultado Esperado | Reglas | Justificación |
|---|---|---|---|---|
| 15 | 0 min, normal, boleto perdido | $300.00 | R3 y R8 | Boleto perdido, entonces aunque sean $0 por estar 0 minutos, los $300 siguen teniendo prioridad 