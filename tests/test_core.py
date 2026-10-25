import copy, unittest
from arxis.core import FIXTURE, trace, classify
class TraceabilityTest(unittest.TestCase):
    def test_complete_fixture(self): self.assertTrue(all(x["complete"] for x in trace(FIXTURE)))
    def test_broken_fixture(self):
        x=copy.deepcopy(FIXTURE); x["artifacts"]=x["artifacts"][:-1]; self.assertFalse(all(v["complete"] for v in trace(x)))
    def test_classifier_discloses_review(self): self.assertTrue(classify("fire-strategy.pdf")["human_review_required"])
