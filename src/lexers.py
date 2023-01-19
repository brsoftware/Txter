"""
This is a file of a project of the Bright Software Foundation.

======================= Project and File Information ===========================

Project Name:                           Txter

Project Name Identifier:                brTxter

Project Version (for This File):        0.5.0

Project Status (for This File):         beta testing...

Project Start Date:                     Dec 23, 2022 UTC

Project Start Version:                  0.2.0 [alpha]

Project End Date:                       --None--

Project End Version:                    --None--

Project Activate State:                 Remains Activate

Project Type:                           Freeware

Project Copyright:                      Copyleft

Project License:                        Bright Software License

Project Developer:                      Bright Software Foundation Development Team

Project Creator:                        Bright Software Foundation

Project Used Programming Language(s):   Python 3

Project Download Mirror:                https://sourceforge.net/projects/brtxter

Project Source Hosting Mirror:          https://github.com/brsoftware/txter


File Name:                              lexers.py

File Type:                              Source File

File Belongs To:                        Txter / brTxter

================================================================================

Bright Software Foundation 2022 - 2023
"""


#
# Importing packages and modules...
#


# PyQt
from PyQt5.QtGui import QColor
from PyQt5.Qsci import *


#
# Defining the class(es)...
#


class LexerNone(QsciLexerCustom):
    """
    No lexer.
    Defining for beauty and uniform.
    """

    def __init__(self, font, parent=None):
        """
        Initializing method for LexerNone.

        :param font: QFont (must)
        :param parent: QObject | None
        """

        # Super the class to the parent.
        super().__init__(parent)

        # Initializing variables.
        self.__font = font

        # Setting default fonts.
        self.setDefaultFont(self.__font)

    def description(self, style):
        """
        Description: No description.

        :param style: Q_UNUSED(int)
        :return: 'No lexer'
        """

        return "No lexer"

    def styleText(self, start, end):
        """
        Style no text.

        :param start: Q_UNUSED(int)
        :param end: Q_UNUSED(end)
        :return: None
        """

        pass


class LexerCPlusPlus(QsciLexerCPP):
    """
    C++ Lexer.
    """

    def __init__(self, font, parent=None):
        """
        Initializing method for LexerCPlusPlus.

        :param font: QFont (must)
        :param parent: QObject | None
        """

        # Super the class to the parent.
        super().__init__(parent)

        # Defining the variables...
        self.__font = font

        self.__comment_kw_color = QColor()
        self.__comment_kw_color.setNamedColor("#fca510")

        self.__kw_color = QColor()
        self.__kw_color.setNamedColor("#3333ff")

        self.__string_color = QColor()
        self.__string_color.setNamedColor("#00aa00")

        # Setting fold commands...
        self.setFoldCompact(False)
        self.setFoldComments(True)
        self.setFoldAtElse(True)
        self.setFoldPreprocessor(True)

        # Setting default foreground color...
        self.setColor(self.__comment_kw_color, QsciLexerCPP.CommentDocKeyword)
        self.setColor(self.__comment_kw_color, QsciLexerCPP.InactiveCommentDocKeyword)
        self.setColor(self.__kw_color, QsciLexerCPP.Keyword)
        self.setColor(self.__kw_color, QsciLexerCPP.KeywordSet2)
        self.setColor(self.__kw_color, QsciLexerCPP.InactiveKeyword)
        self.setColor(self.defaultColor(QsciLexerCPP.Default), QsciLexerCPP.Operator)
        self.setColor(self.__string_color, QsciLexerCPP.SingleQuotedString)
        self.setColor(self.__string_color, QsciLexerCPP.DoubleQuotedString)
        self.setColor(self.__string_color, QsciLexerCPP.UnclosedString)
        self.setColor(self.__string_color, QsciLexerCPP.RawString)
        self.setColor(self.__string_color, QsciLexerCPP.VerbatimString)
        self.setColor(self.__string_color, QsciLexerCPP.HashQuotedString)
        self.setColor(self.__string_color, QsciLexerCPP.InactiveDoubleQuotedString)
        self.setColor(self.__string_color, QsciLexerCPP.InactiveHashQuotedString)
        self.setColor(self.__string_color, QsciLexerCPP.InactiveRawString)
        self.setColor(self.__string_color, QsciLexerCPP.InactiveSingleQuotedString)
        self.setColor(self.__string_color, QsciLexerCPP.InactiveTripleQuotedVerbatimString)
        self.setColor(self.__string_color, QsciLexerCPP.InactiveUnclosedString)
        self.setColor(self.__string_color, QsciLexerCPP.InactiveVerbatimString)
        self.setColor(self.__string_color, QsciLexerCPP.TripleQuotedVerbatimString)

        # Setting default font...
        self.setDefaultFont(self.__font)
        self.setFont(self.__font, QsciLexerCPP.Comment)
        self.setFont(self.__font, QsciLexerCPP.CommentDoc)
        self.setFont(self.__font, QsciLexerCPP.CommentDocKeyword)
        self.setFont(self.__font, QsciLexerCPP.CommentDocKeywordError)
        self.setFont(self.__font, QsciLexerCPP.CommentLine)
        self.setFont(self.__font, QsciLexerCPP.CommentLineDoc)
        self.setFont(self.__font, QsciLexerCPP.InactiveComment)
        self.setFont(self.__font, QsciLexerCPP.InactiveCommentDoc)
        self.setFont(self.__font, QsciLexerCPP.InactiveCommentDocKeyword)
        self.setFont(self.__font, QsciLexerCPP.InactiveCommentDocKeywordError)
        self.setFont(self.__font, QsciLexerCPP.InactiveCommentLine)
        self.setFont(self.__font, QsciLexerCPP.InactiveCommentLineDoc)
        self.setFont(self.__font, QsciLexerCPP.SingleQuotedString)
        self.setFont(self.__font, QsciLexerCPP.DoubleQuotedString)
        self.setFont(self.__font, QsciLexerCPP.UnclosedString)
        self.setFont(self.__font, QsciLexerCPP.RawString)
        self.setFont(self.__font, QsciLexerCPP.VerbatimString)
        self.setFont(self.__font, QsciLexerCPP.HashQuotedString)
        self.setFont(self.__font, QsciLexerCPP.InactiveDoubleQuotedString)
        self.setFont(self.__font, QsciLexerCPP.InactiveHashQuotedString)
        self.setFont(self.__font, QsciLexerCPP.InactiveRawString)
        self.setFont(self.__font, QsciLexerCPP.InactiveSingleQuotedString)
        self.setFont(self.__font, QsciLexerCPP.InactiveTripleQuotedVerbatimString)
        self.setFont(self.__font, QsciLexerCPP.InactiveUnclosedString)
        self.setFont(self.__font, QsciLexerCPP.InactiveVerbatimString)
        self.setFont(self.__font, QsciLexerCPP.TripleQuotedVerbatimString)
        self.setFont(self.__font, QsciLexerCPP.Operator)
        self.setFont(self.__font, QsciLexerCPP.InactiveOperator)
        self.setFont(self.__font, QsciLexerCPP.Number)
        self.setFont(self.__font, QsciLexerCPP.Keyword)
        self.setFont(self.__font, QsciLexerCPP.KeywordSet2)
        self.setFont(self.__font, QsciLexerCPP.InactiveKeyword)
        self.setFont(self.__font, QsciLexerCPP.InactiveKeywordSet2)


