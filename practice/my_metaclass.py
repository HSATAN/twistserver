# _*_ coding:utf-8 _*_
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
def choose_class(classname=None, parent=(),attr={}):
    attrs = ((name, value) for name, value in attr.items() if not name.startswith('__'))
    uppersttrs = dict((name.upper(), value) for name, value in attrs)
    return type(classname, parent,uppersttrs)

class Foo(object):

    __metaclass__ =  choose_class

    fib = "这个属性名会被转为大写"

foo = Foo()
print(foo.FIB)
print(hasattr(foo, "FIB"))
foo.fib = "这是新属性"
print(foo.fib)
print(foo.__class__)


class UpperAttr(object):
    # def __new__(cls, name, bases, attrdict,  *args, **kwargs):
    #     attrs = ((name, value) for name, value in attrdict.items() if  not name.startswith('__'))
    #     upperattrs = dict((name.upper(), value) for name, value in attrs)
    #     return super(UpperAttr, cls).__new__(cls, name,bases,upperattrs, *args, **kwargs)
    # lll = "zhe shi xiao xie"
    def __new__(cls, *args, **kwargs):
        print('__new__')
        return object.__new__(cls,*args, **kwargs)
    def __call__(self, *args, **kwargs):
        print('__call__')
        return "nihao"

ins = UpperAttr()
data = ['this is the first document',
        'this is the second document']
vectorizer = CountVectorizer()
tfidftra = TfidfTransformer()
X = vectorizer.fit_transform(data)
tfidf = tfidftra.fit_transform(X)
print(X)
print(vectorizer.get_feature_names())
print(tfidf)
