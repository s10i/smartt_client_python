
# Standard library imports
import socket
import ssl
import select

# Local imports
from smartt_simple_protocol import SmarttSimpleProtocol


class SmarttClientException(BaseException):
    pass


##############################################################################
### SmarttClient class - encapsulates connection and communication with Smartt
### server, preseting a nice and easy to use API to the user
class SmarttClient(object):

    ####################
    # Attributes lists #
    ####################
    getClientAttributesNames = [
        "natural_person_or_legal_person",
        "name_or_corporate_name",
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
        "registration_datetime"
    ]

    getStockAttributesNames = [
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
        "expiration_date"
    ]

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
        "price",
        "financial_volume",
        "validity_type",
        "validity",
        "number_of_traded_stocks",
        "average_nominal_price",
        "status",
        "absolute_brokerage_tax_cost",
        "percentual_brokerage_tax_cost",
        "iss_tax_cost"
    ]

    getOrdersEventsAttributes = [
        "order_id",
        "investment_code",
        "brokerage_id",
        "number_of_events",
        "datetime",
        "event_type",
        "description"
    ]

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
        "financial_volume",
        "validity",
        "valid_after_market",
        "trailing_activation_price",
        "adjustment_price",
        "status",
        "sent_order_id"
    ]

    getStopOrdersEventsAttributes = [
        "stop_order_id",
        "investment_code",
        "brokerage_id",
        "number_of_events",
        "datetime",
        "event_type",
        "description"
    ]

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
        "price",
        "financial_volume",
        "trading_tax_cost",
        "liquidation_tax_cost",
        "register_tax_cost",
        "income_tax_cost",
        "withholding_income_tax_cost",
        "other_taxes_cost"
    ]

    getPortfolioAttributes = [
        "stock_code",
        "position_type",
        "number_of_stocks",
        "average_price",
        "financial_volume"
    ]

    getAvailableLimitsAttributes = [
        "spot_limit",
        "option_limit",
        "margin_limit"
    ]
    ##########################################################################

    #############
    # API Enums #
    #############
    marketNames = [
        "Bovespa",
        "BMF"
    ]

    orderStatuses = [
        "canceled",
        "executed",
        "hung",
        "hung_cancellable",
        "hung_pending",
        "partially_canceled",
        "partially_executed",
        "partially_executed_cancellable",
        "rejected",
        "expired"
    ]

    ordersEventsTypes = [
        "order_sent",
        "order_canceled",
        "order_changed",
        "order_executed",
        "order_expired"
    ]

    stopOrderStatuses = [
        "canceled_by_client",
        "canceled_expired_option",
        "canceled_not_allowed_market",
        "canceled_not_enough_balance",
        "canceled_not_positioned",
        "canceled_order_limit_exceeded",
        "hung",
        "sent",
        "expired"
    ]

    stopOrdersEventsTypes = [
        "stop_order_sent",
        "stop_order_canceled",
        "stop_order_triggered",
        "stop_order_expired"
    ]

    validityTypes = [
        "HJ",
        "DE",
        "AC"
    ]
    ##########################################################################

    ### Init function - connects to the server (possibly initializing the SSL
    ### protocol as well) and setups the protocol handler
    def __init__(self, host="smartt.s10i.com.br", port=5060, use_ssl=True,
                 print_raw_messages=False):
        self.host = host
        self.port = port
        self.smartt_socket = socket.create_connection((self.host, self.port))
        if use_ssl:
            self.smartt_socket = ssl.wrap_socket(self.smartt_socket)

        self.protocol = SmarttSimpleProtocol(self.smartt_socket.recv,
                                             self.smartt_socket.send,
                                             print_raw_messages)

    # Generic Wrapper for all Smartt functions - sends the function message
    # and returns the response (next message from the server)
    def smarttFunction(self, message):
        self.protocol.send(message)
        response = self.protocol.receive()

        if len(response) > 0 and response[0] == "ERROR":
            if len(response) != 2:
                print "STRANGE! Error response doesn't have 2 values: %s" % \
                      str(response)
            raise SmarttClientException(response[0] + ": " + response[1])

        return response

    ##########################################################################
    ### Generic messages (list of strings) handling ###
    ###################################################
    def sendMessage(self, message):
        self.protocol.send(message)

    def receiveMessage(self):
        return self.protocol.receive()
    ##########################################################################

    ##########################################################################
    ### Raw messages handling ###
    #############################
    def sendRawMessage(self, message):
        self.smartt_socket.send(message)

    # Reads everything available until timing out
    def receiveRawMessage(self):
        # Read in chunks of at most 4K - the magical number for recv calls :)
        receive_size = 4096
        # Timeout of half a second - just enough so that a continuous
        # transmission from the server isn't missed (totally arbitrary choice)
        select_timeout = 0.5

        # Has to receive something, so just use the blocking function
        data = self.smartt_socket.recv(receive_size)

        # Wait and check for data, if available, read, if times out, stops
        while len(select.select([self.smartt_socket], [], [],
                                select_timeout)[0]) > 0:
            data += self.smartt_socket.recv(receive_size)

        return data
    ##########################################################################

    ##########################################################################
    ### Helper functions ###
    ########################
    def checkAttributes(self, attributes, possibleValues):
        for attribute in attributes:
            if attribute not in possibleValues:
                raise SmarttClientException("Invalid attribute: " + attribute)

    def formatString(self, name, value, optional=True):
        if value is None:
            if not optional:
                raise SmarttClientException("Non-optional parameter is NULL: "
                                            + name)
            else:
                return []

        return [("%s=%s" % (name, value))]

    def formatInteger(self, name, value, optional=True):
        formattedValue = (str(int(value))
                          if value is not None else None)
        return self.formatString(name, formattedValue, optional)

    def formatFloat(self, name, value, optional=True):
        formattedValue = (("%.2f" % float(value))
                          if value is not None else None)
        return self.formatString(name, formattedValue, optional)

    def formatDatetime(self, name, value, optional=True):
        formattedValue = (value.strftime("%Y-%m-%d %H:%M:%S")
                          if value is not None else None)
        return self.formatString(name, formattedValue, optional)

    def formatDate(self, name, value, optional=True):
        formattedValue = (value.strftime("%Y-%m-%d")
                          if value is not None else None)
        return self.formatString(name, formattedValue, optional)

    def formatBoolean(self, name, value, falseAndTrueValues, optional=True):
        formattedValue = None
        if value == 0 or value is False or value == falseAndTrueValues[0]:
            formattedValue = "0"
        elif value == 1 or value is True or value == falseAndTrueValues[1]:
            formattedValue = "1"
        else:
            raise SmarttClientException("Invalid boolean value '" + name +
                                        "': " + value)

        return self.formatString(name, formattedValue, optional)

    def formatEnum(self, name, value, enumValues, optional=True):
        if value is not None and value not in enumValues:
            raise SmarttClientException("Invalid '" + name +
                                        "' parameter value: " + value)

        return self.formatString(name, value, optional)

    def formatDictResponse(self, values, attributes, defaultAttributes=[]):
        if len(attributes) == 0:
            attributes = defaultAttributes

        return dict(zip(attributes, values))

    def formatListOfDictsResponse(self, values, attributes, defaultAttributes):
        if len(attributes) == 0:
            attributes = defaultAttributes

        k = len(attributes)
        return [self.formatDictResponse(values[i:i + k], attributes) for i in
                xrange(0, len(values), k)]

    ##########################################################################
    ### Smartt functions ###
    ########################
    def login(self, username, password):
        message = ["login"]

        message += self.formatString("s10i_login", username, False)
        message += self.formatString("s10i_password", password, False)

        return self.smarttFunction(message)[0]

    def logged(self):
        message = ["logged"]

        return self.smarttFunction(message)[0]

    def logout(self):
        message = ["logout"]

        return self.smarttFunction(message)[0]

    def getClient(self, attributes):
        self.checkAttributes(attributes, self.getClientAttributesNames)

        message = ["get_client"]

        message += attributes

        clientValues = self.smarttFunction(message)

        return self.formatDictResponse(clientValues, attributes,
                                       self.getClientAttributesNames)

    def getTime(self):
        message = ["get_time"]

        return self.smarttFunction(message)[0]

    def getStock(self, stock_code, market_name=None, attributes=[]):
        self.checkAttributes(attributes, self.getStockAttributesNames)

        message = ["get_stock"]

        message += self.formatString("stock_code", stock_code)
        message += self.formatEnum("market_name", market_name,
                                   self.marketNames)
        message += attributes

        stockValues = self.smarttFunction(message)

        return self.formatDictResponse(stockValues, attributes,
                                       self.getStockAttributesNames)

    def sendOrder(self, investment_code=None, brokerage_id=None,
                  order_type=None, stock_code=None, number_of_stocks=None,
                  price=None, market_name=None, validity_type=None,
                  validity=None):
        message = ["send_order"]

        message += self.formatString("investment_code", investment_code, False)
        message += self.formatInteger("brokerage_id", brokerage_id, True)
        message += self.formatBoolean("order_type", order_type,
                                      ["buy", "sell"], False)
        message += self.formatString("stock_code", stock_code, False)
        message += self.formatEnum("market_name", market_name,
                                   self.marketNames)
        message += self.formatInteger("number_of_stocks", number_of_stocks,
                                      False)
        message += self.formatFloat("price", price, False)
        message += self.formatEnum("validity_type", validity_type,
                                   self.validityTypes)

        if validity_type == "DE":
            message += self.formatDate("validity", validity, False)

        response = self.smarttFunction(message)

        return ("Order sent: %s" % response[1])

    def cancelOrder(self, order_id):
        message = ["cancel_order"]

        message += self.formatInteger("order_id", order_id, False)

        response = self.smarttFunction(message)

        return ("Order canceled: %s" % response[1])

    def changeOrder(self, order_id, new_number_of_stocks=None, new_price=None):
        message = ["change_order"]

        message += self.formatInteger("order_id", order_id, False)
        message += self.formatInteger("new_number_of_stocks",
                                      new_number_of_stocks)
        message += self.formatFloat("new_price", new_price)

        response = self.smarttFunction(message)

        return ("Order modified: %s" % response[1])

    def sendStopOrder(self, investment_code, brokerage_id,
                      order_type, stop_order_type,
                      stock_code, number_of_stocks, stop_price, limit_price,
                      validity, valid_after_market,
                      market_name=None, trailing_activation_price=None,
                      adjustment_price=None):
        message = ["send_stop_order"]

        message += self.formatString("investment_code", investment_code, False)
        message += self.formatInteger("brokerage_id", brokerage_id)
        message += self.formatBoolean("order_type", order_type,
                                      ["buy", "sell"], False)
        message += self.formatBoolean("stop_order_type", stop_order_type,
                                      ["loss", "gain"], False)
        message += self.formatString("stock_code", stock_code, False)
        message += self.formatEnum("market_name", market_name,
                                   self.marketNames)
        message += self.formatInteger("number_of_stocks", number_of_stocks,
                                      False)
        message += self.formatFloat("stop_price", stop_price, False)
        message += self.formatFloat("limit_price", limit_price, False)
        message += self.formatDate("validity", validity, False)
        message += self.formatBoolean("valid_after_market", valid_after_market,
                                      ["no", "yes"], False)

        response = self.smarttFunction(message)

        return ("Stop order sent: %s" % response[1])

    def cancelStopOrder(self, stop_order_id):
        message = ["cancel_stop_order"]

        message += self.formatInteger("stop_order_id", stop_order_id)

        response = self.smarttFunction(message)

        return ("Stop order canceled: %s" % response[1])

    def getOrders(self, order_id=None, investment_code=None, brokerage_id=None,
                  initial_datetime=None, final_datetime=None, status=None,
                  attributes=[]):
        self.checkAttributes(attributes, self.getOrdersAttributes)

        message = ["get_orders"]

        message += self.formatInteger("order_id", order_id)
        message += self.formatString("investment_code", investment_code)
        message += self.formatInteger("brokerage_id", brokerage_id)
        message += self.formatDatetime("initial_datetime", initial_datetime)
        message += self.formatDatetime("final_datetime", final_datetime)
        message += self.formatEnum("status", status, self.orderStatuses)
        message += attributes

        values = self.smarttFunction(message)

        return self.formatListOfDictsResponse(values, attributes,
                                              self.getOrdersAttributes)

    def getOrdersEvents(self, order_id=None, investment_code=None,
                        brokerage_id=None,
                        initial_datetime=None, final_datetime=None,
                        event_type=None, attributes=[]):
        self.checkAttributes(attributes, self.getOrdersEventsAttributes)

        message = ["get_orders_events"]

        message += self.formatInteger("order_id", order_id)
        message += self.formatString("investment_code", investment_code)
        message += self.formatInteger("brokerage_id", brokerage_id)
        message += self.formatDatetime("initial_datetime", initial_datetime)
        message += self.formatDatetime("final_datetime", final_datetime)
        message += self.formatEnum("event_type", event_type,
                                   self.ordersEventsTypes)
        message += attributes

        values = self.smarttFunction(message)

        return self.formatListOfDictsResponse(values, attributes,
                                              self.getOrdersEventsAttributes)

    def getStopOrders(self, stop_order_id=None, investment_code=None,
                      brokerage_id=None,
                      initial_datetime=None, final_datetime=None, status=None,
                      attributes=[]):
        self.checkAttributes(attributes, self.getStopOrdersAttributes)

        message = ["get_stop_orders"]

        message += self.formatInteger("stop_order_id", stop_order_id)
        message += self.formatString("investment_code", investment_code)
        message += self.formatInteger("brokerage_id", brokerage_id)
        message += self.formatDatetime("initial_datetime", initial_datetime)
        message += self.formatDatetime("final_datetime", final_datetime)
        message += self.formatEnum("status", status, self.stopOrderStatuses)
        message += attributes

        values = self.smarttFunction(message)

        return self.formatListOfDictsResponse(values, attributes,
                                              self.getStopOrdersAttributes)

    def getStopOrdersEvents(self, stop_order_id=None, investment_code=None,
                            brokerage_id=None,
                            initial_datetime=None, final_datetime=None,
                            event_type=None, attributes=[]):
        self.checkAttributes(attributes, self.getStopOrdersEventsAttributes)

        message = ["get_stop_orders_events"]

        message += self.formatInteger("stop_order_id", stop_order_id)
        message += self.formatString("investment_code", investment_code)
        message += self.formatInteger("brokerage_id", brokerage_id)
        message += self.formatDatetime("initial_datetime", initial_datetime)
        message += self.formatDatetime("final_datetime", final_datetime)
        message += self.formatEnum("event_type", event_type,
                                   self.stopOrdersEventsTypes)
        message += attributes

        values = self.smarttFunction(message)

        return self.formatListOfDictsResponse(values, attributes,
                                              self.
                                              getStopOrdersEventsAttributes)

    def getTrades(self, order_id=None, investment_code=None, brokerage_id=None,
                  initial_datetime=None, final_datetime=None, attributes=[]):
        self.checkAttributes(attributes, self.getTradesAttributes)

        message = ["get_trades"]

        message += self.formatInteger("order_id", order_id)
        message += self.formatString("investment_code", investment_code)
        message += self.formatInteger("brokerage_id", brokerage_id)
        message += self.formatDatetime("initial_datetime", initial_datetime)
        message += self.formatDatetime("final_datetime", final_datetime)
        message += attributes

        values = self.smarttFunction(message)

        return self.formatListOfDictsResponse(values, attributes,
                                              self.getTradesAttributes)

    def getPortfolio(self, investment_code=None, brokerage_id=None,
                     attributes=[]):
        self.checkAttributes(attributes, self.getPortfolioAttributes)

        message = ["get_portfolio"]

        message += self.formatString("investment_code", investment_code, False)
        message += self.formatInteger("brokerage_id", brokerage_id)
        message += attributes

        values = self.smarttFunction(message)

        return {
            "investment_code": values[0],
            "brokerage_id": int(values[1]),
            "portfolio": self.formatListOfDictsResponse(
                             values[2:],
                             attributes,
                             self.getPortfolioAttributes
                         )
        }

    def getAvailableLimits(self, investment_code=None, brokerage_id=None,
                           attributes=[]):
        self.checkAttributes(attributes, self.getAvailableLimitsAttributes)

        message = ["get_available_limits"]

        message += self.formatString("investment_code", investment_code)
        message += self.formatInteger("brokerage_id", brokerage_id)
        message += attributes

        values = self.smarttFunction(message)

        return self.formatListOfDictsResponse(values, attributes,
                                              self.
                                              getAvailableLimitsAttributes)
    ##########################################################################

##############################################################################
