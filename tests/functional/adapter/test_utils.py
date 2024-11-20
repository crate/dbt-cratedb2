import pytest

from dbt.tests.adapter.utils.test_any_value import BaseAnyValue
from dbt.tests.adapter.utils.test_array_append import BaseArrayAppend
from dbt.tests.adapter.utils.test_array_concat import BaseArrayConcat
from dbt.tests.adapter.utils.test_array_construct import BaseArrayConstruct
from dbt.tests.adapter.utils.test_bool_or import BaseBoolOr
from dbt.tests.adapter.utils.test_cast import BaseCast
from dbt.tests.adapter.utils.test_cast_bool_to_text import BaseCastBoolToText
from dbt.tests.adapter.utils.test_concat import BaseConcat
from dbt.tests.adapter.utils.test_current_timestamp import BaseCurrentTimestampAware
from dbt.tests.adapter.utils.test_date import BaseDate
from dbt.tests.adapter.utils.test_dateadd import BaseDateAdd
from dbt.tests.adapter.utils.test_datediff import BaseDateDiff
from dbt.tests.adapter.utils.test_date_spine import BaseDateSpine
from dbt.tests.adapter.utils.test_date_trunc import BaseDateTrunc
from dbt.tests.adapter.utils.test_equals import BaseEquals
from dbt.tests.adapter.utils.test_escape_single_quotes import (
    BaseEscapeSingleQuotesQuote,
    BaseEscapeSingleQuotesBackslash,
)
from dbt.tests.adapter.utils.test_except import BaseExcept
from dbt.tests.adapter.utils.test_generate_series import BaseGenerateSeries
from dbt.tests.adapter.utils.test_get_intervals_between import BaseGetIntervalsBetween
from dbt.tests.adapter.utils.test_get_powers_of_two import BaseGetPowersOfTwo
from dbt.tests.adapter.utils.test_hash import BaseHash
from dbt.tests.adapter.utils.test_intersect import BaseIntersect
from dbt.tests.adapter.utils.test_last_day import BaseLastDay
from dbt.tests.adapter.utils.test_length import BaseLength
from dbt.tests.adapter.utils.test_listagg import BaseListagg
from dbt.tests.adapter.utils.test_null_compare import BaseNullCompare, BaseMixedNullCompare
from dbt.tests.adapter.utils.test_position import BasePosition
from dbt.tests.adapter.utils.test_replace import BaseReplace
from dbt.tests.adapter.utils.test_right import BaseRight
from dbt.tests.adapter.utils.test_safe_cast import BaseSafeCast
from dbt.tests.adapter.utils.test_split_part import BaseSplitPart
from dbt.tests.adapter.utils.test_string_literal import BaseStringLiteral
from dbt.tests.adapter.utils.test_timestamps import BaseCurrentTimestamps
from dbt.tests.adapter.utils.test_validate_sql import BaseValidateSqlMethod


class TestAnyValue(BaseAnyValue):
    pass


class TestArrayAppend(BaseArrayAppend):
    pass


class TestArrayConcat(BaseArrayConcat):
    pass


class TestArrayConstruct(BaseArrayConstruct):
    pass


@pytest.mark.skip("CrateDB: Does not implement `bool_or` aggregate function")
class TestBoolOr(BaseBoolOr):
    pass


class TestCast(BaseCast):
    pass


@pytest.mark.skip(
    "CrateDB: Upstream SQL template refers to column `input`, which needs to be quoted"
)
class TestCastBoolToText(BaseCastBoolToText):
    pass


class TestConcat(BaseConcat):
    pass


class TestCurrentTimestamp(BaseCurrentTimestampAware):
    pass


@pytest.mark.skip("CrateDB: Unknown function: to_date('2023-09-10', 'YYYY-MM-DD')")
class TestDate(BaseDate):
    pass


@pytest.mark.skip("CrateDB: '<=' not supported between instances of 'str' and 'int'")
class TestDateSpine(BaseDateSpine):
    pass


@pytest.mark.skip("CrateDB: Type `date` does not support storage")
class TestDateTrunc(BaseDateTrunc):
    pass


class TestDateAdd(BaseDateAdd):
    pass


@pytest.mark.skip("CrateDB: Unknown function: date_part('hour', data.second_date)")
class TestDateDiff(BaseDateDiff):
    pass


class TestEquals(BaseEquals):
    pass


class TestEscapeSingleQuotesQuote(BaseEscapeSingleQuotesQuote):
    pass


@pytest.mark.skip("Not implemented in `dbt-postgres<1.8`, fails in `dbt-postgres>=1.8`")
class TestEscapeSingleQuotesBackslash(BaseEscapeSingleQuotesBackslash):
    pass


@pytest.mark.skip("CrateDB: Does not implement `EXCEPT`")
class TestExcept(BaseExcept):
    pass


class TestGenerateSeries(BaseGenerateSeries):
    pass


@pytest.mark.skip("CrateDB: Cannot cast `'09/12/2023'` of type `text` to type `date`")
class TestGetIntervalsBetween(BaseGetIntervalsBetween):
    pass


class TestGetPowersOfTwo(BaseGetPowersOfTwo):
    pass


class TestHash(BaseHash):
    pass


@pytest.mark.skip("CrateDB: Does not implement `INTERSECT`")
class TestIntersect(BaseIntersect):
    pass


@pytest.mark.skip("CrateDB: Type `date` does not support storage")
class TestLastDay(BaseLastDay):
    pass


class TestLength(BaseLength):
    pass


@pytest.mark.skip("CrateDB: Unknown error")
class TestListagg(BaseListagg):
    pass


class TestMixedNullCompare(BaseMixedNullCompare):
    pass


class TestNullCompare(BaseNullCompare):
    pass


class TestPosition(BasePosition):
    pass


class TestReplace(BaseReplace):
    pass


class TestRight(BaseRight):
    pass


class TestSafeCast(BaseSafeCast):
    pass


@pytest.mark.skip("CrateDB: Error `index in split_part must be greater than zero`")
class TestSplitPart(BaseSplitPart):
    pass


class TestStringLiteral(BaseStringLiteral):
    pass


class TestCurrentTimestamps(BaseCurrentTimestamps):
    pass


class TestValidateSqlMethod(BaseValidateSqlMethod):
    pass
