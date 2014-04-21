# Copyright 2014 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from __future__ import (nested_scopes, generators, division, absolute_import, with_statement,
                        print_function, unicode_literals)

from twitter.common.collections import maybe_list

from pants.base.build_manual import manual
from pants.base.target import Target, TargetDefinitionException
from pants.targets.exportable_jvm_library import ExportableJvmLibrary
from pants.targets.java_library import JavaLibrary


@manual.builddict(tags=['scala'])
class ScalaLibrary(ExportableJvmLibrary):
  """A collection of Scala code.

  Normally has conceptually-related sources; invoking the ``compile`` goal
  on this target compiles scala and generates classes. Invoking the ``bundle``
  goal on this target creates a ``.jar``; but that's an unusual thing to do.
  Instead, a ``jvm_binary`` might depend on this library; that binary is a
  more sensible thing to bundle.
  """

  def __init__(self, *args, **kwargs):
    """
    :param string name: The name of this target, which combined with this
      build file defines the target :class:`pants.base.address.Address`.
    :param sources: A list of filenames representing the source code
      this library is compiled from.
    :type sources: list of strings
    :param java_sources:
      :class:`pants.targets.java_library.JavaLibrary` or list of
      JavaLibrary targets this library has a circular dependency on.
      Prefer using dependencies to express non-circular dependencies.
    :param Artifact provides:
      The :class:`pants.targets.artifact.Artifact`
      to publish that represents this target outside the repo.
    :param dependencies: List of :class:`pants.base.target.Target` instances
      this target depends on.
    :type dependencies: list of targets
    :param excludes: List of :class:`pants.targets.exclude.Exclude` instances
      to filter this target's transitive dependencies against.
    :param resources: An optional list of paths (DEPRECATED) or ``resources``
      targets containing resources that belong on this library's classpath.
    :param exclusives: An optional list of exclusives tags.
    """
    super(ScalaLibrary, self).__init__(*args, **kwargs)
    self.add_labels('scala')


  @property
  def java_sources(self):
    return [source for source in self.payload.sources if source.endswith('.java')]