class LexerCSS(QsciLexerCSS):
    """
    CSS Lexer.
    """

    def __init__(self, font, parent=None):
        """
        Initializing method for LexerCSS.

        :param font: QFont (must)
        :param parent: QObject | None
        """

        # Super the class to the parent.
        super().__init__(parent)

        # Defining variables.
        self.__font = font

        self.__kw_color = QColor()
        self.__kw_color.setNamedColor("#fca510")

        self.__tag_color = QColor()
        self.__tag_color.setNamedColor("blue")

        self.__string_color = QColor()
        self.__string_color.setNamedColor("#00aa00")

        # Setting default foreground color.
        self.setColor(self.__kw_color, QsciLexerCSS.ClassSelector)
        self.setColor(self.__kw_color, QsciLexerCSS.IDSelector)
        self.setColor(self.__tag_color, QsciLexerCSS.Tag)
        self.setColor(self.defaultColor(QsciLexerCSS.Default), QsciLexerCSS.Operator)
        self.setColor(self.__string_color, QsciLexerCSS.SingleQuotedString)
        self.setColor(self.__string_color, QsciLexerCSS.DoubleQuotedString)

        # Setting default font.
        self.setDefaultFont(self.__font)
        self.setFont(self.__font, QsciLexerCSS.Comment)
        self.setFont(self.__font, QsciLexerCSS.SingleQuotedString)
        self.setFont(self.__font, QsciLexerCSS.DoubleQuotedString)


