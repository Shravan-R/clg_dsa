class TextEditor:

    def __init__(self, initial_text=""):
        self._text = initial_text
        self.undo_stack = []
        self.redo_stack = []

    def get_text(self):
        return self._text

    def _apply_insert(self, pos, text):
        pos = max(0, min(pos, len(self._text)))
        self._text = self._text[:pos] + text + self._text[pos:]

    def _apply_delete(self, pos, length):
        if pos < 0:
            pos = 0
        if pos >= len(self._text) or length <= 0:
            return ""
        end = min(len(self._text), pos + length)
        removed = self._text[pos:end]
        self._text = self._text[:pos] + self._text[end:]
        return removed

    def insert(self, pos, text):
        if not text:
            return
        self._apply_insert(pos, text)
        self.undo_stack.append(('delete', pos, text))
        self.redo_stack.clear()

    def append(self, text):
        self.insert(len(self._text), text)

    def delete(self, pos, length):
        removed = self._apply_delete(pos, length)
        if removed:
            self.undo_stack.append(('insert', pos, removed))
            self.redo_stack.clear()

    def undo(self):
        if not self.undo_stack:
            return False
        typ, pos, data = self.undo_stack.pop()

        if typ == 'insert':
            # Undo a delete by reinserting text
            self._apply_insert(pos, data)
            self.redo_stack.append(('delete', pos, data))

        elif typ == 'delete':
            # Undo an insert by deleting text
            removed = self._apply_delete(pos, len(data))
            self.redo_stack.append(('insert', pos, removed))

        return True

    def redo(self):
        if not self.redo_stack:
            return False

        typ, pos, data = self.redo_stack.pop()

        if typ == 'insert':
            self._apply_insert(pos, data)
            self.undo_stack.append(('delete', pos, data))

        elif typ == 'delete':
            removed = self._apply_delete(pos, len(data))
            self.undo_stack.append(('insert', pos, removed))

        return True

    def debug_stacks(self):
        return {
            'undo_stack': list(self.undo_stack),
            'redo_stack': list(self.redo_stack)
        }


if __name__ == "__main__":
    ed = TextEditor()
    ed.append("Hello")
    ed.append(", world")
    print("After appends:", ed.get_text())
    ed.insert(5, " beautiful")
    print("After insert:", ed.get_text())
    ed.delete(5, 10)
    print("After delete:", ed.get_text())
    ed.undo()
    print("After undo:", ed.get_text())
    ed.undo()
    print("After second undo:", ed.get_text())
    ed.redo()
    print("After redo:", ed.get_text())
    print("Stacks:", ed.debug_stacks())
