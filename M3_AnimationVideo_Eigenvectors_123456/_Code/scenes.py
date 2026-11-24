"""
scenes.py
=========
Manim Community Edition animation script explaining Eigenvalues & Eigenvectors
for a first-year undergraduate Linear Algebra student.

Matrix Example:
    A = [[2, 1],
         [1, 2]]

Eigenpairs:
    λ₁ = 3,  v₁ = [ 1,  1 ]ᵀ  (Yellow)
    λ₂ = 1,  v₂ = [ 1, -1 ]ᵀ  (Blue)

Color Scheme:
    - Background: Black
    - x-axis basis vector î: GREEN
    - y-axis basis vector ĵ: RED
    - Eigenvector 1 (λ=3): YELLOW
    - Eigenvector 2 (λ=1): BLUE
    - Generic/Transformed vectors: ORANGE / WHITE / GREY

All scenes use pure Manim vectors, geometric mobjects, and Text (Pango/Cairo)
to ensure 100% reliable rendering on any system without requiring external
LaTeX distributions.
"""

from manim import *
import numpy as np

# Global presentation settings
config.background_color = "#0e1117"  # Deep clean dark theme
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30

# Consistent color constants
COLOR_IHAT = GREEN
COLOR_JHAT = RED
COLOR_EIG1 = YELLOW
COLOR_EIG2 = "#3399FF"  # Bright vibrant blue
COLOR_GENERIC = "#FFA500"  # Orange
COLOR_TEXT_PRIMARY = WHITE
COLOR_TEXT_MUTED = "#A0AAB2"


# ==============================================================================
# Helper functions for clean mathematical visual layout
# ==============================================================================

def create_matrix_box(matrix_data, title="A", color=WHITE, font_size=28):
    """
    Creates a clearly formatted visual 2x2 matrix with brackets and labels.
    """
    title_mob = Text(f"{title} =", font_size=font_size, color=color, weight=BOLD)
    
    # Text grid for entries
    row1 = Text(f"{matrix_data[0][0]}    {matrix_data[0][1]}", font_size=font_size, color=color)
    row2 = Text(f"{matrix_data[1][0]}    {matrix_data[1][1]}", font_size=font_size, color=color)
    grid = VGroup(row1, row2).arrange(DOWN, buff=0.25)
    
    # Left and right visual brackets
    bracket_l = Text("[", font_size=font_size * 2, color=color)
    bracket_r = Text("]", font_size=font_size * 2, color=color)
    bracket_l.next_to(grid, LEFT, buff=0.15)
    bracket_r.next_to(grid, RIGHT, buff=0.15)
    
    matrix_group = VGroup(title_mob, bracket_l, grid, bracket_r)
    matrix_group.arrange(RIGHT, buff=0.2)
    return matrix_group


# ==============================================================================
# Scene 0: Title Scene
# ==============================================================================

class TitleScene(Scene):
    """
    Opening Title Frame introducing the topic, student credentials,
    and foundational premise.
    """
    def construct(self):
        title = Text("Eigenvalues & Eigenvectors", font_size=56, color=WHITE, weight=BOLD)
        subtitle = Text("Directions That Only Stretch Under Linear Transformations", 
                        font_size=28, color="#58C4DD")
        
        divider = Line(LEFT * 5, RIGHT * 5, color=GREY_B, stroke_width=2)
        
        student_name = Text("Student: Aaryan Sharma", font_size=26, color=COLOR_TEXT_MUTED)
        student_id = Text("ID: e25b071369  |  Batch: Turing", font_size=24, color=COLOR_TEXT_MUTED)
        course_info = Text("Linear Algebra | University Animation Project", font_size=22, color=GREY_A)
        
        header_group = VGroup(title, subtitle, divider).arrange(DOWN, buff=0.35)
        credits_group = VGroup(student_name, student_id, course_info).arrange(DOWN, buff=0.25)
        all_content = VGroup(header_group, credits_group).arrange(DOWN, buff=0.8).center()
        
        # Narration lead-in pause
        self.wait(1)
        self.play(FadeIn(title, shift=UP * 0.5), run_time=1.5)
        self.play(FadeIn(subtitle, shift=UP * 0.3), Create(divider), run_time=1.5)
        self.wait(1.5)
        
        self.play(FadeIn(credits_group, shift=UP * 0.4), run_time=1.5)
        # Ample timing gap for student introduction narration
        self.wait(8)
        
        self.play(FadeOut(all_content, shift=DOWN * 0.5), run_time=1.5)
        self.wait(1)


