### Application Test Logs

#### Test 1: Academic Policy Query (Late Submission Penalty)
* **Question:** `What is the penalty per calendar day for late coursework submission?`
* **Retrieved Chunks:**
  * **[1] File:** `grading_policy.txt` | **Chunk Index:** `1` | **Distance:** `0.2531`  
    > *"Late Submission Penalties: Coursework submitted after the deadline receives an automatic penalty of 10% deduction per calendar day late. Work submitted more than 3 days past the deadline will receive a grade of zero unless supported by an official medical certificate."*
  * **[2] File:** `grading_policy.txt` | **Chunk Index:** `0` | **Distance:** `0.2886`  
    > *"# Academic Grading and Assignment Submission Policy 1. Late Submission Penalties: Coursework submitted after the deadline receives an automatic penalty of 10% deduction per calendar day late."*
  * **[3] File:** `008_Setting_Up_a_Secure_Wireless_Network.txt` | **Chunk Index:** `7` | **Distance:** `0.5200`  
    > *"is limits the spread of malware or unauthorized access in case of a breach. **Step 9: Regularly Update Your Router's Firmware** Regularly check for and install firmware updates for your router to ensure you have the latest security patches and features. **Step 10: Monitor Your Network**"*
  * **[4] File:** `002_Resetting_a_Forgotten_PIN.txt` | **Chunk Index:** `5` | **Distance:** `0.5269`  
    > *"eed this limit, you will need to contact the IT Helpdesk to reset your PIN. By following these steps, you should be able to reset your forgotten PIN and regain access to company systems and applications. If you encounter any issues during the process, please do not hesitate to reach out to the IT Helpdesk for further assistance."*
  * **[5] File:** `library_services.txt` | **Chunk Index:** `4` | **Distance:** `0.5863`  
    > *"Late Returns & Fines: Overdue items incur a daily late fine of $0.50 per book. Unpaid balances exceeding $10 will temporarily suspend student course enrollment and graduation clearance."*
* **Final Answer:**
  > According to the context, the penalty per calendar day for late coursework submission is a 10% deduction[cite: 1].

---

#### Test 2: IT Documentation Query (Mobile Email Prerequisites)
* **Question:** `What are the prerequisites before setting up company email on a mobile device?`
* **Retrieved Chunks:**
  * **[1] File:** `001_Setting_Up_a_Mobile_Device_for_Company_Email.txt` | **Chunk Index:** `0` | **Distance:** `0.0751`  
    > *"**Setting Up a Mobile Device for Company Email** **Prerequisites:** * Mobile device with a supported operating system (iOS, Android, or Windows) * Company email account credentials * Mobile device management (MDM) profile installed (if required by company policy) **Step 1: Ensure Mobile Device Management (MDM) Profile is Installed (if required)**"*
  * **[2] File:** `001_Setting_Up_a_Mobile_Device_for_Company_Email.txt` | **Chunk Index:** `2` | **Distance:** `0.1704`  
    > *"partment for assistance. **Step 2: Set Up Email Account on Mobile Device** 1. Go to the Settings app on your mobile device. 2. Select "Mail" or "Email" (depending on your device's operating system). 3. Tap "Add Account" or "Create a new account". 4. Select "Exchange" or "Corporate" as the account type. 5. Enter your company email address and password. 6. If prompted, enter the company's email server address (e.g., mail.company.com). 7. Select the desired synchronization options (e.g., sync email, contacts, calendar)."*
  * **[3] File:** `library_services.txt` | **Chunk Index:** `6` | **Distance:** `0.8340`  
    > *"3. Study Room Bookings: Group study rooms must be reserved via the library mobile app at least 2 hours in advance."*
  * **[4] File:** `wifi_access.txt` | **Chunk Index:** `5` | **Distance:** `0.8377`  
    > *"Device Limit: Each student may register a maximum of two active personal devices (e.g., one laptop and one smartphone) on the student network at the same time. 3."*
  * **[5] File:** `wifi_access.txt` | **Chunk Index:** `4` | **Distance:** `0.8403`  
    > *"2. Device Limit: Each student may register a maximum of two active personal devices (e.g., one laptop and one smartphone) on the student network at the same time."*
