# -----------------------------------------------------------------------------
# Copyright 2015-2022 by PyCLibrary Authors, see AUTHORS for more details.
#
# Distributed under the terms of the MIT/X11 license.
#
# The full license is in the file LICENCE, distributed with this software.
# -----------------------------------------------------------------------------
"""The version information for this release of PyCLibrary.

"""
from collections import namedtuple

# The major release number. Differences in the major number indicate
# possibly large differences in API.
MAJOR = 0

# The minor release number. Differences in the minor number indicate
# possibly small differences in the API, but these changes will come
# backwards compatibility support when possible. Minor releases are
# typically used for large feature additions.
MINOR = 2

# The micro release number. The micro release number is incremented
# for bug fix releases and small feature additions.
MICRO = 1

# The status indicate if this is a development or pre-release version
STATUS = ''

#: A namedtuple of the version info for the current release.
version_info = namedtuple('version_info', 'major minor micro status')
version_info = version_info(MAJOR, MINOR, MICRO, STATUS)
# Remove everything but the 'version_info' from this module.
del namedtuple, MAJOR, MINOR, MICRO, STATUS

__version__ = ('{0}.{1}.{2}'.format(*version_info) if not version_info.status
               else '{0}.{1}.{2}.{3}'.format(*version_info))
