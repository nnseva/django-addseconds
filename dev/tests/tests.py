from django.template import Context, Template
from django.test import TestCase
from django.utils import dateparse


class ModuleTest(TestCase):
    maxDiff = None

    def test_001_parse_date(self):
        """Test whether the parse_date tt works"""
        self.assertEqual(
            Template(
                """{% load addseconds %}{{ "2011-11-01"|parse_date|date:"Y/m/d" }}"""
            ).render(Context({})).strip(),
            '2011/11/01'
        )
        self.assertEqual(
            Template(
                """{% load addseconds %}{{ ""|parse_date|date:"Y/m/d" }}"""
            ).render(Context({})).strip(),
            ''
        )
        self.assertEqual(
            Template(
                """{% load addseconds %}{{ value|parse_date|date:"Y/m/d" }}"""
            ).render(Context({'value': None})).strip(),
            ''
        )
        self.assertEqual(
            Template(
                """{% load addseconds %}{{ value|parse_date|date:"Y/m/d" }}"""
            ).render(Context({'value': 1})).strip(),
            ''
        )

    def test_002_parse_time(self):
        """Test whether the parse_time tt works"""
        self.assertEqual(
            Template(
                """{% load addseconds %}{{ "11:01"|parse_time|time:"H-i-s" }}"""
            ).render(Context({})).strip(),
            '11-01-00'
        )
        self.assertEqual(
            Template(
                """{% load addseconds %}{{ ""|parse_time|time:"H-i-s" }}"""
            ).render(Context({})).strip(),
            ''
        )
        self.assertEqual(
            Template(
                """{% load addseconds %}{{ value|parse_time|time:"H-i-s" }}"""
            ).render(Context({'value': None})).strip(),
            ''
        )
        self.assertEqual(
            Template(
                """{% load addseconds %}{{ value|parse_time|time:"H-i-s" }}"""
            ).render(Context({'value': 1})).strip(),
            ''
        )

    def test_003_parse_datetime(self):
        """Test whether the parse_datetime tt works"""
        self.assertEqual(
            Template(
                """{% load addseconds %}{{ "2011-11-01 12:12"|parse_datetime|date:"Y/m/d/H/i/s" }}"""
            ).render(Context({})).strip(),
            '2011/11/01/12/12/00'
        )
        self.assertEqual(
            Template(
                """{% load addseconds %}{{ ""|parse_datetime|date:"Y/m/d/H/i/s" }}"""
            ).render(Context({})).strip(),
            ''
        )
        self.assertEqual(
            Template(
                """{% load addseconds %}{{ value|parse_datetime|date:"Y/m/d/H/i/s" }}"""
            ).render(Context({'value': None})).strip(),
            ''
        )
        self.assertEqual(
            Template(
                """{% load addseconds %}{{ value|parse_datetime|date:"Y/m/d/H/i/s" }}"""
            ).render(Context({'value': 1})).strip(),
            ''
        )

    def test_004_addseconds(self):
        """Test whether the addseconds tt works"""
        self.assertEqual(
            Template(
                """{% load addseconds %}{{ "2011-11-01 12:12"|parse_datetime|addseconds:3670|date:"Y/m/d/H/i/s" }}"""
            ).render(Context({})).strip(),
            '2011/11/01/13/13/10'
        )
        self.assertEqual(
            Template(
                """{% load addseconds %}{{ "2011-11-01 12:12"|parse_datetime|addseconds:-3600|date:"Y/m/d/H/i/s" }}"""
            ).render(Context({})).strip(),
            '2011/11/01/11/12/00'
        )

    def test_005_addseconds_types(self):
        """Test whether the addseconds works with different types"""
        ts = dateparse.parse_datetime("2011-11-01 12:12")
        self.assertEqual(
            Template(
                """{% load addseconds %}{{ value|addseconds:-3600|date:"Y/m/d/H/i/s" }}"""
            ).render(Context({'value': ts})).strip(),
            '2011/11/01/11/12/00'
        )
        self.assertEqual(
            Template(
                """{% load addseconds %}{{ value|addseconds:-3600|date:"Y/m/d/H/i/s" }}"""
            ).render(Context({'value': ts.timestamp()})).strip(),
            '2011/11/01/11/12/00'
        )
        self.assertEqual(
            Template(
                """{% load addseconds %}{{ value|addseconds:3600|date:"Y/m/d/H/i/s" }}"""
            ).render(Context({'value': ts.date()})).strip(),
            '2011/11/01/01/00/00'
        )
        self.assertEqual(
            Template(
                """{% load addseconds %}{{ value|addseconds:3600|date:"Y/m/d/H/i/s" }}"""
            ).render(Context({'value': None})).strip(),
            ''
        )
        self.assertEqual(
            Template(
                """{% load addseconds %}{{ ""|addseconds:-3600|date:"Y/m/d/H/i/s" }}"""
            ).render(Context({})).strip(),
            ''
        )
        self.assertEqual(
            Template(
                """{% load addseconds %}{{ value|addseconds:"-3600"|date:"Y/m/d/H/i/s" }}"""
            ).render(Context({'value': ts})).strip(),
            '2011/11/01/11/12/00'
        )
        self.assertEqual(
            Template(
                """{% load addseconds %}{{ value|addseconds:"qqq"|date:"Y/m/d/H/i/s" }}"""
            ).render(Context({'value': ts})).strip(),
            ''
        )
        self.assertEqual(
            Template(
                """{% load addseconds %}{{ value|addseconds:""|date:"Y/m/d/H/i/s" }}"""
            ).render(Context({'value': ts})).strip(),
            ''
        )
