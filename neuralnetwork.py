from manimlib.imports import *

class Forward(Scene):
    def construct(self):
        introduction_text = TextMobject("Let's take as example a neural network with")
        input_layers_text = TextMobject("3 input layers", color=PURPLE)
        input_layers_text.next_to(introduction_text, DOWN)
        and_text = TextMobject("and")
        and_text.next_to(introduction_text, DOWN)
        output_layers_text = TextMobject("2 output layers", color=GREEN)
        output_layers_text.next_to(introduction_text, DOWN)
        text_group = VGroup(introduction_text, input_layers_text)

        forward_text = TextMobject("Forward propagation")
        forward_text.shift(3*UP)

        weights_formula_name = TextMobject("$w$", color=GREEN)
        weights_formula = TextMobject("$=\\begin{bmatrix}w_{11} & w_{12} & w_{13}\\\\w_{21} & w_{22} & w_{23}\end{bmatrix}$")
        weights_formula.next_to(weights_formula_name, RIGHT)
        weights_group = VGroup(weights_formula_name, weights_formula)

        input_formula_name = TextMobject("$a^{(l-1)}$", color=RED)
        input_formula = TextMobject("$=\\begin{bmatrix}a^{(l-1)}_1 & \\ldots \\\\ a^{(l-1)}_2 & \\ldots \\\\ a^{(l-1)}_2 & \\ldots \\\\ \\end{bmatrix}$")
        input_formula.next_to(input_formula_name, RIGHT)
        input_group = VGroup(input_formula, input_formula_name)
        input_group.shift(2*DOWN)

        bias_formula_name = TextMobject("$b$", color=PURPLE)
        bias_formula = TextMobject("$=\\begin{bmatrix} b_{1} & b_{2} \\end{bmatrix}$")
        bias_formula.next_to(bias_formula_name, RIGHT)
        bias_group = VGroup(bias_formula, bias_formula_name)
        bias_group.shift(2*UP)

        parameters_group = VGroup(weights_group, input_group, bias_group)
        parameters_group.to_edge(LEFT)

        cal_next_layer = TextMobject("Values of the next layer")
        cal_next_layer.shift(3*RIGHT)

        forward_formula_s = TexMobject("a^{(l)}", "=", "\\sigma", "\\left(", "\\quad", "\\right)")
        forward_formula = TexMobject("z^{(l)}", "=", "a^{(l-1)}", "\cdot", "w", "+", "b")
        forward_formula_s[0].set_color(BLUE)
        forward_formula_s[2].set_color(PINK)
        forward_formula_s[4].set_color(ORANGE)
        forward_formula[0].set_color(ORANGE)
        forward_formula[2].set_color(RED)
        forward_formula[4].set_color(GREEN)
        forward_formula[6].set_color(PURPLE)
        forward_formula.next_to(cal_next_layer, DOWN)
        forward_formula_s.next_to(forward_formula, DOWN)

        self.play(Write(introduction_text))
        self.wait(0.5)
        self.play(Write(input_layers_text))
        self.wait(0.5)
        self.play(Transform(input_layers_text, and_text))
        self.wait(0.5)
        self.play(Transform(input_layers_text, output_layers_text))
        self.wait(0.5)
        self.play(ReplacementTransform(text_group, forward_text))
        self.wait(1)
        self.play(Write(input_group))
        self.wait(1)
        self.play(Write(weights_group))
        self.wait(1)
        self.play(Write(bias_group))
        self.wait(2)
        self.play(Write(cal_next_layer))
        self.wait(0.5)
        self.play(Write(forward_formula))
        self.wait(1)
        self.play(Write(forward_formula_s))
        forward_formula[0].move_to(forward_formula_s[4])
        self.wait(1)
        self.play(Indicate(input_formula_name), Indicate(forward_formula[2]))
        self.wait(1)
        self.play(Indicate(weights_formula_name), Indicate(forward_formula[4]))
        self.wait(1)
        self.play(Indicate(bias_formula_name), Indicate(forward_formula[6]))
        self.wait(2)

