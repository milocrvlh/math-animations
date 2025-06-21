from manim import *

config.disable_caching = True  # Desativa arquivos temporários

class ComutatividadeAdicao(Scene):
    def construct(self):

        # Mostra o texto
        text = Tex("Propriedade Comutativa da Adição")
        self.play(FadeIn(text))
        self.wait(1)
        self.play(FadeOut(text))
        self.wait(1)
        
        # Faz Comutações de Inteiros
        eq1 = MathTex("3","+", "4","=","7")
        eq2 = MathTex("4","+", "3","=","7")
        self.play(Write(eq1))
        self.play(TransformMatchingShapes(eq1, eq2, path_arc=PI/2))
        self.wait(1)
        self.play(TransformMatchingShapes(eq2, eq1, path_arc=PI/2))
        self.wait(1)
        self.play(TransformMatchingShapes(eq1, eq2, path_arc=PI/2))
        self.wait(1)
        self.play(TransformMatchingShapes(eq2, eq1, path_arc=PI/2))
        self.wait(1)


        # Substitui as Variaveis
        variaveis1 =  VGroup(MathTex("a"), MathTex("b"), MathTex("c")).arrange_submobjects().shift(UP)

        eq3 = MathTex("a","+", "b","=","c")
        eq4 = MathTex("b","+", "a","=","c")
        self.play(TransformMatchingTex(Group(eq1, variaveis1), eq3))

        # Faz comutações das variáveis
        self.play(TransformMatchingShapes(eq3, eq4, path_arc=PI/2))
        self.wait(1)
        self.play(TransformMatchingShapes(eq4, eq3, path_arc=PI/2))
        self.wait(1)
        self.play(TransformMatchingShapes(eq3, eq4, path_arc=PI/2))
        self.wait(1)
        self.play(TransformMatchingShapes(eq4, eq3, path_arc=PI/2))
        self.wait(1)

        # Mostra a forma final da propriedade
        variaveis2 =  VGroup(MathTex("b"), MathTex("+"), MathTex("a")).arrange_submobjects().shift(UP)
        eq5 = MathTex("a","+", "b","=","b","+","a")
        self.play(TransformMatchingTex(Group(eq3,variaveis2), eq5))
        self.wait(3)
        
class AssociatividadeAdicao(Scene):
    def construct(self):
        
        # Mostra o texto
        text = Tex("Propriedade Associativa da Adição")
        self.play(FadeIn(text))
        self.wait(1)
        self.play(FadeOut(text))
        self.wait(1)

        # Exemplo superior
        eqiup = MathTex("(", "a", "+", "b", ")" "+", "c").shift(1.5 * UP)
        variaveisup = VGroup(MathTex("2"), MathTex("5"), MathTex("3")).arrange_submobjects().shift(2.5 * UP)


        eq1up = MathTex("(","2","+", "5",")", "+","3").shift(1.5 * UP)
        eq2up = MathTex("=","7","+","3").shift(1.5 * UP)
        eq3up = MathTex("=","10").shift(1.5 * UP)

        # Exemplo inferior
        eqidown =  MathTex( "a", "+", "(", "b", "+", "c",")" ).shift(1.5 * DOWN)
        variaveisdown = VGroup(MathTex("2"), MathTex("5"), MathTex("3")).arrange_submobjects().shift(0.5 * DOWN)

        eq1down = MathTex("2", "+", "(", "5", "+","3", ")").shift(1.5 * DOWN)
        eq2down = MathTex("=","2","+","8").shift(1.5 * DOWN)
        eq3down = MathTex("=","10").shift(1.5 * DOWN)


        # Animações Simultâneas de ambos os lados da Propriedade
        self.play(Write(eqiup), Write(eqidown))
        self.wait(6)
        self.play(TransformMatchingTex(Group(eqiup, variaveisup), eq1up), TransformMatchingTex(Group(eqidown, variaveisdown), eq1down))
        self.wait(6)
        self.play(Transform(eq1up, eq2up), Transform(eq1down, eq2down))
        self.wait(6)
        self.play(Transform(eq1up, eq3up), Transform(eq1down, eq3down))
        self.wait(6)
        self.play(FadeOut(eq1up), FadeOut(eq1down))
        
        # Conclusão da Propriedade
        eqf =  MathTex("(", "a", "+", "b", ")" "+", "c", "=", "a", "+", "(", "b", "+", "c",")" )
        self.play(Write(eqf))
        self.wait(6)

class NeutroAdicao(Scene):
    def construct(self):
        
        # Mostra o texto
        text = Tex("Propriedade da Existência do Elemento Neutro da Adição")
        self.play(FadeIn(text))
        self.wait(2)
        self.play(FadeOut(text))
        self.wait(1)
        
        
        # Mostra Exemplos de somas com o neutro
        eq1 = MathTex("3", "+", "0", "=", "3")
        eq2 = MathTex("7", "+", "0", "=", "7")
        eq3 = MathTex("95", "+", "0", "=", "95")
        eq4 = MathTex("10", "+", "0", "=", "10")
        
        self.play(Write(eq1))
        self.wait(2)
        self.play(Transform(eq1, eq2))
        self.wait(2)
        self.play(Transform(eq1, eq3))
        self.wait(2)
        self.play(Transform(eq1, eq4))
        self.wait(2)

        # Substitui o número por uma variável
        variaveis = MathTex("a").shift(UP)
        eq5 = MathTex("a", "+", "0", "=", "a")
        self.play(TransformMatchingTex(Group(variaveis, eq1), eq5))
        self.wait(3)

class OpostoAdicao(Scene):
    def construct(self):
        # Mostra o texto
        text = Tex("Propriedade da Existência do Oposto da Adição")
        self.play(FadeIn(text))
        self.wait(2)
        self.play(FadeOut(text))
        self.wait(1)
        
        
        # Mostra Exemplos de somas com o neutro
        eq1 = MathTex("5", "+", "(","-", "5", ")")
        eq2 = MathTex("20", "+", "(","-", "20", ")")
        eq3 = MathTex("92", "+", "(","-", "92", ")")
        zero =MathTex("=", "0")
        
        self.play(Write(eq1[0]))
        self.wait(1)
        self.play(Transform(eq1[0], eq1[0:6]))
        self.wait(1)
        self.play(Transform(eq1[0], zero))
        self.wait(1)
        self.play(Unwrite(eq1[0]))

        self.wait(1)
        self.play(Write(eq2[0]))
        self.wait(1)
        self.play(Transform(eq2[0], eq2[0:6]))
        self.wait(1)
        self.play(Transform(eq2[0], zero))
        self.wait(1)
        self.play(Unwrite(eq2[0]))

        self.wait(1)
        self.play(Write(eq3[0]))
        self.wait(1)
        self.play(Transform(eq3[0], eq3[0:6]))
        self.wait(1)
        self.play(Transform(eq3[0], zero))
        self.wait(1)
        self.play(Unwrite(eq3[0]))
        self.wait(1)



        # Substitui o número por uma variável
        eq5 = MathTex("a", "+", "(","-", "a", ")" "=", "0")
        self.play(Write(eq5))
        self.wait(5)





        
        

        
        
        

       