import random

from interfaces import TestSelector, SDCTest


class SampleTestSelector(TestSelector):
    """
    This is a sample test selector implementing the TestSelector interface.
    """
    def __init__(self, test):
        pass

    def initialize(self, test_suite: list[SDCTest]) -> None:
        pass

    def select(self, test_suite: list[SDCTest]) -> list[bool]:
        return [random.random() < 0.5 for _ in test_suite]

    def name(self) -> str:
        return 'sample_test_selector'
