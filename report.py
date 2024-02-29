import sys
try:
    class define:
        def __init__(self, reign, period):
            self.period = period
            self.reign = reign
            __annotations__.__class__.__contains__.__call__.__class__.__hash__
        def  __init_subclass__(self):
            return self.reign, self.period
        def boom(self):
            return self.period, self.reign
    class report(define):
        def __init__(self, reign, period):
            super(report, self).__init__(reign, period)
    signal = report(sys.argv[1], sys.argv[2])
    signal.boom()
except:
    print("Nope")