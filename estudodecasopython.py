def valida_cpf_simples(cpf):

  # Remove caracteres não numéricos (se houver)
  cpf_sem_caracteres = ''.join(i for i in cpf if i.isdigit())

  # Valida o tamanho do CPF (deve ter 11 dígitos)
  if len(cpf_sem_caracteres) != 11:
    return False

  # Converte o CPF em lista de dígitos
  digitos = list(map(int, cpf_sem_caracteres))

  # Cálculo do primeiro dígito verificador (DV1)
  soma_dv1 = 0
  multiplicador = 10
  for i in range(len(digitos)):
    soma_dv1 += digitos[i] * multiplicador
    multiplicador -= 1

  resto_dv1 = soma_dv1 % 11
  dv1 = 0 if resto_dv1 == 0 else 11 - resto_dv1

  # Cálculo do segundo dígito verificador (DV2)
  soma_dv2 = 0
  multiplicador = 11
  for i in range(len(digitos)):
    soma_dv2 += digitos[i] * multiplicador
    multiplicador -= 1

  resto_dv2 = soma_dv2 % 11
  dv2 = 0 if resto_dv2 == 0 else 11 - resto_dv2

  # Validação final: verifica se os DVs conferem com os dígitos informados
  return digitos[9] == dv1 and digitos[10] == dv2

# Exemplo de uso
cpf_teste = "12345678901"  # CPF válido para teste

if valida_cpf_simples(cpf_teste):
  print(f"O CPF {cpf_teste} é válido!")
else:
  print(f"O CPF {cpf_teste} é inválido!")
