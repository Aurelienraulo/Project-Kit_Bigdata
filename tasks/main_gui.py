import tkinter as tk
from tkinter import messagebox
from tasks.tasklist import TaskList


def use_gui(task_list):
    """
    Creates a graphical user interface (GUI) for a task manager application.

    Args:
        task_list (TaskList): An instance of the TaskList class representing a list of tasks.

    Example Usage:
        task_list = TaskList()
        use_gui(task_list)

    Flow:
        1. Creates a Tkinter root window and sets its title.
        2. Creates an instance of the TaskManagerGUI class, passing the root window and the task_list as arguments.
        3. Calls the run method of the TaskManagerGUI instance, which starts the GUI event loop and displays the GUI to the user.

    Returns:
        None. It creates a GUI for the task manager application.
    """
    root = tk.Tk()
    root.title("Gestionnaire de Tâches - Interface Graphique")

    gui = TaskManagerGUI(root, task_list)
    gui.run()


class TaskManagerGUI:
    def __init__(self, root, task_list):
        """
        Initializes the GUI for a task manager application.

        Args:
            root (tk.Tk): The root window of the GUI.
            task_list (TaskList): An instance of the TaskList class representing a list of tasks.

        Returns:
            None

        Summary:
        The __init__ method of the TaskManagerGUI class initializes the GUI for a task manager application. It creates the main window and divides it into three parts: left, middle, and right. The left part is for adding tasks, the middle part is for displaying the list of tasks, and the right part is for displaying the details of the selected task. It also creates buttons and input fields for adding tasks, displaying tasks, deleting tasks, marking tasks as completed, and displaying archived tasks.

        Example Usage:
        task_list = TaskList()
        root = tk.Tk()
        gui = TaskManagerGUI(root, task_list)
        gui.run()
        """
        self.root = root
        self.root.title("Gestionnaire de Tâches - Interface Graphique")
        self.task_list = task_list

        # Divisez la fenêtre en trois parties (gauche, milieu et droite)
        left_frame = tk.Frame(root)
        left_frame.pack(side=tk.LEFT, padx=10)

        middle_frame = tk.Frame(root)
        middle_frame.pack(side=tk.LEFT, padx=10)

        self.right_frame = tk.Frame(root)
        self.right_frame.pack(side=tk.LEFT, padx=10)
        self.right_frame.pack_forget()  # Masquer le cadre initialement

        # Partie gauche pour l'ajout de tâches
        label_name = tk.Label(left_frame, text="Nom de la tâche:")
        label_name.pack()
        self.input_name = tk.Entry(left_frame)
        self.input_name.pack()

        label_description = tk.Label(
            left_frame, text="Description de la tâche:")
        label_description.pack()
        self.input_description = tk.Entry(left_frame)
        self.input_description.pack()

        add_button = tk.Button(
            left_frame, text="Ajouter Tâche", command=self.add_task)
        add_button.pack()

        # Partie milieu pour la liste des tâches
        taches_en_cours_label = tk.Label(middle_frame, text="Tâches en cours")
        taches_en_cours_label.pack()

        instruction_label = tk.Label(
            middle_frame, text="Sélectionnez une tâche pour voir les détails")
        instruction_label.pack()

        self.task_listbox = tk.Listbox(middle_frame, height=10, width=40)
        self.task_listbox.pack()
        self.selected_task = None

        # Partie droite pour afficher les détails de la tâche sélectionnée
        self.details_label = tk.Label(
            self.right_frame, text="Détails de la Tâche")
        self.details_label.pack()
        self.details_text = tk.Text(self.right_frame, height=10, width=40)
        self.details_text.pack()

        # Bouton pour supprimer la tâche sélectionnée
        self.delete_button = tk.Button(
            self.right_frame, text="Supprimer", command=self.delete_selected_task)
        self.delete_button.pack_forget()  # Masquer le bouton initialement

        # Bouton pour marqué terminée la tâche sélectionnée
        self.complete_button = tk.Button(
            self.right_frame, text="Marquer comme Complétée", command=self.complete_selected_task)
        self.complete_button.pack_forget()  # Masquer le bouton initialement

        self.display_archived_button = tk.Button(
            middle_frame, text="Afficher Tâches Archivées", command=self.display_archived_tasks)
        self.display_archived_button.pack_forget()

    def delete_selected_task(self):
        """
        Deletes the selected task from the task list.

        If there is a selected task, it retrieves the name of the task and removes it from the task list using the `remove_task` method of the `TaskList` class.
        It sets `self.selected_task` to None and updates the display of tasks by calling the `display_tasks` method.
        It updates the text of the `details_label` to "Détails de la Tâche" and clears the text in the `details_text` widget.
        """

        if self.selected_task:
            task_name = self.selected_task.name
            self.task_list.remove_task(task_name)
            self.selected_task = None
            self.display_tasks()
            self.details_label.config(text="Détails de la Tâche")
            self.details_text.delete(1.0, tk.END)

    def complete_selected_task(self):
        """
        Marks the selected task as completed.

        If there is a selected task, it retrieves the name of the task and marks it as completed using the `mark_task_completed` method of the `TaskList` class.
        It sets `self.selected_task` to None and updates the display of tasks by calling the `display_tasks` method.
        It updates the text of the `details_label` to "Détails de la Tâche" and clears the text in the `details_text` widget.
        """

        if self.selected_task:
            task_name = self.selected_task.name
            self.task_list.mark_task_completed(task_name)
            self.selected_task = None
            self.display_tasks()
            self.details_label.config(text="Détails de la Tâche")
            self.details_text.delete(1.0, tk.END)

    def add_task(self):
        """
        Adds a task to the task list.

        Retrieves the name and description of a task from the input fields in the GUI.
        Calls the add_task method of the TaskList class to add the task to the task list.
        If successful, shows a success message box and clears the input fields.
        Finally, calls the display_tasks method to update the display of tasks.
        """
        name = self.input_name.get()
        description = self.input_description.get()

        try:
            self.task_list.add_task(name, description)
            messagebox.showinfo(
                "Succès", f"Tâche '{name}' ajoutée à la liste.")
            self.input_name.delete(0, tk.END)
            self.input_description.delete(0, tk.END)
            self.display_tasks()
        except ValueError as e:
            messagebox.showerror("Erreur", f"Erreur : {e}")

    def display_tasks(self):
        """
        Displays the list of tasks.

        Clears the task listbox in the GUI.
        Iterates over the tasks in the task list and inserts their names into the task listbox.
        """
        self.task_listbox.delete(0, tk.END)

        for task in self.task_list.tasks:
            self.task_listbox.insert(tk.END, task.name)

    def display_archived_tasks(self):
        """
        Displays the archived tasks.

        Retrieves the archived tasks from the task list.
        If there are no archived tasks, shows an information message box.
        Otherwise, creates a text string by joining the string representations of the archived tasks.
        Shows an information message box with the text string.
        """
        archived_tasks = self.task_list.archived_tasks
        if not archived_tasks:
            messagebox.showinfo("Tâches Archivées", "Aucune tâche archivée.")
        else:
            archived_tasks_text = "\n".join(
                [str(task) for task in archived_tasks])
            messagebox.showinfo("Tâches Archivées", archived_tasks_text)

    def display_selected_task(self, event):
        """
        Updates the details section of the GUI with the selected task's information and displays buttons for deleting the task, marking it as completed, and displaying archived tasks. If no task is selected, it hides the details section and the buttons.

        :param event: The event object that triggered the method, usually a mouse click event.
        :return: None
        """
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task_index = selected_task_index[0]
            self.selected_task = self.task_list.tasks[selected_task_index]
            self.details_label.config(
                text=f"Détails de la Tâche '{self.selected_task.name}'")
            self.details_text.delete(1.0, tk.END)  # Effacez le contenu actuel
            task_details = str(self.selected_task)
            self.details_text.insert(tk.END, task_details)

            # Afficher le cadre des détails et les boutons en utilisant self
            self.right_frame.pack()
            self.delete_button.pack()
            self.complete_button.pack()

            # Afficher le bouton "Afficher les tâches archivées"
            self.display_archived_button.pack()
        else:
            # Masquer le cadre des détails, les boutons et le bouton "Afficher les tâches archivées" si aucune tâche n'est sélectionnée
            self.right_frame.pack_forget()
            self.delete_button.pack_forget()
            self.complete_button.pack_forget()

            # Masquer le bouton "Afficher les tâches archivées"
            self.display_archived_button.pack_forget()

    def run(self):
        """
        Starts the GUI event loop and displays the GUI to the user.

        Example Usage:
        ```python
        task_list = TaskList()
        root = tk.Tk()
        gui = TaskManagerGUI(root, task_list)
        gui.run()
        ```

        Inputs: None

        Flow:
        1. Binds the `display_selected_task` method to the `<<ListboxSelect>>` event of the `task_listbox` widget.
        2. Starts the GUI event loop by calling the `mainloop` method of the `root` window.

        Outputs: None
        """
        self.task_listbox.bind("<<ListboxSelect>>", self.display_selected_task)
        self.root.mainloop()


if __name__ == "__main__":
    task_list = TaskList()
    use_gui(task_list)