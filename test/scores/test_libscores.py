# -*- encoding: utf-8 -*-
from __future__ import print_function
import unittest

import numpy as np

from autosklearn.metrics import acc_metric


class LibScoresTest(unittest.TestCase):
    _multiprocess_can_split_ = True

    def test_accuracy_metric_4_binary_classification(self):
        # 100% correct
        expected = np.array([0, 1, 1, 1, 0, 0, 1, 1, 1, 0]).reshape((-1, 1))
        prediction = expected.copy()
        score = acc_metric(expected, prediction)
        self.assertEqual(1, score)

        # 100% incorrect
        prediction = (expected.copy() - 1) * -1
        score = acc_metric(expected, prediction)
        self.assertAlmostEqual(-1, score)

        # Random
        prediction = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])
        score = acc_metric(expected, prediction)
        self.assertAlmostEqual(0, score)

    def test_accuracy_metric_4_multiclass_classification(self):
        # 100% correct
        expected = np.array([[0, 0, 1, 1, 0, 1, 0, 1, 0, 1],
                             [1, 1, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0,
                                                              1, 0, 1, 0]])
        prediction = expected.copy()
        score = acc_metric(expected, prediction)
        self.assertEqual(1, score)

        # 100% incorrect
        prediction = (expected.copy() - 1) * -1
        score = acc_metric(expected, prediction)
        self.assertAlmostEqual(-1, score)

        # Pseudorandom
        prediction = np.array([[1, 0, 0, 1, 0, 0, 1, 0, 0, 1], [0, 1, 0, 0, 1,
                                                                0, 0, 1, 0, 0],
                               [0, 0, 1, 0, 0, 1, 0, 0, 1, 0]])
        score = acc_metric(expected, prediction)
        self.assertAlmostEqual(0.33333333, score)

    def test_accuracy_metric_4_multilabel_classification(self):
        # 100% correct
        expected = np.array([[0, 0, 1, 1, 0, 1, 0, 1, 0, 1],
                             [1, 1, 0, 0, 1, 0, 1, 0, 1, 0], [1, 1, 0, 0, 1, 0,
                                                              1, 0, 1, 0]])
        prediction = expected.copy()
        score = acc_metric(expected, prediction)
        self.assertEqual(1, score)

        # 100% incorrect
        prediction = (expected.copy() - 1) * -1
        score = acc_metric(expected, prediction)
        self.assertAlmostEqual(-1, score)

        # Pseudorandom
        prediction = np.array([[0, 0, 0, 0, 0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0,
                                                                1, 1, 1, 1, 1],
                               [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]])
        score = acc_metric(expected, prediction)
        self.assertAlmostEqual(-0.0666666666, score)
