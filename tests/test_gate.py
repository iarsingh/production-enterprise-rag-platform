from fastapi.testclient import TestClient
from prodrag.main import app

client = TestClient(app)


def test_pass_and_fail():
    good = client.post("/check", json={'citation': 'runbook.md:3', 'image_digest': 'sha256:abc', 'image': 'api:1.2.3'}).json()
    assert good["passed"] is True
    assert good["applied"] is False
    bad = client.post("/check", json={'citation': 'runbook.md:3', 'image': 'api:latest'}).json()
    assert bad["passed"] is False
    assert "image_tag_latest" in bad["failed"]
