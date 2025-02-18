from manim import *
import numpy as np

class CorazonAnimado(Scene):
    def construct(self):
        # Configuración de los ejes
        ejes = Axes(
            x_range=[-2, 2, 0.1],
            y_range=[-1, 2, 0.1],
            axis_config={"color": WHITE},
            x_length=7,
            y_length=6,
            x_axis_config={"tick_size": 0.05},
            y_axis_config={"tick_size": 0.05}
        )
        ejes.shift(UP * 1)  

        k_tracker = ValueTracker(0.00)

        titulo = Text("¿Quieres ser mi San Valentín?", font_size=48, color=RED)
        titulo.move_to(ejes.get_bottom()).shift(DOWN * 0.5)

        att_text = Text("ATT: Diego Rave", font_size=32, color=RED_D)
        att_text.next_to(titulo, DOWN)  
        
        graph = always_redraw(
            lambda: ejes.plot_parametric_curve(
                lambda t: np.array([
                    t,
                    (t**2)**(1/3) + 0.7 * np.sin(k_tracker.get_value() * t) * np.sqrt(3 - t**2),
                    0
                ]),
                t_range=[-np.sqrt(3), np.sqrt(3)],
                color=RED
            )
        )

        # Animaciones
        self.play(DrawBorderThenFill(ejes))  # Dibuja los ejes
        self.play(Create(graph))  # Crea la gráfica
        self.play(Write(titulo))  # Escribe el título
        self.play(Write(att_text))  # Escribe el texto "ATT: Diego Rave"
        self.play(k_tracker.animate.set_value(100.00), run_time=8, rate_func=linear)  # Anima k
        self.wait(2)  # Espera al final