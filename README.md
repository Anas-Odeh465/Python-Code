---

# 🎄 Advent of Code 2024 - Day 2: Red-Nosed Reports

This repository contains my personal solution for the **Day 2 challenge** of Advent of Code 2024. The goal was to analyze a series of "reports" (lists of numbers) and determine which ones are "Safe" based on specific trend and distance rules.

## 🧠 The Logic Behind the Solution

To ensure accuracy, I implemented a **two-stage classification pipeline**. Instead of checking everything at once, the program breaks down the problem like a real-world processing plant:

1. **Stage 1: Trend Classification (`classify`)**
* Determines if a report is strictly **Increasing** or **Decreasing**.
* It uses a `role_value` system to track every step. If the trend breaks (e.g., increases then decreases), it's immediately flagged as `Unsafe`.


2. **Stage 2: Delta Validation (`process`)**
* Checks the "distance" between adjacent numbers.
* A report is only confirmed as `Safe` if the difference between every two numbers is at least **1** and at most **3**.



## 🚀 Key Features

* **Interactive Verbose Mode:** Upon launching, the program asks if you want to see the full "Internal Logs." This is great for debugging or seeing exactly *why* a report failed.
* **Human-Readable Logging:** The console output is beautifully formatted with headers, arrows, and clear error messages (e.g., `out of 1-3 level range`).
* **Dynamic Scaling:** The code is designed to handle lists of any length and dictionaries with any number of reports.
* **Zero Dependencies:** Pure Python. No external libraries needed.

## 🛠️ How to Run

1. Make sure you have **Python 3.x** installed.
2. Clone the repository or download `test.py`.
3. Run the script via terminal:
```bash
python test.py

```


4. Follow the on-screen prompts to toggle logs on or off.

## 📊 Sample Output (with Logs enabled)

```text
### 4) Starting with -> report_4: [1, 3, 2, 4, 5] 

[1 <= 3]: Increasing
[3 >= 2]: Decreasing
[2 <= 4]: Increasing

X [Not safe order] report_4: [1, 3, 2, 4, 5] >> status: Unsafe <<

```

## 📂 Project Structure

* `main()`: The entry point that orchestrates the flow.
* `displayOption()`: Handles user input and UI preferences.
* `classify()`: Logic for trend analysis.
* `process()`: Logic for mathematical difference validation.
* `displayFinalReportsOutput()`: Clean, summarized final results.

---

**Happy Coding!** 🚀
*Part of the Advent of Code 2024 journey.*

---