# ==============================================================================
# Scene 1: Hook Scene
# ==============================================================================

class HookScene(Scene):
    """
    Poses the core motivational question:
    'When a matrix transforms space, are there any directions that don't get rotated?'
    Demonstrates standard basis and generic vectors deforming under matrix A.
    """
    def construct(self):
        question = Text(
            "When a matrix transforms space, are there any directions that don't get rotated?",
            font_size=26,
            color=WHITE,
            weight=BOLD
        ).to_edge(UP, buff=0.5)
        
        matrix_A = np.array([[2.0, 1.0], [1.0, 2.0]])
        matrix_badge = create_matrix_box([[2, 1], [1, 2]], title="Transformation A", color=YELLOW)
        matrix_badge.to_corner(UL, buff=0.6).shift(DOWN * 0.4)
        
        # Coordinate Plane
        plane = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-3.5, 3.5, 1],
            x_length=9,
            y_length=6.3,
            background_line_style={"stroke_color": GREY_C, "stroke_width": 1, "stroke_opacity": 0.35},
            axis_config={"color": GREY_A, "stroke_width": 2}
        ).shift(RIGHT * 1.5 + DOWN * 0.2)
        
        # Basis vectors & sample vector
        # î = [1, 0] (Green), ĵ = [0, 1] (Red), w = [1, 1.5] (Generic Orange)
        i_vec = Arrow(plane.c2p(0, 0), plane.c2p(1, 0), buff=0, color=COLOR_IHAT, stroke_width=5)
        i_label = Text("î = [1, 0]ᵀ", font_size=20, color=COLOR_IHAT, weight=BOLD).next_to(i_vec, DOWN, buff=0.15)
        
        j_vec = Arrow(plane.c2p(0, 0), plane.c2p(0, 1), buff=0, color=COLOR_JHAT, stroke_width=5)
        j_label = Text("ĵ = [0, 1]ᵀ", font_size=20, color=COLOR_JHAT, weight=BOLD).next_to(j_vec, LEFT, buff=0.15)
        
        w_vec = Arrow(plane.c2p(0, 0), plane.c2p(1, 1.5), buff=0, color=COLOR_GENERIC, stroke_width=4)
        w_label = Text("w", font_size=22, color=COLOR_GENERIC).next_to(w_vec.get_end(), UR, buff=0.1)
        
        # Entrance animations
        self.play(Write(question), run_time=2)
        self.wait(1.5)
        
        self.play(FadeIn(plane), FadeIn(matrix_badge), run_time=1.5)
        self.play(GrowArrow(i_vec), FadeIn(i_label), GrowArrow(j_vec), FadeIn(j_label), run_time=1.5)
        self.play(GrowArrow(w_vec), FadeIn(w_label), run_time=1)
        self.wait(3)
        
        # Explanation text on left side
        obs_text = Text("Observe how most vectors\nrotate away from their lines...", 
                        font_size=20, color=COLOR_TEXT_MUTED, line_spacing=1.3)
        obs_text.next_to(matrix_badge, DOWN, buff=0.6).align_to(matrix_badge, LEFT)
        self.play(FadeIn(obs_text), run_time=1.5)
        self.wait(2)
        
        # Target vectors after multiplying by A:
        # A @ [1, 0] = [2, 1]
        # A @ [0, 1] = [1, 2]
        # A @ [1, 1.5] = [2(1)+1.5, 1+2(1.5)] = [3.5, 4]
        i_target = Arrow(plane.c2p(0, 0), plane.c2p(2, 1), buff=0, color=COLOR_IHAT, stroke_width=5)
        i_label_target = Text("A î = [2, 1]ᵀ", font_size=20, color=COLOR_IHAT, weight=BOLD).next_to(i_target.get_end(), DR, buff=0.1)
        
        j_target = Arrow(plane.c2p(0, 0), plane.c2p(1, 2), buff=0, color=COLOR_JHAT, stroke_width=5)
        j_label_target = Text("A ĵ = [1, 2]ᵀ", font_size=20, color=COLOR_JHAT, weight=BOLD).next_to(j_target.get_end(), UL, buff=0.1)
        
        w_target = Arrow(plane.c2p(0, 0), plane.c2p(3.5, 4), buff=0, color=COLOR_GENERIC, stroke_width=4)
        w_label_target = Text("A w", font_size=22, color=COLOR_GENERIC).next_to(w_target.get_end(), UR, buff=0.1)
        
        # Animate the linear transformation
        self.play(
            Transform(i_vec, i_target),
            Transform(i_label, i_label_target),
            Transform(j_vec, j_target),
            Transform(j_label, j_label_target),
            Transform(w_vec, w_target),
            Transform(w_label, w_label_target),
            run_time=3.5
        )
        self.wait(3)
        
        hook_summary = Text("Both î and ĵ rotated!\nAre any directions preserved?", 
                            font_size=22, color=YELLOW, weight=BOLD, line_spacing=1.3)
        hook_summary.next_to(obs_text, DOWN, buff=0.6).align_to(obs_text, LEFT)
        self.play(FadeIn(hook_summary), run_time=1.5)
        
        # Narration pause
        self.wait(5)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.5)
        self.wait(1)


