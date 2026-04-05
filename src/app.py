"""
Anzony Santos
April 3, 2026
TUI for application
"""
from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Input, Static, Label, Header, Button
from textual.containers import Vertical, Horizontal
from textual import events, on
from textual.reactive import reactive

import verb_utils

""" Global Variables """
all_verbs: list = []
current_tense: str = "present"
current_verbs: list = []

current_verb: dict = {}
current_form: str = "yo"
current_answer: str = ""

class TenseScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        with Vertical(classes="tense-heading"):
            yield Label("Spanish Verb Conjugation Trainer", id="tense-title")
            # yield Label("With the Conjugation Trainer you can improve your knowledge of the most frequent forms of the most important Spanish verbs.")
            yield Label("Select verb tense:", id="tense-subtitle")

        with Vertical(classes="tense-card"):
            yield Button("Present Tense", classes="fake-label", id="present-tense")
            # yield Label("Él habla conmigo.")
            # yield Label("(He talks with me.")
        with Vertical(classes="tense-card"):
            yield Button("Preterite", classes="fake-label", id="preterite-tense")
            # yield Label("De repente él habló de otra cosa.")
            # yield Label("(Suddenly he spoke of something else.)")
        with Vertical(classes="tense-card"):
            yield Button("Imperfect", classes="fake-label", id="imperfect-tense")
            # yield Label("Ella siempre hablaba del imperfecto.")
            # yield Label("(She always talked of the imperfect.)")
        with Vertical(classes="tense-card"):
            yield Button("Future Tense", classes="fake-label", id="future-tense")
            # yield Label("Manana ella hablará de su futuro.")  # Dont forget to add the tilda to the n on Manana
            # yield Label("(Tommorow she will talk of her future.)")
        with Vertical(classes="tense-card"):
            yield Button("Present Subjunctive", classes="fake-label", id="present-subjunctive-tense")
            # yield Label("Es importante que él no hable con nadie sobre eso.")
            # yield Label("(It is important that he doesn't talk with anybody about it.)")
        with Vertical(classes="tense-card"):
            yield Button("Imperfect Subjunctive", classes="fake-label", id="imperfect-subjunctive-tense")
            # yield Label("Si él hablara menos, ella hablaría con él.")
            # yield Label("(If he talked less, she would talke with him.)")
        with Vertical(classes="tense-card"):
            yield Button("Conditional", classes="fake-label", id="conditional-tense")
            # yield Label("Si él hablara menos, ella hablaría con él.")
            # yield Label("(If he talked less, she would talke with him.)")

    def on_mount(self) -> None:
        self.screen.styles.background = "#e8dcad"

    @on(Button.Pressed, "#present-tense")
    def select_present_tense(self):
        global current_tense
        current_tense = "present"
        self.app.push_screen("verb_screen")

    @on(Button.Pressed, "#preterite-tense")
    def select_preterite_tense(self):
        global current_tense
        current_tense = "preterite"
        self.app.push_screen("verb_screen")

    @on(Button.Pressed, "#imperfect-tense")
    def select_imperfect_tense(self):
        self.exit()  # PLACEHOLDER

    @on(Button.Pressed, "#future-tense")
    def select_future_tense(self):
        self.exit()  # PLACEHOLDER

    @on(Button.Pressed, "#present-subjunctive-tense")
    def select_present_subjunctive_tense(self):
        self.exit()  # PLACEHOLDER

    @on(Button.Pressed, "#imperfect-subjunctive-tense")
    def select_imperfect_subjunctive_tense(self):
        self.exit()  # PLACEHOLDER

    @on(Button.Pressed, "#conditional-tense-tense")
    def select_conditional_tense(self):
        self.exit()  # PLACEHOLDER


class VerbSelectorScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Label("Select verbs:", id="verb-heading")

        with Vertical(id="segment_1"):
            with Vertical(classes="verb-selector-card"):
                yield Button("Basic", classes="fake-label", id="basic-verbs")
            with Vertical(classes="verb-selector-card"):
                yield Button("Regular", classes="fake-label", id="regular-verbs")
            with Vertical(classes="verb-selector-card"):
                yield Button("Irregular", classes="fake-label", id="irregular-verbs")
            with Vertical(classes="verb-selector-card"):
                yield Button("Topic: Learning", classes="fake-label", id="learning-verbs")
            with Vertical(classes="verb-selector-card"):
                yield Button("Topic: Traveling", classes="fake-label", id="traveling-verbs")

    def on_mount(self) -> None:
        self.screen.styles.background = "#e8dcad"

    @on(Button.Pressed, "#basic-verbs")
    def select_basic_verbs(self):
        self.app.push_screen("main_screen")

    @on(Button.Pressed, "#regular-verbs")
    def select_regular_verbs(self):
        self.exit()

    @on(Button.Pressed, "#irregular-verbs")
    def select_irregular_verbs(self):
        self.exit()

    @on(Button.Pressed, "#traveling-verbs")
    def select_traveling_verbs(self):
        self.exit()

    @on(Button.Pressed, "#learning-verbs")
    def select_learning_verbs(self):
        self.exit()


class MainScreen(Screen):  # Screen for the main game loop
    main_verb = reactive({'infinitive': 'Loading...'})
    main_form = reactive("")
    main_answer = reactive("")
    main_total_correct = 0
    main_total_answered = 0
    main_string = reactive(f'[{main_total_correct}/{main_total_answered}]')
    main_temp_string = reactive("")


    def compose(self) -> ComposeResult:
        yield Header("Spaleoff")
        with Horizontal(id="main-content"):
            with Vertical(classes="column", id="column_1"):
                yield Label(self.main_form, id="verb-form-label")
            with Vertical(classes="column", id="column_2"):
                yield Label(self.main_verb["infinitive"], id="verb-label")
                yield Input("", id="conjugation-input")
         #       yield Label(f'Correct: {self.main_temp_string}', id="temp-id")
            with Vertical(classes="column", id="column_3"):
                yield Label("Translation")
                with Horizontal(id="accent-box"):
                    yield Button("á", classes="accent-letters")
                    yield Button("é", classes="accent-letters")
                    yield Button("í", classes="accent-letters")
                    yield Button("ó", classes="accent-letters")
                    yield Button("ú", classes="accent-letters")
                yield Label(self.main_string, id="counter")

    @on(Input.Submitted, "#conjugation-input")
    def handle_submission(self, event):
        if (verb_utils.validate_answer(event.value, self.main_answer)):
            self.main_total_correct += 1
        # self.main_temp_string = event.value
        self.main_total_answered += 1

        global all_verbs
        global current_tense

        global current_verb
        global current_form
        global current_answer

        temp_triple_tuple = verb_utils.update_verb_attributes(all_verbs, current_tense)
        current_verb, (current_form, current_answer) = temp_triple_tuple

        self.main_verb = current_verb
        self.main_form = current_form
        self.main_answer = current_answer
        self.main_string = f'[{self.main_total_correct}/{self.main_total_answered}]'

        self.query_one("#verb-label").update(self.main_verb["infinitive"])
        self.query_one("#verb-form-label").update(self.main_form)
        self.query_one("#counter").update(self.main_string)
        # self.query_one("#temp-id").update(self.main_temp_string)
        print("Presed Enter")
        
        event.input.clear()

    def on_mount(self) -> None:
        self.screen.styles.background = "#e8dcad"

        global all_verbs
        global current_tense

        global current_verb
        global current_form
        global current_answer

        temp_triple_tuple = verb_utils.update_verb_attributes(all_verbs, current_tense)
        current_verb, (current_form, current_answer) = temp_triple_tuple

        self.main_verb = current_verb
        self.main_form = current_form
        self.main_answer = current_answer

        self.query_one("#verb-label").update(self.main_verb["infinitive"])
        self.query_one("#verb-form-label").update(self.main_form)


class MyApp(App):
    CSS_PATH = "app.tcss"
    TITLE = "Spaleoff"
    SCREENS = {"tense_screen": TenseScreen, "verb_screen": VerbSelectorScreen, "main_screen": MainScreen}

    def on_mount(self) -> None:
        self.push_screen(TenseScreen())


if __name__ == "__main__":
    all_verbs = verb_utils.get_verbs()
    MyApp().run()