class LexerHTML(QsciLexerHTML):
    """
    HTML Lexer.
    """

    def __init__(self, font, parent=None):
        """
        Initializing method for LexerHTML.

        :param font: QFont (must)
        :param parent: QObject | None
        """

        # Super the class to the parent.
        super().__init__(parent)

        # Defining variables...
        self.__font = font

        self.__default_color = QColor()
        self.__default_color.setNamedColor("#888888")

        self.__kw_color = QColor()
        self.__kw_color.setNamedColor("#5538ab")

        self.__tag_color = QColor()
        self.__tag_color.setNamedColor("blue")

        self.__string_color = QColor()
        self.__string_color.setNamedColor("#00aa00")

        # Setting default foreground color...
        self.setDefaultColor(self.__default_color)

        self.setColor(self.__string_color, QsciLexerHTML.VBScriptString)
        self.setColor(self.__string_color, QsciLexerHTML.SGMLDoubleQuotedString)
        self.setColor(self.__string_color, QsciLexerHTML.SGMLSingleQuotedString)
        self.setColor(self.__string_color, QsciLexerHTML.HTMLSingleQuotedString)
        self.setColor(self.__string_color, QsciLexerHTML.HTMLDoubleQuotedString)
        self.setColor(self.__string_color, QsciLexerHTML.ASPJavaScriptDoubleQuotedString)
        self.setColor(self.__string_color, QsciLexerHTML.ASPJavaScriptSingleQuotedString)
        self.setColor(self.__string_color, QsciLexerHTML.ASPJavaScriptUnclosedString)
        self.setColor(self.__string_color, QsciLexerHTML.ASPPythonDoubleQuotedString)
        self.setColor(self.__string_color, QsciLexerHTML.ASPPythonSingleQuotedString)
        self.setColor(self.__string_color, QsciLexerHTML.ASPPythonTripleDoubleQuotedString)
        self.setColor(self.__string_color, QsciLexerHTML.ASPPythonTripleSingleQuotedString)
        self.setColor(self.__string_color, QsciLexerHTML.ASPVBScriptString)
        self.setColor(self.__string_color, QsciLexerHTML.ASPVBScriptUnclosedString)
        self.setColor(self.__string_color, QsciLexerHTML.JavaScriptDoubleQuotedString)
        self.setColor(self.__string_color, QsciLexerHTML.JavaScriptSingleQuotedString)
        self.setColor(self.__string_color, QsciLexerHTML.JavaScriptUnclosedString)
        self.setColor(self.__string_color, QsciLexerHTML.PHPDoubleQuotedString)
        self.setColor(self.__string_color, QsciLexerHTML.PHPSingleQuotedString)
        self.setColor(self.__string_color, QsciLexerHTML.PythonTripleDoubleQuotedString)
        self.setColor(self.__string_color, QsciLexerHTML.PythonTripleSingleQuotedString)
        self.setColor(self.__string_color, QsciLexerHTML.PythonDoubleQuotedString)
        self.setColor(self.__string_color, QsciLexerHTML.PythonSingleQuotedString)
        self.setColor(self.__string_color, QsciLexerHTML.VBScriptUnclosedString)
        self.setColor(self.__kw_color, QsciLexerHTML.PHPKeyword)
        self.setColor(self.__kw_color, QsciLexerHTML.PythonKeyword)
        self.setColor(self.__kw_color, QsciLexerHTML.VBScriptKeyword)
        self.setColor(self.__kw_color, QsciLexerHTML.ASPPythonKeyword)
        self.setColor(self.__kw_color, QsciLexerHTML.JavaScriptKeyword)
        self.setColor(self.__kw_color, QsciLexerHTML.ASPVBScriptKeyword)
        self.setColor(self.__kw_color, QsciLexerHTML.ASPJavaScriptKeyword)
        self.setColor(self.__tag_color, QsciLexerHTML.Tag)
        self.setColor(self.__tag_color, QsciLexerHTML.OtherInTag)
        self.setColor(self.__tag_color, QsciLexerHTML.XMLTagEnd)
        self.setColor(self.__default_color, QsciLexerHTML.Default)

        # Setting default font...
        self.setDefaultFont(self.__font)
        self.setFont(self.__font, QsciLexerHTML.HTMLComment)
        self.setFont(self.__font, QsciLexerHTML.SGMLComment)
        self.setFont(self.__font, QsciLexerHTML.PHPComment)
        self.setFont(self.__font, QsciLexerHTML.SGMLParameterComment)
        self.setFont(self.__font, QsciLexerHTML.PHPCommentLine)
        self.setFont(self.__font, QsciLexerHTML.ASPJavaScriptComment)
        self.setFont(self.__font, QsciLexerHTML.ASPPythonComment)
        self.setFont(self.__font, QsciLexerHTML.ASPVBScriptComment)
        self.setFont(self.__font, QsciLexerHTML.ASPJavaScriptCommentLine)
        self.setFont(self.__font, QsciLexerHTML.ASPJavaScriptCommentDoc)
        self.setFont(self.__font, QsciLexerHTML.JavaScriptCommentLine)
        self.setFont(self.__font, QsciLexerHTML.JavaScriptCommentDoc)
        self.setFont(self.__font, QsciLexerHTML.VBScriptComment)
        self.setFont(self.__font, QsciLexerHTML.PythonComment)
        self.setFont(self.__font, QsciLexerHTML.ASPXCComment)
        self.setFont(self.__font, QsciLexerHTML.JavaScriptComment)
        self.setFont(self.__font, QsciLexerHTML.JavaScriptKeyword)
        self.setFont(self.__font, QsciLexerHTML.JavaScriptUnclosedString)
        self.setFont(self.__font, QsciLexerHTML.JavaScriptSingleQuotedString)
        self.setFont(self.__font, QsciLexerHTML.JavaScriptDoubleQuotedString)
        self.setFont(self.__font, QsciLexerHTML.JavaScriptCommentLine)
        self.setFont(self.__font, QsciLexerHTML.JavaScriptCommentDoc)
        self.setFont(self.__font, QsciLexerHTML.JavaScriptDefault)
        self.setFont(self.__font, QsciLexerHTML.JavaScriptRegex)
        self.setFont(self.__font, QsciLexerHTML.JavaScriptNumber)
        self.setFont(self.__font, QsciLexerHTML.JavaScriptStart)
        self.setFont(self.__font, QsciLexerHTML.JavaScriptSymbol)
        self.setFont(self.__font, QsciLexerHTML.JavaScriptWord)
        self.setFont(self.__font, QsciLexerHTML.ASPJavaScriptComment)
        self.setFont(self.__font, QsciLexerHTML.ASPJavaScriptKeyword)
        self.setFont(self.__font, QsciLexerHTML.ASPJavaScriptUnclosedString)
        self.setFont(self.__font, QsciLexerHTML.ASPJavaScriptSingleQuotedString)
        self.setFont(self.__font, QsciLexerHTML.ASPJavaScriptDoubleQuotedString)
        self.setFont(self.__font, QsciLexerHTML.ASPJavaScriptCommentLine)
        self.setFont(self.__font, QsciLexerHTML.ASPJavaScriptCommentDoc)
        self.setFont(self.__font, QsciLexerHTML.ASPJavaScriptDefault)
        self.setFont(self.__font, QsciLexerHTML.ASPJavaScriptRegex)
        self.setFont(self.__font, QsciLexerHTML.ASPJavaScriptNumber)
        self.setFont(self.__font, QsciLexerHTML.ASPJavaScriptStart)
        self.setFont(self.__font, QsciLexerHTML.ASPJavaScriptSymbol)
        self.setFont(self.__font, QsciLexerHTML.ASPJavaScriptWord)
        self.setFont(self.__font, QsciLexerHTML.PHPKeyword)
        self.setFont(self.__font, QsciLexerHTML.PHPOperator)
        self.setFont(self.__font, QsciLexerHTML.PHPSingleQuotedString)
        self.setFont(self.__font, QsciLexerHTML.PHPDoubleQuotedString)
        self.setFont(self.__font, QsciLexerHTML.PHPCommentLine)
        self.setFont(self.__font, QsciLexerHTML.PHPVariable)
        self.setFont(self.__font, QsciLexerHTML.PHPDefault)
        self.setFont(self.__font, QsciLexerHTML.PHPNumber)
        self.setFont(self.__font, QsciLexerHTML.PHPStart)
        self.setFont(self.__font, QsciLexerHTML.PHPVariable)
        self.setFont(self.__font, QsciLexerHTML.PHPDoubleQuotedVariable)
        self.setFont(self.__font, QsciLexerHTML.SGMLBlockDefault)
        self.setFont(self.__font, QsciLexerHTML.SGMLSingleQuotedString)
        self.setFont(self.__font, QsciLexerHTML.SGMLDoubleQuotedString)
        self.setFont(self.__font, QsciLexerHTML.SGMLParameter)
        self.setFont(self.__font, QsciLexerHTML.SGMLEntity)
        self.setFont(self.__font, QsciLexerHTML.SGMLDefault)
        self.setFont(self.__font, QsciLexerHTML.SGMLError)
        self.setFont(self.__font, QsciLexerHTML.SGMLSpecial)
        self.setFont(self.__font, QsciLexerHTML.ASPPythonKeyword)
        self.setFont(self.__font, QsciLexerHTML.ASPPythonTripleSingleQuotedString)
        self.setFont(self.__font, QsciLexerHTML.ASPPythonSingleQuotedString)
        self.setFont(self.__font, QsciLexerHTML.ASPPythonDoubleQuotedString)
        self.setFont(self.__font, QsciLexerHTML.ASPPythonTripleDoubleQuotedString)
        self.setFont(self.__font, QsciLexerHTML.ASPPythonClassName)
        self.setFont(self.__font, QsciLexerHTML.ASPPythonDefault)
        self.setFont(self.__font, QsciLexerHTML.ASPPythonOperator)
        self.setFont(self.__font, QsciLexerHTML.ASPPythonNumber)
        self.setFont(self.__font, QsciLexerHTML.ASPPythonStart)
        self.setFont(self.__font, QsciLexerHTML.ASPPythonFunctionMethodName)
        self.setFont(self.__font, QsciLexerHTML.ASPPythonIdentifier)
        self.setFont(self.__font, QsciLexerHTML.PythonKeyword)
        self.setFont(self.__font, QsciLexerHTML.PythonTripleSingleQuotedString)
        self.setFont(self.__font, QsciLexerHTML.PythonSingleQuotedString)
        self.setFont(self.__font, QsciLexerHTML.PythonDoubleQuotedString)
        self.setFont(self.__font, QsciLexerHTML.PythonTripleDoubleQuotedString)
        self.setFont(self.__font, QsciLexerHTML.PythonClassName)
        self.setFont(self.__font, QsciLexerHTML.PythonDefault)
        self.setFont(self.__font, QsciLexerHTML.PythonOperator)
        self.setFont(self.__font, QsciLexerHTML.PythonNumber)
        self.setFont(self.__font, QsciLexerHTML.PythonStart)
        self.setFont(self.__font, QsciLexerHTML.PythonFunctionMethodName)
        self.setFont(self.__font, QsciLexerHTML.PythonIdentifier)
        self.setFont(self.__font, QsciLexerHTML.Tag)
        self.setFont(self.__font, QsciLexerHTML.UnknownTag)
        self.setFont(self.__font, QsciLexerHTML.Default)

    def keywords(self, style):
        """
        Styling the keywords.

        :param style: int (must)
        :return: None
        """

        if style == 1:
            # HTML tags and its attributes

            return (
                "a abbr acronym address applet area artical aside audio "
                "b base basefont bdo big blockquote body br button "
                "caption canvas center cite code col colgroup command "
                "datalist dd del details dfn dir div dl dt "
                "em embed"
                "fieldset figure font footer form frame frameset "
                "h1 h2 h3 h4 h5 h6 head header hgroup hr html "
                "i iframe img input ins isindex "
                "kbd keygen "
                "label legend li link "
                "map mark menu meta meter "
                "nav noframes noscript "
                "object ol optgroup option output "
                "p param pre progress "
                "q "
                "ruby "
                "s samp script section select small span strike strong style "
                "sub sup "
                "table tbody td textarea tfoot th thead time title tr tt "
                "u ul "
                "var video "
                "wbr "
                "xml xmlns "
                "abbr accept-charset accept accesskey action align "
                "alink alt archive axis "
                "background bgcolor border "
                "cellpadding cellspacing char charoff charset checked "
                "cite class classid clear codebase codetype color "
                "cols colspan compact content coords "
                "data datafld dataformatas datapagesize datasrc "
                "datetime declare defer dir disabled "
                "enctype event "
                "face for frame frameborder "
                "headers height href hreflang hspace http-equiv "
                "id ismap label lang language leftmargin link "
                "longdesc "
                "marginwidth marginheight maxlength media method "
                "multiple "
                "name nohref noresize noshade nowrap "
                "object onblur onchange onclick ondblclick onfocus "
                "onkeydown onkeypress onkeyup onload onmousedown "
                "onmousemove onmouseover onmouseout onmouseup onreset "
                "onselect onsubmit onunload "
                "profile prompt "
                "readonly rel rev rows rowspan rules "
                "scheme scope selected shape size span src standby "
                "start style summary "
                "tabindex target text title topmargin type "
                "usemap "
                "valign value valuetype version vlink vspace "
                "width "
                "text password checkbox radio submit reset file "
                "hidden image "
                "public !doctype")

        if style == 2:
            # ASP.NET

            return (
                "abstract boolean break byte case catch char class const continue "
                "debugger default delete do double else enum export extends final "
                "finally float for function goto if implements import in instanceof "
                "int interface long native new package private protected public "
                "return short static super switch synchronized this throw throws "
                "transient try typeof var void volatile while with"
            )

        if style == 3:
            # Visual Basic

            return (
                "and begin case call continue do each else elseif end "
                "erase error event exit false for function get gosub "
                "goto if implement in load loop lset me mid new next "
                "not nothing on or property raiseevent rem resume "
                "return rset select set stop sub then to true unload "
                "until wend while with withevents attribute alias as "
                "boolean byref byte byval const compare currency date "
                "declare dim double enum explicit friend global "
                "integer let lib long module object option optional "
                "preserve private property public redim single static "
                "string type variant"
            )

        if style == 4:
            # Python {3}! {3}!

            return ("False None True and as assert async await break class continue def del elif else except "
                    "finally for from global if import in is lambda nonlocal not or pass raise return try "
                    "while with yield")

        if style == 5:
            # Cython

            return (
                "and argv as argc break case cfunction class continue "
                "declare default do die "
                "echo else elseif empty enddeclare endfor endforeach "
                "endif endswitch endwhile e_all e_parse e_error "
                "e_warning eval exit extends "
                "false for foreach function global "
                "http_cookie_vars http_get_vars http_post_vars "
                "http_post_files http_env_vars http_server_vars "
                "if include include_once list new not null "
                "old_function or "
                "parent php_os php_self php_version print "
                "require require_once return "
                "static switch stdclass this true var xor virtual "
                "while "
                "__file__ __line__ __sleep __wakeup"
            )


