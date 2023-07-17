import sys
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI

class ConversationChain:
    def __init__(self, translated_text):
        self.translated_text = translated_text
        self.text_splitter = CharacterTextSplitter(separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        self.extracted_trans_string = " ".join(self.translated_text)
        self.text_chunks = self.text_splitter.split_text(self.extracted_trans_string)
        self.embeddings = OpenAIEmbeddings(openai_api_key= "")
        self.vectorstore = FAISS.from_texts(texts=self.text_chunks, embedding=self.embeddings)
        self.conversation_chain = ConversationalRetrievalChain.from_llm(
            llm=ChatOpenAI(
                openai_api_key= "",
                model_name="gpt-3.5-turbo",
                temperature=0
            ),
            retriever=self.vectorstore.as_retriever()
        )

        self.chat_history = []

    def run_docbot(self, translated_text):
        conversation = ConversationChain(translated_text)

        print("---------------------------------------------------------------------------------")
        print(' chatbox ')
        print('---------------------------------------------------------------------------------')

        while True:
            query = input("Prompt: ")
        
            if query in ["exit", "quit", "q", "f"]:
                print('Exiting')
                sys.exit()

            if query == '':
                continue

            result = conversation.conversation_chain({"question": query, "chat_history": conversation.chat_history})
            print("Answer: " + result["answer"])
            conversation.chat_history.append((query, result["answer"]))


