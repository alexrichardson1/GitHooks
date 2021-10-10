#!/usr/bin/python3

import unittest
from pyfakefs.fake_filesystem_unittest import TestCase
import importlib
hook = importlib.import_module("commit-msg")


@unittest.expectedFailure
class ExitFailure(unittest.TestCase):
    def test_exit_failure(self):
        hook.exit_failure()


@unittest.expectedFailure
class FollowsConventionFailure(unittest.TestCase):
    def test_follows_convention_empty_message(self):
        hook.follows_convention("")

    def test_follows_convention_empty_scope(self):
        hook.follows_convention("feat(): Add func")
        hook.follows_convention("feat(  ): Add func")

    def test_follows_convention_no_scope(self):
        hook.follows_convention("feat: Add func")
        hook.follows_convention("refactor: Add func")
        hook.follows_convention("test: Add func")

    def test_follows_convention_case_sensitive(self):
        hook.follows_convention("Feat(foo): Add func")
        hook.follows_convention("feaT(foo): Add func")
        hook.follows_convention("Refactor(foo): Add func")
        hook.follows_convention("rEFactor(foo): Add func")
        hook.follows_convention("feat(foo): add func")

    def test_follows_convention_verbose_message(self):
        hook.follows_convention(
            "feat(foo): This is a realllllllyyyyyyyyy long commit message and should fail")

    def test_follows_convention_empty_message_trailing_punctuation(self):
        hook.follows_convention("fix(foo): No trailing punctuation!")
        hook.follows_convention("fix(foo): No trailing punctuation?")
        hook.follows_convention("fix(foo): No trailing punctuation...")
        hook.follows_convention("fix(foo): No trailing punctuation.")
        hook.follows_convention("fix(foo): No trailing punctuation:")
        hook.follows_convention("fix(foo): No trailing punctuation(")
        hook.follows_convention("fix(foo): No trailing punctuation)")


class FollowsConvention(unittest.TestCase):
    def test_follows_convention_allowed_types(self):
        hook.follows_convention("feat(foo): Add feature")
        hook.follows_convention("fix(foo): Remove syntax error")
        hook.follows_convention("style(foo): Format code")
        hook.follows_convention("refactor(foo): Change feature")
        hook.follows_convention("perf(foo): Add concurreny")
        hook.follows_convention("test(foo): Change feature")
        hook.follows_convention("docs(README): Add section to README")
        hook.follows_convention("chore(foo): Organise file structure")
        hook.follows_convention("build(foo): Add dependency")
        hook.follows_convention("ci(Dockerfile): Add RUN command")


class UpdateCommitMsg(TestCase):
    def setUp(self):
        self.setUpPyfakefs()
        self.file_path = "/foo/bar/commit_msg.txt"

    def test_update_commit_msg_following_convention_unchanged(self):
        commit_msg = "feat(foo): Add feature"
        self.fs.create_file(self.file_path, contents=commit_msg)
        self.assertTrue(hook.update_commit_msg(self.file_path) == [commit_msg])

    def test_update_commit_msg_trailing_space_removed(self):
        commit_msg = "     feat(foo): Add feature"
        self.fs.create_file(self.file_path, contents=commit_msg)
        self.assertTrue(
            hook.update_commit_msg(
                self.file_path) == [
                commit_msg.lstrip()])


if __name__ == '__main__':
    unittest.main(exit=False)
