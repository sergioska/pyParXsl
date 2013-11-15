__author__ = 'sergioska'

import abc


class AbstractProcessor(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self, content, stylesheet):
        self.content = content
        self.stylesheet = stylesheet

    @abc.abstractmethod
    def process(self):
        raise NotImplementedError


