"""
Anzony Santos
April 3, 2026
TUI for application
"""
from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Input, Static, Label, Header, Button
from textual.containers import Vertical, Horizontal, Grid
from textual import events
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
            yield Button("Present Tense", classes="fake-label")
            # yield Label("Él habla conmigo.")
            # yield Label("(He talks with me.")
        with Vertical(classes="tense-card"):
            yield Button("Preterite", classes="fake-label")
            # yield Label("De repente él habló de otra cosa.")
            # yield Label("(Suddenly he spoke of something else.)")
        with Vertical(classes="tense-card"):
            yield Button("Imperfect", classes="fake-label")
            # yield Label("Ella siempre hablaba del imperfecto.")
            # yield Label("(She always talked of the imperfect.)")
        with Vertical(classes="tense-card"):
            yield Button("Future Tense", classes="fake-label")
            # yield Label("Manana ella hablará de su futuro.")  # Dont forget to add the tilda to the n on Manana
            # yield Label("(Tommorow she will talk of her future.)")
        with Vertical(classes="tense-card"):
            yield Button("Present Subjunctive", classes="fake-label")
            # yield Label("Es importante que él no hable con nadie sobre eso.")
            # yield Label("(It is important that he doesn't talk with anybody about it.)")
        with Vertical(classes="tense-card"):
            yield Button("Imperfect Subjunctive", classes="fake-label")
            # yield Label("Si él hablara menos, ella hablaría con él.")
            # yield Label("(If he talked less, she would talke with him.)")
        with Vertical(classes="tense-card"):
            yield Button("Conditional", classes="fake-label")
            # yield Label("Si él hablara menos, ella hablaría con él.")
            # yield Label("(If he talked less, she would talke with him.)")

    def on_mount(self) -> None:
        self.screen.styles.background = "#e8dcad"


class VerbSelectorScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Label("Select verbs:", id="verb-heading")

        with Vertical(id="segment_1"):
            with Vertical(classes="verb-selector-card"):
                yield Button("Basic", classes="fake-label")
            with Vertical(classes="verb-selector-card"):
                yield Button("Regular", classes="fake-label")
            with Vertical(classes="verb-selector-card"):
                yield Button("Irregular", classes="fake-label")
            with Vertical(classes="verb-selector-card"):
                yield Button("Topic: Learning", classes="fake-label")
            with Vertical(classes="verb-selector-card"):
                yield Button("Topic: Traveling", classes="fake-label")

    def on_mount(self) -> None:
        self.screen.styles.background = "#e8dcad"


class MainScreen(Screen):  # Screen for the main game loop
    main_verb = reactive({'infinitive': 'Loading...'})
    main_form = reactive("")
    main_answer = reactive("")

    def compose(self) -> ComposeResult:
        yield Header("Spaleoff")
        with Horizontal(id="main-content"):
            with Vertical(classes="column"):
                yield Label(self.main_form, id="verb-form-label")
            with Vertical(classes="column"):
                yield Label(self.main_verb["infinitive"], id="verb-label")
                yield Input("", id="conjugation-input")
                yield Label("Correct: ")
            with Vertical(classes="column"):
                yield Label("Translation")
                with Horizontal(id="accent-box"):
                    yield Button("á", classes="accent-letters")
                    yield Button("é", classes="accent-letters")
                    yield Button("í", classes="accent-letters")
                    yield Button("ó", classes="accent-letters")
                    yield Button("ú", classes="accent-letters")
                yield Label("[0/0]")

    def on_key(self, event: events.Key) -> None:
        if event.key == "enter":
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
            print("Presed Enter")

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
    BINDINGS = [("t", "push_screen('tense_screen')", "TenseScreen"),
                ("v", "push_screen('verb_screen')", "VerbSelectorScreen"),
                ("m", "push_screen('main_screen')", "MainScreen")]

    def on_mount(self) -> None:
        self.push_screen(TenseScreen())


def send_to_validate(user_input: str) -> bool:
    return verb_utils.validate_answer(user_input, current_answer)


if __name__ == "__main__":
    all_verbs = verb_utils.get_verbs()
    MyApp().run()
