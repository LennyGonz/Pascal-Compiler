# coding=utf-8

TYPE_VARIABLE = 'var'  # var a;
TYPE_FUNCTION = 'func'  # (a + 1) == 2
TYPE_PROCEDURE = 'pro'
TYPE_EXPRESSIONS = 'expr'  # a = 1.0;
TYPE_STATEMENTS = 'stat'  # int pow(int n, int m)
TYPE_PARAMETER = 'par'
TYPE_ARRAY = 'arr'

class SymbolObject(object):
    """
    Key for symbol table hashmap
    static int k;
    name: k
    data_type: int
    attribute: static
    kind: var
    """
    def __init__(self, name, type_of_object, data_type, dp=None, attribute=None, others=None):
        self.name = name
        self.type_of_object = type_of_object
        self.data_type = data_type
        if attribute is not None:
            for attr, value in attribute.iteritems():
                self.__setattr__(attr, value)
        self.dp = dp
        if others is None:
            self.others = others
        else:
            self.others = []

    def __unicode__(self):
        return '<%s, %s, %i, %s>' % (self.name, self.type_of_object, self.dp, self.data_type)

    def __repr__(self):
        return '<%s, %s, %i, %s>' % (self.name, self.type_of_object, self.dp, self.data_type)

