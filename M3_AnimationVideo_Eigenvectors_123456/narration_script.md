# Comprehensive Narration & Voice-Over Script

**Project:** University Animation Project — Linear Algebra  
**Student:** Aaryan Sharma  
**Batch:** Turing  
**Student ID:** e25b071369  
**Video:** [`_Video.mp4`](file:///Users/aaryan6969/Desktop/animation-video-M3/M3_AnimationVideo_Eigenvectors_123456/_Video.mp4)  
**Total Runtime:** 4 minutes 10 seconds (249.60 seconds)  
**Purpose:** Word-for-word voice-over script ensuring that **everything appearing, transforming, and deforming on the screen is verbalized aloud**.

---

## 🎙️ Recording Quick-Guide (3 Easy Options on macOS)

### Option 1: Live Voiceover in iMovie (Easiest & Most Natural)
1. Open **iMovie** on your Mac (`open -a "iMovie"`).
2. Create a new **Movie project**, and drag `_Video.mp4` into the timeline.
3. Click the **Microphone icon** (Record Voiceover) just beneath the video preview window.
4. Press the red record button, read the script below as the animations play, and press Stop when finished.
5. Go to **File → Share → File** to export your completed video with voiceover.

### Option 2: Voice Memos / QuickTime Player + Auto-Muxer Script
1. Open **Voice Memos** or **QuickTime Player** (**File → New Audio Recording**).
2. Play `_Video.mp4` on your screen while reading the script into your microphone.
3. Save your audio recording as `voiceover.m4a` inside the project folder:  
   `/Users/aaryan6969/Desktop/animation-video-M3/M3_AnimationVideo_Eigenvectors_123456/voiceover.m4a`
4. Run our automated muxing script:
   ```bash
   python _Code/mux_voiceover.py voiceover.m4a
   ```
   This automatically synchronizes the audio and exports:  
   `M3_AnimationVideo_Eigenvectors_123456/_Video_with_Voiceover.mp4`.

---

## 📜 Word-for-Word Timecoded Teleprompter Script

### Scene 0: Title & Student Introduction (`TitleScene`)
**Timeline:** `0:00` → `0:17.5` *(17.5 seconds)*

* **[0:00 - 0:05]** *(Visual: Title "Eigenvalues & Eigenvectors" and subtitle "Directions That Only Stretch Under Linear Transformations" appear.)*  
  🗣️ **Spoken:**  
  *"Welcome to this animation tutorial on eigenvalues and eigenvectors: directions that only stretch under linear transformations."*

* **[0:05 - 0:13]** *(Visual: Divider line and student details display: Student: Aaryan Sharma, ID: e25b071369, Batch: Turing, Linear Algebra.)*  
  🗣️ **Spoken:**  
  *"I am Aaryan Sharma, student ID e-2-5-b-0-7-1-3-6-9, from Batch Turing. In this video, we will explore the geometric meaning of eigenvectors and learn how to calculate them step-by-step for a two-by-two matrix."*

* **[0:13 - 0:17]** *(Visual: Elements fade out to a dark background.)*  
  🗣️ **Spoken:**  
  *"Let's begin by observing how a matrix alters space."*

---

### Scene 1: The Hook — Invariant Directions (`HookScene`)
**Timeline:** `0:17.5` → `0:47.0` *(29.5 seconds)*

* **[0:17.5 - 0:24]** *(Visual: Question writes across the top: 'When a matrix transforms space, are there any directions that don't get rotated?')*  
  🗣️ **Spoken:**  
  *"When a matrix transforms space, are there any directions that don't get rotated?"*

* **[0:24 - 0:31]** *(Visual: Coordinate plane fades in with matrix badge A = [[2,1],[1,2]]. Vector i-hat appears in green along the horizontal axis, j-hat in red along the vertical axis, and vector w in orange.)*  
  🗣️ **Spoken:**  
  *"Here is our coordinate plane. In green, we have the standard unit vector i-hat along the x-axis, and in red, j-hat along the y-axis, alongside a generic orange vector w. In the upper corner is our transformation matrix: A equals [[2, 1], [1, 2]]."*

* **[0:31 - 0:38]** *(Visual: Text notes 'Observe how most vectors rotate away from their lines...' Space deforms smoothly.)*  
  🗣️ **Spoken:**  
  *"Watch what happens when matrix A transforms space. Notice how most vectors tilt and rotate away from their original lines."*

* **[0:38 - 0:47]** *(Visual: i-hat transforms to [2,1] in green; j-hat transforms to [1,2] in red; w transforms to [3.5, 4] in orange. Summary text appears: 'Both i-hat and j-hat rotated! Are any directions preserved?')*  
  🗣️ **Spoken:**  
  *"i-hat tilts upward to [2, 1] transpose. j-hat tilts to the right to [1, 2] transpose. And our orange vector swings off its line completely. Both standard basis vectors rotated! Are there any special directions whose lines are preserved?"*

---

### Scene 2: Concept Introduction (`ConceptIntroScene`)
**Timeline:** `0:47.0` → `1:20.5` *(33.5 seconds)*

* **[0:47 - 0:56]** *(Visual: Title 'The Eigenvalue Equation' appears. A large yellow-boxed equation writes: 'A v = λ v'.)*  
  🗣️ **Spoken:**  
  *"Yes! And that brings us to the core equation of linear algebra: A times v equals lambda times v."*

* **[0:56 - 1:08]** *(Visual: Definitions appear sequentially: Yellow 'A: The Square Transformation Matrix', Blue 'v: An Eigenvector (non-zero vector whose span direction is preserved)', Green 'λ: An Eigenvalue (scalar scaling factor stretching v)'.)*  
  🗣️ **Spoken:**  
  *"Let's define each term clearly before using it. A is our square transformation matrix. v is an eigenvector—a non-zero vector whose direction line is completely preserved. And lambda is the eigenvalue—the scalar factor by which v stretches, shrinks, or keeps its length."*

* **[1:08 - 1:20]** *(Visual: Framed Learning Objective card displays.)*  
  🗣️ **Spoken:**  
  *"Our learning objective is: 'By the end of this video, you will be able to explain eigenvectors as directions a matrix only stretches, and find them for a 2 by 2 matrix.' Let's see these invariant directions with our own eyes."*

---

### Scene 3: Visual Intuition (`VisualIntuitionScene`)
**Timeline:** `1:20.5` → `1:57.0` *(36.5 seconds)*

* **[1:20.5 - 1:33]** *(Visual: Coordinate plane displays two dashed diagonal lines: Yellow Line 1 along y = x, Blue Line 2 along y = -x. Vector v1 in yellow on y = x, vector v2 in blue on y = -x, and random orange vector u appear.)*  
  🗣️ **Spoken:**  
  *"Look at the two dashed diagonal lines on our grid. Line 1 in yellow lies along y equals x, holding vector v1. Line 2 in blue lies along y equals negative x, holding vector v2. We also have a random orange vector u pointing into the first quadrant."*

* **[1:33 - 1:47]** *(Visual: The transformation applies! Vector u rotates off into [3.0, 4.5]. Vector v1 stretches from [1, 1] to [3, 3] along the yellow line. Vector v2 remains exactly at [1, -1] along the blue line.)*  
  🗣️ **Spoken:**  
  *"Now, watch the matrix act! The random vector rotates away into space. But look at our two eigenvectors! Yellow vector v1 stays perfectly on the yellow line, stretched threefold to [3, 3] transpose! And blue vector v2 stays right on the blue line, with its length completely unchanged!"*

* **[1:47 - 1:57]** *(Visual: Highlight boxes appear around 'A v1 = 3 v1 (λ1 = 3)' and 'A v2 = 1 v2 (λ2 = 1)'.)*  
  🗣️ **Spoken:**  
  *"v1 scaled by lambda 1 equals 3. v2 scaled by lambda 2 equals 1. They experience pure stretching without any rotation. Now let's calculate these exact numbers algebraically."*

---

### Scene 4: Worked Example (`WorkedExampleScene`)
**Timeline:** `1:57.0` → `2:49.1` *(52.1 seconds)*

* **[1:57 - 2:05]** *(Visual: Title: 'Worked Example: Finding Eigenvalues & Eigenvectors'. 'Step 1: Solve the Characteristic Equation det(A - λI) = 0' appears.)*  
  🗣️ **Spoken:**  
  *"Step 1: To find the eigenvalues, we solve the characteristic equation: determinant of A minus lambda I equals zero."*

* **[2:05 - 2:20]** *(Visual: Step-by-step determinant expansion appears line-by-line:
  det([[2-λ, 1], [1, 2-λ]]) = 0
  (2 - λ)(2 - λ) - (1)(1) = 0
  (2 - λ)² - 1 = 0  =>  λ² - 4λ + 3 = 0
  (λ - 3)(λ - 1) = 0
  Result highlighted in yellow box: 'Eigenvalues: λ1 = 3, λ2 = 1'.)*  
  🗣️ **Spoken:**  
  *"We subtract lambda along the main diagonal. Computing the determinant gives (2 minus lambda) times (2 minus lambda) minus (1 times 1) equals zero. That simplifies to (2 minus lambda) squared minus 1 equals zero, or lambda squared minus 4 lambda plus 3 equals zero. Factoring gives (lambda minus 3) times (lambda minus 1) equals zero. This yields our two eigenvalues: lambda 1 equals 3, and lambda 2 equals 1!"*

* **[2:20 - 2:38]** *(Visual: Screen transitions to Step 2 with two columns:
  Column 1 (Yellow): For λ1 = 3: (A - 3I)v = 0 => [[-1, 1], [1, -1]][x, y]ᵀ = [0, 0]ᵀ => -x + y = 0 => y = x => v1 = [1, 1]ᵀ.
  Column 2 (Blue): For λ2 = 1: (A - 1I)v = 0 => [[1, 1], [1, 1]][x, y]ᵀ = [0, 0]ᵀ => x + y = 0 => y = -x => v2 = [1, -1]ᵀ.)*  
  🗣️ **Spoken:**  
  *"Step 2: We solve (A minus lambda I) times v equals zero for each eigenvalue. For lambda 1 equals 3, the matrix becomes [[-1, 1], [1, -1]], giving negative x plus y equals zero, so y equals x. Setting x to 1 gives our first eigenvector: v1 equals [1, 1] transpose in yellow. For lambda 2 equals 1, the matrix becomes [[1, 1], [1, 1]], giving x plus y equals zero, so y equals negative x. Setting x to 1 gives our second eigenvector: v2 equals [1, -1] transpose in blue."*

* **[2:38 - 2:49]** *(Visual: Green box appears: 'Numerical Verification: Av = λv'. Shows A v1 = [[2,1],[1,2]][1,1]ᵀ = [3,3]ᵀ = 3 v1 ✓ and A v2 = [[2,1],[1,2]][1,-1]ᵀ = [1,-1]ᵀ = 1 v2 ✓.)*  
  🗣️ **Spoken:**  
  *"We verify by direct substitution: A times [1, 1] gives [3, 3], which is exactly 3 times v1! And A times [1, -1] gives [1, -1], which is 1 times v2! Both calculations check out with one hundred percent accuracy."*

---

### Scene 5: Geometric Interpretation & Determinant (`InterpretationScene`)
**Timeline:** `2:49.1` → `3:21.1` *(32.0 seconds)*

* **[2:49 - 3:00]** *(Visual: Grid shows standard basis vectors i-hat (green) and j-hat (red), with unit square of Area = 1. Eigenvectors v1 (yellow) and v2 (blue) also appear. Info panel lists det(A) = 3 and det(A) = λ1 × λ2 = 3 × 1 = 3.)*  
  🗣️ **Spoken:**  
  *"Now let's connect the algebra back to geometry. Consider the unit square formed by basis vectors i-hat and j-hat, with an initial area of 1."*

* **[3:00 - 3:12]** *(Visual: Unit square transforms into a yellow parallelogram with 'Transformed Area = 3'. i-hat maps to [2, 1], j-hat maps to [1, 2], and v1 stretches to [3, 3].)*  
  🗣️ **Spoken:**  
  *"Under matrix A, the unit square shears and stretches into a parallelogram with an area of exactly 3. Notice that the determinant of A is (2)(2) - (1)(1) = 3."*

* **[3:12 - 3:21]** *(Visual: Highlight box frames 'det(A) = λ1 × λ2 = 3 × 1 = 3'.)*  
  🗣️ **Spoken:**  
  *"Notice the connection: the determinant equals lambda 1 times lambda 2: 3 times 1 equals 3! The determinant is the geometric area scaling factor, and the eigenvectors decouple this 2D distortion into independent 1D scaling axes."*

---

### Scene 6: Summary & Credits (`SummaryScene`)
**Timeline:** `3:21.1` → `3:55.6` *(34.5 seconds)*

* **[3:21 - 3:35]** *(Visual: Title 'Summary: Core Takeaways'. Three bullet points appear:
  1. Invariant Directions: Eigenvectors v stay along their span line under matrix A.
  2. Scaling Factors: Eigenvalues λ stretch each eigenvector (solve det(A - λI) = 0).
  3. Matrix Insight: det(A) = λ1 × λ2 gives the geometric area scaling factor of the map.)*  
  🗣️ **Spoken:**  
  *"To summarize our three core takeaways: First, eigenvectors are the invariant directions that experience zero rotation under a matrix transformation. Second, eigenvalues are the scalar factors by which those directions stretch. Third, the product of the eigenvalues equals the determinant, representing the overall area scaling factor."*

* **[3:35 - 3:45]** *(Visual: References box displays 3Blue1Brown and Gilbert Strang, with Music Credit placeholder.)*  
  🗣️ **Spoken:**  
  *"Special thanks to Grant Sanderson's 3Blue1Brown series and Gilbert Strang's classic textbook for pedagogical inspiration."*

* **[3:45 - 3:55]** *(Visual: Yellow disclosure banner displays: 'AI tools (Antigravity / Gemini) were used to help generate the Manim code. I reviewed and tested it.')*  
  🗣️ **Spoken:**  
  *"As disclosed on screen, AI tools were used to help generate the Manim code, which I thoroughly reviewed, tested, and verified."*

---

### Closing Frame (`ClosingScene`)
**Timeline:** `3:55.6` → `4:09.6` *(14.0 seconds)*

* **[3:55 - 4:09.6]** *(Visual: Centered card appears: 'Thank You for Watching! Master Linear Algebra One Direction at a Time.' Fades out to black.)*  
  🗣️ **Spoken:**  
  *"Thank you so much for watching, and best of luck with your linear algebra journey!"*
