import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QInputDialog,QAction,QWidgetAction,QCheckBox,QMessageBox
from PyQt5.uic import loadUi
from database import Note,my_session



class My_Main_Window(QMainWindow):
    def __init__(self):
        super(My_Main_Window,self).__init__()
        loadUi(r"C:\Users\pc\Documents\Python Developer Roadmap\Databases\Notes app\Notes App.ui",self)
        self.setWindowTitle("Untitled")
        self.resize(500,500)

        
            
        self.clear_unsaved()

        #Connect actions to function
        self.actionNew_Note.triggered.connect(self.create_note)
        self.actionSave_As.triggered.connect(self.save_as)
        self.actionSave_Note.triggered.connect(self.save_note)

        #connect menus to functions and actions to the actions under the menus
        self.menuView_Notes.aboutToShow.connect(self.add_dynamic_menu_items_viewnotes)
        self.menuView_Notes.triggered.connect(self.view_note)

        self.menuDelete_Note.aboutToShow.connect(self.add_dynamic_menu_items_deletenotes)
        self.menuDelete_Note.triggered.connect(self.delete_note)
        self.menuDelete_Note.aboutToHide.connect(self.delete_note)
 

    def clear_unsaved(self):
            """Delete Unsaved notes at the beginning of each new session"""
            with my_session:
                unsaved = my_session.query(Note).filter_by(saved = 0).all()
                for i in unsaved:
                    my_session.delete(i)
                    my_session.commit()

    def create_note(self):
            """Clear the existing text"""
            try: 
                self.plainTextEdit.clear()
                with my_session:
                    new_note = Note(name="Untitled")
                    new_note.saved = False
                    self.plainTextEdit.setProperty("note_object", new_note)
                    my_session.add(new_note)
                    my_session.commit()
            except:
                pass

         
    def save_note(self):
        """saves note to database"""
        try:

            content = self.plainTextEdit.toPlainText()
            with my_session:
                note =  self.plainTextEdit.property("note_object")
                note.content = content
                note.saved= True
                my_session.add(note)
                my_session.commit()
            self.plainTextEdit.clear()
        except:pass


    def save_as(self,action):
        """Saves note as a name"""
        content = self.plainTextEdit.toPlainText()
        note =  self.plainTextEdit.property("note_object")
        note_name, _ = QInputDialog.getText(self,"file Name", "Enter the File Name: ")
        with my_session:
            note.content = content
            note.name = note_name
            note.saved = True
            my_session.add(note)
            my_session.commit()
        self.plainTextEdit.clear()
    def view_notes(self):
        """Returns a list of note objects"""
        with my_session:
             list_of_notes = []
             notes = my_session.query(Note).all()
             for note in notes:
                 list_of_notes.append(note)
        return list_of_notes   
    
   

    def add_dynamic_menu_items_viewnotes(self):
        """Create a submenu based on previously created notes"""
        self.actions = []
        self.menuView_Notes.clear()
        my_list= self.view_notes()
        for item  in my_list:
            action = QAction(item.name, self)
            action.setData(item)
            self.menuView_Notes.addAction(action)
            

            
    def add_dynamic_menu_items_deletenotes(self):
        """Create a submenu based on previously created notes"""
        self.menuDelete_Note.clear()
        my_list= self.view_notes()
        for item  in my_list:
            check_box = QCheckBox(item.name)
            widget_action = QWidgetAction(self)
            widget_action.setDefaultWidget(check_box)
            widget_action.setData(item)
            self.menuDelete_Note.addAction(widget_action)
           

    def delete_note(self):
        """Delete a note from the database"""
        checked_items = []
        for action in self.menuDelete_Note.actions():
            widget = action.defaultWidget()
            if isinstance(widget, QCheckBox) and widget.isChecked():
                checked_items.append(action.data())
        for item in checked_items:
            with my_session:
                my_session.delete(item)
                my_session.commit()
        
    

    def view_note(self,action):
        """View the contents of a note"""
        self.plainTextEdit.setPlainText(action.data().content)
        self.plainTextEdit.setProperty("data_object", action.data())
    



def main():
    app = QApplication(sys.argv)
    window = My_Main_Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
