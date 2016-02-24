
def setupSmarttFunctions(obj):
    obj.login = login
    obj.loginAttributes = loginAttributes
    obj.logout = logout
    obj.logoutAttributes = logoutAttributes
    obj.logged = logged
    obj.loggedAttributes = loggedAttributes
    obj.loginApiKey = loginApiKey
    obj.loginApiKeyAttributes = loginApiKeyAttributes
    obj.checkPassword = checkPassword
    obj.checkPasswordAttributes = checkPasswordAttributes
    obj.getClient = getClient
    obj.getClientAttributes = getClientAttributes
    obj.updateClient = updateClient
    obj.updateClientAttributes = updateClientAttributes
    obj.getApiKeys = getApiKeys
    obj.getApiKeysAttributes = getApiKeysAttributes
    obj.insertApiKey = insertApiKey
    obj.insertApiKeyAttributes = insertApiKeyAttributes
    obj.deleteApiKey = deleteApiKey
    obj.deleteApiKeyAttributes = deleteApiKeyAttributes
    obj.getClientNumbers = getClientNumbers
    obj.getClientNumbersAttributes = getClientNumbersAttributes
    obj.getActivatedBrokerages = getActivatedBrokerages
    obj.getActivatedBrokeragesAttributes = getActivatedBrokeragesAttributes
    obj.getClientBrokerages = getClientBrokerages
    obj.getClientBrokeragesAttributes = getClientBrokeragesAttributes
    obj.insertClientBrokerage = insertClientBrokerage
    obj.insertClientBrokerageAttributes = insertClientBrokerageAttributes
    obj.updateClientBrokerage = updateClientBrokerage
    obj.updateClientBrokerageAttributes = updateClientBrokerageAttributes
    obj.deleteClientBrokerages = deleteClientBrokerages
    obj.deleteClientBrokeragesAttributes = deleteClientBrokeragesAttributes
    obj.getTradingSystems = getTradingSystems
    obj.getTradingSystemsAttributes = getTradingSystemsAttributes
    obj.insertTradingSystem = insertTradingSystem
    obj.insertTradingSystemAttributes = insertTradingSystemAttributes
    obj.updateTradingSystem = updateTradingSystem
    obj.updateTradingSystemAttributes = updateTradingSystemAttributes
    obj.getSetups = getSetups
    obj.getSetupsAttributes = getSetupsAttributes
    obj.insertSetup = insertSetup
    obj.insertSetupAttributes = insertSetupAttributes
    obj.updateSetup = updateSetup
    obj.updateSetupAttributes = updateSetupAttributes
    obj.getInvestments = getInvestments
    obj.getInvestmentsAttributes = getInvestmentsAttributes
    obj.insertInvestment = insertInvestment
    obj.insertInvestmentAttributes = insertInvestmentAttributes
    obj.updateInvestment = updateInvestment
    obj.updateInvestmentAttributes = updateInvestmentAttributes
    obj.sendOrder = sendOrder
    obj.sendOrderAttributes = sendOrderAttributes
    obj.cancelOrder = cancelOrder
    obj.cancelOrderAttributes = cancelOrderAttributes
    obj.changeOrder = changeOrder
    obj.changeOrderAttributes = changeOrderAttributes
    obj.getOrders = getOrders
    obj.getOrdersAttributes = getOrdersAttributes
    obj.getNumberOfOrders = getNumberOfOrders
    obj.getNumberOfOrdersAttributes = getNumberOfOrdersAttributes
    obj.getOrdersEvents = getOrdersEvents
    obj.getOrdersEventsAttributes = getOrdersEventsAttributes
    obj.getNumberOfOrdersEvents = getNumberOfOrdersEvents
    obj.getNumberOfOrdersEventsAttributes = getNumberOfOrdersEventsAttributes
    obj.getOrderId = getOrderId
    obj.getOrderIdAttributes = getOrderIdAttributes
    obj.insertExternalOrder = insertExternalOrder
    obj.insertExternalOrderAttributes = insertExternalOrderAttributes
    obj.updateExternalOrder = updateExternalOrder
    obj.updateExternalOrderAttributes = updateExternalOrderAttributes
    obj.deleteExternalOrders = deleteExternalOrders
    obj.deleteExternalOrdersAttributes = deleteExternalOrdersAttributes
    obj.sendStopOrder = sendStopOrder
    obj.sendStopOrderAttributes = sendStopOrderAttributes
    obj.cancelStopOrder = cancelStopOrder
    obj.cancelStopOrderAttributes = cancelStopOrderAttributes
    obj.changeStopOrder = changeStopOrder
    obj.changeStopOrderAttributes = changeStopOrderAttributes
    obj.getStopOrders = getStopOrders
    obj.getStopOrdersAttributes = getStopOrdersAttributes
    obj.getNumberOfStopOrders = getNumberOfStopOrders
    obj.getNumberOfStopOrdersAttributes = getNumberOfStopOrdersAttributes
    obj.getStopOrdersEvents = getStopOrdersEvents
    obj.getStopOrdersEventsAttributes = getStopOrdersEventsAttributes
    obj.getNumberOfStopOrdersEvents = getNumberOfStopOrdersEvents
    obj.getNumberOfStopOrdersEventsAttributes = getNumberOfStopOrdersEventsAttributes
    obj.getStopOrderId = getStopOrderId
    obj.getStopOrderIdAttributes = getStopOrderIdAttributes
    obj.getTrades = getTrades
    obj.getTradesAttributes = getTradesAttributes
    obj.getNumberOfTrades = getNumberOfTrades
    obj.getNumberOfTradesAttributes = getNumberOfTradesAttributes
    obj.getReport = getReport
    obj.getReportAttributes = getReportAttributes
    obj.getDailyCumulativePerformance = getDailyCumulativePerformance
    obj.getDailyCumulativePerformanceAttributes = getDailyCumulativePerformanceAttributes
    obj.getDailyDrawdown = getDailyDrawdown
    obj.getDailyDrawdownAttributes = getDailyDrawdownAttributes
    obj.getPortfolio = getPortfolio
    obj.getPortfolioAttributes = getPortfolioAttributes
    obj.cancelAllPendingOrders = cancelAllPendingOrders
    obj.cancelAllPendingOrdersAttributes = cancelAllPendingOrdersAttributes
    obj.cancelAllPendingStopOrders = cancelAllPendingStopOrders
    obj.cancelAllPendingStopOrdersAttributes = cancelAllPendingStopOrdersAttributes
    obj.resetPortfolio = resetPortfolio
    obj.resetPortfolioAttributes = resetPortfolioAttributes
    obj.getAvailableLimits = getAvailableLimits
    obj.getAvailableLimitsAttributes = getAvailableLimitsAttributes
    obj.getFinancialTransactions = getFinancialTransactions
    obj.getFinancialTransactionsAttributes = getFinancialTransactionsAttributes
    obj.getNumberOfFinancialTransactions = getNumberOfFinancialTransactions
    obj.getNumberOfFinancialTransactionsAttributes = getNumberOfFinancialTransactionsAttributes
    obj.insertFinancialTransaction = insertFinancialTransaction
    obj.insertFinancialTransactionAttributes = insertFinancialTransactionAttributes
    obj.updateFinancialTransaction = updateFinancialTransaction
    obj.updateFinancialTransactionAttributes = updateFinancialTransactionAttributes
    obj.deleteFinancialTransactions = deleteFinancialTransactions
    obj.deleteFinancialTransactionsAttributes = deleteFinancialTransactionsAttributes
    obj.getIndicators = getIndicators
    obj.getIndicatorsAttributes = getIndicatorsAttributes
    obj.insertIndicator = insertIndicator
    obj.insertIndicatorAttributes = insertIndicatorAttributes


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


