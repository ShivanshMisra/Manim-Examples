from manimlib.imports import *


class ScrollScene(Scene):
    CONFIG={
        "camera_config":{"background_color":WHITE}
    }
    def construct(self) :
        Rg = TextMobject("A new number $ \\kappa $")
        e1 = TextMobject("Let $\\displaystyle \\kappa = {1 \\over 0}$")
        Text = TextMobject("You might say that $ \\kappa $ is undefined \\\\ but who is to stop us from defining it.")
        Rg2 = TextMobject("Arithmetic with $ \\kappa $")
        eq1 = TexMobject(r"\kappa + n = \kappa \, \, \text{for} \, \,  n \in \mathds{R}")
        eq2 = TexMobject(r"\kappa \cdot n = \kappa")
        eq3 = TexMobject(r"\kappa^{n} = \kappa")
        Rg3 = TextMobject("If you think about it then you will \\\\ find a weird association between 0, $ \\kappa $ , $ \\infty $")
        eq4= TexMobject(r"\kappa + n = \kappa \longleftrightarrow 0 + n = 0 \longleftrightarrow \infty + n = \infty")
        eq5= TexMobject(r"\kappa \cdot n = \kappa \longleftrightarrow 0 \cdot n = 0 \longleftrightarrow \infty \cdot n = \infty")
        eq6 = TexMobject(r"\kappa^{n} = \kappa \longleftrightarrow 0^{n} = 0 \longleftrightarrow \infty^{n} = \infty")
        Rg4 = TextMobject("This association between 0,$ \\kappa $,$ \\infty $. \\\\ Prompts a understanding that $ \\kappa $ must be equal to $ \\infty $ or 0 \\\\ And this is a true fact that $ \\kappa $ is equal to 0 or $\\infty$ \\\\ and no other finite or infinite quantity.")
        Rg5 = TextMobject("This whole $\\kappa$-thing is a compact way to understand \\\\ the fact that ${1 \\over 0} = 0 \\lor {1 \\over 0} = \\infty $ and no other number")
        Rg.set_color(BLACK)
        e1.set_color(RED)
        Text.set_color(BLACK)
        Rg2.set_color(BLACK)
        Rg3.set_color(BLACK)
        Rg4.set_color_by_gradient(RED , YELLOW)
        Rg5.set_color_by_gradient(YELLOW , RED)
        Rg4.scale(.75)
        Rg5.scale(.75)
        eq1.set_color(BLACK)
        eq2.set_color(BLACK)
        eq3.set_color(BLACK)
        eq1.move_to(UP)
        eq3.move_to(DOWN)
        eq4.set_color(BLACK)
        eq5.set_color(BLACK)
        eq6.set_color(BLACK)
        eq5.move_to(DOWN)
        eq6.move_to(DOWN*2)
        self.play(Write(Rg))
        self.wait()
        self.play(Rg.move_to, 2*UP)
        self.wait()
        self.play(Write(e1))
        self.wait(.5)
        self.play(e1.move_to, UP)
        self.play(
            ReplacementTransform(e1 , Text)
            )
        self.wait(2)
        self.play(FadeOut(Text))
        self.wait()
        self.play(
            ReplacementTransform(Rg , Rg2)
            )
        self.wait()
        self.play(Rg2.move_to, 2*UP)
        self.wait()
        self.play(
            FadeInFromDown(eq1),
            Write(eq2),
            ShowCreation(eq3)
            )
        self.wait(3)
        self.play(
            FadeOut(eq1),
            FadeOut(eq2),
            FadeOut(eq3),
            )
        self.wait()
        self.play(
            ReplacementTransform(Rg2 , Rg3)
            )
        self.wait()
        self.play(Rg3.move_to, 2*UP)
        self.wait()
        self.play(
            FadeInFromDown(eq4),
            Write(eq5),
            ShowCreation(eq6)
            )
        self.wait(3)
        self.play(
            FadeOut(eq4),
            FadeOut(eq5),
            FadeOut(eq6),
            FadeOut(Rg3)
            )
        self.wait()
        self.play(Write(Rg4))
        self.wait(3)
        self.play(
            ReplacementTransform(Rg4, Rg5)
            )
        self.wait()
