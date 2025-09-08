import streamlit as st
import pandas as pd

# --- CRC (Cyclic Reduadancy Check) Core Logic ---

def xor(a, b):
    """Performs bitwise XOR on two binary strings."""
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
        else:
            tmp = xor('0' * pick, tmp) + dividend[pick]
        pick += 1

    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0' * pick, tmp)

    return tmp

def generate_crc_codeword(data, key):
    """Generates a CRC codeword and returns the codeword and remainder."""
    key_len = len(key)
    appended_data = data + '0' * (key_len - 1)
    remainder = mod2div(appended_data, key)
    codeword = data + remainder
    return codeword, remainder

def verify_crc(codeword, key):
    """Verifies a CRC codeword. Returns True if the remainder is all zeros."""
    remainder = mod2div(codeword, key)
    return '1' not in remainder

# --- Hamming Code Core Logic ---

def calculate_hamming_code(data):
    """Calculates the Hamming code for a given data string."""
    d = list(map(int, data))
    n = len(d)

    # 1. Calculate the number of parity bits (r) needed
    r = 1
    while 2**r < n + r + 1:
        r += 1

    # 2. Create the codeword array with placeholders for parity bits
    codeword = [0] * (n + r)
    data_idx = 0
    for i in range(1, n + r + 1):
        if (i & (i - 1)) != 0:  # Check if 'i' is not a power of 2
            codeword[i - 1] = d[data_idx]
            data_idx += 1

    # 3. Calculate the value for each parity bit
    for i in range(r):
        p_pos = 2**i
        parity_val = 0
        for j in range(1, len(codeword) + 1):
            if j & p_pos:
                parity_val ^= codeword[j - 1]
        codeword[p_pos - 1] = parity_val

    return ''.join(map(str, codeword))

def correct_hamming_code(codeword):
    """Detects and corrects a single-bit error in a Hamming codeword."""
    c = list(map(int, codeword))
    n = len(c)
    r = 0
    while 2**r < n + 1:
        r += 1

    error_pos = 0
    # 1. Recalculate parity and form the error syndrome
    for i in range(r):
        p_pos = 2**i
        parity_val = 0
        for j in range(1, n + 1):
            if j & p_pos:
                parity_val ^= c[j - 1]
        if parity_val != 0:
            error_pos += p_pos

    # 2. If error_pos is not 0, an error exists.
    if error_pos != 0:
        corrected_codeword_list = c[:]
        # Flip the bit at the detected error position
        corrected_codeword_list[error_pos - 1] ^= 1
        corrected_codeword = "".join(map(str, corrected_codeword_list))
        return corrected_codeword, error_pos
    else:
        # No error found
        return codeword, 0

# --- Streamlit UI ---

st.set_page_config(page_title="Network Error Codes Simulator", layout="wide")

st.title("🖥️ CRC and Hamming Code Simulator")
st.write("A tool to demonstrate and compare Cyclic Redundancy Check (CRC) for error detection and Hamming Code for error detection & correction.")

st.sidebar.header("⚙️ Simulation Controls")

# Input fields
data = st.sidebar.text_input("Enter Data Bits (e.g., 1011001)", "1011001")
crc_key = st.sidebar.text_input("Enter CRC Generator Polynomial (e.g., 1011)", "1011")

# Validate inputs
if not all(c in '01' for c in data) or not all(c in '01' for c in crc_key) or not data or not crc_key:
    st.sidebar.error("Please enter valid binary strings for both data and CRC key.")
else:
    # --- Step 1: Codeword Generation ---
    st.header("Step 1: Codeword Generation")
    
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("CRC Codeword")
        crc_codeword, crc_remainder = generate_crc_codeword(data, crc_key)
        st.write(f"**Original Data:** `{data}`")
        st.write(f"**CRC Generator:** `{crc_key}`")
        st.write(f"**Calculated Remainder:** `{crc_remainder}`")
        st.success(f"**Transmitted CRC Codeword:** `{crc_codeword}`")

    with col2:
        st.subheader("Hamming Codeword")
        hamming_codeword = calculate_hamming_code(data)
        st.write(f"**Original Data:** `{data}`")
        st.write(f"**Parity Bits Calculated:** Dynamically")
        st.success(f"**Transmitted Hamming Codeword:** `{hamming_codeword}`")
        
    st.markdown("---")

    # --- Step 2: Error Simulation ---
    st.header("Step 2: Error Simulation")
    st.write("Select a bit position in the **transmitted codewords** to introduce a single-bit error.")

    # Let user select which codeword to base the error position on
    max_len = max(len(crc_codeword), len(hamming_codeword))
    error_pos = st.slider("Select Bit Position to Flip (1-based index)", 1, max_len, 5)

    # --- Step 3: Error Detection & Correction ---
    st.header("Step 3: Receiving and Verifying Data")
    col3, col4 = st.columns(2)
    
    # CRC Error Handling
    with col3:
        st.subheader("CRC Verification")
        if error_pos > len(crc_codeword):
             st.warning(f"Error position {error_pos} is out of bounds for the CRC codeword (length {len(crc_codeword)}).")
             st.write(f"**Received Codeword (No Error):** `{crc_codeword}`")
             st.info("CRC Check: No error introduced, so no error detected.")
        else:
            crc_list = list(crc_codeword)
            crc_list[error_pos - 1] = '1' if crc_list[error_pos - 1] == '0' else '0'
            erroneous_crc = "".join(crc_list)
            
            st.write(f"**Original Codeword:** `{crc_codeword}`")
            st.warning(f"**Received (Corrupted) Codeword:** `{erroneous_crc}`")
            
            if not verify_crc(erroneous_crc, crc_key):
                st.error("**CRC Check Result:** 🚩 Error DETECTED!")
            else:
                st.info("**CRC Check Result:** No error was detected (Note: CRC can miss some multi-bit errors).")

    # Hamming Code Error Handling
    with col4:
        st.subheader("Hamming Code Correction")
        if error_pos > len(hamming_codeword):
            st.warning(f"Error position {error_pos} is out of bounds for the Hamming codeword (length {len(hamming_codeword)}).")
            st.write(f"**Received Codeword (No Error):** `{hamming_codeword}`")
            st.info("Hamming Check: No error introduced, so no correction needed.")
        else:
            hamming_list = list(hamming_codeword)
            hamming_list[error_pos - 1] = '1' if hamming_list[error_pos - 1] == '0' else '0'
            erroneous_hamming = "".join(hamming_list)
            
            st.write(f"**Original Codeword:** `{hamming_codeword}`")
            st.warning(f"**Received (Corrupted) Codeword:** `{erroneous_hamming}`")
            
            corrected_code, found_error_pos = correct_hamming_code(erroneous_hamming)
            
            if found_error_pos != 0:
                st.error(f"**Hamming Check Result:** 🚩 Error DETECTED at bit position **{found_error_pos}**.")
                st.success(f"**Corrected Codeword:** `{corrected_code}`")
            else:
                st.info("**Hamming Check Result:** No error was detected.")