loginApiKeyAttributes = [
    "message"]


def loginApiKey(self, apiKey = None):
    message = ["login_api_key"]
    message += self.formatString("api_key", apiKey, optional=False)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = (response[0])
    return parsedResponse


checkPasswordAttributes = [
    "message"]


def checkPassword(self, s10iPassword = None):
    message = ["check_password"]
    message += self.formatString("s10i_password", s10iPassword, optional=False)
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
    "ip_used_to_sign_up",
    "registration_datetime",
    "plan",
    "has_customized_strategies",
    "is_active",
    "plan_expiration_date"]


def getClient(self, returnAttributes = None):
    message = ["get_client"]
    message += self.formatAttributes("return_attributes", returnAttributes, self.getClientAttributes)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = self.formatDictResponse(response[0:], returnAttributes, self.getClientAttributes)
    return parsedResponse


updateClientAttributes = [
    "message"]


def updateClient(self, s10iPassword = None, naturalPersonOrLegalPerson = None, nameOrCorporateName = None, gender = None, document = None, email = None, newS10iPassword = None, address = None, number = None, complement = None, neighborhood = None, postalCode = None, city = None, state = None, country = None, birthday = None, mainPhone = None, secondaryPhone = None, company = None):
    message = ["update_client"]
    message += self.formatString("s10i_password", s10iPassword, optional=False)
    message += self.formatBoolean("natural_person_or_legal_person", naturalPersonOrLegalPerson, optional=True)
    message += self.formatString("name_or_corporate_name", nameOrCorporateName, optional=True)
    message += self.formatString("gender", gender, optional=True)
    message += self.formatString("document", document, optional=True)
    message += self.formatString("email", email, optional=True)
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


getApiKeysAttributes = [
    "api_key"]


def getApiKeys(self, returnAttributes = None):
    message = ["get_api_keys"]
    message += self.formatAttributes("return_attributes", returnAttributes, self.getApiKeysAttributes)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = (response[0])
    return parsedResponse


insertApiKeyAttributes = [
    "message"]


def insertApiKey(self):
    message = ["insert_api_key"]
    response = self.smarttFunction(filter(None, message))
    parsedResponse = (response[0])
    return parsedResponse


deleteApiKeyAttributes = [
    "message"]