* **Final Answer:**
  > According to the context, the prerequisites before setting up company email on a mobile device are:
  > * Mobile device with a supported operating system (iOS, Android, or Windows)
  > * Company email account credentials
  > * Mobile device management (MDM) profile installed (if required by company policy)
  > 
  > Source: [1] `001_Setting_Up_a_Mobile_Device_for_Company_Email.txt`

---

#### Test 3: Academic Policy Query (Grade Appeals Window)
* **Question:** `How many days does a student have to submit a written grade appeal?`
* **Retrieved Chunks:**
  * **[1] File:** `grading_policy.txt` | **Chunk Index:** `6` | **Distance:** `0.2653`  
    > *"3. Grade Appeals: A student wishing to dispute a final exam mark must submit a written appeal form to the Academic Registrar within 7 working days following grade publication."*
  * **[2] File:** `007_Troubleshooting_Issues_with_Company-Issued_Tablets.txt` | **Chunk Index:** `8` | **Distance:** `0.5326`  
    > *"upport if the issue cannot be resolved through these troubleshooting steps. If none of the above steps resolve the issue, please escalate the issue to advanced support, providing as much detail as possible about the problem and the steps taken so far."*
  * **[3] File:** `grading_policy.txt` | **Chunk Index:** `0` | **Distance:** `0.5354`  
    > *"# Academic Grading and Assignment Submission Policy 1. Late Submission Penalties: Coursework submitted after the deadline receives an automatic penalty of 10% deduction per calendar day late."*
  * **[4] File:** `002_Resetting_a_Forgotten_PIN.txt` | **Chunk Index:** `5` | **Distance:** `0.5437`  
    > *"eed this limit, you will need to contact the IT Helpdesk to reset your PIN. By following these steps, you should be able to reset your forgotten PIN and regain access to company systems and applications. If you encounter any issues during the process, please do not hesitate to reach out to the IT Helpdesk for further assistance."*
  * **[5] File:** `grading_policy.txt` | **Chunk Index:** `1` | **Distance:** `0.5996`  
    > *"Late Submission Penalties: Coursework submitted after the deadline receives an automatic penalty of 10% deduction per calendar day late. Work submitted more than 3 days past the deadline will receive a grade of zero unless supported by an official medical certificate."*
* **Final Answer:**
  > According to the grading policy [1], a student wishing to dispute a final exam mark must submit a written appeal form to the Academic Registrar within 7 working days following grade publication.

---

#### Test 4: Out-of-Corpus Academic Guardrail Test (Dormitory Refund Policy)
* **Question:** `What is the university policy and deadline for requesting a refund on dormitory housing fees?`
* **Retrieved Chunks:**
  * **[1] File:** `003_Configuring_VPN_Access_for_Remote_Workers.txt` | **Chunk Index:** `7` | **Distance:** `0.5080`  
    > *"tinue to experience issues, contact the IT helpdesk for further assistance. **Security Reminders** * Always keep your VPN client software up-to-date. * Never share your login credentials with anyone. * Avoid using public Wi-Fi or unsecured networks to access company resources via VPN."*
  * **[2] File:** `007_Troubleshooting_Issues_with_Company-Issued_Tablets.txt` | **Chunk Index:** `8` | **Distance:** `0.5091`  
    > *"upport if the issue cannot be resolved through these troubleshooting steps. If none of the above steps resolve the issue, please escalate the issue to advanced support, providing as much detail as possible about the problem and the steps taken so far."*
  * **[3] File:** `grading_policy.txt` | **Chunk Index:** `0` | **Distance:** `0.7428`  
    > *"# Academic Grading and Assignment Submission Policy 1. Late Submission Penalties: Coursework submitted after the deadline receives an automatic penalty of 10% deduction per calendar day late."*
  * **[4] File:** `library_services.txt` | **Chunk Index:** `0` | **Distance:** `0.7951`  
    > *"# Central University Library Guidelines 1. Borrowing Privileges: Undergraduate students may borrow up to 5 physical books for a duration of 14 calendar days."*
  * **[5] File:** `library_services.txt` | **Chunk Index:** `4` | **Distance:** `0.7954`  
    > *"Late Returns & Fines: Overdue items incur a daily late fine of $0.50 per book. Unpaid balances exceeding $10 will temporarily suspend student course enrollment and graduation clearance."*
