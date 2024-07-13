class LLPUtil:
    @staticmethod
    def parse_llp(mode: PrintMode, vec: list, record_fn: Callable):
        """
        Parse the Lock-Less Persistence (LLP) based on the traversal mode.
        
        :param mode: Traversal mode (ALL or CURRENT)
        :param vec: List of LLP vectors
        :param record_fn: Function to process each record
        """
        if mode == PrintMode.ALL:
            print("Traversing all LLPs")
        elif mode == PrintMode.CURRENT:
            print("Traversing current LLP")
        
        # Call the record function for each item in vec
        for item in vec:
            record_fn(item)

    @staticmethod
    def dump_vec_details(LLP_vec: list, s: str = ""):
        """
        Dump details of the LLP vector.
        
        :param LLP_vec: List of LLP vectors
        :param s: Optional annotating string
        """
        print(f"Dumping details of the vector: {s}")
        for item in LLP_vec:
            print(f"Item: {item}")

    @staticmethod
    def formatted_dump(os, print_mode: PrintMode, exch_msg: str):
        """
        Format and dump the exchange message based on the print mode.
        
        :param os: Output stream
        :param print_mode: Print mode (LINE_MODE, VERBOSE_MODE, PARAGRAPH_MODE, CUSTOM_MODE)
        :param exch_msg: Exchange message to be printed
        """
        if print_mode != PrintMode.LINE_MODE:
            os.write("\n")
        
        if print_mode == PrintMode.LINE_MODE:
            os.write(f"{exch_msg} | ")
        elif print_mode in [PrintMode.VERBOSE_MODE, PrintMode.PARAGRAPH_MODE]:
            os.write(f"{exch_msg}\n")
        elif print_mode == PrintMode.CUSTOM_MODE:
            os.write(f"{exch_msg}")
        else:
            print(f"Unknown PrintMode [{print_mode}]")

# Example usage
def example_record_fn(item):
    print(f"Processing item: {item}")

LLP_vec = ["vec1", "vec2"]
LLPUtil.parse_llp(PrintMode.ALL, LLP_vec, example_record_fn)
LLPUtil.dump_vec_details(LLP_vec, "Example Vector")
