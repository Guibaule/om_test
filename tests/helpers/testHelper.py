def test(message: str, test, before = None, after = None):
    if(before is not None): before()
    print(message)
    test()

    if(after is not None): after()