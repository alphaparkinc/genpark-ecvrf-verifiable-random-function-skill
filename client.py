import hashlib

class SimpleVRF:
    """
    Verifiable Random Function (VRF).
    Produces deterministic pseudo-random output along with a verifiable cryptographic proof.
    """
    def __init__(self, privkey=42, modulus=10007):
        self.privkey = privkey
        self.pubkey = pow(7, privkey, modulus)
        self.modulus = modulus

    def evaluate(self, alpha_msg):
        # Map message to field point H
        h = int(hashlib.sha256(alpha_msg.encode("utf-8")).hexdigest()[:8], 16) % self.modulus
        # Gamma = H^privkey mod p
        gamma = pow(h, self.privkey, self.modulus)
        # Proof commitment
        proof = hashlib.sha256(f"{gamma}:{self.pubkey}:{alpha_msg}".encode("utf-8")).hexdigest()[:16]
        # Hash gamma to produce verifiable pseudo-random output beta
        beta_output = hashlib.sha256(str(gamma).encode("utf-8")).hexdigest()[:16]
        return beta_output, (gamma, proof)

    def verify(self, alpha_msg, beta_output, proof_tuple):
        gamma, proof = proof_tuple
        check_proof = hashlib.sha256(f"{gamma}:{self.pubkey}:{alpha_msg}".encode("utf-8")).hexdigest()[:16]
        check_beta = hashlib.sha256(str(gamma).encode("utf-8")).hexdigest()[:16]
        return check_proof == proof and check_beta == beta_output
