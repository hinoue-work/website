# -*- coding: UTF-8 -*-
# vim: set expandtab sw=4 ts=4 sts=4:
#
# phpMyAdmin web site
#
# Copyright (C) 2008 - 2015 Michal Cihar <michal@cihar.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
from django.db import models
from markupfield.fields import MarkupField
import datetime

YEAR_TODAY = datetime.date.today().year
YEAR_CHOICES = [(i, i) for i in range(2003, YEAR_TODAY + 1)]

class PMASA(models.Model):
    year = models.IntegerField(
        choices=YEAR_CHOICES, default=YEAR_TODAY
    )
    sequence = models.IntegerField(
        help_text='Sequence number of PMASA in given year'
    )
    date = models.DateField(
        default=datetime.date.today
    )
    updated = models.DateField(
        null=True,
        blank=True,
        help_text='Set this in case of major update to the entry'
    )
    summary = models.CharField(max_length=200)
    description = MarkupField(default_markup_type='markdown')
    severity = models.CharField(max_length=200)
    mitigation = models.TextField(blank=True)
    affected = models.TextField()
    unaffected = models.TextField(blank=True)
    solution = models.TextField(
        max_length=200,
        default='Upgrade to phpMyAdmin ? or newer or apply patch listed below.'
    )
    references = models.TextField(
        max_length=200,
        help_text='Links to reporter etc.'
    )
    cve = models.CharField(
        max_length=200,
        help_text='Space separated list of related CVE entries'
    )
    cwe = models.CharField(
        max_length=200,
        default='661',
        help_text='Space separated list of CWE classifications'
    )
    commits = models.TextField(
        help_text=(
            'Space separated list of commits, commits for different branches '
            'should be placed on separate line prefixed with version prefix. '
            'For example: 3.5: 01d35b3558e47fba947719857bd71f6fd9e5dce8'
        )
    )
    draft = models.BooleanField(
        default=True,
        help_text='Draft entries are not shown in website listings'
    )

    class Meta(object):
        unique_together = ('year', 'sequence')
        ordering = ('-year', '-sequence')
        verbose_name = 'PMASA'
        verbose_name_plural = 'PMASAs'

    def __unicode__(self):
        return 'PMASA-{0}-{1}'.format(self.year, self.sequence)
