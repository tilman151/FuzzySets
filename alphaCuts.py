"""The alphaCuts module.

Module for the first assignment of Fuzzy Systems

"""
import collections


class FuzzySet(collections.OrderedDict):
    """This class implements a horizontal representation of a fuzzy set.

    After calling the constructor add an alpha cut using the []-Operator. An
    alpha cut is represented as a list of tuples. Each tuple is an interval
    of the cut.

    Example:
        >>> import alphaCuts
        >>> s = alphaCuts.FuzzySet([0.4,0.3,1.0])
        >>> s[1.0] = [(1, 2), (4,6)]

    """
    def __init__(self, degrees):
        """Initialzize the fuzzy set with a finite number of membership degrees.

        It is checked whether the memberships are in the real interval.

        Args:
            degrees (:obj:`list` of :obj:`int`): List of membership degrees

        """
        if all(0 <= item <= 1.0 for item in degrees):
            emptyLists = [[] for x in xrange(len(degrees))]
            dictData = zip(sorted(degrees, reverse=True), emptyLists)
            super(FuzzySet, self).__init__(dictData)
        else:
            raise ValueError("Membership degrees have to be in [0,1]")

    def getMembershipDegree(self, instance):
        """
        Return the membership degree of an arbirary real number concerning
        this fuzzy set.

        Args:
            instance (float): Instance of interest

        """
        for (key, list) in self.iteritems():
            for (begin, end) in list:
                if (instance >= begin and instance <= end):
                    return key

        return 0.0
