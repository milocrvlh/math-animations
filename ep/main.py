from manim import *

class Definicao(Scene):
    def construct(self):
        # Expressão com chave e "n vezes" (sem acento)
        a_n_e = MathTex(
            r'\underbrace{a \cdot a \cdot a \cdot a \cdots a}_{n \text{ vezes}}',
            font_size=96
        )
        a_n_d = MathTex(r'= a^n', font_size=96)

        # Animação
        self.play(Write(a_n_e))
        self.wait(1)
        self.play(ReplacementTransform(a_n_e, a_n_d))
        self.wait(1.5)


class Propriedade1(Scene):
    def construct(self):
        # Expressões
        eq1 = MathTex(r'a^n \cdot a^m', font_size=96)
        eq2 = MathTex(
            r'\underbrace{=(a \cdot a \cdot a \cdot a \cdots a)}_{n \text{ vezes}} \cdot \underbrace{(a \cdot a \cdot a \cdot a \cdots a)}_{m \text{ vezes}}',
            font_size=75
        )
        eq3 = MathTex(
            r'\underbrace{=a \cdot a \cdot a \cdot a \cdot a \cdot a \cdot a \cdot a \cdot a \cdots a}_{n + m \text{ vezes}}',
            font_size=75
        )
        eq4 = MathTex(r'= a^{n+m}', font_size=96)
        eqf = MathTex(r'\therefore a^n \cdot a^m = a^{n+m}', font_size=96)

        # Animação
        self.play(Write(eq1))  # Mostra a primeira expressão
        self.wait(2)  

        # Transforma a primeira expressão na segunda
        self.play(ReplacementTransform(eq1, eq2))
        self.wait(4)  

        # Transforma a segunda expressão na terceira
        self.play(ReplacementTransform(eq2, eq3))
        self.wait(4)  

        # Transforma a terceira expressão na quarta
        self.play(ReplacementTransform(eq3, eq4))
        self.wait(4)  

        # Mostra a propriedade
        self.play(Transform(eq4, eqf))
        self.wait(4)  

class Propriedade1Consequencia(Scene):
    def construct(self):
        # Expressões
        eq1 = MathTex(r'\text{Se n = 1, então}', font_size=96)
        eq2 = MathTex(
            r'a^1 = a',
            font_size=96
        )
        # Animação
        self.play(Write(eq1))  # Mostra a primeira expressão
        self.wait(2)  

        # Transforma a primeira expressão na segunda
        self.play(ReplacementTransform(eq1, eq2))
        self.wait(2)  

class Propriedade2(Scene):
    def construct(self):
        # Expressões
        eq1 = MathTex(r'\frac{a^n}{a^m}', font_size=96)
        eq2 = MathTex(
            r'=\frac{\overbrace{(a \cdot a \cdot a \cdot a \cdot a \cdots a)}^{n \text{ vezes}}}{ \underbrace{(a \cdot a \cdot a \cdot a \cdots a)}_{m \text{ vezes}}}',
            font_size=75
        )
        eq3 = MathTex(
            r'\underbrace{=a \cdots a}_{n - m \text{ vezes}}',
            font_size=96
        )
        eq4 = MathTex(r'= a^{n-m}', font_size=96)
        eqf = MathTex(r'\therefore \frac{a^n}{a^m} = a^{n-m}', font_size=96)

        # Animação
        self.play(Write(eq1))  # Mostra a primeira expressão
        self.wait(2)  

        # Transforma a primeira expressão na segunda
        self.play(ReplacementTransform(eq1, eq2))
        self.wait(4)  

        # Transforma a segunda expressão na terceira
        self.play(ReplacementTransform(eq2, eq3))
        self.wait(4)  

        # Transforma a terceira expressão na quarta
        self.play(ReplacementTransform(eq3, eq4))
        self.wait(4)  

        # Mostra a propriedade
        self.play(Transform(eq4, eqf))
        self.wait(4)  

