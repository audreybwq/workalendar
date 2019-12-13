from datetime import date
from gettext import gettext_lazy as __, gettext as _
from ..core import WesternCalendar, ChristianMixin
from ..core import MON, TUE, WED, FRI
from ..registry_tools import iso_register


@iso_register('CL')
class Chile(WesternCalendar, ChristianMixin):
    "Chile"
    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (5, 1, __("Labour Day")),
        (5, 21, __("Navy Day")),
        (6, 29, __("Saint Peter and Saint Paul")),
        (7, 16, __("Our Lady of Mount Carmel")),
        (9, 18, __("National holiday")),
        (9, 19, __("Army holiday")),
        (10, 12, __("Columbus Day")),
        (12, 31, __("Banking Holiday")),
    )
    include_good_friday = True
    include_easter_saturday = True
    include_assumption = True
    include_all_saints = True
    include_immaculate_conception = True

    def get_variable_days(self, year):
        days = super().get_variable_days(year)
        september_17 = date(year, 9, 17)
        if september_17.weekday() == MON:
            days.append((september_17, _('"Bridge" holiday')))
        september_20 = date(year, 9, 20)
        if september_20.weekday() == FRI:
            days.append((september_20, _('"Bridge" holiday')))

        reformation_day = date(year, 10, 31)
        if reformation_day.weekday() == WED:
            reformation_day = date(year, 11, 2)
        elif reformation_day.weekday() == TUE:
            reformation_day = date(year, 10, 27)

        days.append((reformation_day, _("Reformation Day")))

        return days
