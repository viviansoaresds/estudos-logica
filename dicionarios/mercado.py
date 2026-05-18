
mercado = []
produto1 = {"nome": "carne",
           "quantidade": "1Kg",
           "validade": "23/05/26",
           "preço": 49.90
         }

produto2 = {"nome": "arroz",
            "quantidade": "5Kg",
            "validade": "23/05/26",
            "preço": 22.90        
            }

produto3 = {"nome": "café",
            "quantidade": "500g",
            "validade": "23/10/26",
            "preço": 25.90 
            }

mercado.append(produto1)
mercado.append(produto2)
mercado.append(produto3)

total_compra = 0
for produto in mercado:
    total_compra = total_compra + produto["preço"]
print(f"O valor total da compra foi: {total_compra:.2f}.")   