class Propriedade2CasoEspecial(Scene):
    def construct(self):
        # Expressões
        eq1 = MathTex(r'1 = \frac{a^n}{a^n}', font_size=96)
        eq2 = MathTex(
            r'=\frac{\overbrace{(a \cdot a \cdot a \cdot a \cdots a)}^{n \text{ vezes}}}{ \underbrace{(a \cdot a \cdot a \cdot a \cdots a)}_{n \text{ vezes}}}',
            font_size=75
        )
        eq3 = MathTex(
            r'\underbrace{=a \cdot a \cdot a \cdot a \cdots a}_{n - n \text{ vezes}}',
            font_size=96
        )

        eq4= MathTex(r'= a^{n-n}', font_size=96)
        eq5= MathTex(r'= a^0', font_size=96)
        
        eqf = MathTex(r'\therefore a^0 = 1', font_size=96)

        # Animação
        self.play(Write(eq1)) 
        self.wait(2)  

        # Transforma a primeira expressão na segunda
        self.play(ReplacementTransform(eq1, eq2))
        self.wait(4)  

        # Transforma a segunda expressão na terceira
        self.play(ReplacementTransform(eq2, eq3))
        self.wait(3)  

        # Transforma a terceira expressão na quarta
        self.play(ReplacementTransform(eq3, eq4))        
        self.wait(0.5)  
 
        # Mostra a propriedade
        self.play(ReplacementTransform(eq4, eq5))
        self.wait(3)  

        # Mostra a propriedade
        self.play(ReplacementTransform(eq5, eqf))
        self.wait(3)

class Propriedade2Corolario(Scene):
    def construct(self):
        # Expressões
        eq1 = MathTex(r'\frac{1}{a^m}', font_size=96)
        eq2 = MathTex(r'=\frac{a^0}{a^m}', font_size=96)
        eq3 = MathTex(r'=a^{0-m}', font_size=96)
        eq4 = MathTex(r'=a^{-m}', font_size=96)
        eqf = MathTex(r'\therefore \frac{1}{a^m} = a^{-m}', font_size=96)

        # Animação
        self.play(Write(eq1))  # Mostra a primeira expressão
        self.wait(2)  

        # Transforma a primeira expressão na segunda
        self.play(ReplacementTransform(eq1, eq2))
        self.wait(4)  

        # Transforma a segunda expressão na terceira
        self.play(ReplacementTransform(eq2, eq3))
        self.wait(1)  

        # Transforma a terceira expressão na quarta
        self.play(TransformMatchingTex(eq3, eq4))
        self.wait(4)  

        # Mostra a propriedade
        self.play(Transform(eq4, eqf))
        self.wait(5)  

class Propriedade3(Scene):
    def construct(self):
        # Expressões
        eq1 = MathTex(r'(a^n)^m', font_size=96)
        eq2 = MathTex(r'=\underbrace{(a \cdot a \cdot a \cdot a \cdot a \cdots a)^m}_{n \text{ vezes}}', font_size=96)
        eq3 = MathTex(r'=\underbrace{(\underbrace{a \cdot a \cdot a \cdot a \cdot a \cdots a)}_{n \text{ vezes}}\cdot\underbrace{(a \cdot a \cdot a \cdot a \cdot a \cdots a)}_{n \text{ vezes}}\cdot\underbrace{(a \cdot a \cdot a \cdot a \cdot a \cdots a)}_{n \text{ vezes}}}_{m \text{ vezes}}', font_size=40)
        eq4 = MathTex(r'=\underbrace{a \cdot a \cdot a \cdot a \cdot a \cdot a\cdot a \cdot a \cdot a \cdot a \cdot a \cdot a \cdot a \cdot a \cdot a \cdot a \cdot a \cdots a}_{m \cdot n \text{ vezes}}', font_size=40)
        eqf = MathTex(r'\therefore(a^n)^m = a^{n \cdot m}', font_size=96)

        # Animação
        self.play(Write(eq1))  # Mostra a primeira expressão
        self.wait(2)  

        # Transforma a primeira expressão na segunda
        self.play(ReplacementTransform(eq1, eq2))
        self.wait(5)  

        # Transforma a segunda expressão na terceira
        self.play(ReplacementTransform(eq2, eq3))
        self.wait(5)  

        # Transforma a terceira expressão na quarta
        self.play(ReplacementTransform(eq3, eq4))
        self.wait(4)  

        # Mostra a propriedade
        self.play(Transform(eq4, eqf))
        self.wait(5)  

