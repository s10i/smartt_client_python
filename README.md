
# pysmartt - S10I Smartt Python Client

Bibliotecas e aplicações cliente para o Smartt na linguagem Python.

O código desta biblioteca é aberto, distribuído sob a licença BSD de duas
cláusulas (ver arquivo LICENSE).


## Dependências

Python 2: 2.7 ou superior
ou
Python 3: 3.1 ou superior

## Instalação

Para instalar via `pip`, basta utilizar o seguinte comando:

```
pip install git+https://github.com/s10i/smartt_client_python/
```

## Uso

Esta biblioteca facilita o uso do S10I Smartt, provendo funções simples em Python
para chamar funções remotas da API do Smartt.

```python
    from pysmartt import smartt_client

    client = smartt_client.SmarttClient()

    print(client.login("LOGIN", "PASSWORD"))
```

Em geral, para cada função do Smartt, há um método na classe SmarttClient, com o mesmo
nome escrito no padrão lowerCammelCase. Por exemplo, a função get_client do Smartt,
que pode ser encontrada na referência da API, é mapeada para o método
SmarttClient.getClient(). O mesmo ocorre com os parâmetros. Ou seja, no caso da função
getClient, que recebe um único parâmetro opcional "return_attributes", o parâmetro
correspondente do método SmarttClient.getClient chama-se returnAttributes, e é uma
lista de strings.

Assim, uma chamada válida para a função getClient do Smartt seria:

```python
    client.getClient(returnAttributes=["email", "s10i_login", "city"])
```

O resultado desta chamada será um dicionário, com três chaves:
"email", "s10i_login" e "city", e com os valores correspondentes.

### Listas

Funções do Smartt que retornam listas correspondem a métodos que retornam listas
do Python. Por exemplo, a seguinte chamada da função get_orders do Smartt:

```python
    orders = client.getOrders(investmentCode="paper")
```

Retorna uma lista de dicionários. Podemos exibir, então, todas as ordens do usuário com:

```python
    print len(orders), "orders made."
    for order in orders:
        print "\n", order
```

O que exibirá algo como (formatado para melhor visualização):

```
    2 orders made.

    {'absolute_brokerage_tax_cost': u'0.00',
     'average_nominal_price': u'0.000000',
     'brokerage_id': u'1000',
     'datetime': u'2013-08-06 17:48:52',
     'financial_volume': u'0.00',
     'investment_code': u'paper',
     'is_real': u'0',
     'iss_tax_cost': u'0.00',
     'market_name': u'Bovespa',
     'nominal_price': u'5.00',
     'number_of_stocks': u'100',
     'number_of_traded_stocks': u'0',
     'order_id': u'15741',
     'order_id_in_brokerage': u'14143',
     'order_type': u'1',
     'percentual_brokerage_tax_cost': u'0.000000',
     'status': u'expired',
     'stock_code': u'PETR4F',
     'validity': u'2013-08-06',
     'validity_type': u'HJ'}

    {'absolute_brokerage_tax_cost': u'0.00',
     'average_nominal_price': u'0.000000',
     'brokerage_id': u'1000',
     'datetime': u'2013-08-06 17:50:29',
     'financial_volume': u'0.00',
     'investment_code': u'paper',
     'is_real': u'0',
     'iss_tax_cost': u'0.00',
     'market_name': u'Bovespa',
     'nominal_price': u'5.00',
     'number_of_stocks': u'100',
     'number_of_traded_stocks': u'0',
     'order_id': u'15742',
     'order_id_in_brokerage': u'14144',
     'order_type': u'1',
     'percentual_brokerage_tax_cost': u'0.000000',
     'status': u'canceled',
     'stock_code': u'PETR4F',
     'validity': u'2013-08-06',
     'validity_type': u'HJ'}
```

O mesmo vale também para a função get_portfolio, que no Smartt retorna
dois campos seguidos de uma lista, e no cliente retorna apenas a lista (caso deseje
as outras duas informações, elas poderão ser obtidas com a função get_investments).

### Datas

Para passar datas como parâmetros, use as classes date e datetime do Python:

```python
    import datetime

    # Imprime todos os trades realizados hoje no Paper Trading
    print c.getTrades(investmentCode="paper",
                      initialDatetime=datetime.date.today())
```

### Resultados

Os valores são retornados em tipos apropriados para cada função do Smartt: listas, quando
o Smartt pode retornar mais de um objeto, dicionários, quando o Smartt retorna vários campos,
e um tipo escalar (string, int, ou outro) quando o valor de retorno da função do Smartt
for sempre um único valor. Este é o caso, pode exemplo, da função cancel_order.

```python
    # Envia uma tentativa de cancelamento de uma ordem.
    # Como a função do Smartt retorna apenas o id da ordem,
    # c.cancelOrder() retorna um inteiro
    print c.cancelOrder(orderId=12345)
```

No entanto, valores dentro de dicionários são retornados como vêm do Smartt, ou seja,
como strings. Para convertê-los para inteiros, floats ou datas, basta usar
as funções nativas do Python diretamente: int(), float() e datetime.datetime.strptime().

## Exemplo

```python
    from pysmartt import smartt_client

    client = smartt_client.SmarttClient()

    print client.logged()

    print client.login("LOGIN", "PASSWORD")

    print client.getPortfolio("auto")

    # Envia uma ordem de compra de uma ação da Petrobrás a R$5,00
    print client.sendOrder(investment_code="auto", order_type=0,
                           stock_code="PETR4", number_of_stocks=100,
                           price=5.00)

    client.logout()
```