# ==============================================================================
# Scene 2: Concept Introduction Scene
# ==============================================================================

class ConceptIntroScene(Scene):
    """
    Defines the fundamental equation: A v = λ v.
    Defines A, v, and λ with crystal clarity and presents the formal learning objective.
    """
    def construct(self):
        title = Text("The Eigenvalue Equation", font_size=40, color=WHITE, weight=BOLD).to_edge(UP, buff=0.6)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=1)
        self.wait(1)
        
        # Core equation: A v = λ v
        eq_text = Text("A v  =  λ v", font_size=60, color=WHITE, weight=BOLD)
        eq_box = SurroundingRectangle(eq_text, color=YELLOW, buff=0.35, stroke_width=2.5)
        eq_group = VGroup(eq_text, eq_box).shift(UP * 1.5)
        
        self.play(Write(eq_text), Create(eq_box), run_time=2)
        self.wait(2)
        
        # Definitions of components
        def_A = VGroup(
            Text("A", font_size=32, color=YELLOW, weight=BOLD),
            Text(": The Square Transformation Matrix (e.g. 2×2 linear map)", font_size=24, color=WHITE)
        ).arrange(RIGHT, buff=0.2)
        
        def_v = VGroup(
            Text("v", font_size=32, color="#3399FF", weight=BOLD),
            Text(": An Eigenvector (a non-zero vector whose span direction is preserved)", font_size=24, color=WHITE)
        ).arrange(RIGHT, buff=0.2)
        
        def_lambda = VGroup(
            Text("λ", font_size=32, color=GREEN, weight=BOLD),
            Text(": An Eigenvalue (the scalar scaling factor stretching v)", font_size=24, color=WHITE)
        ).arrange(RIGHT, buff=0.2)
        
        defs = VGroup(def_A, def_v, def_lambda).arrange(DOWN, buff=0.45, aligned_edge=LEFT).shift(DOWN * 0.2)
        
        for item in [def_A, def_v, def_lambda]:
            self.play(FadeIn(item, shift=RIGHT * 0.4), run_time=1.5)
            self.wait(1.5)
        
        self.wait(2)
        
        # Learning Objective Banner
        goal_title = Text("Learning Objective", font_size=24, color=YELLOW, weight=BOLD)
        goal_text = Text(
            '"By the end of this video, you will be able to explain eigenvectors as directions\n'
            ' a matrix only stretches, and find them for a 2×2 matrix."',
            font_size=20,
            color=WHITE,
            line_spacing=1.3,
            slant=ITALIC
        )
        goal_content = VGroup(goal_title, goal_text).arrange(DOWN, buff=0.2)
        goal_card = SurroundingRectangle(goal_content, color=GREY_C, buff=0.3, fill_color="#1a1e24", fill_opacity=0.8)
        goal_group = VGroup(goal_card, goal_content).to_edge(DOWN, buff=0.6)
        
        self.play(FadeIn(goal_group, shift=UP * 0.4), run_time=2)
        # Narration gap for reading learning goal and setting up example
        self.wait(12)
        
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.5)
        self.wait(1)


# ==============================================================================
# Scene 3: Visual Intuition Scene
# ==============================================================================

