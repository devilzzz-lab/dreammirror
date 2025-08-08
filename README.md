# 🤝 Contributing to DreamMirror AI

Welcome to the DreamMirror AI project! 🌙 This document outlines the rules and workflow for contributing as a team member.

---

## 🔒 Branch Policy

| Branch Name | Purpose                            | Who Can Push         |
|-------------|------------------------------------|----------------------|
| main        | Production-ready code (protected)  | 🔐 Only Devil (lead) |
| srimathi    | Personal branch for srimathi       | ✅ srimathi only     |
| saran       | Personal branch for saran          | ✅ saran only        |
| swetha      | Personal branch for swetha         | (same rule)          |

---

## 🧑‍💻 Your Contribution Workflow

1. Clone the repo:

   ```bash
   git clone https://github.com/yourusername/dreammirror.git
   cd dreammirror
   ```

2. Checkout your personal branch:

   ```bash
   git checkout teammate1  # use your assigned branch nam
   ```

3. Pull the latest main (if needed):

   ```bash
   git pull origin main
   ```

4. Make changes → Stage → Commit → Push:

   ```bash
   git add .
   git commit -m "Your commit message here"
   git push origin teammate1
   ```

5. (Optional) Open a pull request to request code review or merge into dev branch.

---

## 🔐 Main Branch is Protected

- You cannot push or merge directly into main.
- You can push to your assigned branches only.
- Only Devil (project owner) can approve and merge code into main.
- This ensures stable and production-ready code in the main branch.

---

## ✅ Best Practices

- Follow branch naming conventions: `feature/your-feature`, `bugfix/fix-name`, etc.
- Write clean and modular code.
- Keep commits meaningful and focused.
- If you need a new branch created for you, contact Devil.

---

Thanks for contributing! Let's build something beautiful 🌌