class LexerJava(QsciLexerJava):
    """
    Java Lexer.
    """

    def __init__(self, font, parent=None):
        """
        Initializing method for Lexer Java.

        :param font: QFont (must)
        :param parent: QObject | None
        """

        # Super the class to the parent.
        super().__init__(parent)

        # Defining variables...
        self.__font = font

        self.__comment_kw_color = QColor()
        self.__comment_kw_color.setNamedColor("#fca510")

        self.__kw_color = QColor()
        self.__kw_color.setNamedColor("#3333ff")

        self.__string_color = QColor()
        self.__string_color.setNamedColor("#00aa00")

        # Setting default foreground color...
        self.setColor(self.__comment_kw_color, QsciLexerJava.CommentDocKeyword)
        self.setColor(self.__comment_kw_color, QsciLexerJava.InactiveCommentDocKeyword)
        self.setColor(self.__kw_color, QsciLexerJava.Keyword)
        self.setColor(self.__kw_color, QsciLexerJava.KeywordSet2)
        self.setColor(self.__kw_color, QsciLexerJava.InactiveKeyword)
        self.setColor(self.defaultColor(QsciLexerJava.Default), QsciLexerJava.Operator)
        self.setColor(self.__string_color, QsciLexerJava.SingleQuotedString)
        self.setColor(self.__string_color, QsciLexerJava.DoubleQuotedString)
        self.setColor(self.__string_color, QsciLexerJava.UnclosedString)
        self.setColor(self.__string_color, QsciLexerJava.RawString)
        self.setColor(self.__string_color, QsciLexerJava.VerbatimString)
        self.setColor(self.__string_color, QsciLexerJava.HashQuotedString)
        self.setColor(self.__string_color, QsciLexerJava.InactiveDoubleQuotedString)
        self.setColor(self.__string_color, QsciLexerJava.InactiveHashQuotedString)
        self.setColor(self.__string_color, QsciLexerJava.InactiveRawString)
        self.setColor(self.__string_color, QsciLexerJava.InactiveSingleQuotedString)
        self.setColor(self.__string_color, QsciLexerJava.InactiveTripleQuotedVerbatimString)
        self.setColor(self.__string_color, QsciLexerJava.InactiveUnclosedString)
        self.setColor(self.__string_color, QsciLexerJava.InactiveVerbatimString)
        self.setColor(self.__string_color, QsciLexerJava.TripleQuotedVerbatimString)

        # Setting default font...
        self.setDefaultFont(self.__font)
        self.setFont(self.__font, QsciLexerJava.Comment)
        self.setFont(self.__font, QsciLexerJava.CommentDoc)
        self.setFont(self.__font, QsciLexerJava.CommentDocKeyword)
        self.setFont(self.__font, QsciLexerJava.CommentDocKeywordError)
        self.setFont(self.__font, QsciLexerJava.CommentLine)
        self.setFont(self.__font, QsciLexerJava.CommentLineDoc)
        self.setFont(self.__font, QsciLexerJava.InactiveComment)
        self.setFont(self.__font, QsciLexerJava.InactiveCommentDoc)
        self.setFont(self.__font, QsciLexerJava.InactiveCommentDocKeyword)
        self.setFont(self.__font, QsciLexerJava.InactiveCommentDocKeywordError)
        self.setFont(self.__font, QsciLexerJava.InactiveCommentLine)
        self.setFont(self.__font, QsciLexerJava.InactiveCommentLineDoc)
        self.setFont(self.__font, QsciLexerJava.SingleQuotedString)
        self.setFont(self.__font, QsciLexerJava.DoubleQuotedString)
        self.setFont(self.__font, QsciLexerJava.UnclosedString)
        self.setFont(self.__font, QsciLexerJava.RawString)
        self.setFont(self.__font, QsciLexerJava.VerbatimString)
        self.setFont(self.__font, QsciLexerJava.HashQuotedString)
        self.setFont(self.__font, QsciLexerJava.InactiveDoubleQuotedString)
        self.setFont(self.__font, QsciLexerJava.InactiveHashQuotedString)
        self.setFont(self.__font, QsciLexerJava.InactiveRawString)
        self.setFont(self.__font, QsciLexerJava.InactiveSingleQuotedString)
        self.setFont(self.__font, QsciLexerJava.InactiveTripleQuotedVerbatimString)
        self.setFont(self.__font, QsciLexerJava.InactiveUnclosedString)
        self.setFont(self.__font, QsciLexerJava.InactiveVerbatimString)
        self.setFont(self.__font, QsciLexerJava.TripleQuotedVerbatimString)
        self.setFont(self.__font, QsciLexerJava.Operator)
        self.setFont(self.__font, QsciLexerJava.InactiveOperator)
        self.setFont(self.__font, QsciLexerJava.Number)
        self.setFont(self.__font, QsciLexerJava.Keyword)
        self.setFont(self.__font, QsciLexerJava.KeywordSet2)
        self.setFont(self.__font, QsciLexerJava.InactiveKeyword)
        self.setFont(self.__font, QsciLexerJava.InactiveKeywordSet2)
        
        
