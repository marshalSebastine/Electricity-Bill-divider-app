class Bill():
        """
    This object contains data about the total bill amount to be payed by the flat owners
    in a specific period of time
    """

        def __init__(self,amount,period):
            self.amount=amount
            self.period=period


class FlatMate():
        """
    Represents one of the person who lives in apartment for a number of days
    and he pays for the bill on the basis on number of days he spent in flat at 
    given period.
    """

        def __init__(self,name,in_days):
            self.name=name
            self.in_days=in_days
        def amount_topay(self,bill,flatmate):
            return(round((self.in_days/(self.in_days+flatmate.in_days))*bill.amount,2))