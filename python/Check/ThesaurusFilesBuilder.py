import os
import pathlib
from typing import List

from python.Check.ThesaurusFiles import ThesaurusFiles


class ThesaurusFilesBuilder:
    def __init__(self):
        pass

    @classmethod
    def thesauri_files(cls) -> List[ThesaurusFiles]:
        current_dir = pathlib.Path(__file__).parent.absolute()
        path_thesauri = str(current_dir) + "/../../thesauri"
        thesauri_files: List[ThesaurusFiles] = []
        for root, subdirs, files in os.walk(path_thesauri):
            json_files = list(filter(cls._is_a_json_file, files))
            cls.__create_and_add_thesaurus_files(root, json_files, thesauri_files)
        thesauri_files = sorted(thesauri_files, key=lambda thesaurus_file: thesaurus_file.thesaurus_version)
        return thesauri_files

    @classmethod
    def __create_and_add_thesaurus_files(cls, root: str, json_files: List[str],
                                         thesauri_files: List[ThesaurusFiles]) -> None:
        if len(json_files) == 0:
            return
        thesaurus_files = ThesaurusFiles(root)
        [thesaurus_files.add_json_file(json_file) for json_file in json_files]
        thesaurus_files.check_files()
        thesauri_files.append(thesaurus_files)

    @classmethod
    def _is_a_json_file(cls, file: str):
        return file.endswith(".json")
