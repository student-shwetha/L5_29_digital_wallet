\# Lab 5: Static Code Analysis Report



\## 1. Objective



The objective of this lab is to identify and fix security vulnerabilities, code quality issues, and coding standard violations in a Python digital wallet program using Bandit, Pylint, and Flake8.



\## 2. Tools Used



\- \*\*Bandit:\*\* Identifies potential security issues in Python code.

\- \*\*Pylint:\*\* Checks code quality, naming conventions, documentation, and programming practices.

\- \*\*Flake8:\*\* Detects Python style violations and formatting problems.



\## 3. Issues Identified and Fixes Applied



| No. | Tool | Issue Identified | Fix Applied |

|---|---|---|---|

| 1 | Bandit | B105 — Hardcoded gateway secret | Changed the gateway secret to be read from an environment variable. |

| 2 | Bandit | B324 — Weak SHA-1 hashing algorithm | Replaced SHA-1 with PBKDF2-HMAC-SHA256 for the demonstration PIN hash. |

| 3 | Bandit | B306 — Insecure temporary file creation using `tempfile.mktemp()` | Replaced it with `tempfile.NamedTemporaryFile()`. |

| 4 | Bandit | B311 — Use of a non-cryptographic random generator for OTP generation | Used Python's `secrets` module to generate the OTP. |

| 5 | Pylint | Missing module and function docstrings | Added documentation strings to the module and functions. |

| 6 | Pylint | Naming convention violations | Updated function and variable names to follow Python naming conventions. |

| 7 | Pylint | Mutable default argument (`log=\[]`) | Changed the default argument to `None` and initialized the list inside the function. |

| 8 | Pylint | Use of a `global` statement | Stored the daily transaction limit in a settings dictionary. |

| 9 | Pylint | Unused function parameter | Explicitly referenced the parameter in the demonstration function. |

| 10 | Flake8 | Incorrect whitespace around operators and commas | Corrected spacing and formatting. |

| 11 | Flake8 | Incorrect blank-line formatting | Added the required blank lines between function definitions. |



\## 4. Before-and-After Analysis Results



\### Pylint

\- \*\*Before:\*\* Score of 5.69/10.

\- \*\*After:\*\* Score of 10.00/10.

\- \*\*Result:\*\* Improved documentation, naming conventions, and code quality.



\### Bandit

\- \*\*Before:\*\* Four security findings were reported.

\- \*\*After:\*\* No issues were identified by Bandit.

\- \*\*Result:\*\* Addressed the reported findings related to the gateway secret, hashing, temporary files, and OTP generation.



\### Flake8

\- \*\*Before:\*\* Four formatting violations were reported.

\- \*\*After:\*\* No violations were reported.

\- \*\*Result:\*\* Corrected spacing and blank-line formatting issues.



The before-and-after reports are included in this repository.



\## 5. Reflection Questions and Answers



\### Question 1: Why is static code analysis important?



Static code analysis helps identify potential bugs, security vulnerabilities, and coding standard violations without executing the program. It improves code quality, readability, maintainability, and security.



\### Question 2: What did you learn from using Bandit?



Bandit helped identify potential security risks, including hardcoded secrets, weak hashing, insecure temporary file creation, and unsuitable random number generation for OTPs. I learned the importance of using safer alternatives to address these issues.



\### Question 3: What issues did Pylint identify, and how did fixing them improve the code?



Pylint identified missing docstrings, naming convention violations, a mutable default argument, an unused parameter, and the use of a global statement. Fixing these issues improved code organization, readability, and maintainability. The final Pylint score was 10/10.



\### Question 4: What did Flake8 help you improve?



Flake8 identified formatting problems such as incorrect spacing around operators and commas and insufficient blank lines. Correcting these violations made the code more consistent with Python style guidelines.



\### Question 5: What challenges did you face while fixing the issues?



The main challenge was understanding each tool's findings and correcting the issues without changing the intended program behavior. I reran the program and the static analysis tools after making the changes to verify the results.



\## 6. Conclusion



This lab demonstrated how Bandit, Pylint, and Flake8 can be used together to improve Python code security, quality, and formatting. After applying the fixes, the program achieved a Pylint score of 10/10, Bandit reported no issues, and Flake8 reported no violations.



These results apply to the checks performed by the selected tools; they do not guarantee that the program is completely free of security vulnerabilities.

