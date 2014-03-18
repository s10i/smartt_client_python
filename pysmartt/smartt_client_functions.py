
def setupSmarttFunctions(obj):
    obj.login = login
    obj.loginAttributes = loginAttributes
    obj.logout = logout
    obj.logoutAttributes = logoutAttributes
    obj.logged = logged
    obj.loggedAttributes = loggedAttributes
    obj.getClient = getClient
    obj.getClientAttributes = getClientAttributes
    obj.updateClient = updateClient
    obj.updateClientAttributes = updateClientAttributes
    obj.getClientBrokerages = getClientBrokerages
    obj.getClientBrokeragesAttributes = getClientBrokeragesAttributes
    obj.insertClientBrokerage = insertClientBrokerage
    obj.insertClientBrokerageAttributes = insertClientBrokerageAttributes
    obj.updateClientBrokerage = updateClientBrokerage
    obj.updateClientBrokerageAttributes = updateClientBrokerageAttributes
    obj.getStock = getStock
    obj.getStockAttributes = getStockAttributes
    obj.sendOrder = sendOrder
    obj.sendOrderAttributes = sendOrderAttributes
    obj.cancelOrder = cancelOrder
    obj.cancelOrderAttributes = cancelOrderAttributes
    obj.changeOrder = changeOrder
    obj.changeOrderAttributes = changeOrderAttributes
    obj.getOrders = getOrders
    obj.getOrdersAttributes = getOrdersAttributes
    obj.getOrdersEvents = getOrdersEvents
    obj.getOrdersEventsAttributes = getOrdersEventsAttributes
    obj.getOrderId = getOrderId
    obj.getOrderIdAttributes = getOrderIdAttributes
    obj.sendStopOrder = sendStopOrder
    obj.sendStopOrderAttributes = sendStopOrderAttributes
    obj.cancelStopOrder = cancelStopOrder
    obj.cancelStopOrderAttributes = cancelStopOrderAttributes
    obj.changeStopOrder = changeStopOrder
    obj.changeStopOrderAttributes = changeStopOrderAttributes
    obj.getStopOrders = getStopOrders
    obj.getStopOrdersAttributes = getStopOrdersAttributes
    obj.getStopOrdersEvents = getStopOrdersEvents
    obj.getStopOrdersEventsAttributes = getStopOrdersEventsAttributes
    obj.getStopOrderId = getStopOrderId
    obj.getStopOrderIdAttributes = getStopOrderIdAttributes
    obj.getTrades = getTrades
    obj.getTradesAttributes = getTradesAttributes
    obj.getInvestments = getInvestments
    obj.getInvestmentsAttributes = getInvestmentsAttributes
    obj.getReport = getReport
    obj.getReportAttributes = getReportAttributes
    obj.getDailyCumulativePerformance = getDailyCumulativePerformance
    obj.getDailyCumulativePerformanceAttributes = getDailyCumulativePerformanceAttributes
    obj.getDailyDrawdown = getDailyDrawdown
    obj.getDailyDrawdownAttributes = getDailyDrawdownAttributes
    obj.getPortfolio = getPortfolio
    obj.getPortfolioAttributes = getPortfolioAttributes
    obj.getAvailableLimits = getAvailableLimits
    obj.getAvailableLimitsAttributes = getAvailableLimitsAttributes
    obj.getSetups = getSetups
    obj.getSetupsAttributes = getSetupsAttributes
    obj.updateSetup = updateSetup
    obj.updateSetupAttributes = updateSetupAttributes
    obj.getFinancialTransactions = getFinancialTransactions
    obj.getFinancialTransactionsAttributes = getFinancialTransactionsAttributes
    obj.insertFinancialTransaction = insertFinancialTransaction
    obj.insertFinancialTransactionAttributes = insertFinancialTransactionAttributes
    obj.updateFinancialTransaction = updateFinancialTransaction
    obj.updateFinancialTransactionAttributes = updateFinancialTransactionAttributes
    obj.deleteFinancialTransactions = deleteFinancialTransactions
    obj.deleteFinancialTransactionsAttributes = deleteFinancialTransactionsAttributes


loginAttributes = [
    "message"]


def login(self, s10iLogin = None, s10iPassword = None):
    message = ["login"]
    message += self.formatString("s10i_login", s10iLogin, optional=False)
    message += self.formatString("s10i_password", s10iPassword, optional=False)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = (response[0])
    return parsedResponse