def deleteApiKey(self, apiKey = None):
    message = ["delete_api_key"]
    message += self.formatString("api_key", apiKey, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = (response[0])
    return parsedResponse


getClientNumbersAttributes = [
    "number_of_orders_executed_on_bovespa",
    "number_of_minis_traded_on_bmf",
    "number_of_contracts_traded_on_bmf"]


def getClientNumbers(self, brokerageId = None, investmentCode = None, initialDatetime = None, finalDatetime = None, returnAttributes = None):
    message = ["get_client_numbers"]
    message += self.formatInteger("brokerage_id", brokerageId, optional=True)
    message += self.formatString("investment_code", investmentCode, optional=True)
    message += self.formatDatetime("initial_datetime", initialDatetime, optional=True)
    message += self.formatDatetime("final_datetime", finalDatetime, optional=True)
    message += self.formatAttributes("return_attributes", returnAttributes, self.getClientNumbersAttributes)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = self.formatDictResponse(response[0:], returnAttributes, self.getClientNumbersAttributes)
    return parsedResponse


getActivatedBrokeragesAttributes = [
    "id",
    "name",
    "corporate_name"]


def getActivatedBrokerages(self, returnAttributes = None):
    message = ["get_activated_brokerages"]
    message += self.formatAttributes("return_attributes", returnAttributes, self.getActivatedBrokeragesAttributes)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = self.formatListOfDictsResponse(response[0:], returnAttributes, self.getActivatedBrokeragesAttributes)
    return parsedResponse


getClientBrokeragesAttributes = [
    "brokerage_id",
    "brokerage_office_id",
    "cblc_bovespa_code",
    "cblc_bmf_code",
    "insertion_datetime",
    "status",
    "approval_datetime"]


def getClientBrokerages(self, brokerageId = None, cblcBovespaCode = None, cblcBmfCode = None, status = None, returnAttributes = None):
    message = ["get_client_brokerages"]
    message += self.formatInteger("brokerage_id", brokerageId, optional=True)
    message += self.formatString("cblc_bovespa_code", cblcBovespaCode, optional=True)
    message += self.formatString("cblc_bmf_code", cblcBmfCode, optional=True)
    message += self.formatString("status", status, optional=True)
    message += self.formatAttributes("return_attributes", returnAttributes, self.getClientBrokeragesAttributes)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = self.formatListOfDictsResponse(response[0:], returnAttributes, self.getClientBrokeragesAttributes)
    return parsedResponse


insertClientBrokerageAttributes = [
    "message"]


def insertClientBrokerage(self, brokerageId = None, brokerageOfficeId = None, cblcBovespaCode = None, cblcBmfCode = None, status = None):
    message = ["insert_client_brokerage"]
    message += self.formatInteger("brokerage_id", brokerageId, optional=False)
    message += self.formatInteger("brokerage_office_id", brokerageOfficeId, optional=True)
    message += self.formatString("cblc_bovespa_code", cblcBovespaCode, optional=True)
    message += self.formatString("cblc_bmf_code", cblcBmfCode, optional=True)
    message += self.formatString("status", status, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = (response[0])
    return parsedResponse


updateClientBrokerageAttributes = [
    "message"]


def updateClientBrokerage(self, brokerageId = None, cblcBovespaCode = None, cblcBmfCode = None):
    message = ["update_client_brokerage"]
    message += self.formatInteger("brokerage_id", brokerageId, optional=False)
    message += self.formatString("cblc_bovespa_code", cblcBovespaCode, optional=True)
    message += self.formatString("cblc_bmf_code", cblcBmfCode, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = (response[0])
    return parsedResponse


deleteClientBrokeragesAttributes = [
    "message"]


def deleteClientBrokerages(self, brokerageId = None, cblcBovespaCode = None, cblcBmfCode = None, status = None):
    message = ["delete_client_brokerages"]
    message += self.formatInteger("brokerage_id", brokerageId, optional=True)
    message += self.formatString("cblc_bovespa_code", cblcBovespaCode, optional=True)
    message += self.formatString("cblc_bmf_code", cblcBmfCode, optional=True)
    message += self.formatString("status", status, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = (response[0])
    return parsedResponse


getTradingSystemsAttributes = [
    "code",
    "description"]


def getTradingSystems(self, code = None, returnAttributes = None):
    message = ["get_trading_systems"]
    message += self.formatString("code", code, optional=True)
    message += self.formatAttributes("return_attributes", returnAttributes, self.getTradingSystemsAttributes)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = self.formatListOfDictsResponse(response[0:], returnAttributes, self.getTradingSystemsAttributes)
    return parsedResponse


insertTradingSystemAttributes = [
    "message"]


def insertTradingSystem(self, code = None, description = None):
    message = ["insert_trading_system"]
    message += self.formatString("code", code, optional=False)
    message += self.formatString("description", description, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = (response[0])
    return parsedResponse


updateTradingSystemAttributes = [
    "message"]


def updateTradingSystem(self, code = None, newCode = None, description = None):
    message = ["update_trading_system"]
    message += self.formatString("code", code, optional=False)
    message += self.formatString("new_code", newCode, optional=True)
    message += self.formatString("description", description, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = (response[0])
    return parsedResponse


getSetupsAttributes = [
    "code",
    "description",
    "operational_limit",
    "spot_absolute_brokerage_tax",
    "spot_percentual_brokerage_tax",
    "option_absolute_brokerage_tax",
    "option_percentual_brokerage_tax",
    "ibov_contract_day_trade_brokerage_tax",
    "ibov_mini_day_trade_brokerage_tax",
    "dollar_contract_day_trade_brokerage_tax",
    "dollar_mini_day_trade_brokerage_tax",
    "other_absolute_brokerage_tax",
    "other_percentual_brokerage_tax",
    "position_trading_tax",
    "position_liquidation_tax",
    "position_register_tax",
    "position_other_taxes",
    "day_trade_trading_tax",
    "day_trade_liquidation_tax",
    "day_trade_register_tax",
    "day_trade_other_taxes",
    "iss_tax",
    "custody_tax"]


def getSetups(self, code = None, returnAttributes = None):
    message = ["get_setups"]
    message += self.formatString("code", code, optional=True)
    message += self.formatAttributes("return_attributes", returnAttributes, self.getSetupsAttributes)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = self.formatListOfDictsResponse(response[0:], returnAttributes, self.getSetupsAttributes)
    return parsedResponse


insertSetupAttributes = [
    "message"]


def insertSetup(self, code = None, description = None, operationalLimit = None, spotAbsoluteBrokerageTax = None, spotPercentualBrokerageTax = None, optionAbsoluteBrokerageTax = None, optionPercentualBrokerageTax = None, ibovContractDayTradeBrokerageTax = None, ibovMiniDayTradeBrokerageTax = None, dollarContractDayTradeBrokerageTax = None, dollarMiniDayTradeBrokerageTax = None, otherAbsoluteBrokerageTax = None, otherPercentualBrokerageTax = None, positionTradingTax = None, positionLiquidationTax = None, positionRegisterTax = None, positionOtherTaxes = None, dayTradeTradingTax = None, dayTradeLiquidationTax = None, dayTradeRegisterTax = None, dayTradeOtherTaxes = None, issTax = None, custodyTax = None):
    message = ["insert_setup"]
    message += self.formatString("code", code, optional=False)
    message += self.formatString("description", description, optional=True)
    message += self.formatString("operational_limit", operationalLimit, optional=False)
    message += self.formatDecimal2("spot_absolute_brokerage_tax", spotAbsoluteBrokerageTax, optional=True)
    message += self.formatDecimal6("spot_percentual_brokerage_tax", spotPercentualBrokerageTax, optional=True)
    message += self.formatDecimal2("option_absolute_brokerage_tax", optionAbsoluteBrokerageTax, optional=True)
    message += self.formatDecimal6("option_percentual_brokerage_tax", optionPercentualBrokerageTax, optional=True)
    message += self.formatDecimal2("ibov_contract_day_trade_brokerage_tax", ibovContractDayTradeBrokerageTax, optional=True)
    message += self.formatDecimal2("ibov_mini_day_trade_brokerage_tax", ibovMiniDayTradeBrokerageTax, optional=True)
    message += self.formatDecimal2("dollar_contract_day_trade_brokerage_tax", dollarContractDayTradeBrokerageTax, optional=True)
    message += self.formatDecimal2("dollar_mini_day_trade_brokerage_tax", dollarMiniDayTradeBrokerageTax, optional=True)
    message += self.formatDecimal2("other_absolute_brokerage_tax", otherAbsoluteBrokerageTax, optional=True)
    message += self.formatDecimal6("other_percentual_brokerage_tax", otherPercentualBrokerageTax, optional=True)
    message += self.formatDecimal6("position_trading_tax", positionTradingTax, optional=True)
    message += self.formatDecimal6("position_liquidation_tax", positionLiquidationTax, optional=True)
    message += self.formatDecimal2("position_register_tax", positionRegisterTax, optional=True)
    message += self.formatDecimal2("position_other_taxes", positionOtherTaxes, optional=True)
    message += self.formatDecimal6("day_trade_trading_tax", dayTradeTradingTax, optional=True)
    message += self.formatDecimal6("day_trade_liquidation_tax", dayTradeLiquidationTax, optional=True)
    message += self.formatDecimal6("day_trade_register_tax", dayTradeRegisterTax, optional=True)
    message += self.formatDecimal2("day_trade_other_taxes", dayTradeOtherTaxes, optional=True)
    message += self.formatDecimal6("iss_tax", issTax, optional=True)
    message += self.formatDecimal2("custody_tax", custodyTax, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = (response[0])
    return parsedResponse


updateSetupAttributes = [
    "message"]


def updateSetup(self, code = None, newCode = None, description = None, operationalLimit = None, spotAbsoluteBrokerageTax = None, spotPercentualBrokerageTax = None, optionAbsoluteBrokerageTax = None, optionPercentualBrokerageTax = None, ibovContractDayTradeBrokerageTax = None, ibovMiniDayTradeBrokerageTax = None, dollarContractDayTradeBrokerageTax = None, dollarMiniDayTradeBrokerageTax = None, otherAbsoluteBrokerageTax = None, otherPercentualBrokerageTax = None, positionTradingTax = None, positionLiquidationTax = None, positionRegisterTax = None, positionOtherTaxes = None, dayTradeTradingTax = None, dayTradeLiquidationTax = None, dayTradeRegisterTax = None, dayTradeOtherTaxes = None, issTax = None, custodyTax = None):
    message = ["update_setup"]
    message += self.formatString("code", code, optional=False)
    message += self.formatString("new_code", newCode, optional=True)
    message += self.formatString("description", description, optional=True)
    message += self.formatString("operational_limit", operationalLimit, optional=True)
    message += self.formatDecimal2("spot_absolute_brokerage_tax", spotAbsoluteBrokerageTax, optional=True)
    message += self.formatDecimal6("spot_percentual_brokerage_tax", spotPercentualBrokerageTax, optional=True)
    message += self.formatDecimal2("option_absolute_brokerage_tax", optionAbsoluteBrokerageTax, optional=True)
    message += self.formatDecimal6("option_percentual_brokerage_tax", optionPercentualBrokerageTax, optional=True)
    message += self.formatDecimal2("ibov_contract_day_trade_brokerage_tax", ibovContractDayTradeBrokerageTax, optional=True)
    message += self.formatDecimal2("ibov_mini_day_trade_brokerage_tax", ibovMiniDayTradeBrokerageTax, optional=True)
    message += self.formatDecimal2("dollar_contract_day_trade_brokerage_tax", dollarContractDayTradeBrokerageTax, optional=True)
    message += self.formatDecimal2("dollar_mini_day_trade_brokerage_tax", dollarMiniDayTradeBrokerageTax, optional=True)
    message += self.formatDecimal2("other_absolute_brokerage_tax", otherAbsoluteBrokerageTax, optional=True)
    message += self.formatDecimal6("other_percentual_brokerage_tax", otherPercentualBrokerageTax, optional=True)
    message += self.formatDecimal6("position_trading_tax", positionTradingTax, optional=True)
    message += self.formatDecimal6("position_liquidation_tax", positionLiquidationTax, optional=True)
    message += self.formatDecimal2("position_register_tax", positionRegisterTax, optional=True)
    message += self.formatDecimal2("position_other_taxes", positionOtherTaxes, optional=True)
    message += self.formatDecimal6("day_trade_trading_tax", dayTradeTradingTax, optional=True)
    message += self.formatDecimal6("day_trade_liquidation_tax", dayTradeLiquidationTax, optional=True)
    message += self.formatDecimal6("day_trade_register_tax", dayTradeRegisterTax, optional=True)
    message += self.formatDecimal2("day_trade_other_taxes", dayTradeOtherTaxes, optional=True)
    message += self.formatDecimal6("iss_tax", issTax, optional=True)
    message += self.formatDecimal2("custody_tax", custodyTax, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = (response[0])
    return parsedResponse


getInvestmentsAttributes = [
    "code",
    "description",
    "brokerage_id",
    "trading_system_code",
    "setup_code",
    "is_real",
    "initial_capital",
    "initial_datetime",
    "final_datetime"]


def getInvestments(self, brokerageId = None, code = None, returnAttributes = None):
    message = ["get_investments"]
    message += self.formatInteger("brokerage_id", brokerageId, optional=True)
    message += self.formatString("code", code, optional=True)
    message += self.formatAttributes("return_attributes", returnAttributes, self.getInvestmentsAttributes)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = self.formatListOfDictsResponse(response[0:], returnAttributes, self.getInvestmentsAttributes)
    return parsedResponse


insertInvestmentAttributes = [
    "message"]


def insertInvestment(self, brokerageId = None, tradingSystemCode = None, setupCode = None, code = None, description = None, initialCapital = None, initialDatetime = None, finalDatetime = None):
    message = ["insert_investment"]
    message += self.formatInteger("brokerage_id", brokerageId, optional=False)
    message += self.formatString("trading_system_code", tradingSystemCode, optional=False)
    message += self.formatString("setup_code", setupCode, optional=False)
    message += self.formatString("code", code, optional=False)
    message += self.formatString("description", description, optional=True)
    message += self.formatString("initial_capital", initialCapital, optional=False)
    message += self.formatDatetime("initial_datetime", initialDatetime, optional=True)
    message += self.formatDatetime("final_datetime", finalDatetime, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = (response[0])
    return parsedResponse


updateInvestmentAttributes = [
    "message"]


def updateInvestment(self, brokerageId = None, code = None, tradingSystemCode = None, setupCode = None, description = None, initialCapital = None, initialDatetime = None, finalDatetime = None):
    message = ["update_investment"]
    message += self.formatInteger("brokerage_id", brokerageId, optional=False)
    message += self.formatString("code", code, optional=False)
    message += self.formatString("trading_system_code", tradingSystemCode, optional=True)
    message += self.formatString("setup_code", setupCode, optional=True)
    message += self.formatString("description", description, optional=True)
    message += self.formatString("initial_capital", initialCapital, optional=True)
    message += self.formatDatetime("initial_datetime", initialDatetime, optional=True)
    message += self.formatDatetime("final_datetime", finalDatetime, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = (response[0])
    return parsedResponse


sendOrderAttributes = [
    "order_id"]


def sendOrder(self, brokerageId = None, investmentCode = None, orderType = None, marketName = None, stockCode = None, numberOfStocks = None, isMarketOrder = None, price = None, validityType = None, validity = None, entryExitOrReversal = None, reason = None, ipClientParamsSaved = None, ipClientStrategyStart = None, strategyId = None):
    message = ["send_order"]
    message += self.formatInteger("brokerage_id", brokerageId, optional=False)
    message += self.formatString("investment_code", investmentCode, optional=False)
    message += self.formatBoolean("order_type", orderType, optional=False)
    message += self.formatString("market_name", marketName, optional=False)
    message += self.formatString("stock_code", stockCode, optional=False)
    message += self.formatInteger("number_of_stocks", numberOfStocks, optional=False)
    message += self.formatBoolean("is_market_order", isMarketOrder, optional=True)
    message += self.formatDecimal2("price", price, optional=True)
    message += self.formatString("validity_type", validityType, optional=True)
    message += self.formatDate("validity", validity, optional=True)
    message += self.formatString("entry_exit_or_reversal", entryExitOrReversal, optional=True)
    message += self.formatString("reason", reason, optional=True)
    message += self.formatString("ip_client_params_saved", ipClientParamsSaved, optional=True)
    message += self.formatString("ip_client_strategy_start", ipClientStrategyStart, optional=True)
    message += self.formatString("strategy_id", strategyId, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = int(response[1])
    return parsedResponse


cancelOrderAttributes = [
    "order_id"]


def cancelOrder(self, orderId = None, reason = None, ipClientParamsSaved = None, ipClientStrategyStart = None, strategyId = None):
    message = ["cancel_order"]
    message += self.formatInteger("order_id", orderId, optional=False)
    message += self.formatString("reason", reason, optional=True)
    message += self.formatString("ip_client_params_saved", ipClientParamsSaved, optional=True)
    message += self.formatString("ip_client_strategy_start", ipClientStrategyStart, optional=True)
    message += self.formatString("strategy_id", strategyId, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = int(response[1])
    return parsedResponse


changeOrderAttributes = [
    "order_id"]


def changeOrder(self, orderId = None, newNumberOfStocks = None, newPrice = None, reason = None, ipClientParamsSaved = None, ipClientStrategyStart = None, strategyId = None):
    message = ["change_order"]
    message += self.formatInteger("order_id", orderId, optional=False)
    message += self.formatInteger("new_number_of_stocks", newNumberOfStocks, optional=True)
    message += self.formatDecimal2("new_price", newPrice, optional=True)
    message += self.formatString("reason", reason, optional=True)
    message += self.formatString("ip_client_params_saved", ipClientParamsSaved, optional=True)
    message += self.formatString("ip_client_strategy_start", ipClientStrategyStart, optional=True)
    message += self.formatString("strategy_id", strategyId, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = int(response[1])
    return parsedResponse


getOrdersAttributes = [
    "order_id",
    "order_id_in_brokerage",
    "brokerage_id",
    "investment_code",
    "is_real",
    "order_type",
    "market_name",
    "stock_code",
    "datetime",
    "number_of_stocks",
    "nominal_price",
    "financial_volume",
    "validity_type",
    "validity",
    "number_of_traded_stocks",
    "average_nominal_price",
    "status",
    "brokerage_tax_cost",
    "iss_tax_cost",
    "sent_by_reset_portfolio",
    "sent_by_insert_external_order",
    "triggered_stop_order_id",
    "entry_exit_or_reversal",
    "absolute_average_simple_profit",
    "percentual_average_simple_profit",
    "gross_profit"]


def getOrders(self, orderId = None, brokerageId = None, investmentCode = None, initialDatetime = None, finalDatetime = None, marketName = None, stockCode = None, status = None, includeExternalOrders = None, offset = None, limit = None, returnAttributes = None):
    message = ["get_orders"]
    message += self.formatInteger("order_id", orderId, optional=True)
    message += self.formatInteger("brokerage_id", brokerageId, optional=True)
    message += self.formatString("investment_code", investmentCode, optional=True)
    message += self.formatDatetime("initial_datetime", initialDatetime, optional=True)
    message += self.formatDatetime("final_datetime", finalDatetime, optional=True)
    message += self.formatString("market_name", marketName, optional=True)
    message += self.formatString("stock_code", stockCode, optional=True)
    message += self.formatString("status", status, optional=True)
    message += self.formatBoolean("include_external_orders", includeExternalOrders, optional=True)
    message += self.formatInteger("offset", offset, optional=True)
    message += self.formatInteger("limit", limit, optional=True)
    message += self.formatAttributes("return_attributes", returnAttributes, self.getOrdersAttributes)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = self.formatListOfDictsResponse(response[0:], returnAttributes, self.getOrdersAttributes)
    return parsedResponse


getNumberOfOrdersAttributes = [
    "number_of_orders"]


def getNumberOfOrders(self, orderId = None, brokerageId = None, investmentCode = None, initialDatetime = None, finalDatetime = None, marketName = None, stockCode = None, status = None, offset = None, limit = None):
    message = ["get_number_of_orders"]
    message += self.formatInteger("order_id", orderId, optional=True)
    message += self.formatInteger("brokerage_id", brokerageId, optional=True)
    message += self.formatString("investment_code", investmentCode, optional=True)
    message += self.formatDatetime("initial_datetime", initialDatetime, optional=True)
    message += self.formatDatetime("final_datetime", finalDatetime, optional=True)
    message += self.formatString("market_name", marketName, optional=True)
    message += self.formatString("stock_code", stockCode, optional=True)
    message += self.formatString("status", status, optional=True)
    message += self.formatInteger("offset", offset, optional=True)
    message += self.formatInteger("limit", limit, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = int(response[0])
    return parsedResponse


getOrdersEventsAttributes = [
    "order_id",
    "brokerage_id",
    "investment_code",
    "number_of_events",
    "datetime",
    "event_type",
    "description",
    "reason"]


def getOrdersEvents(self, orderId = None, brokerageId = None, investmentCode = None, initialDatetime = None, finalDatetime = None, eventType = None, offset = None, limit = None, returnAttributes = None):
    message = ["get_orders_events"]
    message += self.formatInteger("order_id", orderId, optional=True)
    message += self.formatInteger("brokerage_id", brokerageId, optional=True)
    message += self.formatString("investment_code", investmentCode, optional=True)
    message += self.formatDatetime("initial_datetime", initialDatetime, optional=True)
    message += self.formatDatetime("final_datetime", finalDatetime, optional=True)
    message += self.formatString("event_type", eventType, optional=True)
    message += self.formatInteger("offset", offset, optional=True)
    message += self.formatInteger("limit", limit, optional=True)
    message += self.formatAttributes("return_attributes", returnAttributes, self.getOrdersEventsAttributes)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = self.formatListOfDictsResponse(response[0:], returnAttributes, self.getOrdersEventsAttributes)
    return parsedResponse


getNumberOfOrdersEventsAttributes = [
    "number_of_orders_events"]


def getNumberOfOrdersEvents(self, orderId = None, brokerageId = None, investmentCode = None, initialDatetime = None, finalDatetime = None, eventType = None, offset = None, limit = None):
    message = ["get_number_of_orders_events"]
    message += self.formatInteger("order_id", orderId, optional=True)
    message += self.formatInteger("brokerage_id", brokerageId, optional=True)
    message += self.formatString("investment_code", investmentCode, optional=True)
    message += self.formatDatetime("initial_datetime", initialDatetime, optional=True)
    message += self.formatDatetime("final_datetime", finalDatetime, optional=True)
    message += self.formatString("event_type", eventType, optional=True)
    message += self.formatInteger("offset", offset, optional=True)
    message += self.formatInteger("limit", limit, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = int(response[0])
    return parsedResponse


getOrderIdAttributes = [
    "order_id"]


def getOrderId(self, orderIdInBrokerage = None, brokerageId = None, marketName = None, stockCode = None, date = None):
    message = ["get_order_id"]
    message += self.formatString("order_id_in_brokerage", orderIdInBrokerage, optional=False)
    message += self.formatInteger("brokerage_id", brokerageId, optional=False)
    message += self.formatString("market_name", marketName, optional=False)
    message += self.formatString("stock_code", stockCode, optional=False)
    message += self.formatDate("date", date, optional=False)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = int(response[0])
    return parsedResponse


insertExternalOrderAttributes = [
    "order_id"]


def insertExternalOrder(self, brokerageId = None, investmentCode = None, orderType = None, marketName = None, stockCode = None, numberOfStocks = None, price = None, entryExitOrReversal = None, reason = None, datetime = None):
    message = ["insert_external_order"]
    message += self.formatInteger("brokerage_id", brokerageId, optional=False)
    message += self.formatString("investment_code", investmentCode, optional=False)
    message += self.formatBoolean("order_type", orderType, optional=False)
    message += self.formatString("market_name", marketName, optional=False)
    message += self.formatString("stock_code", stockCode, optional=False)
    message += self.formatInteger("number_of_stocks", numberOfStocks, optional=False)
    message += self.formatDecimal2("price", price, optional=False)
    message += self.formatString("entry_exit_or_reversal", entryExitOrReversal, optional=True)
    message += self.formatString("reason", reason, optional=True)
    message += self.formatDatetime("datetime", datetime, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = int(response[1])
    return parsedResponse


updateExternalOrderAttributes = [
    "order_id"]


def updateExternalOrder(self, orderId = None, brokerageId = None, investmentCode = None, orderType = None, marketName = None, stockCode = None, numberOfStocks = None, price = None, entryExitOrReversal = None, reason = None, datetime = None):
    message = ["update_external_order"]
    message += self.formatInteger("order_id", orderId, optional=False)
    message += self.formatInteger("brokerage_id", brokerageId, optional=True)
    message += self.formatString("investment_code", investmentCode, optional=True)
    message += self.formatBoolean("order_type", orderType, optional=True)
    message += self.formatString("market_name", marketName, optional=True)
    message += self.formatString("stock_code", stockCode, optional=True)
    message += self.formatInteger("number_of_stocks", numberOfStocks, optional=True)
    message += self.formatDecimal2("price", price, optional=True)
    message += self.formatString("entry_exit_or_reversal", entryExitOrReversal, optional=True)
    message += self.formatString("reason", reason, optional=True)
    message += self.formatDatetime("datetime", datetime, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = int(response[1])
    return parsedResponse


deleteExternalOrdersAttributes = [
    "message"]


def deleteExternalOrders(self, orderId = None, brokerageId = None, investmentCode = None, initialDatetime = None, finalDatetime = None, marketName = None, stockCode = None, status = None, offset = None, limit = None):
    message = ["delete_external_orders"]
    message += self.formatInteger("order_id", orderId, optional=True)
    message += self.formatInteger("brokerage_id", brokerageId, optional=True)
    message += self.formatString("investment_code", investmentCode, optional=True)
    message += self.formatDatetime("initial_datetime", initialDatetime, optional=True)
    message += self.formatDatetime("final_datetime", finalDatetime, optional=True)
    message += self.formatString("market_name", marketName, optional=True)
    message += self.formatString("stock_code", stockCode, optional=True)
    message += self.formatString("status", status, optional=True)
    message += self.formatInteger("offset", offset, optional=True)
    message += self.formatInteger("limit", limit, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = (response[0])
    return parsedResponse


sendStopOrderAttributes = [
    "stop_order_id"]


def sendStopOrder(self, brokerageId = None, investmentCode = None, orderType = None, stopOrderType = None, marketName = None, stockCode = None, numberOfStocks = None, stopPrice = None, isMarketOrder = None, limitPrice = None, validity = None, entryExitOrReversal = None, reason = None, ipClientParamsSaved = None, ipClientStrategyStart = None, strategyId = None):
    message = ["send_stop_order"]
    message += self.formatInteger("brokerage_id", brokerageId, optional=False)
    message += self.formatString("investment_code", investmentCode, optional=False)
    message += self.formatBoolean("order_type", orderType, optional=False)
    message += self.formatBoolean("stop_order_type", stopOrderType, optional=False)
    message += self.formatString("market_name", marketName, optional=False)
    message += self.formatString("stock_code", stockCode, optional=False)
    message += self.formatInteger("number_of_stocks", numberOfStocks, optional=False)
    message += self.formatDecimal2("stop_price", stopPrice, optional=False)
    message += self.formatBoolean("is_market_order", isMarketOrder, optional=True)
    message += self.formatDecimal2("limit_price", limitPrice, optional=True)
    message += self.formatDate("validity", validity, optional=False)
    message += self.formatString("entry_exit_or_reversal", entryExitOrReversal, optional=True)
    message += self.formatString("reason", reason, optional=True)
    message += self.formatString("ip_client_params_saved", ipClientParamsSaved, optional=True)
    message += self.formatString("ip_client_strategy_start", ipClientStrategyStart, optional=True)
    message += self.formatString("strategy_id", strategyId, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = int(response[1])
    return parsedResponse


cancelStopOrderAttributes = [
    "stop_order_id"]


def cancelStopOrder(self, stopOrderId = None, reason = None, ipClientParamsSaved = None, ipClientStrategyStart = None, strategyId = None):
    message = ["cancel_stop_order"]
    message += self.formatInteger("stop_order_id", stopOrderId, optional=False)
    message += self.formatString("reason", reason, optional=True)
    message += self.formatString("ip_client_params_saved", ipClientParamsSaved, optional=True)
    message += self.formatString("ip_client_strategy_start", ipClientStrategyStart, optional=True)
    message += self.formatString("strategy_id", strategyId, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = int(response[1])
    return parsedResponse


changeStopOrderAttributes = [
    "stop_order_id"]


def changeStopOrder(self, stopOrderId = None, newNumberOfStocks = None, newStopPrice = None, newLimitPrice = None, reason = None, ipClientParamsSaved = None, ipClientStrategyStart = None, strategyId = None):
    message = ["change_stop_order"]
    message += self.formatInteger("stop_order_id", stopOrderId, optional=False)
    message += self.formatInteger("new_number_of_stocks", newNumberOfStocks, optional=True)
    message += self.formatDecimal2("new_stop_price", newStopPrice, optional=True)
    message += self.formatDecimal2("new_limit_price", newLimitPrice, optional=True)
    message += self.formatString("reason", reason, optional=True)
    message += self.formatString("ip_client_params_saved", ipClientParamsSaved, optional=True)
    message += self.formatString("ip_client_strategy_start", ipClientStrategyStart, optional=True)
    message += self.formatString("strategy_id", strategyId, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = int(response[1])
    return parsedResponse


getStopOrdersAttributes = [
    "stop_order_id",
    "stop_order_id_in_brokerage",
    "brokerage_id",
    "investment_code",
    "is_real",
    "order_type",
    "stop_order_type",
    "market_name",
    "stock_code",
    "datetime",
    "number_of_stocks",
    "stop_price",
    "limit_price",
    "validity",
    "status",
    "entry_exit_or_reversal",
    "sent_order_id"]


def getStopOrders(self, stopOrderId = None, brokerageId = None, investmentCode = None, initialDatetime = None, finalDatetime = None, marketName = None, stockCode = None, status = None, offset = None, limit = None, returnAttributes = None):
    message = ["get_stop_orders"]
    message += self.formatInteger("stop_order_id", stopOrderId, optional=True)
    message += self.formatInteger("brokerage_id", brokerageId, optional=True)
    message += self.formatString("investment_code", investmentCode, optional=True)
    message += self.formatDatetime("initial_datetime", initialDatetime, optional=True)
    message += self.formatDatetime("final_datetime", finalDatetime, optional=True)
    message += self.formatString("market_name", marketName, optional=True)
    message += self.formatString("stock_code", stockCode, optional=True)
    message += self.formatString("status", status, optional=True)
    message += self.formatInteger("offset", offset, optional=True)
    message += self.formatInteger("limit", limit, optional=True)
    message += self.formatAttributes("return_attributes", returnAttributes, self.getStopOrdersAttributes)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = self.formatListOfDictsResponse(response[0:], returnAttributes, self.getStopOrdersAttributes)
    return parsedResponse


getNumberOfStopOrdersAttributes = [
    "number_of_stop_orders"]


def getNumberOfStopOrders(self, stopOrderId = None, brokerageId = None, investmentCode = None, initialDatetime = None, finalDatetime = None, marketName = None, stockCode = None, status = None, offset = None, limit = None):
    message = ["get_number_of_stop_orders"]
    message += self.formatInteger("stop_order_id", stopOrderId, optional=True)
    message += self.formatInteger("brokerage_id", brokerageId, optional=True)
    message += self.formatString("investment_code", investmentCode, optional=True)
    message += self.formatDatetime("initial_datetime", initialDatetime, optional=True)
    message += self.formatDatetime("final_datetime", finalDatetime, optional=True)
    message += self.formatString("market_name", marketName, optional=True)
    message += self.formatString("stock_code", stockCode, optional=True)
    message += self.formatString("status", status, optional=True)
    message += self.formatInteger("offset", offset, optional=True)
    message += self.formatInteger("limit", limit, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = int(response[0])
    return parsedResponse


getStopOrdersEventsAttributes = [
    "stop_order_id",
    "brokerage_id",
    "investment_code",
    "number_of_events",
    "datetime",
    "event_type",
    "description",
    "reason"]


def getStopOrdersEvents(self, stopOrderId = None, brokerageId = None, investmentCode = None, initialDatetime = None, finalDatetime = None, eventType = None, offset = None, limit = None, returnAttributes = None):
    message = ["get_stop_orders_events"]
    message += self.formatInteger("stop_order_id", stopOrderId, optional=True)
    message += self.formatInteger("brokerage_id", brokerageId, optional=True)
    message += self.formatString("investment_code", investmentCode, optional=True)
    message += self.formatDatetime("initial_datetime", initialDatetime, optional=True)
    message += self.formatDatetime("final_datetime", finalDatetime, optional=True)
    message += self.formatString("event_type", eventType, optional=True)
    message += self.formatInteger("offset", offset, optional=True)
    message += self.formatInteger("limit", limit, optional=True)
    message += self.formatAttributes("return_attributes", returnAttributes, self.getStopOrdersEventsAttributes)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = self.formatListOfDictsResponse(response[0:], returnAttributes, self.getStopOrdersEventsAttributes)
    return parsedResponse


getNumberOfStopOrdersEventsAttributes = [
    "number_of_stop_orders_events"]


def getNumberOfStopOrdersEvents(self, stopOrderId = None, brokerageId = None, investmentCode = None, initialDatetime = None, finalDatetime = None, eventType = None, offset = None, limit = None):
    message = ["get_number_of_stop_orders_events"]
    message += self.formatInteger("stop_order_id", stopOrderId, optional=True)
    message += self.formatInteger("brokerage_id", brokerageId, optional=True)
    message += self.formatString("investment_code", investmentCode, optional=True)
    message += self.formatDatetime("initial_datetime", initialDatetime, optional=True)
    message += self.formatDatetime("final_datetime", finalDatetime, optional=True)
    message += self.formatString("event_type", eventType, optional=True)
    message += self.formatInteger("offset", offset, optional=True)
    message += self.formatInteger("limit", limit, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = int(response[0])
    return parsedResponse


getStopOrderIdAttributes = [
    "stop_order_id"]


def getStopOrderId(self, stopOrderIdInBrokerage = None, brokerageId = None, marketName = None, stockCode = None, date = None):
    message = ["get_stop_order_id"]
    message += self.formatString("stop_order_id_in_brokerage", stopOrderIdInBrokerage, optional=False)
    message += self.formatInteger("brokerage_id", brokerageId, optional=False)
    message += self.formatString("market_name", marketName, optional=False)
    message += self.formatString("stock_code", stockCode, optional=False)
    message += self.formatDate("date", date, optional=False)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = int(response[0])
    return parsedResponse


getTradesAttributes = [
    "trade_id",
    "trade_id_in_brokerage",
    "order_id",
    "brokerage_id",
    "investment_code",
    "is_real",
    "trade_type",
    "market_name",
    "stock_code",
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


def getTrades(self, orderId = None, brokerageId = None, investmentCode = None, initialDatetime = None, finalDatetime = None, marketName = None, stockCode = None, offset = None, limit = None, returnAttributes = None):
    message = ["get_trades"]
    message += self.formatInteger("order_id", orderId, optional=True)
    message += self.formatInteger("brokerage_id", brokerageId, optional=True)
    message += self.formatString("investment_code", investmentCode, optional=True)
    message += self.formatDatetime("initial_datetime", initialDatetime, optional=True)
    message += self.formatDatetime("final_datetime", finalDatetime, optional=True)
    message += self.formatString("market_name", marketName, optional=True)
    message += self.formatString("stock_code", stockCode, optional=True)
    message += self.formatInteger("offset", offset, optional=True)
    message += self.formatInteger("limit", limit, optional=True)
    message += self.formatAttributes("return_attributes", returnAttributes, self.getTradesAttributes)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = self.formatListOfDictsResponse(response[0:], returnAttributes, self.getTradesAttributes)
    return parsedResponse


getNumberOfTradesAttributes = [
    "number_of_trades"]


def getNumberOfTrades(self, orderId = None, brokerageId = None, investmentCode = None, initialDatetime = None, finalDatetime = None, marketName = None, stockCode = None, offset = None, limit = None):
    message = ["get_number_of_trades"]
    message += self.formatInteger("order_id", orderId, optional=True)
    message += self.formatInteger("brokerage_id", brokerageId, optional=True)
    message += self.formatString("investment_code", investmentCode, optional=True)
    message += self.formatDatetime("initial_datetime", initialDatetime, optional=True)
    message += self.formatDatetime("final_datetime", finalDatetime, optional=True)
    message += self.formatString("market_name", marketName, optional=True)
    message += self.formatString("stock_code", stockCode, optional=True)
    message += self.formatInteger("offset", offset, optional=True)
    message += self.formatInteger("limit", limit, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = int(response[0])
    return parsedResponse


getReportAttributes = [
    "brokerage_id",
    "investment_code",
    "setup_code",
    "initial_datetime",
    "final_datetime",
    "number_of_days",
    "total_contributions",
    "total_withdraws",
    "initial_capital",
    "operational_limit",
    "balance",
    "equity",
    "taxes_and_operational_costs",
    "today_gross_result",
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


def getReport(self, brokerageId = None, investmentCode = None, initialDatetime = None, finalDatetime = None, returnAttributes = None):
    message = ["get_report"]
    message += self.formatInteger("brokerage_id", brokerageId, optional=False)
    message += self.formatString("investment_code", investmentCode, optional=False)
    message += self.formatDatetime("initial_datetime", initialDatetime, optional=True)
    message += self.formatDatetime("final_datetime", finalDatetime, optional=True)
    message += self.formatAttributes("return_attributes", returnAttributes, self.getReportAttributes)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = self.formatDictResponse(response[0:], returnAttributes, self.getReportAttributes)
    return parsedResponse


getDailyCumulativePerformanceAttributes = [
    "brokerage_id",
    "investment_code",
    "daily_cumulative_performance"]


def getDailyCumulativePerformance(self, brokerageId = None, investmentCode = None, initialDatetime = None, finalDatetime = None):
    message = ["get_daily_cumulative_performance"]
    message += self.formatInteger("brokerage_id", brokerageId, optional=False)
    message += self.formatString("investment_code", investmentCode, optional=False)
    message += self.formatDatetime("initial_datetime", initialDatetime, optional=True)
    message += self.formatDatetime("final_datetime", finalDatetime, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = self.formatDictResponse(response[0:], [], self.getDailyCumulativePerformanceAttributes)
    return parsedResponse


getDailyDrawdownAttributes = [
    "brokerage_id",
    "investment_code",
    "daily_drawdown"]


def getDailyDrawdown(self, brokerageId = None, investmentCode = None, initialDatetime = None, finalDatetime = None):
    message = ["get_daily_drawdown"]
    message += self.formatInteger("brokerage_id", brokerageId, optional=False)
    message += self.formatString("investment_code", investmentCode, optional=False)
    message += self.formatDatetime("initial_datetime", initialDatetime, optional=True)
    message += self.formatDatetime("final_datetime", finalDatetime, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = self.formatDictResponse(response[0:], [], self.getDailyDrawdownAttributes)
    return parsedResponse


getPortfolioAttributes = [
    "market_name",
    "stock_code",
    "position_type",
    "number_of_stocks",
    "average_price",
    "financial_volume",
    "variation",
    "result",
    "is_market_open",
    "has_pending_reset_orders"]


def getPortfolio(self, brokerageId = None, investmentCode = None, initialDatetime = None, finalDatetime = None, returnAttributes = None):
    message = ["get_portfolio"]
    message += self.formatInteger("brokerage_id", brokerageId, optional=False)
    message += self.formatString("investment_code", investmentCode, optional=False)
    message += self.formatDatetime("initial_datetime", initialDatetime, optional=True)
    message += self.formatDatetime("final_datetime", finalDatetime, optional=True)
    message += self.formatAttributes("return_attributes", returnAttributes, self.getPortfolioAttributes)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = self.formatListOfDictsResponse(response[2:], returnAttributes, self.getPortfolioAttributes)
    return parsedResponse


cancelAllPendingOrdersAttributes = [
    "order_ids"]


def cancelAllPendingOrders(self, brokerageId = None, investmentCode = None, marketName = None, stockCode = None, ipClientParamsSaved = None, ipClientStrategyStart = None, strategyId = None):
    message = ["cancel_all_pending_orders"]
    message += self.formatInteger("brokerage_id", brokerageId, optional=False)
    message += self.formatString("investment_code", investmentCode, optional=False)
    message += self.formatString("market_name", marketName, optional=True)
    message += self.formatString("stock_code", stockCode, optional=True)
    message += self.formatString("ip_client_params_saved", ipClientParamsSaved, optional=True)
    message += self.formatString("ip_client_strategy_start", ipClientStrategyStart, optional=True)
    message += self.formatString("strategy_id", strategyId, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = int(response[0])
    return parsedResponse


cancelAllPendingStopOrdersAttributes = [
    "stop_order_ids"]


def cancelAllPendingStopOrders(self, brokerageId = None, investmentCode = None, marketName = None, stockCode = None, ipClientParamsSaved = None, ipClientStrategyStart = None, strategyId = None):
    message = ["cancel_all_pending_stop_orders"]
    message += self.formatInteger("brokerage_id", brokerageId, optional=False)
    message += self.formatString("investment_code", investmentCode, optional=False)
    message += self.formatString("market_name", marketName, optional=True)
    message += self.formatString("stock_code", stockCode, optional=True)
    message += self.formatString("ip_client_params_saved", ipClientParamsSaved, optional=True)
    message += self.formatString("ip_client_strategy_start", ipClientStrategyStart, optional=True)
    message += self.formatString("strategy_id", strategyId, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = int(response[0])
    return parsedResponse


resetPortfolioAttributes = [
    "order_ids"]


def resetPortfolio(self, brokerageId = None, investmentCode = None, marketName = None, stockCode = None, ipClientParamsSaved = None, ipClientStrategyStart = None, strategyId = None):
    message = ["reset_portfolio"]
    message += self.formatInteger("brokerage_id", brokerageId, optional=False)
    message += self.formatString("investment_code", investmentCode, optional=False)
    message += self.formatString("market_name", marketName, optional=True)
    message += self.formatString("stock_code", stockCode, optional=True)
    message += self.formatString("ip_client_params_saved", ipClientParamsSaved, optional=True)
    message += self.formatString("ip_client_strategy_start", ipClientStrategyStart, optional=True)
    message += self.formatString("strategy_id", strategyId, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = int(response[0])
    return parsedResponse


getAvailableLimitsAttributes = [
    "spot",
    "option",
    "margin"]


def getAvailableLimits(self, brokerageId = None, investmentCode = None, returnAttributes = None):
    message = ["get_available_limits"]
    message += self.formatInteger("brokerage_id", brokerageId, optional=True)
    message += self.formatString("investment_code", investmentCode, optional=True)
    message += self.formatAttributes("return_attributes", returnAttributes, self.getAvailableLimitsAttributes)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = self.formatListOfDictsResponse(response[0:], returnAttributes, self.getAvailableLimitsAttributes)
    return parsedResponse


getFinancialTransactionsAttributes = [
    "financial_transaction_id",
    "brokerage_id",
    "investment_code",
    "datetime",
    "contribution_or_withdrawal",
    "value",
    "operational_tax_cost",
    "description"]


def getFinancialTransactions(self, financialTransactionId = None, brokerageId = None, investmentCode = None, offset = None, limit = None, returnAttributes = None):
    message = ["get_financial_transactions"]
    message += self.formatString("financial_transaction_id", financialTransactionId, optional=True)
    message += self.formatInteger("brokerage_id", brokerageId, optional=True)
    message += self.formatString("investment_code", investmentCode, optional=True)
    message += self.formatInteger("offset", offset, optional=True)
    message += self.formatInteger("limit", limit, optional=True)
    message += self.formatAttributes("return_attributes", returnAttributes, self.getFinancialTransactionsAttributes)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = self.formatListOfDictsResponse(response[0:], returnAttributes, self.getFinancialTransactionsAttributes)
    return parsedResponse


getNumberOfFinancialTransactionsAttributes = [
    "number_of_financial_transactions"]


def getNumberOfFinancialTransactions(self, financialTransactionId = None, brokerageId = None, investmentCode = None, offset = None, limit = None):
    message = ["get_number_of_financial_transactions"]
    message += self.formatString("financial_transaction_id", financialTransactionId, optional=True)
    message += self.formatInteger("brokerage_id", brokerageId, optional=True)
    message += self.formatString("investment_code", investmentCode, optional=True)
    message += self.formatInteger("offset", offset, optional=True)
    message += self.formatInteger("limit", limit, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = int(response[0])
    return parsedResponse


insertFinancialTransactionAttributes = [
    "message"]


def insertFinancialTransaction(self, brokerageId = None, investmentCode = None, datetime = None, contributionOrWithdrawal = None, value = None, operationalTaxCost = None, description = None):
    message = ["insert_financial_transaction"]
    message += self.formatInteger("brokerage_id", brokerageId, optional=False)
    message += self.formatString("investment_code", investmentCode, optional=False)
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


def updateFinancialTransaction(self, financialTransactionId = None, brokerageId = None, investmentCode = None, datetime = None, contributionOrWithdrawal = None, value = None, operationalTaxCost = None, description = None):
    message = ["update_financial_transaction"]
    message += self.formatString("financial_transaction_id", financialTransactionId, optional=False)
    message += self.formatInteger("brokerage_id", brokerageId, optional=True)
    message += self.formatString("investment_code", investmentCode, optional=True)
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


def deleteFinancialTransactions(self, financialTransactionId = None, brokerageId = None, investmentCode = None):
    message = ["delete_financial_transactions"]
    message += self.formatString("financial_transaction_id", financialTransactionId, optional=True)
    message += self.formatInteger("brokerage_id", brokerageId, optional=True)
    message += self.formatString("investment_code", investmentCode, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = (response[0])
    return parsedResponse


getIndicatorsAttributes = [
    "code",
    "description",
    "market_name",
    "stock_code",
    "market_name2",
    "stock_code2",
    "market_name3",
    "stock_code3",
    "datetime",
    "datetime2",
    "datetime3",
    "value",
    "value2",
    "value3",
    "value4",
    "value5"]


def getIndicators(self, code = None, marketName = None, stockCode = None, marketName2 = None, stockCode2 = None, marketName3 = None, stockCode3 = None, maximumNumberOfIndicators = None, initialDatetime = None, finalDatetime = None, initialDatetime2 = None, finalDatetime2 = None, initialDatetime3 = None, finalDatetime3 = None, returnAttributes = None):
    message = ["get_indicators"]
    message += self.formatString("code", code, optional=True)
    message += self.formatString("market_name", marketName, optional=True)
    message += self.formatString("stock_code", stockCode, optional=True)
    message += self.formatString("market_name2", marketName2, optional=True)
    message += self.formatString("stock_code2", stockCode2, optional=True)
    message += self.formatString("market_name3", marketName3, optional=True)
    message += self.formatString("stock_code3", stockCode3, optional=True)
    message += self.formatInteger("maximum_number_of_indicators", maximumNumberOfIndicators, optional=True)
    message += self.formatDatetime("initial_datetime", initialDatetime, optional=True)
    message += self.formatDatetime("final_datetime", finalDatetime, optional=True)
    message += self.formatDatetime("initial_datetime2", initialDatetime2, optional=True)
    message += self.formatDatetime("final_datetime2", finalDatetime2, optional=True)
    message += self.formatDatetime("initial_datetime3", initialDatetime3, optional=True)
    message += self.formatDatetime("final_datetime3", finalDatetime3, optional=True)
    message += self.formatAttributes("return_attributes", returnAttributes, self.getIndicatorsAttributes)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = self.formatListOfDictsResponse(response[0:], returnAttributes, self.getIndicatorsAttributes)
    return parsedResponse


insertIndicatorAttributes = [
    "message"]


def insertIndicator(self, code = None, description = None, marketName = None, stockCode = None, marketName2 = None, stockCode2 = None, marketName3 = None, stockCode3 = None, datetime = None, datetime2 = None, datetime3 = None, value = None, value2 = None, value3 = None, value4 = None, value5 = None):
    message = ["insert_indicator"]
    message += self.formatString("code", code, optional=False)
    message += self.formatString("description", description, optional=True)
    message += self.formatString("market_name", marketName, optional=False)
    message += self.formatString("stock_code", stockCode, optional=False)
    message += self.formatString("market_name2", marketName2, optional=True)
    message += self.formatString("stock_code2", stockCode2, optional=True)
    message += self.formatString("market_name3", marketName3, optional=True)
    message += self.formatString("stock_code3", stockCode3, optional=True)
    message += self.formatDatetime("datetime", datetime, optional=False)
    message += self.formatDatetime("datetime2", datetime2, optional=True)
    message += self.formatDatetime("datetime3", datetime3, optional=True)
    message += self.formatDecimal6("value", value, optional=False)
    message += self.formatDecimal6("value2", value2, optional=True)
    message += self.formatDecimal6("value3", value3, optional=True)
    message += self.formatDecimal6("value4", value4, optional=True)
    message += self.formatDecimal6("value5", value5, optional=True)
    response = self.smarttFunction(filter(None, message))
    parsedResponse = (response[0])
    return parsedResponse