* **Final Answer:**
  > I don't have enough information in the documents to answer that.

---

#### Test 5: Out-of-Corpus IT Guardrail Test (Parental Leave Policy)
* **Question:** `What is the procedure for employees to apply for maternity or paternity leave in the HR portal?`
* **Retrieved Chunks:**
  * **[1] File:** `003_Configuring_VPN_Access_for_Remote_Workers.txt` | **Chunk Index:** `0` | **Distance:** `0.4406`  
    > *"**Configuring VPN Access for Remote Workers** **Overview** This article provides step-by-step instructions for configuring VPN access for remote workers. This allows employees working from home or other remote locations to securely connect to the company network and access company resources. **Prerequisites**"*
  * **[2] File:** `002_Resetting_a_Forgotten_PIN.txt` | **Chunk Index:** `1` | **Distance:** `0.4697`  
    > *"PIN Reset Tool login page. **Step 2: Authenticate with Your Credentials** 1. Enter your company username and password in the required fields. 2. Click the "Login" button to authenticate. **Step 3: Verify Your Identity** 1. You will be prompted to answer your security question. Enter your answer in the required field. 2. Click the "Next" button to proceed. **Step 4: Reset Your PIN**"*
  * **[3] File:** `library_services.txt` | **Chunk Index:** `7` | **Distance:** `0.9523`  
    > *"Study Room Bookings: Group study rooms must be reserved via the library mobile app at least 2 hours in advance. Reservations are capped at a maximum of 3 hours per study group per day."*
  * **[4] File:** `library_services.txt` | **Chunk Index:** `6` | **Distance:** `0.9777`  
    > *"3. Study Room Bookings: Group study rooms must be reserved via the library mobile app at least 2 hours in advance."*
  * **[5] File:** `grading_policy.txt` | **Chunk Index:** `1` | **Distance:** `1.0215`  
    > *"Late Submission Penalties: Coursework submitted after the deadline receives an automatic penalty of 10% deduction per calendar day late. Work submitted more than 3 days past the deadline will receive a grade of zero unless supported by an official medical certificate."*
* **Final Answer:**
  > I don't have enough information in the documents to answer that.





---

### Reflection

Building an offline Retrieval-Augmented Generation (RAG) system with Ollama (`llama3.2` and `nomic-embed-text`), ChromaDB, and Qdrant provided hands-on experience in pipeline orchestration.

**What worked well:** Decoupling the project into modular components (`vector_store.py`, `ingest.py`, `retrieval.py`, and `generate.py`) made the pipeline easy to debug. Slicing documents from scratch using Python's standard `re` library gave complete control over text boundaries without relying on external splitting frameworks. Furthermore, enforcing strict negative constraints in the system prompt successfully prevented hallucinations, ensuring the model answered strictly from provided sources and explicitly refused out-of-corpus queries.

**What was harder than expected:** Harmonizing retrieval across two separate vector stores with different chunking granularities was challenging. Initially, querying both ChromaDB (fine sentence chunks) and Qdrant (broad paragraph chunks) caused document crowding. Because Qdrant's procedural IT paragraphs returned lower cosine distances, broad queries on grading policies retrieved isolated title sentences alongside multiple irrelevant IT paragraphs. This diluted the prompt context and triggered unintended refusal responses from the model. Guaranteeing balanced quota allocations across stores was required to resolve the issue.

**Idea for improvement (Advanced RAG):** I would integrate **Cross-Encoder Reranking** (such as `bge-reranker-large`). While independent vector search is fast, dense bi-encoders evaluate queries and passages in isolation. A cross-encoder performs joint attention over the query and candidate passages, filtering out weak sentence matches and prioritizing the most relevant chunks to combat the "Lost in the Middle" attention degradation effect.