from manim import *

config.disable_caching = True  # Desativa arquivos temporários

class LimitDefinition(Scene):
    def construct(self):
        # Configuração inicial
        axes = Axes(
            x_range=[-1, 3], # Domínio de x
            y_range=[-1, 10], # Contradomínio
            axis_config={"color": BLUE} # cor dos eixos
        )
        func = lambda x: x**2  # Função exemplo: f(x) = x²
        graph = axes.plot(func, color=GREEN) # Plota a função nos eixos

        a = 1.0  # Ponto onde calculamos a derivada

        # Derivada e reta tangente
        derivada = 2 * a  # f'(a) para f(x) = x²
        
        # Equação da reta tangente: y = f(a) + f'(a)(x - a)
        tangent_line = axes.plot(
            lambda x: func(a) + derivada * (x - a),
            color=YELLOW
        )

        # Título e fórmula
        title = Tex("Definição da Derivada", font_size=32).to_edge(UP)
        formula = MathTex(
            r"f'(a) = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h}",
            font_size=28
        ).next_to(title, DOWN) # Posiciona a fórmula abaixo do título

        # Ponto fixo (a, f(a))
        dot_a = Dot(axes.c2p(a, func(a)), color=YELLOW) # cria um ponto no gráfico, posicionado nas coordenadas (a, f(a))
        label_a = MathTex(r"(a, f(a))", font_size=24).next_to(dot_a, UP) # Coloca a notação acima do ponto

        # Ponto móvel (a+h, f(a+h)) e reta secante
        h = ValueTracker(1)  # Valor inicial de h
        dot_h = always_redraw(
            lambda: Dot(
                axes.c2p(a + h.get_value(), func(a + h.get_value())),
                color=RED
            )
        )
        secant_line = always_redraw(
            lambda: axes.get_secant_slope_group(
                x=a,
                graph=graph,
                dx=h.get_value(),
                dx_label=r"h",
                dy_label=r"f(a+h)-f(a)",
                secant_line_color=MAROON
            )
        )

        # Passo 1: Mostrar eixos, gráfico e título
        self.play(Create(axes), Create(graph), Write(title))
        self.wait(1)

        # Passo 2: Mostrar fórmula da derivada
        self.play(Write(formula))
        self.wait(1)

        # Passo 3: Introduzir ponto (a, f(a))
        self.play(FadeIn(dot_a), Write(label_a))
        self.wait(1)

        # Passo 4: Mostrar ponto móvel e reta secante
        self.play(FadeIn(dot_h), Create(secant_line))
        self.wait(1)
        
        # Animação de h → 0
        self.play(
            h.animate.set_value(0.01),  # h diminui até quase zero
            run_time=5,  # Duração de 5 segundos
            rate_func=linear  # Velocidade constante
        )
        self.wait(2)
        
        # Animação final
        self.play(Create(tangent_line))
        self.wait(2)


