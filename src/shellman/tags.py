# -*- coding: utf-8 -*-

"""
Section module.

This module contains the Section class.
"""

import re


class Tag:
    def __init__(self, text):
        self.text = text

    @classmethod
    def from_lines(cls, lines):
        return cls(text="\n".join(l.value for l in lines))


class AuthorTag(Tag):
    pass


class BugTag(Tag):
    pass


class BriefTag(Tag):
    pass


class CaveatTag(Tag):
    pass


class CopyrightTag(Tag):
    pass


class DateTag(Tag):
    pass


class DescTag(Tag):
    pass


class EnvTag:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    @classmethod
    def from_lines(cls, lines):
        name, description = "", []
        for line in lines:
            if line.tag == "env":
                split = line.value.split(" ", 1)
                if len(split) > 1:
                    name = split[0]
                    description.append(split[1])
                else:
                    name = split[0]
            else:
                description.append(line.value)
        return EnvTag(name=name, description="\n".join(description))


class ErrorTag(Tag):
    pass


class ExampleTag:
    def __init__(self, title, code, explanation):
        self.title = title
        self.code = code
        self.explanation = explanation

    @classmethod
    def from_lines(cls, lines):
        title, code, explanation = [], [], []
        current = None
        for line in lines:
            if line.tag == "example":
                if line.value:
                    title.append(line.value)
                current = "title"
            elif line.tag == "example-code":
                if line.value:
                    code.append(line.value)
                current = "code"
            elif line.tag == "example-explanation":
                if line.value:
                    explanation.append(line.value)
                current = "explanation"
            elif not line.tag and line.value:
                if current == "title":
                    title.append(line.value)
                elif current == "code":
                    code.append(line.value)
                elif current == "explanation":
                    explanation.append(line.value)

        return ExampleTag(
            title="\n".join(title),
            code="\n".join(code),
            explanation="\n".join(explanation),
        )


class ExitTag:
    def __init__(self, code, description):
        self.code = code
        self.description = description

    @classmethod
    def from_lines(cls, lines):
        code, description = "", []
        for line in lines:
            if line.tag == "exit":
                split = line.value.split(" ", 1)
                if len(split) > 1:
                    code = split[0]
                    description.append(split[1])
                else:
                    code = split[0]
            else:
                description.append(line.value)
        return ExitTag(code=code, description="\n".join(description))


class FileTag:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    @classmethod
    def from_lines(cls, lines):
        name, description = "", []
        for line in lines:
            if line.tag == "file":
                split = line.value.split(" ", 1)
                if len(split) > 1:
                    name = split[0]
                    description.append(split[1])
                else:
                    name = split[0]
            else:
                description.append(line.value)
        return FileTag(name=name, description="\n".join(description))


class FunctionTag:
    def __init__(
        self,
        prototype,
        brief,
        description,
        arguments,
        preconditions,
        return_codes,
        seealso,
        stderr,
        stdin,
        stdout,
    ):
        self.prototype = prototype
        self.brief = brief
        self.description = description
        self.arguments = arguments
        self.preconditions = preconditions
        self.return_codes = return_codes
        self.seealso = seealso
        self.stderr = stderr
        self.stdin = stdin
        self.stdout = stdout

    @classmethod
    def from_lines(cls, lines):
        brief = ""
        prototype = ""
        description = []
        arguments = []
        return_codes = []
        preconditions = []
        seealso = []
        stderr = []
        stdin = []
        stdout = []
        for line in lines:
            if line.tag == "function":
                prototype = line.value
            elif line.tag == "function-brief":
                brief = line.value
            elif line.tag == "function-description":
                description.append(line.value)
            elif line.tag == "function-argument":
                arguments.append(line.value)
            elif line.tag == "function-precondition":
                preconditions.append(line.value)
            elif line.tag == "function-return":
                return_codes.append(line.value)
            elif line.tag == "function-seealso":
                seealso.append(line.value)
            elif line.tag == "function-stderr":
                stderr.append(line.value)
            elif line.tag == "function-stdin":
                stdin.append(line.value)
            elif line.tag == "function-stdout":
                stdout.append(line.value)
            else:
                description.append(line.value)

        return FunctionTag(
            prototype=prototype,
            brief=brief,
            description="\n".join(description),
            arguments=arguments,
            preconditions=preconditions,
            return_codes=return_codes,
            seealso=seealso,
            stderr=stderr,
            stdin=stdin,
            stdout=stdout,
        )


class HistoryTag(Tag):
    pass


class LicenseTag(Tag):
    pass


class NoteTag(Tag):
    pass


class OptionTag:
    def __init__(self, short, long, positional, default, group, description):
        self.short = short
        self.long = long
        self.positional = positional
        self.default = default
        self.group = group
        self.description = description
        self.__signature = None

    @property
    def signature(self):
        if self.__signature is not None:
            return self.__signature
        sign = ""
        if self.short:
            sign = self.short
            if self.long:
                sign += ", "
            elif self.positional:
                sign += " "
        if self.long:
            if not self.short:
                sign += "    "
            sign += self.long + " "
        if self.positional:
            sign += self.positional
        self.__signature = sign
        return self.__signature

    @classmethod
    def from_lines(cls, lines):
        short, long, positional, default, group = "", "", "", "", ""
        description = []
        for line in lines:
            if line.tag == "option":
                search = re.search(
                    r"^(?P<short>-\w)?"
                    r"(?:, )?"
                    r"(?P<long>--[\w-]+)? ?"
                    r"(?P<positional>.+)?",
                    line.value,
                )
                if search:
                    short, long, positional = search.groups(default="")
                else:
                    positional = line.value
            elif line.tag == "option-default":
                default = line.value
            elif line.tag == "option-group":
                group = line.value
            elif line.tag == "option-description" and line.value:
                description.append(line.value)
            else:
                description.append(line.value)
        return OptionTag(
            short=short,
            long=long,
            positional=positional,
            default=default,
            group=group,
            description="\n".join(description),
        )


class SeealsoTag(Tag):
    pass


class StderrTag(Tag):
    pass


class StdinTag(Tag):
    pass


class StdoutTag(Tag):
    pass


class UsageTag:
    def __init__(self, program, command):
        self.program = program
        self.command = command

    @classmethod
    def from_lines(cls, lines):
        # TODO: only first line kept. Change it?
        program, command = "", ""
        split = lines[0].value.split(" ", 1)
        if len(split) > 1:
            program, command = split
        else:
            program = split[0]
        return UsageTag(program=program, command=command)


class VersionTag:
    def __init__(self, text):
        self.text = text

    @classmethod
    def from_lines(cls, lines):
        # TODO: only first line kept. Change it?
        return VersionTag(text=lines[0].value)


TAGS = {
    None: Tag,
    "author": AuthorTag,
    "bug": BugTag,
    "brief": BriefTag,
    "caveat": CaveatTag,
    "copyright": CopyrightTag,
    "date": DateTag,
    "desc": DescTag,
    "env": EnvTag,
    "error": ErrorTag,
    "example": ExampleTag,
    "exit": ExitTag,
    "file": FileTag,
    "function": FunctionTag,
    "history": HistoryTag,
    "license": LicenseTag,
    "note": NoteTag,
    "option": OptionTag,
    "seealso": SeealsoTag,
    "stderr": StderrTag,
    "stdin": StdinTag,
    "stdout": StdoutTag,
    "usage": UsageTag,
    "version": VersionTag,
}
