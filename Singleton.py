# -*- coding: utf-8 -*-

class Singleton(type):
    """单实例元类，用于某个类需要实现单例模式。
    使用方式示例如下::
    class MyClass(object):
        __metaclass__ = Singleton
        def __init__(self, *args, **kwargs):
            pass
    
    """
    _instances = {}
    def __init__(cls, name, bases, dic):
        super(Singleton, cls).__init__(name, bases, dic)
        cls._instances = {}
        
    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            self._instances[self] = super(Singleton, self).__call__(*args, **kwargs)          
        return self._instances[self]


class MyClass(object):
      __metaclass__ = Singleton
      def __init__(self, *args, **kwargs):
          pass

if __name__ == '__main__':
    s1 = MyClass()
    s2 = MyClass()

    if s1 == s2:
      print 'yes'