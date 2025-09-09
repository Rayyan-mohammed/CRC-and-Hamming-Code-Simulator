# CRC-and-Hamming-Code-Simulator

An interactive web application built with Streamlit to demonstrate and
compare two fundamental error control techniques in computer networks:
Cyclic Redundancy Check (CRC) for error detection and Hamming Code for
error detection and correction.

This tool provides a clear, step-by-step visualization of how data is
encoded, how errors are introduced, and how these algorithms work to
handle data corruption during transmission.

✨ Features - **Interactive UI**\
A user-friendly interface to input custom data and see results in
real-time.

-   **CRC Simulation**
    -   Generates a CRC codeword from user-defined data and a generator
        polynomial.\
    -   Simulates a single-bit error in the transmitted codeword.\
    -   Verifies the received codeword to show how CRC detects the
        error.
-   **Hamming Code Simulation**
    -   Calculates the required number of parity bits and generates a
        Hamming codeword.\
    -   Simulates a single-bit error.\
    -   Detects the exact position of the error and demonstrates the
        self-correction process.
-   **Side-by-Side Comparison**\
    Clearly contrasts the capabilities of CRC (detection only) with
    Hamming Code (detection and correction).

🚀 How to Run Locally Follow these instructions to get the simulator
running on your local machine.

### Prerequisites

-   Python (version 3.8 or higher)\
-   pip (Python's package installer)\
-   git (for cloning the repository)

### 1. Clone the Repository

``` bash
git clone https://github.com/Rayyan-mohammed/CRC-and-Hamming-Code-Simulator.git
cd CRC-and-Hamming-Code-Simulator
```

### 2. Create a Virtual Environment (Recommended)

It's good practice to create a virtual environment to manage project
dependencies.

For Windows:

``` bash
python -m venv venv
.env\Scriptsctivate
```

For macOS/Linux:

``` bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

The required packages are listed in requirements.txt. Install them using
pip:

``` bash
pip install -r requirements.txt
```

### 4. Run the Streamlit App

Once the dependencies are installed, run the following command in your
terminal:

``` bash
streamlit run app.py
```

Your default web browser will open a new tab with the running
application.

🛠️ Technology Stack - **Language**: Python\
- **Framework**: Streamlit (for the web application UI)\
- **Libraries**: Pandas (for structured data display)

📁 File Structure

    .
    ├── app.py             # The main Streamlit application script
    ├── README.md          # Project documentation
    └── requirements.txt   # List of Python dependencies

🤝 Contributing Contributions are welcome! If you have suggestions for
improvements or want to add new features (like simulating burst errors),
please feel free to fork the repository and submit a pull request.

1.  Fork the repository.\
2.  Create your feature branch (`git checkout -b feature/NewFeature`).\
3.  Commit your changes (`git commit -m 'Add some NewFeature'`).\
4.  Push to the branch (`git push origin feature/NewFeature`).\
5.  Open a Pull Request.

📄 License This project is licensed under the MIT License.