logoutAttributes = [
    "message"]


def logout(self):
    message = ["logout"]
    response = self.smarttFunction(filter(None, message))
    parsedResponse = (response[0])
    return parsedResponse


loggedAttributes = [
    "message"]


def logged(self):
    message = ["logged"]
    response = self.smarttFunction(filter(None, message))
    parsedResponse = (response[0])
    return parsedResponse


getClientAttributes = [
    "natural_person_or_legal_person",
    "name_or_corporate_name",
    "gender",
    "document",
    "email",
    "s10i_login",
    "address",
    "number",
    "complement",
    "neighborhood",
    "postal_code",
    "city",
    "state",
    "country",
    "birthday",
    "main_phone",
    "secondary_phone",
    "company",
    "registration_datetime",
    "plan",
    "has_customized_strategies",
    "plan_expiration_date"]


def getClient(self, returnAttributes = None):
    message = ["get_client"]
    message += self.formatAttributes("return_attributes", returnAttributes, self.getClientAttributes)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = self.formatDictResponse(response[0:], returnAttributes, self.getClientAttributes)
    return parsedResponse


updateClientAttributes = [
    "message"]


def updateClient(self, s10iPassword = None, naturalPersonOrLegalPerson = None, nameOrCorporateName = None, gender = None, email = None, s10iLogin = None, newS10iPassword = None, address = None, number = None, complement = None, neighborhood = None, postalCode = None, city = None, state = None, country = None, birthday = None, mainPhone = None, secondaryPhone = None, company = None):
    message = ["update_client"]
    message += self.formatString("s10i_password", s10iPassword, optional=False)
    message += self.formatBoolean("natural_person_or_legal_person", naturalPersonOrLegalPerson, optional=True)
    message += self.formatString("name_or_corporate_name", nameOrCorporateName, optional=True)
    message += self.formatString("gender", gender, optional=True)
    message += self.formatString("email", email, optional=True)
    message += self.formatString("s10i_login", s10iLogin, optional=True)
    message += self.formatString("new_s10i_password", newS10iPassword, optional=True)
    message += self.formatString("address", address, optional=True)
    message += self.formatString("number", number, optional=True)
    message += self.formatString("complement", complement, optional=True)
    message += self.formatString("neighborhood", neighborhood, optional=True)
    message += self.formatString("postal_code", postalCode, optional=True)
    message += self.formatString("city", city, optional=True)
    message += self.formatString("state", state, optional=True)
    message += self.formatString("country", country, optional=True)
    message += self.formatDate("birthday", birthday, optional=True)
    message += self.formatString("main_phone", mainPhone, optional=True)
    message += self.formatString("secondary_phone", secondaryPhone, optional=True)
    message += self.formatString("company", company, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = (response[0])
    return parsedResponse


getClientBrokeragesAttributes = [
    "brokerage_id",
    "cblc_login"]


def getClientBrokerages(self, brokerageId = None, cblcLogin = None, returnAttributes = None):
    message = ["get_client_brokerages"]
    message += self.formatInteger("brokerage_id", brokerageId, optional=True)
    message += self.formatString("cblc_login", cblcLogin, optional=True)
    message += self.formatAttributes("return_attributes", returnAttributes, self.getClientBrokeragesAttributes)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = self.formatListOfDictsResponse(response[0:], returnAttributes, self.getClientBrokeragesAttributes)
    return parsedResponse


insertClientBrokerageAttributes = [
    "message"]


def insertClientBrokerage(self, brokerageId = None, cblcLogin = None):
    message = ["insert_client_brokerage"]
    message += self.formatInteger("brokerage_id", brokerageId, optional=False)
    message += self.formatString("cblc_login", cblcLogin, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = (response[0])
    return parsedResponse


updateClientBrokerageAttributes = [
    "message"]


def updateClientBrokerage(self, brokerageId = None, cblcLogin = None):
    message = ["update_client_brokerage"]
    message += self.formatInteger("brokerage_id", brokerageId, optional=False)
    message += self.formatString("cblc_login", cblcLogin, optional=False)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = (response[0])
    return parsedResponse


getStockAttributes = [
    "stock_code",
    "market_name",
    "company_name",
    "kind_of_stock",
    "isin_code",
    "trading_lot_size",
    "kind_of_quotation",
    "type",
    "code_underlying_stock",
    "exercise_price",
    "expiration_date"]


def getStock(self, stockCode = None, marketName = None, returnAttributes = None):
    message = ["get_stock"]
    message += self.formatString("stock_code", stockCode, optional=False)
    message += self.formatString("market_name", marketName, optional=True)
    message += self.formatAttributes("return_attributes", returnAttributes, self.getStockAttributes)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = self.formatDictResponse(response[0:], returnAttributes, self.getStockAttributes)
    return parsedResponse


sendOrderAttributes = [
    "order_id"]


def sendOrder(self, investmentCode = None, brokerageId = None, orderType = None, stockCode = None, marketName = None, numberOfStocks = None, price = None, validityType = None, validity = None, entryExitOrReversal = None, reason = None):
    message = ["send_order"]
    message += self.formatString("investment_code", investmentCode, optional=False)
    message += self.formatInteger("brokerage_id", brokerageId, optional=True)
    message += self.formatBoolean("order_type", orderType, optional=False)
    message += self.formatString("stock_code", stockCode, optional=False)
    message += self.formatString("market_name", marketName, optional=True)
    message += self.formatInteger("number_of_stocks", numberOfStocks, optional=False)
    message += self.formatDecimal2("price", price, optional=False)
    message += self.formatString("validity_type", validityType, optional=True)
    message += self.formatDate("validity", validity, optional=True)
    message += self.formatString("entry_exit_or_reversal", entryExitOrReversal, optional=True)
    message += self.formatString("reason", reason, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = int(response[1])
    return parsedResponse


cancelOrderAttributes = [
    "order_id"]


def cancelOrder(self, orderId = None, reason = None):
    message = ["cancel_order"]
    message += self.formatInteger("order_id", orderId, optional=False)
    message += self.formatString("reason", reason, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = int(response[1])
    return parsedResponse


changeOrderAttributes = [
    "order_id"]


def changeOrder(self, orderId = None, newNumberOfStocks = None, newPrice = None, reason = None):
    message = ["change_order"]
    message += self.formatInteger("order_id", orderId, optional=False)
    message += self.formatInteger("new_number_of_stocks", newNumberOfStocks, optional=True)
    message += self.formatDecimal2("new_price", newPrice, optional=True)
    message += self.formatString("reason", reason, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = int(response[1])
    return parsedResponse


getOrdersAttributes = [
    "order_id",
    "order_id_in_brokerage",
    "investment_code",
    "brokerage_id",
    "is_real",
    "order_type",
    "stock_code",
    "market_name",
    "datetime",
    "number_of_stocks",
    "nominal_price",
    "financial_volume",
    "validity_type",
    "validity",
    "number_of_traded_stocks",
    "average_nominal_price",
    "status",
    "absolute_brokerage_tax_cost",
    "percentual_brokerage_tax_cost",
    "iss_tax_cost",
    "entry_exit_or_reversal",
    "triggered_stop_order_id"]


def getOrders(self, orderId = None, investmentCode = None, brokerageId = None, initialDatetime = None, finalDatetime = None, stockCode = None, marketName = None, status = None, returnAttributes = None):
    message = ["get_orders"]
    message += self.formatInteger("order_id", orderId, optional=True)
    message += self.formatString("investment_code", investmentCode, optional=True)
    message += self.formatInteger("brokerage_id", brokerageId, optional=True)
    message += self.formatDatetime("initial_datetime", initialDatetime, optional=True)
    message += self.formatDatetime("final_datetime", finalDatetime, optional=True)
    message += self.formatString("stock_code", stockCode, optional=True)
    message += self.formatString("market_name", marketName, optional=True)
    message += self.formatString("status", status, optional=True)
    message += self.formatAttributes("return_attributes", returnAttributes, self.getOrdersAttributes)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = self.formatListOfDictsResponse(response[0:], returnAttributes, self.getOrdersAttributes)
    return parsedResponse


getOrdersEventsAttributes = [
    "order_id",
    "investment_code",
    "brokerage_id",
    "number_of_events",
    "datetime",
    "event_type",
    "description",
    "reason"]


def getOrdersEvents(self, orderId = None, investmentCode = None, brokerageId = None, initialDatetime = None, finalDatetime = None, eventType = None, returnAttributes = None):
    message = ["get_orders_events"]
    message += self.formatInteger("order_id", orderId, optional=True)
    message += self.formatString("investment_code", investmentCode, optional=True)
    message += self.formatInteger("brokerage_id", brokerageId, optional=True)
    message += self.formatDatetime("initial_datetime", initialDatetime, optional=True)
    message += self.formatDatetime("final_datetime", finalDatetime, optional=True)
    message += self.formatString("event_type", eventType, optional=True)
    message += self.formatAttributes("return_attributes", returnAttributes, self.getOrdersEventsAttributes)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = self.formatListOfDictsResponse(response[0:], returnAttributes, self.getOrdersEventsAttributes)
    return parsedResponse


getOrderIdAttributes = [
    "order_id"]


def getOrderId(self, orderIdInBrokerage = None, brokerageId = None, stockCode = None, marketName = None, date = None):
    message = ["get_order_id"]
    message += self.formatString("order_id_in_brokerage", orderIdInBrokerage, optional=False)
    message += self.formatInteger("brokerage_id", brokerageId, optional=False)
    message += self.formatString("stock_code", stockCode, optional=False)
    message += self.formatString("market_name", marketName, optional=True)
    message += self.formatDate("date", date, optional=False)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = int(response[0])
    return parsedResponse


sendStopOrderAttributes = [
    "stop_order_id"]


def sendStopOrder(self, investmentCode = None, brokerageId = None, orderType = None, stopOrderType = None, stockCode = None, marketName = None, numberOfStocks = None, stopPrice = None, limitPrice = None, validity = None, entryExitOrReversal = None, reason = None):
    message = ["send_stop_order"]
    message += self.formatString("investment_code", investmentCode, optional=False)
    message += self.formatInteger("brokerage_id", brokerageId, optional=True)
    message += self.formatBoolean("order_type", orderType, optional=False)
    message += self.formatBoolean("stop_order_type", stopOrderType, optional=False)
    message += self.formatString("stock_code", stockCode, optional=False)
    message += self.formatString("market_name", marketName, optional=True)
    message += self.formatInteger("number_of_stocks", numberOfStocks, optional=False)
    message += self.formatDecimal2("stop_price", stopPrice, optional=False)
    message += self.formatDecimal2("limit_price", limitPrice, optional=False)
    message += self.formatDate("validity", validity, optional=False)
    message += self.formatString("entry_exit_or_reversal", entryExitOrReversal, optional=True)
    message += self.formatString("reason", reason, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = int(response[1])
    return parsedResponse


cancelStopOrderAttributes = [
    "stop_order_id"]


def cancelStopOrder(self, stopOrderId = None, reason = None):
    message = ["cancel_stop_order"]
    message += self.formatInteger("stop_order_id", stopOrderId, optional=False)
    message += self.formatString("reason", reason, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = int(response[1])
    return parsedResponse


changeStopOrderAttributes = [
    "stop_order_id"]


def changeStopOrder(self, stopOrderId = None, newNumberOfStocks = None, newStopPrice = None, newLimitPrice = None, reason = None):
    message = ["change_stop_order"]
    message += self.formatInteger("stop_order_id", stopOrderId, optional=False)
    message += self.formatInteger("new_number_of_stocks", newNumberOfStocks, optional=True)
    message += self.formatDecimal2("new_stop_price", newStopPrice, optional=True)
    message += self.formatDecimal2("new_limit_price", newLimitPrice, optional=True)
    message += self.formatString("reason", reason, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = int(response[1])
    return parsedResponse


getStopOrdersAttributes = [
    "stop_order_id",
    "stop_order_id_in_brokerage",
    "investment_code",
    "brokerage_id",
    "is_real",
    "order_type",
    "stop_order_type",
    "stock_code",
    "market_name",
    "datetime",
    "number_of_stocks",
    "stop_price",
    "limit_price",
    "validity",
    "status",
    "entry_exit_or_reversal",
    "sent_order_id"]


def getStopOrders(self, stopOrderId = None, investmentCode = None, brokerageId = None, initialDatetime = None, finalDatetime = None, stockCode = None, marketName = None, status = None, returnAttributes = None):
    message = ["get_stop_orders"]
    message += self.formatInteger("stop_order_id", stopOrderId, optional=True)
    message += self.formatString("investment_code", investmentCode, optional=True)
    message += self.formatInteger("brokerage_id", brokerageId, optional=True)
    message += self.formatDatetime("initial_datetime", initialDatetime, optional=True)
    message += self.formatDatetime("final_datetime", finalDatetime, optional=True)
    message += self.formatString("stock_code", stockCode, optional=True)
    message += self.formatString("market_name", marketName, optional=True)
    message += self.formatString("status", status, optional=True)
    message += self.formatAttributes("return_attributes", returnAttributes, self.getStopOrdersAttributes)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = self.formatListOfDictsResponse(response[0:], returnAttributes, self.getStopOrdersAttributes)
    return parsedResponse


getStopOrdersEventsAttributes = [
    "stop_order_id",
    "investment_code",
    "brokerage_id",
    "number_of_events",
    "datetime",
    "event_type",
    "description",
    "reason"]


def getStopOrdersEvents(self, stopOrderId = None, investmentCode = None, brokerageId = None, initialDatetime = None, finalDatetime = None, eventType = None, returnAttributes = None):
    message = ["get_stop_orders_events"]
    message += self.formatInteger("stop_order_id", stopOrderId, optional=True)
    message += self.formatString("investment_code", investmentCode, optional=True)
    message += self.formatInteger("brokerage_id", brokerageId, optional=True)
    message += self.formatDatetime("initial_datetime", initialDatetime, optional=True)
    message += self.formatDatetime("final_datetime", finalDatetime, optional=True)
    message += self.formatString("event_type", eventType, optional=True)
    message += self.formatAttributes("return_attributes", returnAttributes, self.getStopOrdersEventsAttributes)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = self.formatListOfDictsResponse(response[0:], returnAttributes, self.getStopOrdersEventsAttributes)
    return parsedResponse


getStopOrderIdAttributes = [
    "stop_order_id"]


def getStopOrderId(self, stopOrderIdInBrokerage = None, brokerageId = None, stockCode = None, marketName = None, date = None):
    message = ["get_stop_order_id"]
    message += self.formatString("stop_order_id_in_brokerage", stopOrderIdInBrokerage, optional=False)
    message += self.formatInteger("brokerage_id", brokerageId, optional=False)
    message += self.formatString("stock_code", stockCode, optional=False)
    message += self.formatString("market_name", marketName, optional=True)
    message += self.formatDate("date", date, optional=False)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = int(response[0])
    return parsedResponse


getTradesAttributes = [
    "order_id",
    "trade_id_in_brokerage",
    "investment_code",
    "brokerage_id",
    "is_real",
    "trade_type",
    "stock_code",
    "market_name",
    "datetime",
    "number_of_stocks",
    "nominal_price",
    "financial_volume",
    "trading_tax_cost",
    "liquidation_tax_cost",
    "register_tax_cost",
    "income_tax_cost",
    "withholding_income_tax_cost",
    "other_taxes_cost"]


def getTrades(self, orderId = None, investmentCode = None, brokerageId = None, initialDatetime = None, finalDatetime = None, stockCode = None, marketName = None, returnAttributes = None):
    message = ["get_trades"]
    message += self.formatInteger("order_id", orderId, optional=True)
    message += self.formatString("investment_code", investmentCode, optional=True)
    message += self.formatInteger("brokerage_id", brokerageId, optional=True)
    message += self.formatDatetime("initial_datetime", initialDatetime, optional=True)
    message += self.formatDatetime("final_datetime", finalDatetime, optional=True)
    message += self.formatString("stock_code", stockCode, optional=True)
    message += self.formatString("market_name", marketName, optional=True)
    message += self.formatAttributes("return_attributes", returnAttributes, self.getTradesAttributes)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = self.formatListOfDictsResponse(response[0:], returnAttributes, self.getTradesAttributes)
    return parsedResponse


getInvestmentsAttributes = [
    "name",
    "code",
    "brokerage_id",
    "setup_code",
    "is_real",
    "initial_datetime",
    "final_datetime"]


def getInvestments(self, investmentCode = None, brokerageId = None, returnAttributes = None):
    message = ["get_investments"]
    message += self.formatString("investment_code", investmentCode, optional=True)
    message += self.formatInteger("brokerage_id", brokerageId, optional=True)
    message += self.formatAttributes("return_attributes", returnAttributes, self.getInvestmentsAttributes)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = self.formatListOfDictsResponse(response[0:], returnAttributes, self.getInvestmentsAttributes)
    return parsedResponse


getReportAttributes = [
    "investment_code",
    "brokerage_id",
    "setup_code",
    "initial_datetime",
    "final_datetime",
    "number_of_days",
    "total_contributions",
    "total_withdraws",
    "initial_capital",
    "balance",
    "equity",
    "taxes_and_operational_costs",
    "gross_return",
    "gross_daily_return",
    "gross_annualized_return",
    "net_return",
    "net_daily_return",
    "net_annualized_return",
    "absolute_initial_drawdown",
    "percentual_initial_drawdown",
    "absolute_maximum_drawdown",
    "percentual_maximum_drawdown",
    "gross_profit",
    "gross_loss",
    "total_gross_profit",
    "net_profit",
    "net_loss",
    "total_net_profit",
    "profit_factor",
    "number_of_eliminations",
    "expected_payoff",
    "absolute_number_of_profit_eliminations",
    "percentual_number_of_profit_eliminations",
    "absolute_largest_profit_elimination",
    "percentual_largest_profit_elimination",
    "average_profit_in_profit_eliminations",
    "maximum_consecutive_profit_eliminations",
    "total_profit_in_maximum_consecutive_profit_eliminations",
    "absolute_number_of_loss_eliminations",
    "percentual_number_of_loss_eliminations",
    "absolute_largest_loss_elimination",
    "percentual_largest_loss_elimination",
    "average_loss_in_loss_eliminations",
    "maximum_consecutive_loss_eliminations",
    "total_loss_in_maximum_consecutive_loss_eliminations",
    "absolute_number_of_eliminations_of_long_positions",
    "percentual_number_of_eliminations_of_long_positions",
    "absolute_number_of_profit_eliminations_of_long_positions",
    "percentual_number_of_profit_eliminations_of_long_positions",
    "absolute_number_of_loss_eliminations_of_long_positions",
    "percentual_number_of_loss_eliminations_of_long_positions",
    "absolute_number_of_eliminations_of_short_positions",
    "percentual_number_of_eliminations_of_short_positions",
    "absolute_number_of_profit_eliminations_of_short_positions",
    "percentual_number_of_profit_eliminations_of_short_positions",
    "absolute_number_of_loss_eliminations_of_short_positions",
    "percentual_number_of_loss_eliminations_of_short_positions"]


def getReport(self, investmentCode = None, brokerageId = None, initialDatetime = None, finalDatetime = None, returnAttributes = None):
    message = ["get_report"]
    message += self.formatString("investment_code", investmentCode, optional=False)
    message += self.formatInteger("brokerage_id", brokerageId, optional=True)
    message += self.formatDatetime("initial_datetime", initialDatetime, optional=True)
    message += self.formatDatetime("final_datetime", finalDatetime, optional=True)
    message += self.formatAttributes("return_attributes", returnAttributes, self.getReportAttributes)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = self.formatDictResponse(response[0:], returnAttributes, self.getReportAttributes)
    return parsedResponse


getDailyCumulativePerformanceAttributes = [
    "investment_code",
    "brokerage_id",
    "daily_cumulative_performance"]


def getDailyCumulativePerformance(self, investmentCode = None, brokerageId = None, initialDatetime = None, finalDatetime = None):
    message = ["get_daily_cumulative_performance"]
    message += self.formatString("investment_code", investmentCode, optional=False)
    message += self.formatInteger("brokerage_id", brokerageId, optional=True)
    message += self.formatDatetime("initial_datetime", initialDatetime, optional=True)
    message += self.formatDatetime("final_datetime", finalDatetime, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = self.formatDictResponse(response[0:], [], self.getDailyCumulativePerformanceAttributes)
    return parsedResponse


getDailyDrawdownAttributes = [
    "investment_code",
    "brokerage_id",
    "daily_drawdown"]


def getDailyDrawdown(self, investmentCode = None, brokerageId = None, initialDatetime = None, finalDatetime = None):
    message = ["get_daily_drawdown"]
    message += self.formatString("investment_code", investmentCode, optional=False)
    message += self.formatInteger("brokerage_id", brokerageId, optional=True)
    message += self.formatDatetime("initial_datetime", initialDatetime, optional=True)
    message += self.formatDatetime("final_datetime", finalDatetime, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = self.formatDictResponse(response[0:], [], self.getDailyDrawdownAttributes)
    return parsedResponse


getPortfolioAttributes = [
    "stock_code",
    "position_type",
    "number_of_stocks",
    "average_price",
    "financial_volume"]


def getPortfolio(self, investmentCode = None, brokerageId = None, initialDatetime = None, finalDatetime = None, returnAttributes = None):
    message = ["get_portfolio"]
    message += self.formatString("investment_code", investmentCode, optional=False)
    message += self.formatInteger("brokerage_id", brokerageId, optional=True)
    message += self.formatDatetime("initial_datetime", initialDatetime, optional=True)
    message += self.formatDatetime("final_datetime", finalDatetime, optional=True)
    message += self.formatAttributes("return_attributes", returnAttributes, self.getPortfolioAttributes)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = self.formatListOfDictsResponse(response[2:], returnAttributes, self.getPortfolioAttributes)
    return parsedResponse


getAvailableLimitsAttributes = [
    "spot",
    "option",
    "margin"]


def getAvailableLimits(self, investmentCode = None, brokerageId = None, returnAttributes = None):
    message = ["get_available_limits"]
    message += self.formatString("investment_code", investmentCode, optional=True)
    message += self.formatInteger("brokerage_id", brokerageId, optional=True)
    message += self.formatAttributes("return_attributes", returnAttributes, self.getAvailableLimitsAttributes)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = self.formatListOfDictsResponse(response[0:], returnAttributes, self.getAvailableLimitsAttributes)
    return parsedResponse


getSetupsAttributes = [
    "name",
    "code",
    "initial_capital",
    "slippage",
    "absolute_brokerage_tax",
    "percentual_brokerage_tax",
    "position_trading_tax",
    "position_liquidation_tax",
    "position_register_tax",
    "position_income_tax",
    "position_withholding_income_tax",
    "position_other_taxes",
    "day_trade_trading_tax",
    "day_trade_liquidation_tax",
    "day_trade_register_tax",
    "day_trade_income_tax",
    "day_trade_withholding_income_tax",
    "day_trade_other_taxes",
    "iss_tax",
    "custody_tax",
    "lease_tax",
    "income_tax_payment"]


def getSetups(self, code = None, returnAttributes = None):
    message = ["get_setups"]
    message += self.formatString("code", code, optional=True)
    message += self.formatAttributes("return_attributes", returnAttributes, self.getSetupsAttributes)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = self.formatListOfDictsResponse(response[0:], returnAttributes, self.getSetupsAttributes)
    return parsedResponse


updateSetupAttributes = [
    "message"]


def updateSetup(self, code = None, name = None, newCode = None, initialCapital = None, slippage = None, absoluteBrokerageTax = None, percentualBrokerageTax = None, positionTradingTax = None, positionLiquidationTax = None, positionRegisterTax = None, positionIncomeTax = None, positionWithholdingIncomeTax = None, positionOtherTaxes = None, dayTradeTradingTax = None, dayTradeLiquidationTax = None, dayTradeRegisterTax = None, dayTradeIncomeTax = None, dayTradeWithholdingIncomeTax = None, dayTradeOtherTaxes = None, issTax = None, custodyTax = None, leaseTax = None, incomeTaxPayment = None):
    message = ["update_setup"]
    message += self.formatString("code", code, optional=False)
    message += self.formatString("name", name, optional=True)
    message += self.formatString("new_code", newCode, optional=True)
    message += self.formatString("initial_capital", initialCapital, optional=True)
    message += self.formatDecimal2("slippage", slippage, optional=True)
    message += self.formatDecimal2("absolute_brokerage_tax", absoluteBrokerageTax, optional=True)
    message += self.formatDecimal6("percentual_brokerage_tax", percentualBrokerageTax, optional=True)
    message += self.formatDecimal6("position_trading_tax", positionTradingTax, optional=True)
    message += self.formatDecimal6("position_liquidation_tax", positionLiquidationTax, optional=True)
    message += self.formatDecimal2("position_register_tax", positionRegisterTax, optional=True)
    message += self.formatDecimal2("position_income_tax", positionIncomeTax, optional=True)
    message += self.formatDecimal2("position_withholding_income_tax", positionWithholdingIncomeTax, optional=True)
    message += self.formatDecimal2("position_other_taxes", positionOtherTaxes, optional=True)
    message += self.formatDecimal6("day_trade_trading_tax", dayTradeTradingTax, optional=True)
    message += self.formatDecimal6("day_trade_liquidation_tax", dayTradeLiquidationTax, optional=True)
    message += self.formatDecimal6("day_trade_register_tax", dayTradeRegisterTax, optional=True)
    message += self.formatDecimal6("day_trade_income_tax", dayTradeIncomeTax, optional=True)
    message += self.formatDecimal6("day_trade_withholding_income_tax", dayTradeWithholdingIncomeTax, optional=True)
    message += self.formatDecimal2("day_trade_other_taxes", dayTradeOtherTaxes, optional=True)
    message += self.formatDecimal6("iss_tax", issTax, optional=True)
    message += self.formatDecimal2("custody_tax", custodyTax, optional=True)
    message += self.formatDecimal6("lease_tax", leaseTax, optional=True)
    message += self.formatString("income_tax_payment", incomeTaxPayment, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = (response[0])
    return parsedResponse


getFinancialTransactionsAttributes = [
    "financial_transaction_id",
    "investment_code",
    "brokerage_id",
    "datetime",
    "contribution_or_withdrawal",
    "value",
    "operational_tax_cost",
    "description"]


def getFinancialTransactions(self, financialTransactionId = None, investmentCode = None, brokerageId = None, returnAttributes = None):
    message = ["get_financial_transactions"]
    message += self.formatString("financial_transaction_id", financialTransactionId, optional=True)
    message += self.formatString("investment_code", investmentCode, optional=True)
    message += self.formatInteger("brokerage_id", brokerageId, optional=True)
    message += self.formatAttributes("return_attributes", returnAttributes, self.getFinancialTransactionsAttributes)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = self.formatListOfDictsResponse(response[0:], returnAttributes, self.getFinancialTransactionsAttributes)
    return parsedResponse


insertFinancialTransactionAttributes = [
    "message"]


def insertFinancialTransaction(self, investmentCode = None, brokerageId = None, datetime = None, contributionOrWithdrawal = None, value = None, operationalTaxCost = None, description = None):
    message = ["insert_financial_transaction"]
    message += self.formatString("investment_code", investmentCode, optional=False)
    message += self.formatInteger("brokerage_id", brokerageId, optional=True)
    message += self.formatDatetime("datetime", datetime, optional=False)
    message += self.formatBoolean("contribution_or_withdrawal", contributionOrWithdrawal, optional=False)
    message += self.formatDecimal2("value", value, optional=False)
    message += self.formatDecimal2("operational_tax_cost", operationalTaxCost, optional=False)
    message += self.formatString("description", description, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = (response[0])
    return parsedResponse


updateFinancialTransactionAttributes = [
    "message"]


def updateFinancialTransaction(self, financialTransactionId = None, investmentCode = None, brokerageId = None, datetime = None, contributionOrWithdrawal = None, value = None, operationalTaxCost = None, description = None):
    message = ["update_financial_transaction"]
    message += self.formatString("financial_transaction_id", financialTransactionId, optional=False)
    message += self.formatString("investment_code", investmentCode, optional=True)
    message += self.formatInteger("brokerage_id", brokerageId, optional=True)
    message += self.formatDatetime("datetime", datetime, optional=True)
    message += self.formatBoolean("contribution_or_withdrawal", contributionOrWithdrawal, optional=True)
    message += self.formatDecimal2("value", value, optional=True)
    message += self.formatDecimal2("operational_tax_cost", operationalTaxCost, optional=True)
    message += self.formatString("description", description, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = (response[0])
    return parsedResponse


deleteFinancialTransactionsAttributes = [
    "message"]


def deleteFinancialTransactions(self, financialTransactionId = None, investmentCode = None, brokerageId = None):
    message = ["delete_financial_transactions"]
    message += self.formatString("financial_transaction_id", financialTransactionId, optional=True)
    message += self.formatString("investment_code", investmentCode, optional=True)
    message += self.formatInteger("brokerage_id", brokerageId, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = (response[0])
    return parsedResponse

