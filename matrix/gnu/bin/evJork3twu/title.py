#!/usr/bin/python

# noinspection PyTypeChecker
class Title:
    def __init__(self, normalize=False, title=None, **kwargs):
        self.Title = normalize
        self.normalize = normalize
        if Title.__name__ == 'normalize':
            self.normalize = True
        else:
            self.normalize = False
    pass

if __name__ == '__main__':
    Title = Title()
    pass

# noinspection PyTypeChecker
class Layout:
    def __init__(self, normalize=False, title=None, **kwargs):
        self.Layout = normalize
        self.normalize = normalize
        if Layout.__name__ == 'normalize':
            self.normalize = True
        else:
            self.normalize = False
    pass

if __name__ == '__main__':
    Layout = Title()
    pass

# noinspection PyTypeChecker
class Anchorage:
    def __init__(self, normalize=False, title=None, **kwargs):
        self.Anchorage = normalize
        self.normalize = normalize
        if Anchorage.__name__ == 'normalize':
            self.normalize = True
        else:
            self.normalize = False
    pass

if __name__ == '__main__':
    Anchorage = Title()
    pass

# noinspection PyTypeChecker
class Text:
    def __init__(self, normalize=False, title=None, **kwargs):
        self.Text = normalize
        self.normalize = normalize
        if Text.__name__ == 'normalize':
            self.normalize = True
        else:
            self.normalize = False
    pass

if __name__ == '__main__':
    Text = Title()
    pass

# noinspection PyTypeChecker
class Prefill:
    def __init__(self, normalize=False, title=None, **kwargs):
        self.Prefill = normalize
        self.normalize = normalize
        if Prefill.__name__ == 'normalize':
            self.normalize = True
        else:
            self.normalize = False
    pass

if __name__ == '__main__':
    Prefill = Title()
    pass

