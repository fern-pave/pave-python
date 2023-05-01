# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
import uuid

import pydantic

from ....core.datetime_utils import serialize_datetime
from .expenditure_tag import ExpenditureTag
from .necessity_level import NecessityLevel
from .normalized_frequency import NormalizedFrequency
from .transaction import Transaction


class RecurringExpenditure(pydantic.BaseModel):
    normalized_merchant_name: str = pydantic.Field(description=("Merchant name cleaned and normalized by Pave.\n"))
    merchant_uuid: uuid.UUID = pydantic.Field(
        description=("Unique identifier of the merchant for the given Recurring Expenditure.\n")
    )
    logo: str = pydantic.Field(description=("A link to the merchant's logo. null if no logo is available.\n"))
    last_amount: float = pydantic.Field(
        description=("Monetary value of the most recent occurrence of the expenditure.\n")
    )
    last_description: str = pydantic.Field(
        description=("Description of the most recent transaction as provided by the data source.\n")
    )
    last_date: dt.date = pydantic.Field(description=("Date of the most recent occurence of the expenditure.\n"))
    avg_amount: float = pydantic.Field(
        description=("Mean monetary value of the transactions for the recurring expenditure.\n")
    )
    iso_currency_code: str = pydantic.Field(description=("ISO4217 currency code. For example USD, GBP, etc.\n"))
    count: int = pydantic.Field(
        description=("Number of transactions in the given date range for the recurring expenditure.\n")
    )
    avg_period_days: int = pydantic.Field(
        description=("Mean number of days between occurrences of the recurring expenditure.\n")
    )
    normalized_frequency: NormalizedFrequency = pydantic.Field(
        description=("Normalized cadence of transactions for the recurring expenditure.\n")
    )
    next_amount: float = pydantic.Field(
        description=("Predicted amount of the next occurrence of the recurring expenditure.\n")
    )
    next_date: dt.date = pydantic.Field(
        description=(
            "Predicted date of the next occurrence of the recurring expenditure. In some cases, the next_date may be in the past as it is calculated by adding the avg_period_days to the most recent transaction date.\n"
        )
    )
    delta_amount: float = pydantic.Field(
        description=(
            "last_amount - previous_amount. For example: 68 indicates a $68 increase, -35 indicates a $35 decrease.\n"
        )
    )
    delta_percent: float = pydantic.Field(
        description=(
            "Percent change of previous_amount to last_amount. For example: .11 indicates an 11% increase, -.08 indicates an 8% decrease.\n"
        )
    )
    tags: typing.List[ExpenditureTag] = pydantic.Field(
        description=("Tags that indicate the nature of the expenditure.\n")
    )
    necessity_level: NecessityLevel = pydantic.Field(
        description=("Indicates level of necessity for a product or service.\n")
    )
    transactions: typing.List[Transaction] = pydantic.Field(
        description=("Array of occurrences for the recurring transaction.\n")
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