class LexerJavaScript(QsciLexerJavaScript):
    """
    JavaScript Lexer.
    """

    def __init__(self, font, parent=None):
        """
        Initializing method for LexerJavaScript.

        :param font: QFont (must)
        :param parent: QObject | None
        """

        # Super the class to the parent
        super().__init__(parent)

        # Defining variables...
        self.__font = font

        self.__default_color = QColor()
        self.__default_color.setNamedColor("#aaaaaa")

        self.__comment_kw_color = QColor()
        self.__comment_kw_color.setNamedColor("#6649cd")

        self.__kw_color = QColor()
        self.__kw_color.setNamedColor("#999900")

        self.__string_color = QColor()
        self.__string_color.setNamedColor("#00aa00")

        # Setting default foreground color...
        self.setDefaultColor(self.__default_color)

        self.setColor(self.__comment_kw_color, QsciLexerJavaScript.CommentDocKeyword)
        self.setColor(self.__comment_kw_color, QsciLexerJavaScript.InactiveCommentDocKeyword)
        self.setColor(self.__kw_color, QsciLexerJavaScript.Keyword)
        self.setColor(self.__kw_color, QsciLexerJavaScript.KeywordSet2)
        self.setColor(self.__kw_color, QsciLexerJavaScript.InactiveKeyword)
        self.setColor(self.defaultColor(QsciLexerJavaScript.Default), QsciLexerJavaScript.Operator)
        self.setColor(self.__string_color, QsciLexerJavaScript.SingleQuotedString)
        self.setColor(self.__string_color, QsciLexerJavaScript.DoubleQuotedString)
        self.setColor(self.__string_color, QsciLexerJavaScript.UnclosedString)
        self.setColor(self.__string_color, QsciLexerJavaScript.RawString)
        self.setColor(self.__string_color, QsciLexerJavaScript.VerbatimString)
        self.setColor(self.__string_color, QsciLexerJavaScript.HashQuotedString)
        self.setColor(self.__string_color, QsciLexerJavaScript.InactiveDoubleQuotedString)
        self.setColor(self.__string_color, QsciLexerJavaScript.InactiveHashQuotedString)
        self.setColor(self.__string_color, QsciLexerJavaScript.InactiveRawString)
        self.setColor(self.__string_color, QsciLexerJavaScript.InactiveSingleQuotedString)
        self.setColor(self.__string_color, QsciLexerJavaScript.InactiveTripleQuotedVerbatimString)
        self.setColor(self.__string_color, QsciLexerJavaScript.InactiveUnclosedString)
        self.setColor(self.__string_color, QsciLexerJavaScript.InactiveVerbatimString)
        self.setColor(self.__string_color, QsciLexerJavaScript.TripleQuotedVerbatimString)

        # Setting default font...
        self.setDefaultFont(self.__font)
        self.setFont(self.__font, QsciLexerJavaScript.Comment)
        self.setFont(self.__font, QsciLexerJavaScript.CommentDoc)
        self.setFont(self.__font, QsciLexerJavaScript.CommentDocKeyword)
        self.setFont(self.__font, QsciLexerJavaScript.CommentDocKeywordError)
        self.setFont(self.__font, QsciLexerJavaScript.CommentLine)
        self.setFont(self.__font, QsciLexerJavaScript.CommentLineDoc)
        self.setFont(self.__font, QsciLexerJavaScript.InactiveComment)
        self.setFont(self.__font, QsciLexerJavaScript.InactiveCommentDoc)
        self.setFont(self.__font, QsciLexerJavaScript.InactiveCommentDocKeyword)
        self.setFont(self.__font, QsciLexerJavaScript.InactiveCommentDocKeywordError)
        self.setFont(self.__font, QsciLexerJavaScript.InactiveCommentLine)
        self.setFont(self.__font, QsciLexerJavaScript.InactiveCommentLineDoc)
        self.setFont(self.__font, QsciLexerJavaScript.SingleQuotedString)
        self.setFont(self.__font, QsciLexerJavaScript.DoubleQuotedString)
        self.setFont(self.__font, QsciLexerJavaScript.UnclosedString)
        self.setFont(self.__font, QsciLexerJavaScript.RawString)
        self.setFont(self.__font, QsciLexerJavaScript.VerbatimString)
        self.setFont(self.__font, QsciLexerJavaScript.HashQuotedString)
        self.setFont(self.__font, QsciLexerJavaScript.InactiveDoubleQuotedString)
        self.setFont(self.__font, QsciLexerJavaScript.InactiveHashQuotedString)
        self.setFont(self.__font, QsciLexerJavaScript.InactiveRawString)
        self.setFont(self.__font, QsciLexerJavaScript.InactiveSingleQuotedString)
        self.setFont(self.__font, QsciLexerJavaScript.InactiveTripleQuotedVerbatimString)
        self.setFont(self.__font, QsciLexerJavaScript.InactiveUnclosedString)
        self.setFont(self.__font, QsciLexerJavaScript.InactiveVerbatimString)
        self.setFont(self.__font, QsciLexerJavaScript.TripleQuotedVerbatimString)
        self.setFont(self.__font, QsciLexerJavaScript.Operator)
        self.setFont(self.__font, QsciLexerJavaScript.InactiveOperator)
        self.setFont(self.__font, QsciLexerJavaScript.Number)
        self.setFont(self.__font, QsciLexerJavaScript.Keyword)
        self.setFont(self.__font, QsciLexerJavaScript.KeywordSet2)
        self.setFont(self.__font, QsciLexerJavaScript.InactiveKeyword)
        self.setFont(self.__font, QsciLexerJavaScript.InactiveKeywordSet2)


