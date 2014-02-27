
### Standard library imports
from cmd import Cmd
import getpass
import re

### Local imports
from smartt_client import SmarttClient
from smartt_client import SmarttClientException


HEADERCOLORCODE = "\033[95m"
BLUECOLORCODE = "\033[94m"
GREENCOLORCODE = "\033[92m"
YELLOWCOLORCODE = "\033[93m"
REDCOLORCODE = "\033[91m"
ENDOFCOLORCODE = "\033[0m"


### SmarttConsole class - a console/shell application which interfaces with
### the Smartt server
class SmarttConsole(Cmd):
    ##########################################################################
    ### Configurations ###
    ######################
    prompt = "smartt> "

    def preloop(self):
        self.smartt_client = SmarttClient()
    ##########################################################################

    def splitArgs(self, arg):
        extracted_values = re.findall('("([^"]*)")|(\S+)', arg)
        values = [(value[2] if value[0] == "" else value[1])
                  for value in extracted_values]
        return values

    def printValue(self, value):
        if isinstance(value, dict):
            for (name, value) in value.iteritems():
                print "%s: %s" % (name, value)
        elif isinstance(value, list):
            index = 0
            for element in value:
                print str(index) + ":"
                self.printValue(element)
                index += 1
                print ""
        else:
            print value

    def printResponse(self, response):
        print BLUECOLORCODE

        self.printValue(response)

        print ENDOFCOLORCODE

    ##########################################################################
    ### Smartt Functions ###
    ########################
    def do_login(self, arg):
        splitted_args = self.splitArgs(arg)
        if len(splitted_args) == 0:
            print "Login not specified"
            return

        username = splitted_args[0]

        print "Logging in as '%s'" % username
        password = getpass.getpass()

        self.printResponse(self.smartt_client.login(username, password))

    def do_logged(self, arg):
        self.printResponse(self.smartt_client.logged())

    def do_logout(self, arg):
        self.printResponse(self.smartt_client.logout())

    def do_get_client(self, arg):
        attributes = self.splitArgs(arg)
        self.printResponse(self.smartt_client.getClient(attributes))

    def do_get_time(self, arg):
        self.printResponse(self.smartt_client.getTime())

    def do_get_stock(self, arg):
        splitted_args = self.splitArgs(arg)

        stock_code = splitted_args[0]
        market_name = splitted_args[1]
        attributes = splitted_args[2:]

        self.printResponse(
            self.smartt_client.getStock(stock_code, market_name, attributes))

    def do_send_order(self, arg):
        splitted_args = self.splitArgs(arg)

        print "Not implemented"

    def do_cancel_order(self, arg):
        splitted_args = self.splitArgs(arg)

        order_id = splitted_args[0]

        self.printResponse(self.smartt_client.cancelOrder(order_id))

    def do_change_order(self, arg):
        splitted_args = self.splitArgs(arg)

        print "Not implemented"

    def do_send_stop_order(self, arg):
        splitted_args = self.splitArgs(arg)

        print "Not implemented"

    def do_cancel_stop_order(self, arg):
        splitted_args = self.splitArgs(arg)

        stop_order_id = splitted_args[0]

        self.printResponse(self.smartt_client.cancelStopOrder(stop_order_id))

    def do_get_orders(self, arg):
        splitted_args = self.splitArgs(arg)

        self.printResponse(self.smartt_client.getOrders())

    def do_get_orders_events(self, arg):
        splitted_args = self.splitArgs(arg)

        self.printResponse(self.smartt_client.getOrdersEvents())

    def do_get_stop_orders(self, arg):
        splitted_args = self.splitArgs(arg)

        self.printResponse(self.smartt_client.getStopOrders())

    def do_get_stop_orders_events(self, arg):
        splitted_args = self.splitArgs(arg)

        self.printResponse(self.smartt_client.getStopOrdersEvents())

    def do_get_trades(self, arg):
        splitted_args = self.splitArgs(arg)

        self.printResponse(self.smartt_client.getTrades())

    def do_get_portfolio(self, arg):
        splitted_args = self.splitArgs(arg)

        self.printResponse(self.smartt_client.getPortfolio())

    def do_get_available_limits(self, arg):
        splitted_args = self.splitArgs(arg)

        self.printResponse(self.smartt_client.getAvailableLimits())
    ##########################################################################

    ##########################################################################
    ### Lower level Smartt messaging ###
    ####################################
    def do_message(self, arg):
        message = self.splitArgs(arg)
        self.smartt_client.sendMessage(message)
        print self.smartt_client.receiveMessage()

    def do_query(self, arg):
        self.do_message(arg)

    def do_rawmessage(self, arg):
        self.smartt_client.sendRawMessage(arg)
        print self.smartt_client.receiveRawMessage()

    def do_rawquery(self, arg):
        self.do_rawmessage(arg)

    ##########################################################################
    ### Quitting commands ###
    #########################
    def do_EOF(self, arg):
        print ""
        return True

    def do_quit(self, arg):
        return True

    def do_exit(self, arg):
        return True
    ##########################################################################

    ##########################################################################
    ### Wrappers and overloaded functions ###
    #########################################
    def onecmd(self, line):
        ### Wraps commands and catches exceptions
        try:
            return Cmd.onecmd(self, line)
        except SmarttClientException as e:
            print REDCOLORCODE + str(e) + ENDOFCOLORCODE
            return False

    def emptyline(self):
        ### Empty lines do nothing - default is to run last command
        pass

    def default(self, line):
        ### Default message - unknown command
        print(REDCOLORCODE
              + "Unknown command: '{0}' - you sure you typed that right?"
              .format(line) + ENDOFCOLORCODE)
    ##########################################################################

##############################################################################


##############################################################################
### Main function - application starting point ###
##################################################
def main():
    smartt_console = SmarttConsole()
    smartt_console.cmdloop("Welcome to the Smartt Client Console!")
##############################################################################


### If trying to run from here, you're welcome!
if __name__ == "__main__":
    main()
