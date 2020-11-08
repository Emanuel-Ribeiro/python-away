def converte_preco(preco):
  preco = preco.split("R$")[1]
  try:
    preco = preco.split("\n")[0] + "." + preco.split("\n")[1]
  except:
    Exception()
  try:
    preco = preco.split(",")[0] + preco.split(",")[1]
  except:
    Exception()
  return float(preco)