class LexerPython2(QsciLexerPython):
    """
    Python 2 Lexer.
    """

    def __init__(self, font, parent=None):
        """
        Initializing method for LexerPython2.

        :param font: QFont (must)
        :param parent: QObject | None
        """

        # Super the class to the parent.
        super().__init__(parent)

        # Defining the variables...
        self.__font = font

        # Initializing settings...
        self.setIndentationWarning(QsciLexerPython.IndentationWarning.Inconsistent)
        self.setV3BinaryOctalAllowed(False)
        self.setV3BytesAllowed(False)

        # Setting default foreground color...
        self.setColor(QColor("#dd0000"), QsciLexerPython.Comment)
        self.setColor(QColor("#ff7700"), QsciLexerPython.Keyword)
        self.setColor(QColor("#0000ff"), QsciLexerPython.FunctionMethodName)
        self.setColor(QColor("#0000ff"), QsciLexerPython.ClassName)
        self.setColor(QColor("#00aa00"), QsciLexerPython.SingleQuotedString)
        self.setColor(QColor("#00aa00"), QsciLexerPython.SingleQuotedFString)
        self.setColor(QColor("#00aa00"), QsciLexerPython.DoubleQuotedString)
        self.setColor(QColor("#00aa00"), QsciLexerPython.DoubleQuotedFString)
        self.setColor(QColor("#00aa00"), QsciLexerPython.TripleSingleQuotedString)
        self.setColor(QColor("#00aa00"), QsciLexerPython.TripleSingleQuotedFString)
        self.setColor(QColor("#00aa00"), QsciLexerPython.TripleDoubleQuotedString)
        self.setColor(QColor("#00aa00"), QsciLexerPython.TripleDoubleQuotedFString)
        self.setColor(QColor("#007700"), QsciLexerPython.UnclosedString)

        # Setting default font...
        self.setDefaultFont(self.__font)
        self.setFont(self.__font, QsciLexerPython.Comment)

    def description(self, style):
        """
        Description: Python 2

        :param style: Q_UNUSED(int)
        :return: 'Python 2'
        """

        return "Python 2"


