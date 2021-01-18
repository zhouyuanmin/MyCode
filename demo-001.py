"""
使用装饰器限制函数的调用次数
"""

import functools


def call_limit(count):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if decorator.calls >= count:
                raise AssertionError(f"单个程序最多允许调用此方法{count}次")
            decorator.calls += 1
            return func(*args, **kw)

        decorator.calls = 0
        return wrapper

    return decorator


@call_limit(5)
def demo(a, b):
    print(a, b)


if __name__ == '__main__':
    for i in range(20):
        demo(i, i ** 2)
