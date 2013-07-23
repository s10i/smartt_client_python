#!/usr/bin/python
# -*- coding: utf-8

from pysmartt import smartt_client

client = smartt_client.SmarttClient()

print client.logged()

print client.login("LOGIN", "PASSWORD")

print client.getPortfolio("auto")
#print client.getOrders()

# Envia uma ordem de compra de uma ação da Petrobrás a R$5,00
print client.sendOrder(investment_code="auto", order_type="buy",
					   stock_code="PETR3F", number_of_stocks=1,
					   price=5.00)
