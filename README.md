# 🐤 Canary Autofinder

![Python Version](https://img.shields.io/badge/python-3.x-blue?style=flat&logo=python)
![Library](https://img.shields.io/badge/lib-pwntools-red?style=flat&logo=kalilinux)
![License](https://img.shields.io/badge/license-MIT-green?style=flat)
![Status](https://img.shields.io/badge/status-Educational-orange?style=flat)

**Canary Autofinder** is a Python automation script designed to identify potential Stack Canary offsets within ELF binaries. It leverages **Format String Vulnerabilities** to analyze memory leaks and heuristically determine which stack values behave like canaries.

> [!IMPORTANT]
> **⚠️ DISCLAIMER**
>
> This tool was created strictly for **educational purposes, Capture The Flag (CTF) competitions, and security research**.
>
> The author does not endorse or encourage the use of this code for malicious activities. Users are responsible for ensuring they have the appropriate permission to analyze any binaries they target.

---

## 🧐 How it Works

Modern binaries use **Stack Canaries** to prevent buffer overflows. These are random values placed before the return address. This tool identifies them based on two specific behaviors:

1.  **Null Byte Termination:** Canaries (in Little Endian) typically end in `00` (a null byte) to prevent string functions like `printf` or `puts` from inadvertently leaking them.
2.  **Randomization:** The value of the canary changes every time the program is executed.

### The Algorithm
The script performs the following steps:
1.  **Payload Generation:** Constructs a massive Format String payload (`%lx` or `%x`).
2.  **Sampling:** Runs the binary multiple times (default: 100 iterations).
3.  **Heuristic Analysis:**
    * Filters out values that do not end in `00`.
    * Filters out values that remain static (constant) across executions.
4.  **Result:** Returns the offset and the last seen value of the candidate.

---

## 🚀 Getting Started

### Prerequisites

You need **Python 3** and the **pwntools** library.

```bash
pip install pwntools

```

### Installation

Clone the repository to your local machine:

```bash
git clone [https://github.com/HH-Tips/canary_autofinder.git](https://github.com/HH-Tips/canary_autofinder.git)
cd canary_autofinder

```

---

## 💻 Usage

Run the script by passing the target ELF binary as an argument:

```bash
python3 canary_autofinder.py ./path_to_vulnerable_binary

```

### Example Output

```text
[!] Warnings are enabled
[*] '/home/user/vuln_binary'
    Arch:     amd64-64-little
    RELRO:    Full RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled

... (running analysis) ...

Possibili Canaries:
OFFSET  LAST_VALUE
0x28:   1a2b3c4d5e6f00

```

---

## ⚙️ Configuration

You can tweak the analysis parameters directly in the script source code:

```python
n = 1000       # Number of stack positions to leak
tests = 100    # Number of execution iterations to test randomness

```

---

## 🤝 Contributing

Contributions are welcome! If you have suggestions to improve the heuristic detection or support for other architectures, feel free to open an issue or a pull request.

## 📝 License

This project is open-source and intended for learning.
