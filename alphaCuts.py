"""The alphaCuts module.

Module for the first assignment of Fuzzy Systems

"""
import collections


class FuzzySet(collections.OrderedDict):
    """This class implements a horizontal representation of a fuzzy set.

    The constructor receives a list of membership degrees. It is checked,
    whether the degrees are in [0,1]. If not an exception is raised. The
    ordered list of degrees is passed to the constructor of the super class.

    Args:
        degrees (:obj:`list` of float): List of membership degrees for the
        alpha cuts of the fuzzy set

    """
    def __init__(self, degrees):
        if (all(item <= 1.0 for item in degrees) and
                all(item >= 0 for item in degrees)):
            super(FuzzySet, self).__init__(zip(
                sorted(degrees, reverse=True),
                [[] for x in xrange(len(degrees))]
                ))
        else:
            raise ValueError("Membership degrees have to be in [0,1]")

    """
    Returns the membership degree of an arbirary real number concerning this
    fuzzy set.

    Args:
        instance (float): Instance of interest

    """
    def getMembershipDegree(self, instance):
        for (key, list) in self.iteritems():
            for (begin, end) in list:
                if (instance >= begin and instance <= end):
                    return key

        return 0.0
