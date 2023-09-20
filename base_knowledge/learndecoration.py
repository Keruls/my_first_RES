# 装饰器
def decoration(old_fn):
    # *args, **kwargs accept any params.
    def make_new(*args, **kwargs):
        print('decorated begin!')
        # *args, **kwargs are analysed.
        old_fn(*args, **kwargs)
        print('decorated end!')
    return make_new

def fn1(a):
    print('i am fn1,my param is:', a)

# 装饰方法1
fn3 = decoration(fn1)
fn3(456)

# 装饰方法2,fn2被装饰了
@decoration
def fn2(a: int, b: str):
    print('i am fn1,my param is:%d and %s' % (a, b))

fn2(1111, 'ppppp')