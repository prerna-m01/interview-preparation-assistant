from langchain_text_splitters import RecursiveCharacterTextSplitter

class Chunker:

    def create_chunks(self, text):

        splitter = RecursiveCharacterTextSplitter(
            separators=["\n\n", "\n", ".", " ", ""],
            chunk_size=500,
            chunk_overlap=50
        )

        return splitter.split_text(text)