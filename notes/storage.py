class Note:
    last_id = 0

    @classmethod
    def next_id(cls):
        cls.last_id += 1
        return cls.last_id

    def __init__(self, text: str) -> None:
        self.id = self.next_id()
        self.text = text


class NoteStorage:
    def __init__(self, notes: list[Note] = None) -> None:
        if notes is None:
            notes = []
        self.notes = notes

    def get_all_notes(self):
        return self.notes

notes = [
    Note(text=f"Text {text}")
    for text in range(10)
]

notes_storage = NoteStorage(notes=notes)

