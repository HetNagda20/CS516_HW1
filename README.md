# Moments (CS 516 — HW1): Auto ALT + AI Label Search

This fork adds two ML features:

- **Automatic ALT text** on image upload (Azure Image Analysis 4.0 — captions + tags)  
- **Keyword search** over **AI-detected labels** (`/search?category=ml&q=...`)

**Specific commit for grading:**  
https://github.com/HetNagda20/CS516_HW1/commit/4fca22c837b3cdc37a525ad152fd4d4cbadbf2f0

---

## Prerequisites

- macOS / Linux / Windows  
- **uv** (fast Python package manager)
  - macOS: `brew install uv`
  - Windows: `winget install --id=astral-sh.uv -e`
  - Alt: `pip install uv`
- Azure AI Vision (Computer Vision) resource with **Image Analysis 4.0 captions** enabled in 'US-East'.

---

## Setup and Running the App

1) **Clone**
```bash
git clone git@github.com:HetNagda20/CS516_HW1.git
cd CS516_HW1

```
2) **Create `.env` in the root folder.(Do Not Commit)**
   **If you don't have Azure API setup then follow this:** [Azure API Host Setup](#azure-api-host-setup-image-analysis)</br>
```
VISION_API=azure
VISION_KEY=<your_azure_vision_key>
VISION_ENDPOINT=https://<your-resource>.cognitiveservices.azure.com
```
  

3) **Install dependencies**</br>
    Navigate to your project directory. 
```shell
uv sync
```
4) **To initialize the app, run the flask init-app command:**
```shell
uv run flask init-app
```
5) **(Optional)If you just want to try it out, generate fake data with flask lorem command then run the app:**
```shell
uv run flask lorem
```
(If you see an error for any missing dependencies, you can add them in the following way and try running the command again)
```shell
uv add Faker
```

**Lorem will create a test account:**

email: admin@helloflask.com \
password: moments

Now you can run the app:
```shell
uv run flask run
```
* Running on http://127.0.0.1:5000/

## How to use

- **Upload a photo**
  - Go to **Upload** and add any image.
  - The app will generate **ALT text automatically** (you’ll see an **“Auto ALT”** pill on the photo page).
  - Screen readers will use this ALT text; you can verify by viewing page source or Inspect Element:
    - Look for `<img ... alt="your caption here">`.

- **Override ALT with your own text**
  - On the photo page, edit **Description** and save.
  - Your description becomes the `alt` text and the **Auto ALT** badge disappears.

- **Search with AI labels**
  - Use the header search (defaults to **AI Labels**), or visit URLs like:
    ```
    /search?category=ml&q=dog
    /search?category=ml&q=golden retriever
    /search?category=ml&q=cat, sofa
    ```
  - Terms split by spaces/commas are **AND-matched** (case-insensitive) against AI labels (and also checked in `alt_text` for simple plural/singular matches).

- **Tips**
  - If you used `flask lorem`, those images may not have ML labels; upload a new photo to see captions and labels.
  - If search returns no results, try a single term that appears in the label chips on the photo sidebar.
---   
## Azure API Host Setup (Image Analysis)
1) **Prereqs**

- An Azure subscription where you **can create resources**.
  - If you see “You do not have permissions to create resource groups…”, ask the subscription admin for Contributor access or use your own (e.g., Free/Student) subscription.


2) **Create a Resource Group (Portal)**

   1. Go to **portal.azure.com** → **Resource groups** → **Create**.
   2. Name: e.g., `cs516-hw1`
   3. Region: pick one that supports **Image Analysis 4.0 captions** (Currently I am using **East US**).
   4. Create.

3) **Create the Vision resource**
   1. Create a resource → search Azure AI services (or Azure AI Vision / Computer Vision).
   2. Create the Vision resource.
   3. Subscription: your sub
   4. Resource group: `cs516-hw1`
   5. Region: **East US** (or any IA 4.0 captions region)
   6. Pricing tier: S0 (trial fine)
   7. Create.
   8. Let the deployment complete.
      
4) **Get the Endpoint and Key:**
   Portal: Resource → Keys and Endpoint
   1. Endpoint: https://<your-resource>.cognitiveservices.azure.com
   2. Key: use Key 1 (or Key 2)
