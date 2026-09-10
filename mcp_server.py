from client import SimpleVRF
import json

def handle_request(req):
    vrf = SimpleVRF()
    action = req.get("action")
    if action == "evaluate":
        alpha = req.get("alpha", "")
        beta, proof = vrf.evaluate(alpha)
        return {"status": "ok", "beta": beta, "proof": proof}
    elif action == "verify":
        alpha = req.get("alpha", "")
        beta = req.get("beta", "")
        proof = tuple(req.get("proof", []))
        valid = vrf.verify(alpha, beta, proof)
        return {"status": "ok", "valid": valid}
    return {"status": "error", "message": "Unknown action"}

if __name__ == "__main__":
    print(json.dumps(handle_request({"action": "evaluate", "alpha": "test"})))
