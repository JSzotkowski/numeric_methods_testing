from includes.RecordsSorter import RecordsSorter
from includes.CSVFormatter import CSVFormatter
from includes.FileManager import FileManager
from includes.UserConsole import UserConsole
from includes.Plotter import Plotter
import json
import os


class Core:
    def __init__(self, records):
        self.records = records if records is not None else []
        self.optimization_finished = False

        self.main_menu()

    def append_record(self, record):
        self.records.append(record)

    def optimize_records(self):
        assert len(self.records) > 0

        for record in self.records:
            record.optimize()
            UserConsole.print_optimization_finished(record)

        self.optimization_finished = True
        UserConsole.print_optimizations_finished()

        return self.records

    def get_records(self):
        assert self.optimization_finished

        return self.records

    def get_all_records_json_array(self):
        assert self.optimization_finished

        ans = []

        for rec in self.records:
            ans.append(rec.get_json_dict())

        return ans

    def __getitem__(self, item):
        return self.records[item]

    def __setitem__(self, key, value):
        self.records[key] = value

    def main_menu(self):
        menu = [
            "Quit program.",
            "Optimize programmed functions using given optimizers.",
            "Load previous optimization from output.json file.",
            "Save current optimization to output.json file.",
            "Draw function optimization plot.",
            "Export optimizations CSV files sorted by functions.",
            "Print simplified results."
        ]

        callbacks = [
            exit,
            self.optimize_records,
            self.load_previous_optimization,
            self.save_current_optimization,
            self.draw_menu,
            self.export_optimizations_csv_files_sorted_by_functions,
            self.print_simplified_results
        ]

        while True:
            user_choice = UserConsole.let_user_select_from_menu(menu)
            callbacks[user_choice]()

    def draw_menu(self):
        message = "Select what function optimization you'd like to draw or go back to main menu."

        menu = [
            "Go back to main menu.",
        ]

        menu.extend([rec.get_label() for rec in self.records])

        plot_type_menu = [
            "Go back to previous menu.",
            "Surface plot.",
            "Contour plot."
        ]

        plotter = Plotter()

        plot_type_menu_message = "Here are available types of plots that can be drawn. "
        plot_type_menu_message += "You can also go back to previous menu."

        plot_type_menu_callbacks = [
            0,
            plotter.surface_plot,
            plotter.contour_plot
        ]

        while True:
            user_choice = UserConsole.let_user_select_from_menu(menu, message)
            if user_choice == 0:
                break

            plotter.set_record(self.records[user_choice - 1])
            while True:
                user_choice = UserConsole.let_user_select_from_menu(plot_type_menu, plot_type_menu_message)
                if user_choice == 0:
                    break
                plot_type_menu_callbacks[user_choice]()

    def save_current_optimization(self):
        r = self.get_all_records_json_array()

        with open("/home/jiri/PycharmProjects/numeric_methods_testing/output files/output.json", "w") as outfile:
            json.dump(r, outfile, indent=4)

    def load_previous_optimization(self):
        print("Method not implemented yet. Instead all optimizations will be removed, the memory will be freed now.")
        self.records = []
        self.optimization_finished = False

    def export_optimizations_csv_files_sorted_by_functions(self):
        assert self.optimization_finished
        output_dir_path = "/home/jiri/PycharmProjects/numeric_methods_testing/"
        output_dir_path += "output files/optimizations sorted by functions"

        optimization_lists_dict = RecordsSorter.get_optimization_lists_dict_by_functions(
            self.get_all_records_json_array())

        for function_name, optimization_list in optimization_lists_dict.items():
            lines_to_save = CSVFormatter.get_csv_lines_for_all_optimizations_of_single_function(optimization_list)

            fm = FileManager(os.path.join(output_dir_path, f'{function_name}.csv'))
            fm.save_list_to_file(lines_to_save)

    def print_simplified_results(self):
        assert self.optimization_finished

        temp = self.records
        self.records = sorted(self.records, key=lambda k: k.number_of_steps)
        for i, rec in enumerate(self.records):
            print(f'{i+1}. {rec.number_of_steps} - {rec.get_label()}')

        self.records = temp
