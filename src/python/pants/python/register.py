# Copyright 2014 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from __future__ import (nested_scopes, generators, division, absolute_import, with_statement,
                        print_function, unicode_literals)


from pants.python.commands.build import Build
from pants.python.commands.py import Py
from pants.python.commands.setup_py import SetupPy
from pants.python.targets.python_antlr_library import PythonAntlrLibrary
from pants.python.targets.python_artifact import PythonArtifact
from pants.python.targets.python_binary import PythonBinary
from pants.python.targets.python_library import PythonLibrary
from pants.python.targets.python_requirement import PythonRequirement
from pants.python.targets.python_requirement_library import PythonRequirementLibrary
from pants.python.targets.python_requirements import python_requirements
from pants.python.targets.python_tests import PythonTests
from pants.python.targets.python_thrift_library import PythonThriftLibrary


def target_aliases():
  return {
    'python_antlr_library': PythonAntlrLibrary,
    'python_binary': PythonBinary,
    'python_library': PythonLibrary,
    'python_requirement_library': PythonRequirementLibrary,
    'python_test_suite': Dependencies,  # Legacy alias.
    'python_tests': PythonTests,
    'python_thrift_library': PythonThriftLibrary,
  }


def object_aliases():
  return {
    'python_requirement': PythonRequirement,
    'python_artifact': PythonArtifact,
    'setup_py': PythonArtifact,
  }


def partial_path_relative_util_aliases():
  return {
    'python_requirements': python_requirements,
  }


def applicative_path_relative_util_aliases():
  return {}


def commands():
  for cmd in (Build, Goal, Py, SetupPy):
    cmd._register()


def goals():
  pass

