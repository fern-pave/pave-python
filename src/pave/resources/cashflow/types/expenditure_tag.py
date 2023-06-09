# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ExpenditureTag(str, enum.Enum):
    AUTO_INSURANCE = "Auto_Insurance"
    AUTO_LOAN_BNPL = "Auto Loan BNPL"
    BILL = "Bill"
    CASH_ADVANCE = "Cash Advance"
    CHILD_SUPPORT = "Child Support"
    CREDIT_BUILDER = "Credit Builder"
    CREDIT_CARD = "Credit Card"
    CREDIT_CARD_CASH_ADVANCE = "Credit Card Cash Advance"
    DEBT_COLLECTION = "Debt Collection"
    EDUCATION = "Education"
    ELECTRIC = "Electric"
    GAS = "Gas"
    GYM = "Gym"
    HOA_FEE = "HOA Fee"
    HR = "HR"
    HEALTH = "Health"
    HEALTH_INSURANCE = "Health Insurance"
    INSURANCE = "Insurance"
    LEASE = "Lease"
    LEASE_TO_OWN = "Lease to Own"
    LOAN = "Loan"
    MORTGAGE = "Mortgage"
    RENT = "Rent"
    RENTERS_INSURANCE = "Renters Insurance"
    SAA_S = "Saas"
    STREAMING = "Streaming"
    STUDENT_LOAN = "Student Loan"
    SUBSCRIPTION = "Subscription"
    TAX = "Tax"
    TELECOM = "Telecom"
    TITLE_LOAN = "Title Loan"
    UTILITY = "Utility"
    WASTE = "Waste"
    WATER = "Water"

    def visit(
        self,
        auto_insurance: typing.Callable[[], T_Result],
        auto_loan_bnpl: typing.Callable[[], T_Result],
        bill: typing.Callable[[], T_Result],
        cash_advance: typing.Callable[[], T_Result],
        child_support: typing.Callable[[], T_Result],
        credit_builder: typing.Callable[[], T_Result],
        credit_card: typing.Callable[[], T_Result],
        credit_card_cash_advance: typing.Callable[[], T_Result],
        debt_collection: typing.Callable[[], T_Result],
        education: typing.Callable[[], T_Result],
        electric: typing.Callable[[], T_Result],
        gas: typing.Callable[[], T_Result],
        gym: typing.Callable[[], T_Result],
        hoa_fee: typing.Callable[[], T_Result],
        hr: typing.Callable[[], T_Result],
        health: typing.Callable[[], T_Result],
        health_insurance: typing.Callable[[], T_Result],
        insurance: typing.Callable[[], T_Result],
        lease: typing.Callable[[], T_Result],
        lease_to_own: typing.Callable[[], T_Result],
        loan: typing.Callable[[], T_Result],
        mortgage: typing.Callable[[], T_Result],
        rent: typing.Callable[[], T_Result],
        renters_insurance: typing.Callable[[], T_Result],
        saa_s: typing.Callable[[], T_Result],
        streaming: typing.Callable[[], T_Result],
        student_loan: typing.Callable[[], T_Result],
        subscription: typing.Callable[[], T_Result],
        tax: typing.Callable[[], T_Result],
        telecom: typing.Callable[[], T_Result],
        title_loan: typing.Callable[[], T_Result],
        utility: typing.Callable[[], T_Result],
        waste: typing.Callable[[], T_Result],
        water: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ExpenditureTag.AUTO_INSURANCE:
            return auto_insurance()
        if self is ExpenditureTag.AUTO_LOAN_BNPL:
            return auto_loan_bnpl()
        if self is ExpenditureTag.BILL:
            return bill()
        if self is ExpenditureTag.CASH_ADVANCE:
            return cash_advance()
        if self is ExpenditureTag.CHILD_SUPPORT:
            return child_support()
        if self is ExpenditureTag.CREDIT_BUILDER:
            return credit_builder()
        if self is ExpenditureTag.CREDIT_CARD:
            return credit_card()
        if self is ExpenditureTag.CREDIT_CARD_CASH_ADVANCE:
            return credit_card_cash_advance()
        if self is ExpenditureTag.DEBT_COLLECTION:
            return debt_collection()
        if self is ExpenditureTag.EDUCATION:
            return education()
        if self is ExpenditureTag.ELECTRIC:
            return electric()
        if self is ExpenditureTag.GAS:
            return gas()
        if self is ExpenditureTag.GYM:
            return gym()
        if self is ExpenditureTag.HOA_FEE:
            return hoa_fee()
        if self is ExpenditureTag.HR:
            return hr()
        if self is ExpenditureTag.HEALTH:
            return health()
        if self is ExpenditureTag.HEALTH_INSURANCE:
            return health_insurance()
        if self is ExpenditureTag.INSURANCE:
            return insurance()
        if self is ExpenditureTag.LEASE:
            return lease()
        if self is ExpenditureTag.LEASE_TO_OWN:
            return lease_to_own()
        if self is ExpenditureTag.LOAN:
            return loan()
        if self is ExpenditureTag.MORTGAGE:
            return mortgage()
        if self is ExpenditureTag.RENT:
            return rent()
        if self is ExpenditureTag.RENTERS_INSURANCE:
            return renters_insurance()
        if self is ExpenditureTag.SAA_S:
            return saa_s()
        if self is ExpenditureTag.STREAMING:
            return streaming()
        if self is ExpenditureTag.STUDENT_LOAN:
            return student_loan()
        if self is ExpenditureTag.SUBSCRIPTION:
            return subscription()
        if self is ExpenditureTag.TAX:
            return tax()
        if self is ExpenditureTag.TELECOM:
            return telecom()
        if self is ExpenditureTag.TITLE_LOAN:
            return title_loan()
        if self is ExpenditureTag.UTILITY:
            return utility()
        if self is ExpenditureTag.WASTE:
            return waste()
        if self is ExpenditureTag.WATER:
            return water()
