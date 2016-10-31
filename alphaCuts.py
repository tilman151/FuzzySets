import collections


class FuzzySet(collections.OrderedDict):
    """docstring for ."""
    def __init__(self, degrees):
        if (all(item <= 1.0 for item in degrees)
                and all(item >= 0 for item in degrees)):
            super(FuzzySet, self).__init__(zip(
                sorted(degrees, reverse=True),
                [[] for x in xrange(len(degrees))]
                ))
        else:
            raise ValueError("Membership degrees have to be in [0,1]")

    def getMembershipDegree(self, instance):
        for (key, list) in self.iteritems():
            for (begin, end) in list:
                if (instance >= begin and instance <= end):
                    return key

        return 0.0