class LexerPython3(QsciLexerPython):
    """
    Python 3 Lexer.
    """

    def __init__(self, font, parent=None):
        """
        Initializing method for LexerPython3.

        :param font: QFont (must)
        :param parent: QObject | None
        """

        # Super the class to the parent.
        super().__init__(parent)

        # Defining variables...
        self.__font = font

        # Initializing folding settings...
        self.setFoldCompact(True)
        self.setFoldQuotes(True)
        self.setFoldComments(True)

        # Initializing other settings...
        self.setIndentationWarning(QsciLexerPython.IndentationWarning.Inconsistent)
        self.setV2UnicodeAllowed(False)

        # Setting default foreground color...
        self.setColor(QColor("#dd0000"), QsciLexerPython.Comment)
        self.setColor(QColor("#ff7700"), QsciLexerPython.Keyword)
        self.setColor(QColor("#0000ff"), QsciLexerPython.FunctionMethodName)
        self.setColor(QColor("#0000ff"), QsciLexerPython.ClassName)
        self.setColor(QColor("#00aa00"), QsciLexerPython.SingleQuotedString)
        self.setColor(QColor("#00aa00"), QsciLexerPython.SingleQuotedFString)
        self.setColor(QColor("#00aa00"), QsciLexerPython.DoubleQuotedString)
        self.setColor(QColor("#00aa00"), QsciLexerPython.DoubleQuotedFString)
        self.setColor(QColor("#00aa00"), QsciLexerPython.TripleSingleQuotedString)
        self.setColor(QColor("#00aa00"), QsciLexerPython.TripleSingleQuotedFString)
        self.setColor(QColor("#00aa00"), QsciLexerPython.TripleDoubleQuotedString)
        self.setColor(QColor("#00aa00"), QsciLexerPython.TripleDoubleQuotedFString)
        self.setColor(QColor("#007700"), QsciLexerPython.UnclosedString)

        # Setting default font...
        self.setDefaultFont(self.__font)
        self.setFont(self.__font, QsciLexerPython.Comment)

    def description(self, style):
        """
        Description: Python 3

        :param style: Q_UNUSED(int)
        :return: 'Python 3'
        """

        return "Python 3"

    def keywords(self, style):
        """
        Returns the keywords of the python language.

        :param style: int
        :return: {import keywords; ' '.join(keywords.kwlist)}
        """

        if style == 1:
            # If style == 1:

            return ("False None True and as assert async await break class continue def del elif else except "
                    "finally for from global if import in is lambda nonlocal not or pass raise return try "
                    "while with yield")
