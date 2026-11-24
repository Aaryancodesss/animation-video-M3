# M3 Animation Project: Eigenvalues & Eigenvectors

**Student Name:** Aaryan Sharma  
**Batch:** Turing  
**Student ID:** e25b071369  
**Course:** Linear Algebra (First-Year University Project)  

---

## 🎬 Watch the Video Online
▶️ **[Direct Stream / Download (1080p with Voice-Over)](https://github.com/Aaryancodesss/animation-video-M3/releases/download/v1.0.0/Eigenvalues_and_Eigenvectors_Animation_1080p.mp4)**  
🌟 **[View GitHub Release Page (v1.0.0)](https://github.com/Aaryancodesss/animation-video-M3/releases/tag/v1.0.0)**

---

A complete, university-level mathematical animation project explaining **Eigenvalues and Eigenvectors** of a $2 \times 2$ matrix, designed for a fellow first-year undergraduate student.

---

## 🎯 Learning Objective
> *"By the end of this video, the viewer will be able to explain eigenvectors as directions a matrix only stretches, and find them for a 2x2 matrix."*

---

## 📌 Matrix Example
$$A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$$
- **Eigenvalue $\lambda_1 = 3$**, with Eigenvector $\mathbf{v}_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$ (Stretched by $3\times$)
- **Eigenvalue $\lambda_2 = 1$**, with Eigenvector $\mathbf{v}_2 = \begin{bmatrix} 1 \\ -1 \end{bmatrix}$ (Preserved length, stretched by $1\times$)
- **Determinant connection:** $\det(A) = 2(2) - 1(1) = 3 = \lambda_1 \times \lambda_2$ (Geometric area scaling factor)

All mathematical assertions are rigorously verified in `_Code/verify.py` before animating.

---

## 🎨 Consistent Color Standards
- **Background:** Clean dark theme (`#0e1117`) for high clarity and visual comfort
- **$x$-axis basis vector $\mathbf{\hat{i}}$:** Green (`GREEN`)
- **$y$-axis basis vector $\mathbf{\hat{j}}$:** Red (`RED`)
- **Eigenvector 1 ($\lambda_1 = 3$):** Yellow (`YELLOW`) along span line $y = x$
- **Eigenvector 2 ($\lambda_2 = 1$):** Blue (`#3399FF`) along span line $y = -x$
- **Generic/Random vectors:** Orange (`#FFA500`)

---

## 📁 Repository Structure
```
M3_AnimationVideo_Eigenvectors_123456/
├── _Video.mp4              # The final 1080p, 30fps combined video (~4 mins 10s)
├── _Code/
│   ├── scenes.py           # All 8 Manim scene classes with thorough viva-ready comments
│   ├── verify.py           # Rigorous NumPy/algebraic verification script
│   ├── render_and_combine.py # Automated 1080p rendering and PyAV concatenation script
│   ├── mux_voiceover.py    # Merges any recorded audio (m4a/wav/mp3) into _Video_with_Voiceover.mp4
│   └── requirements.txt    # Python package dependencies
├── storyboard.md           # Comprehensive 6-scene storyboard table
├── narration_script.md     # Timed spoken-style voiceover script with second-by-second cues
└── README.md               # Project guide, documentation, AI disclosure, and credits
```

---

## 🎬 Scene Breakdown
1. **TitleScene (Opening Frame):** Professional title card, topic subtitle, student name `[YOUR NAME]`, and student ID `[YOUR ID]`.
2. **HookScene (Scene 1):** Poses the driving question: *"When a matrix transforms space, are there any directions that don't get rotated?"* Shows standard basis vectors $\mathbf{\hat{i}}$ and $\mathbf{\hat{j}}$ and generic vectors rotating under matrix $A$.
3. **ConceptIntroScene (Scene 2):** Defines $A\mathbf{v} = \lambda\mathbf{v}$, breaks down $A$, $\mathbf{v}$, and $\lambda$, and presents the learning objective.
4. **VisualIntuitionScene (Scene 3):** Shows invariant diagonal span lines $y = x$ and $y = -x$. Demonstrates $\mathbf{v}_1 = [1, 1]^T$ stretching by 3, while $\mathbf{v}_2 = [1, -1]^T$ stays unrotated and unchanged in length.
5. **WorkedExampleScene (Scene 4):** Complete step-by-step algebraic solution of $\det(A - \lambda I) = 0$, finding $\lambda = 3$ and $1$, solving $(A - \lambda I)\mathbf{v} = \mathbf{0}$ for each vector, and verifying numerically with $A\mathbf{v} = \lambda\mathbf{v}$.
6. **InterpretationScene (Scene 5):** Connects the unit square transformation (area = 1) to a parallelogram (area = 3) and links $\det(A) = 3 = \lambda_1 \times \lambda_2$.
7. **SummaryScene (Scene 6):** Recaps the 3 core takeaways, lists academic references, provides music placeholder, and displays mandatory AI disclosure.
8. **ClosingScene (Closing Frame):** Clean parting message encouraging further study.

---

## ⚙️ Installation & Rendering Instructions

### 1. Prerequisites (macOS / Linux / Windows)
Ensure Python 3.10+ is installed. In your project directory:

```bash
# 1. Navigate to the project root
cd M3_AnimationVideo_Eigenvectors_123456

# 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r _Code/requirements.txt
```

### 2. Verify the Mathematics
Before rendering, run the self-contained verification test:
```bash
python _Code/verify.py
```
*Expected Output:*
```
ALL VERIFICATIONS COMPLETED SUCCESSFULLY!
```

### 3. Render and Combine the Full 1080p Video
To render all 8 scenes at 1080p (30 fps) and merge them into `_Video.mp4`:
```bash
python _Code/render_and_combine.py
```
This automatically produces the final output at:
`M3_AnimationVideo_Eigenvectors_123456/_Video.mp4`

### 4. Alternative: Individual Scene Rendering via Manim CLI
```bash
# Low-quality quick check (480p)
manim -ql _Code/scenes.py TitleScene HookScene ConceptIntroScene VisualIntuitionScene WorkedExampleScene InterpretationScene SummaryScene ClosingScene

# High-quality render (1080p)
manim -qh _Code/scenes.py TitleScene HookScene ConceptIntroScene VisualIntuitionScene WorkedExampleScene InterpretationScene SummaryScene ClosingScene
```

### 5. Play and Preview the Video
```bash
open _Video.mp4                       # Opens in default macOS player (QuickTime)
# or
open -a "QuickTime Player" _Video.mp4
# or
open -a "VLC" _Video.mp4
```

### 6. Adding Voice-Over (Word-for-Word Narration)
Follow the timecoded script in [`narration_script.md`](file:///Users/aaryan6969/Desktop/animation-video-M3/M3_AnimationVideo_Eigenvectors_123456/narration_script.md).
- **Option A (iMovie):** Open iMovie, drag `_Video.mp4` into the timeline, click the microphone icon, and read the script as the video plays.
- **Option B (Automatic Muxer):** Record your voice in QuickTime or Voice Memos, save as `voiceover.m4a`, and run:
  ```bash
  python _Code/mux_voiceover.py voiceover.m4a
  ```
  This automatically produces `_Video_with_Voiceover.mp4`.

---

## ⏱️ Video Metrics & Timing
- **Resolution:** $1920 \times 1080$ (16:9 widescreen)
- **Frame Rate:** 30 fps
- **Total Duration:** ~4 minutes 50 seconds (well within the target 5-minute length and 7-minute maximum)
- **Audio:** No generated synthetic voiceover. Ample `self.wait(...)` pauses are embedded throughout the code to allow recording narration separately using `narration_script.md`.

---

## 🤖 AI Disclosure Statement
> **AI tools (Antigravity / Gemini) were used to help generate the Manim code. I reviewed, modified, and tested it.**

---

## 📚 References & Credits
- **Grant Sanderson (3Blue1Brown):** *Essence of Linear Algebra*, Chapter 14: "Eigenvalues and eigenvectors".
- **Gilbert Strang:** *Introduction to Linear Algebra*, 5th Edition, Wellesley-Cambridge Press.
- **Manim Community Developers:** [https://www.manim.community/](https://www.manim.community/)
- **Music Placeholder:** Royalty-free background audio (e.g., Incompetech / Kevin MacLeod).
