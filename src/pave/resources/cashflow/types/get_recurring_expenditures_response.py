# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from .recurring_expenditure import RecurringExpenditure


class GetRecurringExpendituresResponse(pydantic.BaseModel):
    user_id: str = pydantic.Field(description=("The user ID for which the recurring expenditures were requested.\n"))
    from_: dt.date = pydantic.Field(
        alias="from", description=("Oldest transaction date on which the insight was updated.\n")
    )
    to: dt.date = pydantic.Field(description=("Most recent transaction date on which the insight was updated.\n"))
    recurring_expenditures: typing.List[RecurringExpenditure]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}