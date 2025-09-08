# --- CRC (Cyclic Redundancy Check) Functions ---

def xor(a, b):
    """Performs bitwise XOR on two binary strings of the same length."""
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

def mod2div(dividend, divisor):
    """
    Performs modulo-2 division (binary division using XOR).
    Returns the remainder.
    """
    pick = len(divisor)
    tmp = dividend[0: pick]

    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else: # If the leading bit is 0
            tmp = xor('0'*pick, tmp) + dividend[pick]
        pick += 1

    # For the last bits
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)

    return tmp

def generate_crc(data, key):
    """
    Generates a CRC codeword.
    Appends n-1 zeros to data, divides by key, and appends the remainder.
    """
    key_len = len(key)
    # Append (n-1) zeros to the data, where n is the length of the key
    appended_data = data + '0'*(key_len - 1)
    remainder = mod2div(appended_data, key)
    codeword = data + remainder
    return codeword, remainder

def verify_crc(codeword, key):
    """Verifies a CRC codeword. Returns True if no error is detected."""
    remainder = mod2div(codeword, key)
    # An all-zero remainder means no error detected
    return int(remainder) == 0

# --- Hamming Code Functions ---

def calculate_hamming_code(data):
    """Calculates the Hamming code for a given data string."""
    d = list(map(int, data))
    n = len(d)

    # 1. Calculate the number of parity bits (r) needed
    r = 1
    while 2**r < n + r + 1:
        r += 1

    # 2. Create the codeword array of size n+r with placeholders for parity bits
    codeword = [0] * (n + r)
    j = 0 # data bit index
    k = 0 # codeword bit index
    for i in range(1, n + r + 1):
        # Parity bits are at positions that are powers of 2
        if i == 2**j:
            j += 1
        else:
            codeword[i-1] = d[k]
            k += 1

    # 3. Calculate the value for each parity bit
    for i in range(r):
        p_pos = 2**i
        parity_val = 0
        for j in range(1, len(codeword) + 1):
            if j & p_pos: # Check if the bit position 'j' should be checked by parity bit at 'p_pos'
                parity_val ^= codeword[j-1]
        codeword[p_pos-1] = parity_val

    return ''.join(map(str, codeword))

def correct_hamming_code(codeword):
    """Detects and corrects a single-bit error in a Hamming codeword."""
    c = list(map(int, codeword))
    n = len(c)
    r = 0
    # Calculate the number of parity bits in the received codeword
    while 2**r < n + 1:
        r += 1

    error_pos = 0
    # 1. Recalculate parity and form the error syndrome
    for i in range(r):
        p_pos = 2**i
        parity_val = 0
        for j in range(1, n + 1):
            if j & p_pos: # Bitwise AND to check positions
                parity_val ^= c[j-1]
        
        # If parity is incorrect, add its position to the error position
        if parity_val != 0:
            error_pos += p_pos

    # 2. If error_pos is not 0, an error exists. Flip the bit at that position.
    if error_pos != 0:
        corrected_codeword_list = c[:]
        # Flip the bit at the detected error position
        corrected_codeword_list[error_pos-1] = 1 - corrected_codeword_list[error_pos-1]
        corrected_codeword = "".join(map(str, corrected_codeword_list))
        return corrected_codeword, error_pos
    else:
        # No error found
        return codeword, 0

# --- Main Simulator Function ---

if __name__ == "__main__":
    print("--- CRC and Hamming Code Simulator ---")
    data = input("Enter the data bits (binary string): ")
    crc_key = input("Enter the CRC Generator Polynomial (binary string): ")
    
    if not all(c in '01' for c in data) or not all(c in '01' for c in crc_key):
        print("Error: Please enter valid binary strings.")
    else:
        # --- CRC Demonstration ---
        print("\n--- CRC (Error Detection) ---")
        crc_codeword, remainder = generate_crc(data, crc_key)
        print(f"Original Data: {data}")
        print(f"CRC Remainder: {remainder}")
        print(f"Transmitted Codeword (Data + Remainder): {crc_codeword}")

        # --- Hamming Code Demonstration ---
        print("\n--- Hamming Code (Error Correction) ---")
        hamming_codeword = calculate_hamming_code(data)
        print(f"Original Data: {data}")
        print(f"Transmitted Hamming Codeword: {hamming_codeword}")

        # --- Simulate Error ---
        print("\n--- Simulating a Single-Bit Error ---")
        error_pos = int(input(f"Enter bit position to introduce error (1 to {len(crc_codeword)}): "))

        if 1 <= error_pos <= len(crc_codeword):
            # Introduce error in CRC codeword
            crc_list = list(crc_codeword)
            crc_list[error_pos-1] = '1' if crc_list[error_pos-1] == '0' else '0'
            erroneous_crc = "".join(crc_list)
            print(f"\nErroneous CRC Codeword received: {erroneous_crc}")
            
            # Verify erroneous CRC
            if not verify_crc(erroneous_crc, crc_key):
                print("✅ CRC Check: Error DETECTED! The data is corrupted.")
            else:
                print("❌ CRC Check: No error detected (this can happen with specific multi-bit errors).")

        if 1 <= error_pos <= len(hamming_codeword):
            # Introduce error in Hamming codeword
            hamming_list = list(hamming_codeword)
            hamming_list[error_pos-1] = '1' if hamming_list[error_pos-1] == '0' else '0'
            erroneous_hamming = "".join(hamming_list)
            print(f"\nErroneous Hamming Codeword received: {erroneous_hamming}")

            # Correct erroneous Hamming code
            corrected_code, found_error_pos = correct_hamming_code(erroneous_hamming)
            if found_error_pos != 0:
                print(f"✅ Hamming Check: Error DETECTED at bit position {found_error_pos}.")
                print(f"   Corrected Codeword: {corrected_code}")
            else:
                print("✅ Hamming Check: No error detected.")
        else:
            print("Invalid error position for Hamming code.")