class VisualIntuitionScene(Scene):
    """
    Animates space deforming under matrix A.
    Shows generic vectors swinging off their lines, while the two eigenvectors
    (1, 1) and (1, -1) stay perfectly on their lines, scaled by 3 and 1.
    """
    def construct(self):
        title = Text("Visual Intuition: Preserved Invariant Lines", font_size=28, color=WHITE, weight=BOLD)
        title.to_edge(UP, buff=0.4)
        self.play(FadeIn(title), run_time=1)
        
        # Coordinate Plane
        plane = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-3.5, 3.5, 1],
            x_length=9.5,
            y_length=6.65,
            background_line_style={"stroke_color": GREY_D, "stroke_width": 1, "stroke_opacity": 0.4},
            axis_config={"color": GREY_A, "stroke_width": 2}
        ).shift(RIGHT * 1.2 + DOWN * 0.2)
        
        # Invariant eigen-lines (dashed)
        # Line 1: y = x (Span of [1, 1])
        line_eig1 = DashedLine(plane.c2p(-3.5, -3.5), plane.c2p(3.5, 3.5), color=COLOR_EIG1, stroke_width=2.5, dash_length=0.15)
        label_line1 = Text("Line 1: y = x", font_size=18, color=COLOR_EIG1).next_to(plane.c2p(3, 3), UP, buff=0.15)
        
        # Line 2: y = -x (Span of [1, -1])
        line_eig2 = DashedLine(plane.c2p(-3.5, 3.5), plane.c2p(3.5, -3.5), color=COLOR_EIG2, stroke_width=2.5, dash_length=0.15)
        label_line2 = Text("Line 2: y = -x", font_size=18, color=COLOR_EIG2).next_to(plane.c2p(3, -3), DOWN, buff=0.15)
        
        # Vectors before transformation
        v1_init = Arrow(plane.c2p(0, 0), plane.c2p(1, 1), buff=0, color=COLOR_EIG1, stroke_width=5)
        v1_label = Text("v₁ = [1, 1]ᵀ", font_size=20, color=COLOR_EIG1, weight=BOLD).next_to(v1_init.get_end(), UL, buff=0.1)
        
        v2_init = Arrow(plane.c2p(0, 0), plane.c2p(1, -1), buff=0, color=COLOR_EIG2, stroke_width=5)
        v2_label = Text("v₂ = [1, -1]ᵀ", font_size=20, color=COLOR_EIG2, weight=BOLD).next_to(v2_init.get_end(), UR, buff=0.1)
        
        # Random non-eigenvector
        rand_init = Arrow(plane.c2p(0, 0), plane.c2p(0.5, 2.0), buff=0, color=COLOR_GENERIC, stroke_width=4)
        rand_label = Text("u (random)", font_size=18, color=COLOR_GENERIC).next_to(rand_init.get_end(), RIGHT, buff=0.1)
        
        # Left info panel
        panel_box = RoundedRectangle(corner_radius=0.2, height=5.5, width=4.0, color=GREY_B, fill_color="#14181d", fill_opacity=0.9)
        panel_box.to_corner(UL, buff=0.4).shift(DOWN * 0.4)
        
        panel_title = Text("Matrix Action on Directions", font_size=20, color=YELLOW, weight=BOLD).next_to(panel_box.get_top(), DOWN, buff=0.3)
        panel_msg1 = Text("• Random vectors rotate\n  away from their line.", font_size=16, color=WHITE, line_spacing=1.2).next_to(panel_title, DOWN, buff=0.4).align_to(panel_box, LEFT).shift(RIGHT * 0.3)
        panel_msg2 = Text("• Eigenvectors stay exactly\n  on their original line,\n  scaled by eigenvalue λ.", font_size=16, color=WHITE, line_spacing=1.2).next_to(panel_msg1, DOWN, buff=0.4).align_to(panel_msg1, LEFT)
        
        self.play(FadeIn(plane), FadeIn(panel_box), FadeIn(panel_title), run_time=1.5)
        self.play(Create(line_eig1), FadeIn(label_line1), Create(line_eig2), FadeIn(label_line2), run_time=2)
        self.play(GrowArrow(v1_init), FadeIn(v1_label), GrowArrow(v2_init), FadeIn(v2_label), GrowArrow(rand_init), FadeIn(rand_label), run_time=2)
        self.play(FadeIn(panel_msg1), run_time=1)
        self.wait(3)
        
        # Now transform all vectors by A = [[2, 1], [1, 2]]:
        # A @ [0.5, 2.0] = [2(0.5)+2, 0.5+2(2)] = [3.0, 4.5] (rotates violently!)
        # A @ [1, 1] = [3, 3]  (stretched by 3 along y = x)
        # A @ [1, -1] = [1, -1] (stretched by 1 along y = -x, unchanged!)
        rand_target = Arrow(plane.c2p(0, 0), plane.c2p(3.0, 4.5), buff=0, color=COLOR_GENERIC, stroke_width=4)
        rand_label_target = Text("A u (Rotated!)", font_size=18, color=COLOR_GENERIC).next_to(rand_target.get_end(), RIGHT, buff=0.1)
        
        v1_target = Arrow(plane.c2p(0, 0), plane.c2p(3, 3), buff=0, color=COLOR_EIG1, stroke_width=6)
        v1_label_target = Text("A v₁ = 3 v₁  (λ₁ = 3)", font_size=20, color=COLOR_EIG1, weight=BOLD).next_to(v1_target.get_end(), UL, buff=0.15)
        
        v2_target = Arrow(plane.c2p(0, 0), plane.c2p(1, -1), buff=0, color=COLOR_EIG2, stroke_width=6)
        v2_label_target = Text("A v₂ = 1 v₂  (λ₂ = 1)", font_size=20, color=COLOR_EIG2, weight=BOLD).next_to(v2_target.get_end(), UR, buff=0.15)
        
        self.play(FadeIn(panel_msg2), run_time=1)
        self.wait(2)
        
        # Apply transformation with emphasis
        self.play(
            Transform(rand_init, rand_target),
            Transform(rand_label, rand_label_target),
            Transform(v1_init, v1_target),
            Transform(v1_label, v1_label_target),
            Transform(v2_init, v2_target),
            Transform(v2_label, v2_label_target),
            run_time=4
        )
        self.wait(3)
        
        # Highlight the scaling results
        box_v1 = SurroundingRectangle(v1_label, color=COLOR_EIG1, buff=0.15)
        box_v2 = SurroundingRectangle(v2_label, color=COLOR_EIG2, buff=0.15)
        self.play(Create(box_v1), Create(box_v2), run_time=1.5)
        
        # Ample timing for narration explaining λ=3 stretch and λ=1 preservation
        self.wait(12)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.5)
        self.wait(1)