class Propriedade4(Scene):
    def construct(self):
        # Expressões
        eq1 = MathTex(r'\left(\frac{a}{b}\right)^n', font_size=96)
        eq2 = MathTex(
            r'= \underbrace{\left(\frac{a}{b}\right) \cdot \left(\frac{a}{b}\right) \cdot \left(\frac{a}{b}\right) \cdots \left(\frac{a}{b}\right)}_{n \text{ vezes}}',
            font_size=96
        )
        eq3 = MathTex(
            r'= \underbrace{\frac{a}{b} \cdot \frac{a}{b} \cdot \frac{a}{b} \cdots \frac{a}{b}}_{n \text{ vezes}}',
            font_size=96
        )
        eq4 = MathTex(
            r'=\frac{\overbrace{a\cdot a\cdot a\cdots a}^{n \text{ vezes}}}{\underbrace{b\cdot b\cdot b \cdots b}_{n \text{ vezes}}}',
            font_size=96
        )
        eq5 = MathTex(r'=\frac{a^n}{b^n}', font_size=96)
        eqf = MathTex(r'\therefore \left(\frac{a}{b}\right)^n = \frac{a^n}{b^n}', font_size=96)

        # Animação
        self.play(Write(eq1))  # Mostra a primeira expressão
        self.wait(2)  

        # Transforma a primeira expressão na segunda
        self.play(ReplacementTransform(eq1, eq2))
        self.wait(4)  

        # Transforma a segunda expressão na terceira
        self.play(ReplacementTransform(eq2, eq3))
        self.wait(4)  

        # Transforma a terceira expressão na quarta
        self.play(ReplacementTransform(eq3, eq4))
        self.wait(4)  

        # Mostra a propriedade
        self.play(ReplacementTransform(eq4, eq5))
        self.wait(4)  
        
        # Mostra a propriedade
        self.play(ReplacementTransform(eq5, eqf))
        self.wait(4)

class Propriedade5(Scene):
    def construct(self):
        # Expressões
        eq1 = MathTex(r'(a\cdot b)^n', font_size=96)
        eq2 = MathTex(
            r'= \underbrace{(a\cdot b) \cdot (a\cdot b) \cdot (a\cdot b) \cdot (a\cdot b) \cdots (a\cdot b) }_{n \text{ vezes}}',
            font_size=60
        )
        eq3 = MathTex(
            r'= \underbrace{a\cdot a \cdot a\cdot a \cdots a}_{n \text{ vezes}}\cdot \underbrace{b \cdot b\cdot b \cdot b\cdots b }_{n \text{ vezes}}',
            font_size=60
        )
        eq4 = MathTex(
            r'=a^n\cdot b^n',
            font_size=96
        )
        eqf = MathTex(r'\therefore (a\cdot b)^n = a^n\cdot b^n', font_size=96)

        # Animação
        self.play(Write(eq1))  # Mostra a primeira expressão
        self.wait(2)  

        # Transforma a primeira expressão na segunda
        self.play(ReplacementTransform(eq1, eq2))
        self.wait(4)  

        # Transforma a segunda expressão na terceira
        self.play(ReplacementTransform(eq2, eq3))
        self.wait(4)  

        # Transforma a terceira expressão na quarta
        self.play(ReplacementTransform(eq3, eq4))
        self.wait(4)  

        # Mostra a propriedade
        self.play(ReplacementTransform(eq4, eqf))
        self.wait(4)  
        