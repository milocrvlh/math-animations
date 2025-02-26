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
        title = Tex("Definição Alternativa da Derivada", font_size=32).to_edge(UP)
        formula = MathTex(
            r"f'(a) = \lim_{x \to a} \frac{f(x) - f(a)}{x - a}",
            font_size=28
        ).next_to(title, DOWN)

        # Ponto fixo (a, f(a))
        dot_a = Dot(axes.c2p(a, func(a)), color=YELLOW)
        label_a = MathTex(r"(a, f(a))", font_size=24).next_to(dot_a, UP)

        # Ponto móvel (x, f(x)) e reta secante
        x_tracker = ValueTracker(2.0) 
        dot_x = always_redraw(
            lambda: Dot(
                axes.c2p(x_tracker.get_value(), func(x_tracker.get_value())),
                color=RED
            )
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
        self.play(FadeIn(dot_x), Create(secant_line))
        self.wait(1)
        
        # Animação de x → a
        self.play(
            x_tracker.animate.set_value(a + 0.01),  # x aproxima-se de a
            run_time=5,
            rate_func=linear
        )
        self.wait(2)
        
        # Animação final (reta tangente)
        self.play(Create(tangent_line))
        self.wait(2)