# ==============================================================================
# Scene 4: Worked Example Scene
# ==============================================================================

class WorkedExampleScene(Scene):
    """
    Step-by-step algebraic solution of:
    1. Characteristic equation: det(A - λI) = 0
    2. Solving for eigenvalues: λ₁ = 3, λ₂ = 1
    3. Finding eigenvector for λ = 3: (A - 3I)v = 0 -> v₁ = [1, 1]ᵀ
    4. Finding eigenvector for λ = 1: (A - 1I)v = 0 -> v₂ = [1, -1]ᵀ
    5. Numerical verification: Av = λv
    """
    def construct(self):
        title = Text("Worked Example: Finding Eigenvalues & Eigenvectors", font_size=32, color=WHITE, weight=BOLD)
        title.to_edge(UP, buff=0.4)
        self.play(FadeIn(title), run_time=1)
        self.wait(1)
        
        # Step 1: Characteristic equation setup
        step1_title = Text("Step 1: Solve the Characteristic Equation  det(A - λI) = 0", font_size=22, color=YELLOW, weight=BOLD)
        step1_title.next_to(title, DOWN, buff=0.45).to_edge(LEFT, buff=1.0)
        
        step1_line1 = Text("det([ [ 2-λ,  1   ], [  1,   2-λ ] ]) = 0", font_size=20, color=WHITE)
        step1_line2 = Text("(2 - λ)(2 - λ) - (1)(1) = 0", font_size=20, color=COLOR_TEXT_MUTED)
        step1_line3 = Text("(2 - λ)² - 1 = 0   =>   λ² - 4λ + 3 = 0", font_size=20, color=COLOR_TEXT_MUTED)
        step1_line4 = Text("(λ - 3)(λ - 1) = 0", font_size=22, color=WHITE, weight=BOLD)
        step1_result = Text("=>  Eigenvalues:   λ₁ = 3,   λ₂ = 1", font_size=24, color=YELLOW, weight=BOLD)
        
        step1_group = VGroup(step1_title, step1_line1, step1_line2, step1_line3, step1_line4, step1_result)
        step1_group.arrange(DOWN, buff=0.25, aligned_edge=LEFT).next_to(title, DOWN, buff=0.4).to_edge(LEFT, buff=1.0)
        
        self.play(FadeIn(step1_title), run_time=1)
        self.wait(1.5)
        for line in [step1_line1, step1_line2, step1_line3, step1_line4]:
            self.play(FadeIn(line, shift=RIGHT * 0.3), run_time=1.2)
            self.wait(1.2)
            
        self.play(Write(step1_result), run_time=1.5)
        box_res = SurroundingRectangle(step1_result, color=YELLOW, buff=0.15)
        self.play(Create(box_res), run_time=1)
        self.wait(4)
        
        # Transition to Step 2: Finding eigenvectors
        self.play(FadeOut(step1_group), FadeOut(box_res), run_time=1)
        
        # Step 2: Eigenvector for λ = 3
        sec_title = Text("Step 2: Solve (A - λI)v = 0 for Each Eigenvalue", font_size=22, color=YELLOW, weight=BOLD)
        sec_title.next_to(title, DOWN, buff=0.35).to_edge(LEFT, buff=1.0)
        self.play(FadeIn(sec_title), run_time=1)
        
        # Column for λ = 3
        col1_title = Text("For λ₁ = 3:", font_size=22, color=COLOR_EIG1, weight=BOLD)
        col1_eq1 = Text("(A - 3I)v = 0", font_size=18, color=WHITE)
        col1_eq2 = Text("[ [ -1,  1 ], [  1, -1 ] ] [ x, y ]ᵀ = [ 0, 0 ]ᵀ", font_size=18, color=COLOR_TEXT_MUTED)
        col1_eq3 = Text("-x + y = 0   =>   y = x", font_size=18, color=WHITE)
        col1_res = Text("v₁ = [ 1, 1 ]ᵀ  (Yellow)", font_size=20, color=COLOR_EIG1, weight=BOLD)
        col1_box = SurroundingRectangle(col1_res, color=COLOR_EIG1, buff=0.12)
        
        col1_group = VGroup(col1_title, col1_eq1, col1_eq2, col1_eq3, col1_res)
        col1_group.arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        col1_full = VGroup(col1_group, col1_box).shift(LEFT * 3.2 + DOWN * 0.2)
        
        # Column for λ = 1
        col2_title = Text("For λ₂ = 1:", font_size=22, color=COLOR_EIG2, weight=BOLD)
        col2_eq1 = Text("(A - 1I)v = 0", font_size=18, color=WHITE)
        col2_eq2 = Text("[ [  1,  1 ], [  1,  1 ] ] [ x, y ]ᵀ = [ 0, 0 ]ᵀ", font_size=18, color=COLOR_TEXT_MUTED)
        col2_eq3 = Text("x + y = 0   =>   y = -x", font_size=18, color=WHITE)
        col2_res = Text("v₂ = [ 1, -1 ]ᵀ  (Blue)", font_size=20, color=COLOR_EIG2, weight=BOLD)
        col2_box = SurroundingRectangle(col2_res, color=COLOR_EIG2, buff=0.12)
        
        col2_group = VGroup(col2_title, col2_eq1, col2_eq2, col2_eq3, col2_res)
        col2_group.arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        col2_full = VGroup(col2_group, col2_box).shift(RIGHT * 3.2 + DOWN * 0.2)
        
        self.play(FadeIn(col1_full, shift=RIGHT * 0.4), run_time=2)
        self.wait(3)
        self.play(FadeIn(col2_full, shift=LEFT * 0.4), run_time=2)
        self.wait(4)
        
        # Step 3: Numerical Check
        check_title = Text("Numerical Verification: Av = λv", font_size=22, color=GREEN, weight=BOLD)
        check_v1 = Text("A v₁ = [[2,1],[1,2]] [1, 1]ᵀ = [3, 3]ᵀ = 3 v₁  ✓", font_size=18, color=WHITE)
        check_v2 = Text("A v₂ = [[2,1],[1,2]] [1,-1]ᵀ = [1,-1]ᵀ = 1 v₂  ✓", font_size=18, color=WHITE)
        check_group = VGroup(check_title, check_v1, check_v2).arrange(DOWN, buff=0.2).to_edge(DOWN, buff=0.5)
        check_bg = SurroundingRectangle(check_group, color=GREEN, buff=0.25, fill_color="#102015", fill_opacity=0.85)
        
        self.play(FadeIn(check_bg), FadeIn(check_group), run_time=2)
        # Ample timing gap for student verbal walkthrough of arithmetic
        self.wait(14)
        
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.5)
        self.wait(1)


