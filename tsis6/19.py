def test(a):
        def add(b):
                nonlocal a
                a += 1
                print(a)
                print(b)
                return a+b
        return add
func= test(4)
print(func(4))