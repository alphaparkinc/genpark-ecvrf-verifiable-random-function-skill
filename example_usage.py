from client import SimpleVRF

def main():
    print("=== Testing Verifiable Random Function (VRF) ===")
    vrf = SimpleVRF(privkey=137)
    
    seed = "epoch_round_1048576"
    beta, proof = vrf.evaluate(seed)
    print(f"Seed: {seed}")
    print(f"VRF Random Output (Beta): {beta}")
    print(f"VRF Proof (Gamma, Hash): {proof}")
    
    valid = vrf.verify(seed, beta, proof)
    print(f"Verification Result: {valid}")
    assert valid, "VRF verification failed"
    
    tampered_valid = vrf.verify("wrong_epoch", beta, proof)
    print(f"Tampered Seed Verification (should be False): {tampered_valid}")
    assert not tampered_valid, "Tampered verification succeeded unexpectedly"
    print("=== VRF Verification Complete ===")

if __name__ == "__main__":
    main()
