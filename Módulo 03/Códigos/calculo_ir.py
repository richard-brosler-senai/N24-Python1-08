"""
Programa para calculo do imposto de renda retido na fonte
Author: Richard Brosler
Version: 2024-10-03
"""
from click import clear # importando clear de click
# clear limpa a tela
clear()
# Definindo minhas constantes
"""
Faixa	Base de Cálculo (R$)	Alíquota (%) Dedução
1ª	 Até 2.259,20	            Isento
2ª	De 2.259,21 até 2.826,65	7,5        R$ 169,44
3ª	De 2.826,66 até 3.751,05	15         R$ 381,44
4ª	De 3.751,06 até 4.664,68	22,5       R$ 662,77
Acima de R$ 4.664,68	        27,5%      R$ 896,00
"""
VLR_DEP = 189.59
FX4_LMT, FX4_PER, FX4_DED = 4664.69, 27.5, 896.00
FX3_LMT, FX3_PER, FX3_DED = 3751.06, 22.5, 662.77
FX2_LMT, FX2_PER, FX2_DED = 2826.66, 15.0, 381.44
FX1_LMT, FX1_PER, FX1_DED = 2259.21, 7.5, 169.44
# Solicitar os valores
sal_base = float(input("Digite o salário base: "))
deducoes = float(input("Digite o valor das deduções: "))
depen = int(input("Digite o número de dependentes de IR: "))
# Calculando a base para o imposto
base = sal_base - deducoes - VLR_DEP * depen
# Calculo do imposto
if base >= FX4_LMT:
    vl_ir = base * FX4_PER / 100 - FX4_DED
elif base >= FX3_LMT:
    vl_ir = base * FX3_PER / 100 - FX3_DED
elif base >= FX2_LMT:
    vl_ir = base * FX2_PER / 100 - FX2_DED
elif base >= FX1_LMT:
    vl_ir = base * FX1_PER / 100 - FX1_DED
else:
    vl_ir = 0 # Isento
# Mostrando os resultados
print("O valor do seu IR é",round(vl_ir,2)) # 2 casas decimais
