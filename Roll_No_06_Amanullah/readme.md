README – for Sir 😎

Hey Sir, so if you're reading this after unzipping the stuff, here’s what’s what:

There are **2 folders** inside this zip:
- 📁 `Textyyy`
- 📁 `Dictionaries`

Both of them got their own:
- `code.py` (the actual script)
- `input.txt` (sample file to test on)
- `pseudocode.txt` (notes and structure for how the code works)

---

**Important before running stuff:**

The code **won't run directly** unless you do one of two things:

**Option 1:**  
- Go *inside* either `Textyyy/` or `Dictionaries/` using `cd` in terminal  
- Then run the code from there

**Option 2:**  
- Stay in the main folder (like outside both)  
- BUT then you gotta give **full path** to the file you wanna use as input  
  (like `Textyyy/input.txt` instead of just `input.txt`)  
  Otherwise the code won’t find it and will complain!

---

📝 **What’s different between the two folders?**

📂 `Textyyy/`
- This one gives simple, human-readable output (no dictionaries)
- Just plain ol' text summary written to `output.txt`
- This was based on your *initial* request, to keep it readable and clean

📂 `Dictionaries/`
- This one’s more fancy/serious 😅  
- Output is stored in a structured **dictionary format** (JSON-like, formatted nicely)
- Everything’s sorted, labeled, and packed in `output.txt`
- A bit more detailed and deliberate – counts, lists, unique chars, etc.
- I mean it even includes each instance a thing appeared and save it in dictionary relative to that func.

---

 **Some Extra Notes:**

- Tried to add solid **error handling** everywhere  
  So if anything breaks (file not found, permission probs, invalid input etc),  
  you’ll know exactly *why* it broke and can fix it fast

- No built-in Python functions used for the main logic  
  (like `isuppercase()` or `.split()` or `len()` etc)  
  I went full manual mode like we discussed, using Unicode checks and loops

- Output files get overwritten if you run the code again, just FYI

---

That’s all Sir!  
Let me know if anything feels off or if you want changes.  
Hope this matches what you needed 🔧

– peace out ✌️
