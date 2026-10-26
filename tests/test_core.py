import copy, unittest
from arxis.core import FIXTURE, trace, classify, assess_change
class TraceabilityTest(unittest.TestCase):
    def test_complete_fixture(self): self.assertTrue(all(x["complete"] for x in trace(FIXTURE)))
    def test_broken_fixture(self):
        x=copy.deepcopy(FIXTURE); x["artifacts"]=x["artifacts"][:-1]; self.assertFalse(all(v["complete"] for v in trace(x)))
    def test_classifier_discloses_review(self): self.assertTrue(classify("fire-strategy.pdf")["human_review_required"])
    def test_every_decision_needs_artifact(self):
        x=copy.deepcopy(FIXTURE); x['decisions'].append(dict(id='D4',requirement_ids=['REQ-1'],text='Additional obligation'))
        self.assertFalse(trace(x)[0]['complete'])
    def test_duplicate_and_dangling_rejected(self):
        x=copy.deepcopy(FIXTURE); x['artifacts'].append(x['artifacts'][0])
        with self.assertRaises(ValueError): trace(x)
        x=copy.deepcopy(FIXTURE); x['artifacts'][0]['decision_ids']=['MISSING']
        with self.assertRaises(ValueError): trace(x)
    def test_authority_and_version(self):
        with self.assertRaises(ValueError): assess_change(FIXTURE,'REQ-1','outsider',['lead'],{'ART-1':'2'})
        r=assess_change(FIXTURE,'REQ-1','lead',['lead'],{'ART-1':'1'})
        self.assertEqual(r['status'],'pause')
        r=assess_change(FIXTURE,'REQ-1','lead',['lead'],{'ART-1':'2'})
        self.assertFalse(r['approval_granted']); self.assertEqual(r['affected_artifacts'],['ART-1'])
