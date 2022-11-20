# Should not use MRO as it is too complex
# Life is already complex - don't make it more stressful
# MRO - Method Resolution Order
class A:
    num = 10
    pass


class B(A):
    pass


class C(A):
    num = 1
    pass


class D(B, C):
    pass


print(D.num)
print(D.mro())


#########################################################
class X: pass


class Y: pass


class Z: pass


class A(X, Y): pass


class B(Y, Z): pass


class M(B, A, Z): pass


# ORDER: M -> B -> A -> X -> Y -> Z: Depth First Search
print(M.mro())