# ==============================================================================
# Scene 5: Interpretation Scene
# ==============================================================================

class InterpretationScene(Scene):
    """
    Connects the numerical algebra back to visual geometry:
    - Eigenvector 1 scaled by 3 along (1, 1)
    - Eigenvector 2 unchanged along (1, -1)
    - Basis vectors î and ĵ mapped to matrix columns
    - Determinant as area scaling factor: det(A) = 3 = λ₁ × λ₂.
    """
    def construct(self):
        title = Text("Geometric Interpretation: Eigenbasis & Area Scaling", font_size=28, color=WHITE, weight=BOLD)
        title.to_edge(UP, buff=0.4)
        self.play(FadeIn(title), run_time=1)
        
        plane = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            x_length=8.0,
            y_length=6.0,
            background_line_style={"stroke_color": GREY_D, "stroke_width": 1, "stroke_opacity": 0.4},
            axis_config={"color": GREY_B, "stroke_width": 2}
        ).shift(RIGHT * 1.5 + DOWN * 0.2)
        
        # Basis vectors
        i_vec = Arrow(plane.c2p(0, 0), plane.c2p(1, 0), buff=0, color=COLOR_IHAT, stroke_width=4)
        i_lbl = Text("î", font_size=18, color=COLOR_IHAT, weight=BOLD).next_to(i_vec, DOWN, buff=0.1)
        
        j_vec = Arrow(plane.c2p(0, 0), plane.c2p(0, 1), buff=0, color=COLOR_JHAT, stroke_width=4)
        j_lbl = Text("ĵ", font_size=18, color=COLOR_JHAT, weight=BOLD).next_to(j_vec, LEFT, buff=0.1)
        
        # Unit square on basis vectors
        unit_sq = Polygon(
            plane.c2p(0, 0), plane.c2p(1, 0), plane.c2p(1, 1), plane.c2p(0, 1),
            color=GREEN_A, fill_color=GREEN_E, fill_opacity=0.35, stroke_width=2
        )
        unit_sq_lbl = Text("Initial Area = 1", font_size=14, color=WHITE).move_to(plane.c2p(0.5, 0.5))
        
        # Eigenvectors
        v1 = Arrow(plane.c2p(0, 0), plane.c2p(1, 1), buff=0, color=COLOR_EIG1, stroke_width=5)
        v1_lbl = Text("v₁ (λ=3)", font_size=18, color=COLOR_EIG1, weight=BOLD).next_to(v1.get_end(), UL, buff=0.1)
        
        v2 = Arrow(plane.c2p(0, 0), plane.c2p(1, -1), buff=0, color=COLOR_EIG2, stroke_width=5)
        v2_lbl = Text("v₂ (λ=1)", font_size=18, color=COLOR_EIG2, weight=BOLD).next_to(v2.get_end(), UR, buff=0.1)
        
        # Left side panel explaining area and determinant
        left_panel = RoundedRectangle(corner_radius=0.2, height=5.5, width=4.5, color=GREY_C, fill_color="#14181d", fill_opacity=0.9)
        left_panel.to_corner(UL, buff=0.4).shift(DOWN * 0.4)
        
        t1 = Text("Area Scaling Factor", font_size=20, color=YELLOW, weight=BOLD).next_to(left_panel.get_top(), DOWN, buff=0.3)
        t2 = Text("det(A) = (2)(2) - (1)(1) = 3", font_size=18, color=WHITE).next_to(t1, DOWN, buff=0.35)
        t3 = Text("det(A) = λ₁ × λ₂ = 3 × 1 = 3", font_size=18, color=GREEN, weight=BOLD).next_to(t2, DOWN, buff=0.3)
        t4 = Text("• Any region's area is scaled\n  by exactly det(A) = 3.", font_size=15, color=WHITE, line_spacing=1.2).next_to(t3, DOWN, buff=0.4).align_to(left_panel, LEFT).shift(RIGHT * 0.3)
        t5 = Text("• Eigenvectors decouple the\n  2D stretch into independent\n  1D scaling axes!", font_size=15, color=COLOR_TEXT_MUTED, line_spacing=1.2).next_to(t4, DOWN, buff=0.3).align_to(t4, LEFT)
        
        panel_content = VGroup(t1, t2, t3, t4, t5)
        
        self.play(FadeIn(plane), FadeIn(left_panel), FadeIn(panel_content), run_time=2)
        self.play(GrowArrow(i_vec), FadeIn(i_lbl), GrowArrow(j_vec), FadeIn(j_lbl), Create(unit_sq), FadeIn(unit_sq_lbl), run_time=2)
        self.play(GrowArrow(v1), FadeIn(v1_lbl), GrowArrow(v2), FadeIn(v2_lbl), run_time=2)
        self.wait(3)
        
        # Transform unit square into parallelogram
        # [0, 0] -> [0, 0]
        # [1, 0] -> [2, 1]
        # [0, 1] -> [1, 2]
        # [1, 1] -> [3, 3]
        trans_parallelogram = Polygon(
            plane.c2p(0, 0), plane.c2p(2, 1), plane.c2p(3, 3), plane.c2p(1, 2),
            color=YELLOW_A, fill_color=YELLOW_E, fill_opacity=0.35, stroke_width=2.5
        )
        trans_area_lbl = Text("Transformed Area = 3", font_size=16, color=WHITE, weight=BOLD).move_to(plane.c2p(1.5, 1.5))
        
        i_trans = Arrow(plane.c2p(0, 0), plane.c2p(2, 1), buff=0, color=COLOR_IHAT, stroke_width=4)
        j_trans = Arrow(plane.c2p(0, 0), plane.c2p(1, 2), buff=0, color=COLOR_JHAT, stroke_width=4)
        v1_trans = Arrow(plane.c2p(0, 0), plane.c2p(3, 3), buff=0, color=COLOR_EIG1, stroke_width=6)
        
        self.play(
            Transform(unit_sq, trans_parallelogram),
            Transform(unit_sq_lbl, trans_area_lbl),
            Transform(i_vec, i_trans),
            Transform(j_vec, j_trans),
            Transform(v1, v1_trans),
            run_time=3.5
        )
        self.wait(3)
        
        highlight_box = SurroundingRectangle(t3, color=GREEN, buff=0.15)
        self.play(Create(highlight_box), run_time=1)
        
        # Narration timing gap for visual connection
        self.wait(12)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.5)
        self.wait(1)


