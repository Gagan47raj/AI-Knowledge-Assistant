from pathlib import Path

class DocumentLoader:
    
    def load_documents(self):
        file_path = Path(
            "data/documents/knowledge.txt"
        )

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:
            
            content = file.read()

        return [
            line.strip()
            for line in content.split("\n")
            if line.strip()
        ]