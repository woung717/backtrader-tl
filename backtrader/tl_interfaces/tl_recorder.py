#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Copyright (C) 2015-2023 Daniel Rodriguez
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import collections
import pprint

from backtrader.analyzer import Analyzer

try:  # For new Python versions
    collectionsAbc = collections.abc  # collections.Iterable -> collections.abc.Iterable
except AttributeError:  # For old Python versions
    collectionsAbc = collections  # Используем collections.Iterable

import backtrader as bt
from backtrader.utils.py3 import (map, string_types, integer_types)


class DataEntryBuffer(object):
    def __init__(self):
        self.datetime = list()
        self.open = list()
        self.high = list()
        self.low = list()
        self.close = list()
        self.volume = list()

    def append(self, datetime, open, high, low, close, volume):
        self.datetime.append(datetime)
        self.open.append(open)
        self.high.append(high)
        self.low.append(low)
        self.close.append(close)
        self.volume.append(volume)


class DataEntry(object):

    def __init__(self, _name) -> None:
        self.name: str = _name
        self.buffer = DataEntryBuffer()

class TradingLabsRecorder(Analyzer):
    params = ()

    def __init__(self) -> None:
        self.data_entries: list[DataEntry] = list()

    def _init_data_entries(self, name) -> None:
        self.data_entries.append(DataEntry(name))

    def start(self):
        for data in self.datas:
            self._init_data_entries(name=data._name)

    def next(self):
        for i, data in enumerate(self.datas):
            self.data_entries[i].buffer.append(
                datetime=int(data.datetime.datetime().timestamp()),
                open=data.open[0],
                high=data.high[0],
                low=data.low[0],
                close=data.close[0],
                volume=data.volume[0]
            )

    def stop(self):
        # save data_entries
        # save orders
        # save trades
        # save cash
        # save value
        pass
    
    def notify_order(self, order):
        pass

    def notify_trade(self, trade):
        pass

    def notify_cashvalue(self, cash, value):
        pass

    def notify_fund(self, cash, value, fundvalue, shares):
        pass

    def get_analysis(self):
        return dict()
    