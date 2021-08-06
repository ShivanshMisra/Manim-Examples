class Pointy_Pointer(Scene):
    def construct(self):
        l1 = NumberLine(x_range=[-10,10,1],include_numbers=True,include_tip=False,label_direction=DOWN).move_to(UP)
        l1.scale(0.5)
        l2 = NumberLine(x_range=[-10,10,1],include_numbers=True,include_tip=False,label_direction=DOWN).move_to(2*DOWN)
        l2.scale(0.5)
        tracker=ValueTracker(0)
        Vec1= Triangle(color=WHITE,fill_opacity=0.9).add_updater(lambda m: m.next_to(l1.n2p(tracker.get_value()),UP))
        Vec1.scale(.07)
        Vec1.rotate(60*DEGREES)
        Vec2= Triangle(color=WHITE,fill_opacity=0.9).add_updater(lambda m: m.next_to(l2.n2p((tracker.get_value())**2),UP))
        Vec2.scale(.07)
        Vec2.rotate(60*DEGREES)
        txt1=MathTex("x").add_updater(lambda m: m.next_to(Vec1,UP))
        txt2=MathTex("x^{2}").add_updater(lambda m: m.next_to(Vec2,UP))
        Header=MathTex("f(x)","=","x^{2}").to_edge(UP)
        # f(x)=x^2
        self.play(Write(Header))
        self.wait()
        # number lines
        self.play(Create(l1),Create(l2),run_time=3)
        self.wait()
        # pointer and text
        for element,nect in zip([Vec1,Vec2],[txt1,txt2]):
            self.play(GrowFromCenter(element),Write(nect))
            self.wait()
        # ranging pointer
        for i in (2,3,-2,1,0):
            self.play(tracker.animate.set_value(i))
            self.wait()
