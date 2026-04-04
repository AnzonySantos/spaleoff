"""
Anzony Santos
April 3, 2026
TUI for application
"""
from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Input, Static, Label, Header
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
        yield Static("Spaleoff")
        yield Label("Present")
        yield Label("Preterite")
        # Remeber to add the other tenses when complete


class VerbSelectorScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Static("Spaleoff")
        yield Label("Basic")
        yield Label("Regular")
        yield Label("Irregular")
        yield Label("Topic: Learning")
        yield Label("Topic: Traveling")


class MainScreen(Screen):  # Screen for the main game loop
    main_verb = reactive({'infinitive': 'Loading...'})
    main_form = reactive("")
    main_answer = reactive("")

    def compose(self) -> ComposeResult:
        yield Header("Spaleoff")
        with Horizontal():
            with Vertical():
                yield Label(self.main_form, id="verb-form-label")
            with Vertical():
                yield Label(self.main_verb["infinitive"], id="verb-label")
                yield Input("", id="conjugation-input")
                yield Label("Correct: ")
            with Vertical():
                yield Label("Translation")
                with Horizontal():
                    yield Label("á")
                    yield Label("é")
                    yield Label("í")
                    yield Label("ó")
                    yield Label("ú")
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

    def on_mount(self) -> None:
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
    SCREENS = {"tense_screen": TenseScreen, "verb_screen": VerbSelectorScreen, "main_screen": MainScreen}
    BINDINGS = [("t", "push_screen('tense_screen')", "TenseScreen"),
                ("v", "push_screen('verb_screen')", "VerbSelectorScreen"),
                ("m", "push_screen('main_screen')", "MainScreen")]

    def on_mount(self) -> None:
        self.push_screen(MainScreen())


def send_to_validate(user_input: str) -> bool:
    return verb_utils.validate_answer(user_input, current_answer)


if __name__ == "__main__":
    all_verbs = verb_utils.get_verbs()
    MyApp().run()
