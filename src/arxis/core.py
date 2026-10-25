from __future__ import annotations
import hashlib, json
from pathlib import Path

PROJECT_ID="PRJ-ARXIS-PROTOTYPE"
FIXTURE={"project":"Synthetic residence","requirements":[{"id":"REQ-1","text":"Provide step-free entrance"},{"id":"REQ-2","text":"Limit operational energy demand"},{"id":"REQ-3","text":"Document fire egress"}],"decisions":[{"id":"DEC-1","requirement_ids":["REQ-1"],"text":"Use flush threshold and ramp"},{"id":"DEC-2","requirement_ids":["REQ-2"],"text":"Use high-performance envelope"},{"id":"DEC-3","requirement_ids":["REQ-3"],"text":"Provide protected egress route"}],"artifacts":[{"id":"ART-1","decision_ids":["DEC-1"],"version":"2","name":"access-plan-v2.pdf"},{"id":"ART-2","decision_ids":["DEC-2"],"version":"3","name":"energy-note-v3.pdf"},{"id":"ART-3","decision_ids":["DEC-3"],"version":"1","name":"fire-strategy-v1.pdf"}]}
def classify(name,text=""):
    value=(name+" "+text).lower()
    for label,keys in {"fire-safety":["fire","egress"],"energy":["energy","envelope"],"accessibility":["access","ramp"],"drawing":["plan","section"]}.items():
        if any(k in value for k in keys): return {"suggested_type":label,"confidence":"rule-match","human_review_required":True}
    return {"suggested_type":"unclassified","confidence":"none","human_review_required":True}
def trace(project):
    decisions={d["id"]:d for d in project["decisions"]}; matrix=[]
    for req in project["requirements"]:
        ds=[d["id"] for d in project["decisions"] if req["id"] in d["requirement_ids"]]
        arts=[a["id"] for a in project["artifacts"] if any(d in a["decision_ids"] for d in ds)]
        matrix.append({"requirement_id":req["id"],"decision_ids":ds,"artifact_ids":arts,"complete":bool(ds and arts)})
    return matrix
def run(root: Path):
    (root/"data").mkdir(parents=True,exist_ok=True); (root/"artifacts").mkdir(parents=True,exist_ok=True)
    (root/"data/sample_project.json").write_text(json.dumps(FIXTURE,indent=2),encoding="utf-8")
    matrix=trace(FIXTURE); broken=json.loads(json.dumps(FIXTURE)); broken["artifacts"]=[a for a in broken["artifacts"] if a["id"]!="ART-3"]; broken_matrix=trace(broken)
    classifications={a["id"]:classify(a["name"]) for a in FIXTURE["artifacts"]}
    result={"project_id":PROJECT_ID,"claim_scope":"synthetic documentation-workflow demonstration","traceability_matrix":matrix,"coverage":sum(x["complete"] for x in matrix)/len(matrix),"negative_test_detected":not all(x["complete"] for x in broken_matrix),"classifications":classifications,"prediction_passed":all(x["complete"] for x in matrix) and not all(x["complete"] for x in broken_matrix)}
    (root/"artifacts/results.json").write_text(json.dumps(result,indent=2),encoding="utf-8"); (root/"artifacts/traceability-matrix.json").write_text(json.dumps(matrix,indent=2),encoding="utf-8")
    arts=[]
    for rel in ["artifacts/results.json","artifacts/traceability-matrix.json","data/sample_project.json"]:
        p=root/rel; arts.append({"artifact_id":"ART-"+hashlib.sha256(rel.encode()).hexdigest()[:12].upper(),"path":rel,"sha256":hashlib.sha256(p.read_bytes()).hexdigest(),"validation_status":"tested","reproduce_command":"make reproduce"})
    (root/"artifacts/evidence-manifest.json").write_text(json.dumps({"project_id":PROJECT_ID,"generated":"2026-10-25","data_class":"synthetic","artifacts":arts},indent=2),encoding="utf-8")
    return result
