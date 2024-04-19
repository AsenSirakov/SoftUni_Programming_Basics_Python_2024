def generate_large_prime():
    return random.choice([101, 103, 107, 109, 113, 127, 131, 137, 139, 149])

def generate_private_key():
    return random.randint(2, 100)

def compute_public_key(private_key, g, p):
    return pow(g, private_key, p)

def compute_shared_secret(public_key, private_key, p):
    return pow(public_key, private_key, p)

def factorize_number(number):
    start_time = time.time()
    factors = factorint(number)
    factorization_time = time.time() - start_time
    return factors, factorization_time

def simulate_diffie_hellman():
    p = generate_large_prime()
    g = random.randint(2, p - 1)
    private_key_A = generate_private_key()
    private_key_B = generate_private_key()
    public_key_A = compute_public_key(private_key_A, g, p)
    public_key_B = compute_public_key(private_key_B, g, p)
    shared_secret_A = compute_shared_secret(public_key_B, private_key_A, p)
    shared_secret_B = compute_shared_secret(public_key_A, private_key_B, p)
    assert shared_secret_A == shared_secret_B
    return shared_secret_A, p, g, public_key_A, public_key_B

def simulate_eavesdropper(public_key_A, public_key_B, p):
    shared_secret_E = compute_shared_secret(public_key_B, private_key_A, p)
    return shared_secret_E
shared_secret_A, p, g, public_key_A, public_key_B = simulate_diffie_hellman()
private_key_A = generate_private_key()  # Eavesdropper generates its own private key
shared_secret_E = simulate_eavesdropper(public_key_A, public_key_B, p)
print("Shared Secret (A and B):", shared_secret_A)
print("Shared Secret (Eavesdropper):", shared_secret_E)