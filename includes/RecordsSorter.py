class RecordsSorter:
    @staticmethod
    def get_optimization_lists_dict_by_functions(optimization_records_list: list) -> dict:
        result = dict()

        for rec in optimization_records_list:
            function_name = rec["func"]["label"]

            if function_name not in result.keys():
                result[function_name] = []

            result[function_name].append(rec)

        return result
