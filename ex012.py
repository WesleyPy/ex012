preco = float(input('Qual é o preço do produto? R$ '))
novo = preco - (preco * 5 / 100)
print('O produto que custava {:.2f}R$, na promoção com 5% de desconto vai custar {:.2f}'.format(preco, novo))