class Backward(Scene):
    def construct(self):
        backward_text = TextMobject("Back propagation")
        backward_text.shift(3*UP)

        input_formula = TexMobject("z^{(l)}", "=\\begin{bmatrix}a^{(l-1)}_1 & \\ldots \\\\ a^{(l-1)}_2 & \\ldots \\\\ a^{(l-1)}_2 & \\ldots \\\\ \\end{bmatrix}")
        input_formula[0].set_color(RED)
        input_formula.shift(UP)

        output_formula = TexMobject("y", "=\\begin{bmatrix} a^{(l)}_1 & a^{(l)}_2 \\\\ \\ldots & \\ldots \\\\ \\end{bmatrix}")
        output_formula[0].set_color(TEAL)
        output_formula.shift(2*DOWN)

        formula_group = VGroup(input_formula, output_formula)
        formula_group.to_edge(LEFT)

        error_text = TextMobject("Let's calclulate the error ", "$e$")
        error_text[1].set_color(GOLD)

        error_formula = TexMobject("e","=","a","-","y")
        error_formula[0].set_color(GOLD)
        error_formula[2].set_color(RED)
        error_formula[4].set_color(TEAL)

        error_group = VGroup(error_text, error_formula)
        error_group.to_edge(RIGHT)

        derivate_text = TextMobject("Then, let's derivate the error")
        derivate_text.shift(DOWN)

        derivate_formula = TexMobject("e\\prime", "=2","e","\\cdot", "\\sigma\\prime","(", "z",") \\cdot","a")
        derivate_formula[0].set_color(GOLD)
        derivate_formula[2].set_color(GOLD)
        derivate_formula[4].set_color(PINK)
        derivate_formula[6].set_color(BLUE)
        derivate_formula[8].set_color(RED)
        derivate_formula.shift(DOWN)

        derivate_group = VGroup(derivate_text, derivate_formula)
        derivate_group.to_edge(RIGHT)

        self.play(Write(backward_text), Write(input_formula))
        self.wait(2)
        self.play(Write(output_formula))
        self.wait(1)
        self.play(Write(error_text))
        self.wait(1)
        self.play(Transform(error_text, error_formula))
        self.wait(1)
        self.play(Indicate(input_formula[0]), Indicate(error_formula[2]))
        self.wait(1)
        self.play(Indicate(output_formula[0]), Indicate(error_formula[4]))
        self.wait(2)
        self.play(Write(derivate_text))
        self.wait(1)
        self.play(Transform(derivate_text, derivate_formula))
        self.wait(2)

class IntroduceSigmoid(GraphScene):
    CONFIG = {
        "x_min" : -5,
        "x_max" : 5,
        "x_axis_width" : 12,
        "y_min" : -1,
        "y_max" : 2,
        "y_axis_label" : "",
        "graph_origin" : DOWN,
        "x_labeled_nums" : list(range(-4, 5)),
        "y_labeled_nums" : list(range(-1, 3)),
    }
    def construct(self):
        self.setup_axes(animate=True)
        self.add_title()
        self.add_graph()

    def add_title(self):
        name = TextMobject("Sigmoid", color=PINK)
        name.next_to(ORIGIN, RIGHT, LARGE_BUFF)
        name.to_edge(UP)
        char = self.x_axis_label.replace("$", "")
        equation = TexMobject(
            "\\sigma","(%s) = \\frac{1}{1+e^{-%s}}"%(char, char)
        )
        equation[0].set_color(PINK)
        equation.next_to(name, DOWN)
        self.play(Write(equation), Write(name))

        self.equation = equation
        self.sigmoid_name = name

    def add_graph(self):
        graph = self.get_graph(
            lambda x : 1./(1+np.exp(-x)),
            color = PINK
        )

        self.play(ShowCreation(graph))
        self.wait(2)

        self.sigmoid_graph = graph
