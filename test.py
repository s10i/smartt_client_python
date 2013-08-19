# -*- coding: utf-8
#!/usr/bin/python

import datetime
import pprint
from pysmartt import smartt_client

client = smartt_client.SmarttClient(use_ssl=False)

print client.logged()

print client.login("YOUR_LOGIN", "YOUR_PASSWORD")

print "Available investments:"

pprint.pprint(client.getInvestments(returnAttributes = ["name", "brokerage_id", "is_real"]))

print "\"Paper\" investment portfolio:"

pprint.pprint(client.getPortfolio("paper"))

print len(client.getOrders()), "orders in the investment"

# Envia uma ordem de compra de uma ação da Petrobrás a R$5,00
oid = client.sendOrder(investmentCode="paper", orderType=0,
					   stockCode="PETR3F", numberOfStocks=1,
					   price=5.00)

print "Sent order", oid

pprint.pprint(client.getOrders(orderId = oid))

print "Order's events:"
pprint.pprint(client.getOrdersEvents(orderId = oid))

print "Cancelled order", client.cancelOrder(orderId = oid)

soid = client.sendStopOrder(investmentCode = "paper", orderType = 0, stopOrderType = 0,
                            stockCode = "PETR3F", numberOfStocks = 1, stopPrice = 5.00,
                            limitPrice = 3.00, validAfterMarket = False,
                            validity = datetime.date.today() + datetime.timedelta(days=1))

print "Sent stop order", soid

print "Current stop orders:"

pprint.pprint(client.getStopOrders(investmentCode = "paper"))

print "Cancelled stop order", client.cancelStopOrder(soid)

print client.logout()
