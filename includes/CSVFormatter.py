from math import sqrt


class CSVFormatter:
    @staticmethod
    def get_csv_lines_for_all_optimizations_of_single_function(function_optimizations: list) -> list[str] | None:
        if len(function_optimizations) == 0:
            return

        func_name = function_optimizations[0]["func"]["label"]
        func_commentary = function_optimizations[0]["func"]["commentary"]
        func_desired_minimum = function_optimizations[0]["func"]["desired_minimum"]

        rs = [f'"{func_name}"', f'"{func_commentary}"']

        number_of_columns_per_optimizer = 3

        line = ""
        for opt_rec in function_optimizations:
            line += f'"{opt_rec["label"]}"' + " " * number_of_columns_per_optimizer
        rs.append(line)

        for opt_property in function_optimizations[0]["optimizer"].keys():
            line = ""
            for opt_rec in function_optimizations:
                line += f'"{opt_property}" "{opt_rec["optimizer"][opt_property]}"'
                line += " " * (number_of_columns_per_optimizer - 1)
            rs.append(line)

        max_opt_path_len = len(max(function_optimizations, key=lambda k: len(k["optimizer_path"]))["optimizer_path"])

        line = ""
        for _ in function_optimizations:
            line += f'x y err' + " " * (number_of_columns_per_optimizer - 2)
        rs.append(line)

        for i in range(max_opt_path_len):
            line = ""
            for opt_rec in function_optimizations:
                if i >= len(opt_rec["optimizer_path"]):
                    line += " " * number_of_columns_per_optimizer
                    continue
                x, y = opt_rec["optimizer_path"][i]
                des_x, des_y = func_desired_minimum
                err = sqrt((x - des_x) ** 2 + (y - des_y) ** 2)
                line += f'{x} {y} {err}'
                line += " " * (number_of_columns_per_optimizer - 2)
            rs.append(line)

        return rs
