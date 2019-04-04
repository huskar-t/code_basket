# 单例模式

#### 功能介绍
单例模式实现

#### 使用说明

1. 需要单例模式的类使用如下
    class SessionMgr(object):
        __metaclass__ = Singleton
注：metaclass的实例化结果是类，而class实例化的结果是instance。
metaclass是类似创建类的模板，所有的类都是通过他来create的(调用__new__)，这使得你可以自由的控制
创建类的那个过程，实现你所需要的功能。

