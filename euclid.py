import sys

def debug ( *args , **kwargs ) :
    print(*args, file=sys.stderr, **kwargs)

def extended_euclidean_algorithm ( a , b , sa = 1 , ta = 0 , sb = 0 , tb = 1 ) :

    assert(sa * sb <= 0)
    assert(ta * tb <= 0)

    yield (a, sa, ta)
    if b == 0:
        yield (b, sb, tb)

    else:
        q, _a = a // b, a % b
        _sa = sa - q * sb
        _ta = ta - q * tb
        debug('='*79)
        debug('_a = {} = {} - {} * {}'.format(_a, a, q, b))
        debug('_sa = {} = {} - {} * {}'.format(_sa, sa, q, sb))
        debug('_ta = {} = {} - {} * {}'.format(_ta, ta, q, tb))
        debug('='*79)
        # assert(abs(sb) <= 1 or q <= abs(sb)) # NOT TRUE although q is usually very small
        # assert(abs(tb) <= 1 or q <= abs(tb)) # NOT TRUE although q is usually very small
        yield from extended_euclidean_algorithm( b, _a, sb, tb, _sa, _ta)

if __name__ == '__main__' :
    a = int(sys.argv[1])
    b = int(sys.argv[2])

    for step, (d,x,y) in enumerate(extended_euclidean_algorithm(a,b)):
        print(step, d, x, y)
        assert(b == 0 or abs(x) <= b)
        assert(a == 0 or abs(y) <= a)
        assert(d == x * a + y * b)
        if step % 2 == 0:
            assert(x > 0)
            assert(y <= 0)
        else:
            assert(x <= 0)
            assert(y > 0)
