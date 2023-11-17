import logging
from haystack.nodes import TextConverter, PDFToTextConverter, DocxToTextConverter, PreProcessor


logging.basicConfig(format="%(levelname)s - %(name)s -  %(message)s", level=logging.WARNING)
PDF_PATH = "C:\\Users\\utente17\\Desktop\\QuestIT_project_work\\haystack\\pdf\\fulltext.pdf"

# # # This fetches some sample files to work with


def main():
        
    doc_dir = PDF_PATH      
    converter = PDFToTextConverter(remove_numeric_tables=True, valid_languages=["en"])
    doc_pdf = converter.convert(file_path=PDF_PATH, meta=None)[0]

    preprocessor = PreProcessor(
        clean_empty_lines=True,
        clean_whitespace=True,
        clean_header_footer=False,
        split_by="word",
        split_length=100,
        split_respect_sentence_boundary=True,
    )
    docs_default = preprocessor.process([doc_pdf])
    print(f"n_docs_input: 1\nn_docs_output: {len(docs_default)}")


if __name__ == '__main__':
            logging.getLogger("haystack").setLevel(logging.INFO)
            main()
else:
        print("main non esiste")