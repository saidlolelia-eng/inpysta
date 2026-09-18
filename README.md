# 📸 InPySta (v1.0.4)

> A lightweight, highly custom Python library that simulates an Instagram database engine. Built for fun, experimentation, and mock backend practice!

# Latest Update
Made InPySta faster by using O(1) instead of O(n)! Added
better explanations.

---

## 🚀 What is InPySta?
InPySta is a simple simulation engine for managing user profiles, tracking followers/following networks, handling minor account requirements (parental settings), and editing database entries on the fly. 

*This is a fun project built to experiment with class architectures and command-line interfaces.*

---

## 🛠️ Installation

You can install InPySta directly via the terminal using `pip`:

```bash
pip install inpysta
```

---

## 💻 Quick Start Guide

Get your engine up and running in just a few lines of code:

```python
from inpysta import MockEngineMain

# 1. Initialize the engine core
engine = MockEngineMain("MyInstagramMock")

# 2. Create profile accounts
user1 = engine.CreateUser("coolboy10", 19)
user2 = engine.CreateUser("admin_user", 15) # Prompts parental warning alert

# 3. View the system database state
engine.ViewUsers()
```

---

## 🕹️ Available API Commands

### 🏗️ Engine Management (`MockEngineMain`)

*   **`CreateUser(username: str, userage: int)`**  
    Registers a unique user profile inside the engine global database. Returns the account object configuration.
*   **`DeleteUser(user_object)`**  
    Removes a registered profile reference clean out of the database array.
*   **`ViewUsers()`**  
    Outputs a structured list tracking all active profiles registered on the instance.
*   **`PrintInfo(username: str)`**  
    Displays a visually formatted card containing statistics, counts, age verification, and tracking lists for a specific username.
*   **`EditInfo(username: str)`**  
    Launches an interactive dashboard allowing you to change profile variables like username or age natively from console prompts.
*   **`SetParentalUser(username: str)`**  
    Enables linking an minor account (under 18) to an established adult guardian account inside the platform database.

### 👤 Profile Interaction (`UserProfileAccount`)

When you save a user object via `my_user = engine.CreateUser(...)`, you unlock individual account operations:

*   **`my_user._follow(target_username: str)`**  
    Processes a safe, bidirectional relationship link. Appends the destination user to your `follows` tracking array and adds you to their `followers` log.
*   **`my_user._unfollow(target_username: str)`**  
    Removes the mutual network ties between the current profile and the target user.

---

## 🛡️ License & Acknowledgement
This library is open-source. To use it in your own external projects or modifications, please add clear credit and acknowledgement back to **InPySta**. 

**© 2026 InPySta Dev Studio.** authored by *Elijah J.*.
