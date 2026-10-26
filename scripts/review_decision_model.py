import copy,hashlib,json
from pathlib import Path
from arxis.core import FIXTURE,trace,assess_change
ROOT=Path(__file__).resolve().parents[1]

def main():
    normal=assess_change(FIXTURE,'REQ-1','lead',['lead'],{'ART-1':'2'})
    stale=assess_change(FIXTURE,'REQ-1','lead',['lead'],{'ART-1':'1'})
    broken=copy.deepcopy(FIXTURE); broken['decisions'].append(dict(id='D4',requirement_ids=['REQ-1'],text='Second decision'))
    assert not trace(broken)[0]['complete'] and stale['status']=='pause' and not normal['approval_granted']
    r=dict(id='ARXIS-MANAGEMENT-REVIEW-001',normal=normal,stale=stale,uncovered_decision_detected=True,
           costs=dict(base=4*60+10,bottleneck=8*60+10,unit='synthetic EUR/change'),
           model_sha256=hashlib.sha256((ROOT/'src/arxis/core.py').read_bytes()).hexdigest(),
           limitations=['Structural traceability only','Authority input is not authentication','No actual drawings or engineering approval'])
    (ROOT/'artifacts/management-review.json').write_text(json.dumps(r,indent=2)+'\n')
    (ROOT/'docs/MODEL-VALIDATION-MEMO.md').write_text('''# ARXIS — validation and decision memo

Private synthetic study. Seven repository tests check traceability, missing artifacts, duplicate/dangling IDs, uncovered decisions, rule-based classification disclosure and actor/version controls.

## Result and forecast

The complete three-requirement fixture has structural coverage; removing an artifact or adding an uncovered decision exposes a gap. A version mismatch pauses the change; a recognized actor with matching versions is ready for human impact review, never automatically approved. The original completeness/negative-case prediction holds within this authored fixture.

The pre-recorded coordination-cost case gives EUR 250 per change at four hours and EUR 490 at eight hours. This is assumed effort cost, not a measured saving. Doubling review time does not double the fixed EUR 10 tooling allocation.

## Decision and limitations

Continue with a controlled requirements/decision/version register and a human change-review workflow. Do not infer engineering correctness from graph completeness or deploy the actor-input check as an access-control system. Obtain actual scope, approver mandate, cost and schedule implications before issuing a change.

## Post-mortem

Earlier completeness checked whether any artifact existed beneath a requirement; it could conceal an uncovered second decision. The revised check requires every linked decision to be represented. Duplicate and dangling references are rejected. The reference classifier remains deterministic keyword matching, not a trained AI model. A controlled spreadsheet or existing document system may meet the need without new software.

Handoff: DELIVERY-SPECIFICATION.md, source fixture, tests and artifacts/management-review.json. No client adoption, construction saving or regulatory compliance is claimed.
''')
    print(json.dumps(r,indent=2))
if __name__=='__main__': main()
