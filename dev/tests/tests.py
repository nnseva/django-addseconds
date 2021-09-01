from django.template import Context, Template
from django.test import TestCase


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

    def test_002_parse_time(self):
        """Test whether the parse_time tt works"""
        self.assertEqual(
            Template(
                """{% load addseconds %}{{ "11:01"|parse_time|time:"H-i-s" }}"""
            ).render(Context({})).strip(),
            '11-01-00'
        )

    def test_003_parse_datetime(self):
        """Test whether the parse_datetime tt works"""
        self.assertEqual(
            Template(
                """{% load addseconds %}{{ "2011-11-01 12:12"|parse_datetime|date:"Y/m/d/H/i/s" }}"""
            ).render(Context({})).strip(),
            '2011/11/01/12/12/00'
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
