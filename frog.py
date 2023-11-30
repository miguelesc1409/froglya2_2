import re

from pygments.lexer import RegexLexer, bygroups
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Number, Punctuation

__all__ = ['FrogLexer']

class FrogLexer(RegexLexer):
    """
    Lexer for Frog files.
    """
    name = 'Frog'
    aliases = ['frog']
    filenames = ['*.fg']
    mimetypes = ['text/x-frog']

    tokens = {
        'root': [
            (r'\#', Comment.Single),
            # literal with prepended base
            (r'\d\d?\'[a-zA-Z0-9]+', Number.Integer),
            (r'(\d+\.\d*|\d*\.\d+)([eE][+-]?[0-9]+)?', Number.Float),
            (r'\d+', Number.Integer),
            (r'[\[\](){}|.,;!]', Punctuation),
            (r'"(?:\\x[0-9a-fA-F]+\\|\\u[0-9a-fA-F]{4}|\\U[0-9a-fA-F]{8}|'
             r'\\[0-7]+\\|\\["\\abcefnrstv]|[^\\"])*"', String.Double),
            (r'[& | \| | \!]', Operator),
            (r'([\b\+\b]|[\b\-\b]|[\b\*\b]|[\b\^\b]|[\b\/\b]|[\b\%\b])\b', Operator),
            (r'_', Keyword),  # The don't-care variable
            (r'[int|real|str]', Keyword),
            (r'[during|if|do|but]', Keyword),
            (r'([a-z]+)(:)', bygroups(Name.Namespace, Punctuation)),
            (r'([a-z\u00c0-\u1fff\u3040-\ud7ff\ue000-\uffef]'
             r'[\w$\u00c0-\u1fff\u3040-\ud7ff\ue000-\uffef]*)'
             r'(\s*)(:-|-->)',
             bygroups(Name.Function, Text, Operator)),  # function defn
            (r'([a-z\u00c0-\u1fff\u3040-\ud7ff\ue000-\uffef]'
             r'[\w$\u00c0-\u1fff\u3040-\ud7ff\ue000-\uffef]*)'
             r'(\s*)(\()',
             bygroups(Name.Function, Text, Punctuation)),
            (r'[a-z\u00c0-\u1fff\u3040-\ud7ff\ue000-\uffef]'
             r'[\w$\u00c0-\u1fff\u3040-\ud7ff\ue000-\uffef]*',
             String.Atom),  # atom, characters
            # This one includes !
            (r'[#&*+\-./:<=>?@\\^~\u00a1-\u00bf\u2010-\u303f]+',
             String.Atom),  # atom, graphics
            (r'[A-Z_]\w*', Name.Variable),
            (r'\s+|[\u2000-\u200f\ufff0-\ufffe\uffef]', Text),
        ]
    }
