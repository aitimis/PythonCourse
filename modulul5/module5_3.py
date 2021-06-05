class Note:
    text = 'Default text'
    def add_text(self):
        self.text = self.text + ' New text entry '
    def clear_text(self):
        #self.text = self.text.replace('Default text', '')
        self.text = ''
    def remove_text(self):
        self.text = self.text.replace('Default text', '')
    def count_lines(self):
        count = len(self.text.splitlines())
        return count

note = Note()
print(type(note))
print(type(''))
print('instance value: ', note.text)
note.remove_text()
print('instance value: ', note.text)
note.text = 'new text'
print('instance value: ', note.text)
note.add_text()
print('instance value: ', note.text)
note.clear_text()
print('instance value: ', note.text)
note.add_text('First line \n Second line')
print(note.count_lines())