# ==============================================================================
# Scene 6: Summary & Credits Scene
# ==============================================================================

class SummaryScene(Scene):
    """
    Recaps the 3 core takeaways, presents references and credit placeholders,
    and displays the mandatory AI disclosure statement.
    """
    def construct(self):
        title = Text("Summary: Core Takeaways", font_size=36, color=WHITE, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=1)
        self.wait(1)
        
        # 3 Core takeaways
        point1 = Text("1. Invariant Directions: Eigenvectors v stay along their span line under matrix A.", font_size=18, color=WHITE)
        point2 = Text("2. Scaling Factors: Eigenvalues λ stretch each eigenvector (solve det(A - λI) = 0).", font_size=18, color=WHITE)
        point3 = Text("3. Matrix Insight: det(A) = λ₁ × λ₂ gives the geometric area scaling factor of the map.", font_size=18, color=WHITE)
        
        bullets = VGroup(point1, point2, point3).arrange(DOWN, buff=0.35, aligned_edge=LEFT).shift(UP * 0.8)
        
        for pt in bullets:
            self.play(FadeIn(pt, shift=RIGHT * 0.4), run_time=1.5)
            self.wait(1.5)
            
        self.wait(2)
        
        # References & Credits Box
        credits_title = Text("References & Credits", font_size=20, color=YELLOW, weight=BOLD)
        ref1 = Text("• 3Blue1Brown: Essence of Linear Algebra (Chapter 14: Eigenvalues & Eigenvectors)", font_size=16, color=COLOR_TEXT_MUTED)
        ref2 = Text("• Gilbert Strang: Introduction to Linear Algebra (5th Edition)", font_size=16, color=COLOR_TEXT_MUTED)
        music_credit = Text("• Music Credit: [Royalty-Free Audio Track / Incompetech - Kevin MacLeod]", font_size=16, color=COLOR_TEXT_MUTED)
        
        cred_group = VGroup(credits_title, ref1, ref2, music_credit).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        cred_box = SurroundingRectangle(cred_group, color=GREY_C, buff=0.25, fill_color="#12161b", fill_opacity=0.85)
        cred_full = VGroup(cred_box, cred_group).shift(DOWN * 1.0)
        
        self.play(FadeIn(cred_full, shift=UP * 0.3), run_time=1.5)
        self.wait(2)
        
        # Mandatory AI disclosure statement
        ai_disclosure = Text(
            "AI tools (Antigravity / Gemini) were used to help generate the Manim code. I reviewed and tested it.",
            font_size=17,
            color="#FFCC00",
            weight=BOLD
        ).to_edge(DOWN, buff=0.5)
        
        self.play(FadeIn(ai_disclosure, shift=UP * 0.2), run_time=1.5)
        # Ample timing gap for closing narration and reading credits
        self.wait(14)
        
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.5)
        self.wait(1)


# ==============================================================================
# Scene 7: Closing Frame Scene
# ==============================================================================

class ClosingScene(Scene):
    """
    Simple closing frame.
    """
    def construct(self):
        thank_you = Text("Thank You for Watching!", font_size=52, color=WHITE, weight=BOLD)
        subtext = Text("Master Linear Algebra One Direction at a Time.", font_size=26, color="#58C4DD")
        
        closing_group = VGroup(thank_you, subtext).arrange(DOWN, buff=0.4).center()
        
        self.play(FadeIn(thank_you, scale=0.9), run_time=2)
        self.play(FadeIn(subtext, shift=UP * 0.3), run_time=1.5)
        self.wait(8)
        self.play(FadeOut(closing_group, shift=DOWN * 0.4), run_time=1.5)
        self.wait(1)
