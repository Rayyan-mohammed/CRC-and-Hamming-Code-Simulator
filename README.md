# CRC-and-Hamming-Code-Simulator

An **interactive visualization tool** built with [Streamlit](https://streamlit.io/) that demonstrates two cornerstone error-control mechanisms in computer networks:  

- **Cyclic Redundancy Check (CRC)** → *Error Detection*  
- **Hamming Code** → *Error Detection + Error Correction*  

This simulator provides a **step-by-step, visual, and comparative** representation of how these techniques work — from encoding to error introduction to detection/correction.  

---

## ✨ Key Features  

### 🖥️ Interactive Interface  
- Clean, intuitive UI to experiment with custom inputs.  
- Real-time visualization of encoding, error simulation, and verification.  

### 🔄 CRC Simulation  
- Encode data using CRC with a user-defined generator polynomial.  
- Introduce a **single-bit error** during transmission.  
- Detect corruption by verifying the received codeword.  

### 🛠️ Hamming Code Simulation  
- Compute the number of parity bits automatically.  
- Generate the **Hamming codeword** for the given input.  
- Simulate a **single-bit error**, pinpoint the error location, and demonstrate **self-correction**.  

### ⚖️ Side-by-Side Comparison  
- **CRC** → Detects errors only.  
- **Hamming Code** → Detects *and* corrects errors.  

---

## 🚀 Getting Started  

Follow these steps to set up and run the simulator locally.  

### ✅ Prerequisites  
- Python **3.8+**  
- pip (Python package manager)  
- git  

---

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/Rayyan-mohammed/CRC-and-Hamming-Code-Simulator.git
cd CRC-and-Hamming-Code-Simulator
```

---

### 2️⃣ Create a Virtual Environment (Recommended)  

**Windows**:  
```bash
python -m venv venv
.env\Scripts\activate
```

**macOS/Linux**:  
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the Application  
```bash
streamlit run app.py
```
This will launch the app in your **default web browser**.  

---

## 🛠️ Tech Stack  

- **Language**: Python  
- **Framework**: Streamlit (web app UI)  
- **Libraries**: Pandas (structured data handling, visualization)  

---

## 📂 Project Structure  

```
.
├── app.py             # Main Streamlit application
├── README.md          # Project documentation
└── requirements.txt   # Python dependencies
```

---

## 🤝 Contributing  

Contributions are always welcome! 🚀  

1. Fork the repository.  
2. Create your feature branch:  
   ```bash
   git checkout -b feature/NewFeature
   ```  
3. Commit your changes:  
   ```bash
   git commit -m "Add NewFeature"
   ```  
4. Push to your branch:  
   ```bash
   git push origin feature/NewFeature
   ```  
5. Open a Pull Request.  

Potential improvements:  
- Simulating **burst errors**.  
- Adding **multi-bit error scenarios**.  
- Enhanced **visual analytics**.  

---

## 📜 License  

This project is licensed under the **MIT License**.  
Feel free to use, modify, and distribute it in both personal and commercial projects.  

---

## 📧 Contact  
**Rayyan Mohammed**  
- GitHub: [@Rayyan-mohammed](https://github.com/Rayyan-mohammed)  
- Email: rayyan1652@gmail.com  

Project Link: [CRC and Hamming Code Simulator](https://github.com/Rayyan-mohammed/CRC-and-Hamming-Code-Simulator.git)  