class AltLimitDefinition(Scene):
    def construct(self):
        # Configuração inicial
        axes = Axes(
            x_range=[0, 3],  # Ajuste para focar em x próximo de a
            y_range=[-1, 10],
            axis_config={"color": BLUE}
        )
        func = lambda x: x**3
        graph = axes.plot(func, color=GREEN)
        a = 1.0

        # Derivada e reta tangente
        derivada = 3 * a ** 2
        tangent_line = axes.plot(
            lambda x: func(a) + derivada * (x - a),
            color=YELLOW
        )

        # Título e fórmula
        title = Tex("Definição (Alternativa) da Derivada", font_size=32).to_edge(UP)
        formula = MathTex(
            r"f'(a) = \lim_{x \to a} \frac{f(x) - f(a)}{x - a}",
            font_size=28
        ).next_to(title, DOWN)

        # Ponto fixo (a, f(a))
        dot_a = Dot(axes.c2p(a, func(a)), color=YELLOW)
        label_a = MathTex(r"(a, f(a))", font_size=24).next_to(dot_a, LEFT)

        # Ponto móvel (x, f(x))
        x_tracker = ValueTracker(2.0) 
        dot_x = always_redraw(
            lambda: Dot(
                axes.c2p(x_tracker.get_value(), func(x_tracker.get_value())),
                color=RED
            )
        )
        label_x = always_redraw(
            lambda: MathTex(r"(x, f(x))", font_size=24).next_to(dot_x, LEFT)
        )

        # Reta secante entre (a, f(a)) e (x, f(x))
        secant_line = always_redraw(
            lambda: axes.get_secant_slope_group(
                x=a,
                graph=graph,
                dx=x_tracker.get_value() - a,  # dx = x - a
                dx_label=r"x - a",
                dy_label=r"f(x) - f(a)",
                secant_line_color=MAROON,
            )
        )

        # Passo 1: Mostrar eixos, gráfico e título
        self.play(Create(axes), Create(graph), Write(title))
        self.wait(1)

        # Passo 2: Mostrar fórmula da derivada
        self.play(Write(formula))
        self.wait(1)

        # Passo 3: Introduzir ponto (a, f(a))
        self.play(FadeIn(dot_a), Write(label_a))
        self.wait(1)

        # Passo 4: Mostrar ponto móvel e reta secante
        self.play(FadeIn(dot_x), Write(label_x), Create(secant_line))
        self.wait(1)
        
        # Animação de x → a
        self.play(
            x_tracker.animate.set_value(a + 0.01),  # x aproxima-se de a
            run_time=5,
            rate_func=linear
        )
        self.play(FadeOut(label_x), run_time=0.07)
        self.wait(2)
        
        # Animação final (reta tangente)
        self.play(Create(tangent_line))
        self.wait(2)

class RegraConstante(Scene):
    def construct(self):

        # Equação 1: Derivada
        eq1 = MathTex( r"f'(a)=  \lim_{h \to 0}  \frac{f(a+h)-f(a)}{h}")
        eq1.center()

        texto1 = Tex("Pela definição,")
        texto1.next_to(eq1, UP).shift(LEFT * 3)

        # Equação 2: Definição de f(a) = c
        eq2 = MathTex(
            r"\text{Seja}\quad f(a) = c\implies f(a+h) = c",
            )
        eq2.to_edge(UP)  # Posiciona no canto superior

        texto2 = Tex(", temos:")    
        texto2.next_to(eq2, RIGHT)

        eq3 = MathTex(r"f'(a)=\lim_{h \to 0}\frac{c-c}{h}")
        eq4 = MathTex(r"f'(a)=\lim_{h \to 0} 0")
        eq5 = MathTex(r"f'(a)=0")

        # self.add(index_labels(eq1[0]))    # index the first (and only) term of the MathTex mob

        # Animações 
        self.play(Write(texto1))
        self.play(Write(eq1))
        self.wait(1)
        self.play(Write(eq2))
        self.wait(2)
        self.play(Write(texto2))

class FuncaoReciproca(Scene):
    def construct(self):

        # Definição
        texto1 = Tex("Pela definição,")
        eq1 = MathTex("g'(a)", "=", r"\lim_{h \to 0}", r"\frac{g(a+h)-g(a)}{h}")

        # Suposição
        eq2 = MathTex(
            r"\text{Suponha: }", "g(a)", "=", r"\frac{1}{f(a)}", r"\quad", r"\text{e}", r"\quad", "g(a+h)", "=", r"\frac{1}{f(a+h)}"
            ).to_edge(UP)

        eq3 = MathTex("g'(a)", "=", r"\lim_{h \to 0}", r"\frac{\frac{1}{f(a+h)}-\frac{1}{f(a)}}{h}")
        eq4 = MathTex("g'(a)", "=", r"\lim_{h \to 0}", r"\frac{ \frac{f(a)-f(a+h)}{f(a+h)f(a)} }{h}")
        eq5 = MathTex("g'(a)", "=", r"\lim_{h \to 0}", r"\frac{- \frac{f(a+h)-f(a)}{f(a+h)f(a)} }{h}")



        self.play(FadeIn(texto1))
        self.play(FadeOut(texto1))
        self.play(Write(eq1))
        self.wait(1)
        self.play(Write(eq2))

        self.play(TransformMatchingTex(eq1, eq3), FadeOut(eq2))
        self.wait(2)
        self.play(TransformMatchingTex(eq3, eq4))
        self.wait(1)
        self.play(TransformMatchingTex(eq3, eq4))
        self.wait(1)
