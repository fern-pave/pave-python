# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class NecessityLevel(str, enum.Enum):
    OBLIGATORY = "obligatory"
    """
    Bills that are due and have consequences if they are not paid (eg. loan payments, utility payments, rent)
    """

    ESSENTIAL = "essential"
    """
    Not a bill, but expenses that are vital to a person’s livelihood (eg. groceries, gas)
    """

    NONESSENTIAL = "nonessential"
    """
    Any purchase that is optional (eg. restaurants, entertainment)
    """

    def visit(
        self,
        obligatory: typing.Callable[[], T_Result],
        essential: typing.Callable[[], T_Result],
        nonessential: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is NecessityLevel.OBLIGATORY:
            return obligatory()
        if self is NecessityLevel.ESSENTIAL:
            return essential()
        if self is NecessityLevel.NONESSENTIAL:
            return nonessential()
